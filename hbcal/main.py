#!/usr/bin/env python2.7
"""This is the main module of hbcal. It accepts an input according
   to one calendar and prints the date according to one or more
   other calendars. Calendars supported are Gregorian, Julian, Civil
   (equivalent to Julian up to and including 2nd September 1752 and
   Gregorian from 14th September 1752 - the days in between did not exist),
   and Hebrew."""

# Copyright 2015, 2016, 2019 Mark Stern
#
# This file is part of Hbcal.
#
# Hbcal is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License, version 2,
# as published by the Free Software Foundation.
#
# Hbcal is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hbcal.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import print_function

import codecs
import logging.config
import sys
from argparse import RawDescriptionHelpFormatter
from datetime import datetime, timedelta
try:
    from configparser import RawConfigParser
except ImportError:
    from ConfigParser import RawConfigParser
import os.path as path
from future.builtins import dict
from hbcal.configuration_utilities import (SingleConfigurationParameter,
                                           MultiConfigurationParameter,
                                           BinaryConfigurationParameter,
                                           DuplicateError,
                                           StoreRestrictiveList,
                                           add_negatable_option,
                                           ArgumentParser)
from hbcal.hebrew_calendar.date import Date, DateTime
from hbcal.hebrew_calendar.daf_yomi import (DafYomiCycle, DateBeforeDafYomi,
                                            SubTractate)
from hbcal.hebrew_calendar.weekday import Weekday, YOM
from hbcal.hebrew_calendar.civil_year import (GregorianYear, JulianYear,
                                              BritishYear)
from hbcal.hebrew_calendar.hebrew_year import HebrewYear
from hbcal.hebrew_calendar.hebrew_letters import HebrewString
from hbcal.hebrew_calendar.abs_time import AbsTime
from hbcal.ordinal import ordinal_suffix
from hbcal.version import __version__

CALENDAR_TYPES = {"civil": BritishYear, "gregorian": GregorianYear,
                  "hebrew": HebrewYear, "julian": JulianYear,
                  "daf": DafYomiCycle, }
DAFBIND_TYPES = [x for x in CALENDAR_TYPES if x != "daf"]
REGULAR_FORMAT = u"{weekday:{fmt}} {date:{fmt}}"
REVERSED_FORMAT = u"{date:{fmt}} {weekday:{fmt}}"
REGULAR_MOLAD_FORMAT = REGULAR_FORMAT + " {time:hmp{fmt}}"
REVERSED_MOLAD_FORMAT = "{time:hmp{fmt}} " + REVERSED_FORMAT
BAOMER = HebrewString("{BET}{AYIN}{VAV}{MEM}{RESH}")
ENGLISH_OMER_FORMAT = u"{count}{suffix} day of the omer"
HEBREW_OMER_FORMAT = HebrewString(u"{YOM:{fmt}} {count} {BAOMER:{fmt}}")
REVERSED_OMER_FORMAT = HebrewString(u"{BAOMER:{fmt}} {count} {YOM:{fmt}}")
DAF_FORMAT = u"{date:{fmt}}"
FORMATS = {"normal": {"format": REGULAR_FORMAT,
                      "molad": REGULAR_MOLAD_FORMAT,
                      "omer": HEBREW_OMER_FORMAT,
                      "fmt": "#H"},
           "reverse": {"format": REVERSED_FORMAT,
                       "molad": REVERSED_MOLAD_FORMAT,
                       "omer": REVERSED_OMER_FORMAT,
                       "fmt": "#R"},
           "phonetics": {"format": REGULAR_FORMAT,
                         "molad": REGULAR_MOLAD_FORMAT,
                         "omer": ENGLISH_OMER_FORMAT,
                         "fmt": ""},
           "html": {"format": REGULAR_FORMAT,
                    "molad": REGULAR_MOLAD_FORMAT,
                    "omer": HEBREW_OMER_FORMAT,
                    "fmt": "#h"}}

FORMAT_TYPES = ['normal', 'reverse', 'html', 'phonetics']


def get_config():
    """Read the configuration file.

    Returns the parameters in dictionary format"""

    section = "hbcal"
    parameters = dict([
        ('input calendar', SingleConfigurationParameter(CALENDAR_TYPES,
                                                        'civil')),
        ('dafbind', SingleConfigurationParameter(DAFBIND_TYPES, 'civil')),
        ('format', SingleConfigurationParameter(FORMAT_TYPES, 'normal')),
        ('output calendar', MultiConfigurationParameter(CALENDAR_TYPES,
                                                        ['civil', 'hebrew'],
                                                        (("julian",
                                                          "gregorian",
                                                          "civil"),))),
        ('sedrah', BinaryConfigurationParameter()),
        ('omer', BinaryConfigurationParameter()),
        ('molad', BinaryConfigurationParameter()),
        ('israel', BinaryConfigurationParameter())])

    config = RawConfigParser()
    home = path.expanduser("~")
    filename = path.join(home, '.hbcal.config')
    if config.read(filename):
        for key, value in parameters.items():
            value.parameter_found(key, section, config)
    if config.has_section('loggers'):
        logging.config.fileConfig(filename, disable_existing_loggers=True)
    return parameters


def list_months(year_class, fmt=''):
    """Return a formatted list of values and month names for a Year class.

    Parameters:
        year_class: A subclass of Year
    Return:
        A string comprising value, name for each month in year_class
        Months are separated by new lines.
    """
    return u"\n".join(u"    {value:2d}    {name:{fmt}}".format(value=x.value,
                                                               name=x,
                                                               fmt=fmt)
                      for x in year_class.month_class())


def parse_arguments(args, parameters):
    """Parse the command line arguments

    First parse the format option only, with help turned off, so that
    we can correctly format the Hebrew on the help page. Then parse the
    command line again (including format). Although parse_known_args
    from the first parse returns a list of remaining arguments, we
    cannot use that because the command line might be e.g.:
    hbcal --output hebrew --format reverse 1 2 2016
    If we now remove '--format reverse' we will be left with:
    hbcal --output hebrew 1 2 2016 and the 1 will be misinterpreted as an
    additional argument for the --format option.
    """

    prog_name = path.splitext(path.basename(args[0]))[0]

    # Parse format option first
    fmt_parser = ArgumentParser(prog=prog_name,
                                formatter_class=RawDescriptionHelpFormatter,
                                add_help=False)
    fmt_parser.add_argument("-f", "--format", nargs=1,
                            action=StoreRestrictiveList,
                            choices=FORMAT_TYPES, type=str.lower,
                            default=parameters['format'].value,
                            help="format for output of hebrew")
    fmt_args = fmt_parser.parse_known_args(args[1:])[0]
    fmt = FORMATS[fmt_args.format[0]]['fmt']
    template_directory = path.join(path.dirname(path.realpath(__file__)),
                                   'templates')
    help_file = codecs.open(path.join(template_directory, 'help'),
                            encoding='utf-8')
    epilog = help_file.read().format(
        civil_months=list_months(JulianYear),
        hebrew_months=list_months(HebrewYear, fmt),
        tractates=list_months(DafYomiCycle, fmt),
        fmt=fmt,
        # In Python 3.4 we can use more **s to simplify this
        Shekalim=DafYomiCycle.month_class().SHEKALIM,
        Kinnim=SubTractate.KINNIM,
        Tamid=SubTractate.TAMID,
        Middos=SubTractate.MIDDOS,
        Meilah=DafYomiCycle.month_class().MEILAH,
        **{x.name(): x for x in HebrewYear.month_class()})

    # Parse command line arguments
    parser = ArgumentParser(prog=prog_name,
                            formatter_class=RawDescriptionHelpFormatter,
                            parents=[fmt_parser],
                            description="""
Convert a date to one or more other calendars.""",
                            usage="%(prog)s [options] [date [month [year]]]",
                            epilog=epilog)

    parser.add_argument('--version', action='version',
                        version="{name} {version}".
                        format(name=prog_name, version=__version__))
    parser.add_argument("-i", "--input", nargs=1, action=StoreRestrictiveList,
                        choices=CALENDAR_TYPES, type=str.lower,
                        default=parameters['input calendar'].value,
                        help="input calendar (see Calendars)")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-o", "--output", nargs='*',
                       action=StoreRestrictiveList,
                       choices=CALENDAR_TYPES, type=str.lower,
                       mutex_groups=(('civil', 'gregorian', 'julian'),),
                       default=parameters['output calendar'].value,
                       help="output calendar(s) (see Calendars)")
    parser.add_argument("--dafbind", nargs=1, action=StoreRestrictiveList,
                        choices=DAFBIND_TYPES, type=str.lower,
                        default=parameters['dafbind'].value,
                        help="calendar to which daf yomi calendar should " +
                        "be bound (see daf under Calendars)")
    add_negatable_option(parser, "-m", "--molad", parameters['molad'].value,
                         help="output date and time of molad for hebrew " +
                         "month containing input date")
    add_negatable_option(parser, "-s", "--sedrah",
                         parameters['sedrah'].value,
                         help="output current weekly sedrah")
    add_negatable_option(parser, "-O", "--omer", parameters['omer'].value,
                         help="output day of omer (if relevant)")
    add_negatable_option(parser, "-I", "--israel",
                         parameters['israel'].value,
                         help="use Israel for sedrahs")
    parser.add_argument("date", nargs="?", action="store", type=int,
                        help="day of the month (integer)")
    parser.add_argument("month", nargs="?", action="store", type=int,
                        help="month of the year (integer)")
    parser.add_argument("year", nargs="?", action="store", type=int,
                        help="year (integer)")
    try:
        args = parser.parse_args(args[1:])
    except DuplicateError:
        parser.error("No more than one of 'gregorian', 'julian', 'civil' " +
                     "may be specified as an output calendar")
    for arg in ["input", "format", "dafbind"]:
        setattr(args, arg, getattr(args, arg)[0])

    return args, parser


class DateCache(object):
    """Stores a dictionary of equivalent dates in different calendars."""

    def __init__(self, date):
        self.dates = {date.year.__class__: date}
        self.atime = date.day_start()
        # We want the start of a civil day, so set the hours.
        self.atime = AbsTime(self.atime.weeks, self.atime.days, 6, 0)

    def __getitem__(self, item):
        if item in self.dates:
            return self.dates[item]
        new_date = Date(item, self.atime)  # Store it for future use
        self.dates[item] = new_date
        return new_date


def input_date(args, input_class):
    """Extracts the input date from the command line parameters."""

    if args.year is None:
        # Use the current date (with supplied date and month if any)
        current_datetime = datetime.now()
        # If Hebrew specified, add six hours
        if input_class == HebrewYear or \
                (input_class == DafYomiCycle and args.dafbind == "hebrew"):
            current_datetime += timedelta(hours=6)
        current_date = Date(GregorianYear(current_datetime.year),
                            current_datetime.month, current_datetime.day)
        if args.date is not None:
            if input_class not in (GregorianYear, BritishYear):
                # Convert it before modifying it
                atime = current_date.day_start()
                current_date = Date(input_class, atime)
        current_year = current_date.year
    else:
        current_year = input_class(args.year)
    return Date(current_year,
                args.month if args.month is not None else current_date.month,
                args.date if args.date is not None else current_date.date)


def get_output_line(argv):
    """Generator that returns lines of output as unicode strings.

    Read the configuration file.
    Parse the command line arguments.
    Return the specified date as a unicode string in a requested calendar.
    Return any other requested information (e.g. weekly sedrah).
    """
    args, parser = parse_arguments(argv, get_config())
    try:
        date_cache = DateCache(input_date(args, CALENDAR_TYPES[args.input]))
    except ValueError:
        parser.error("Invalid date")

    if args.molad:
        hebrew_date = date_cache[HebrewYear]
        # Now get the time of the molad
        atime = hebrew_date.year.molad(hebrew_date.month)
        weekday = Weekday(atime.days)
    else:
        weekday = Weekday(date_cache.atime.days)

    for output_type in args.output:
        output_class = CALENDAR_TYPES[output_type]
        output_data = FORMATS[args.format if output_type in ("hebrew", "daf")
                              else "phonetics"]
        if output_type == "daf":
            try:
                date = date_cache[output_class]
            except DateBeforeDafYomi:
                # Just skip this output format
                pass
            else:
                yield DAF_FORMAT.format(date=date, **output_data)
        else:
            if args.molad:
                molad_datetime = DateTime(output_class, atime)
                yield output_data['molad'].format(weekday=weekday,
                                                  date=molad_datetime.date,
                                                  time=molad_datetime.time,
                                                  **output_data)
            else:
                yield output_data['format'].\
                    format(weekday=weekday,
                           date=date_cache[output_class],
                           **output_data)

    output_data = FORMATS[args.format]
    if args.sedrah:
        hebrew_date = date_cache[HebrewYear]
        sedrah = hebrew_date.year.sedrah(hebrew_date.month,
                                         hebrew_date.date,
                                         args.israel)
        yield u"{sedrah:{fmt}}".format(sedrah=sedrah, **output_data)
    if args.omer:
        hebrew_date = date_cache[HebrewYear]
        omer = hebrew_date.year.omer_day(hebrew_date.month,
                                         hebrew_date.date)
        if omer is not None:
            suffix = ordinal_suffix(omer) if output_data['fmt'] == '' else ''
            yield output_data['omer'].format(count=omer,
                                             suffix=suffix,
                                             YOM=YOM,
                                             BAOMER=BAOMER,
                                             **output_data)


def main(argv=None):
    """ Main code for application.

    Outputs required information a line at a time

    Args:
        argv: command line parameters

    """
    if argv is None:
        argv = sys.argv
    for output_line in get_output_line(argv):
        print(output_line)


if __name__ == "__main__":
    main()
