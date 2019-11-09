#!/usr/bin/env python
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
from itertools import chain
try:
    from functools import lru_cache
except ImportError:
    from functools32 import lru_cache
from bidi.algorithm import get_display
from future.builtins import dict
from future.utils import PY2
from hbcal.configuration_utilities import (
    SingleConfigurationParameter,
    MultiConfigurationParameter,
    BinaryConfigurationParameter,
    ConfigurationParameterValueError,
    ConfigurationParameterAmbiguousError,
    StoreRestrictiveSet,
    add_negatable_option,
    ArgumentParser)
from hbcal.hebrew_calendar.date import Date, DateTime
from hbcal.hebrew_calendar.daf_yomi import (DafYomiCycle, DateBeforeDafYomi,
                                            SubTractate)
from hbcal.hebrew_calendar.weekday import YOM
from hbcal.hebrew_calendar.civil_year import (GregorianYear, JulianYear,
                                              BritishYear)
from hbcal.hebrew_calendar.hebrew_year import HebrewYear
from hbcal.hebrew_calendar.hebrew_letters import HEBREW_LETTERS
from hbcal.hebrew_calendar.abs_time import RelTime
from hbcal.hebrew_calendar.gematria import to_letters
from hbcal.ordinal import ordinal_suffix
from hbcal.version import __version__

OUTPUT_CLASSES = {"civil": BritishYear, "gregorian": GregorianYear,
                  "hebrew": HebrewYear, "julian": JulianYear,
                  "daf": DafYomiCycle, "sedrah": HebrewYear,
                  "omer": HebrewYear}
CALENDAR_TYPES = frozenset(('civil', 'gregorian', 'hebrew', 'julian', 'daf'))
DAFBIND_TYPES = [x for x in CALENDAR_TYPES if x != "daf"]
BASE_FORMAT = u'%{weekday_code} %{qualifier}d %B %{qualifier}Y'
DATE_FORMAT = BASE_FORMAT + '{fmt}'
MOLAD_FORMAT = BASE_FORMAT + u" %H:%M {conjunction}%-P {parts}{fmt}"
VAV = u"{VAV}".format(**HEBREW_LETTERS)
BAOMER = u"{BET}{AYIN}{VAV}{MEM}{RESH}".format(**HEBREW_LETTERS)
CHALAKIM = u"{CHET}{LAMED}{QOF}{YOD}{FINAL_MEM}".format(**HEBREW_LETTERS)
ENGLISH_OMER_FORMAT = u"{count}{suffix} day of the omer"
HEBREW_OMER_FORMAT = u"{YOM} {{count}} {BAOMER}".format(YOM=YOM, BAOMER=BAOMER)
DAF_FORMAT = '%B %{qualifier}d{fmt}'
SEDRAH_FORMAT = u"{sedrah:{fmt}}"
ENGLISH_TEMPLATES = {"civil": DATE_FORMAT, "gregorian": DATE_FORMAT,
                     "hebrew": DATE_FORMAT, "julian": DATE_FORMAT,
                     "daf": DAF_FORMAT, "sedrah": SEDRAH_FORMAT,
                     "omer": ENGLISH_OMER_FORMAT}
HEBREW_TEMPLATES = {"civil": DATE_FORMAT, "gregorian": DATE_FORMAT,
                    "hebrew": DATE_FORMAT, "julian": DATE_FORMAT,
                    "daf": DAF_FORMAT, "sedrah": SEDRAH_FORMAT,
                    "omer": HEBREW_OMER_FORMAT}
FORMATS = ['normal', 'reverse', 'phonetics', 'html', 'gematria']


def get_config():
    """Read the configuration file.

    Returns the parameters in dictionary format"""

    section = "hbcal"
    parameters = dict([
        ('input calendar', SingleConfigurationParameter(CALENDAR_TYPES,
                                                        'civil')),
        ('dafbind', SingleConfigurationParameter(DAFBIND_TYPES, 'civil')),
        ('format', MultiConfigurationParameter(FORMATS, ['normal'],
                                               (('normal', 'reverse',
                                                 'phonetics', 'html'),
                                                ('phonetics', 'gematria')))),
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


def list_months(year_class, fmt=None):
    """Return a formatted list of values and month names for a Year class.

    Parameters:
        year_class: A subclass of Year
        fmt:        An array of output format options from the command line
    Return:
        A string comprising value, name for each month in year_class
        Months are separated by new lines.
    """
    line = u"{tab}{value:2d}{tab}{name}"
    if fmt is None:
        fmt = ['phonetics']
    return "\n".join(line.format(tab='    ',
                                 value=x.value,
                                 name=x if 'phonetics' in fmt else reformat(
                                     format(x, '#H'), fmt))
                     for x in year_class.month_class())


def format_month(month, fmt=None):
    """ Format the month as a name

    The output will be based on the format parameter in the command line."""
    if fmt is None:
        fmt = ['phonetics']
    return format(u'{name}'.format(name=month if 'phonetics' in fmt
                                   else reformat(format(month, '#H'), fmt)))


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
    group = fmt_parser.add_mutually_exclusive_group()
    group.add_argument("-f", "--format", nargs='*',
                       action=StoreRestrictiveSet,
                       choices=FORMATS,
                       mutex_groups=(('normal', 'reverse',
                                      'phonetics', 'html'),
                                     ('phonetics', 'gematria')),
                       type=str.lower,
                       default=parameters['format'].value,
                       help="format for output of hebrew")

    fmt_args = fmt_parser.parse_known_args(args[1:])[0]
    fmt = '' if 'phonetics' in fmt_args.format else '#H'
    template_directory = path.join(path.dirname(path.realpath(__file__)),
                                   'templates')
    help_file = codecs.open(path.join(template_directory, 'help'),
                            encoding='utf-8')
    epilog = help_file.read().format(
        civil_months=list_months(JulianYear),
        hebrew_months=list_months(HebrewYear, fmt_args.format),
        tractates=list_months(DafYomiCycle, fmt_args.format),
        fmt=fmt,
        # In Python 3.4 we can use more **s to simplify this
        Shekalim=DafYomiCycle.month_class().SHEKALIM,
        Kinnim=format_month(SubTractate.KINNIM, fmt_args.format),
        Tamid=format_month(SubTractate.TAMID, fmt_args.format),
        Middos=format_month(SubTractate.MIDDOS, fmt_args.format),
        Meilah=format_month(DafYomiCycle.month_class().MEILAH,
                            fmt_args.format),
        **{x.name(): format_month(x, fmt_args.format)
           for x in HebrewYear.month_class()})

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
    parser.add_argument("-i", "--input", nargs=1, action=StoreRestrictiveSet,
                        choices=CALENDAR_TYPES, type=str.lower,
                        default=parameters['input calendar'].value,
                        help="input calendar (see Calendars)")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-o", "--output", nargs='*',
                       action=StoreRestrictiveSet,
                       choices=CALENDAR_TYPES, type=str.lower,
                       mutex_groups=(('civil', 'gregorian', 'julian'),),
                       default=parameters['output calendar'].value,
                       help="output calendar(s) (see Calendars)")
    parser.add_argument("--dafbind", nargs=1, action=StoreRestrictiveSet,
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
    parser.add_argument("month", nargs="?", action="store",
                        help="month of the year (integer)")
    parser.add_argument("year", nargs="?", action="store", type=int,
                        help="year (integer)")
    args = parser.parse_args(args[1:])
    for arg in ["input", "dafbind"]:
        setattr(args, arg, next(iter(getattr(args, arg))))

    return args, parser


@lru_cache()
def get_date_time(atime, date_class):
    """ Gets a datetime from an abs_time and caches it """
    return DateTime(date_class, atime)


def input_time(args):
    """ Extracts an abs_time from input parameters """

    if args.year is None:
        # Use the current date (with supplied date and month if any)
        current_datetime = datetime.now()
        # If Hebrew specified, add six hours
        if (args.input == 'hebrew'
                or (args.input == 'daf' and args.dafbind == "hebrew")):
            current_datetime += timedelta(hours=6)
        current_date = Date(GregorianYear(current_datetime.year),
                            current_datetime.month, current_datetime.day)
        if args.date is not None:
            if args.input not in ('gregorian', 'civil'):
                # Convert it before modifying it
                atime = current_date.day_start
                current_date = Date(OUTPUT_CLASSES[args.input], atime)
        current_year = current_date.year
    else:
        current_year = OUTPUT_CLASSES[args.input](args.year)
    if args.month is None:
        month = current_date.month
    else:
        try:
            month = int(args.month)
        except ValueError:
            month = get_month_from_name(args.month.capitalize(),
                                        current_year)
    input_date = Date(current_year, month,
                      current_date.date if args.date is None else args.date)
    atime = input_date.day_start
    if args.molad:
        hebrew_date = get_date_time(atime, HebrewYear)
        atime = hebrew_date.date.year.molad(hebrew_date.date.month)
    else:
        if (input_date.year.__class__ == HebrewYear
                or (input_date.year.__class__ == DafYomiCycle
                    and args.dafbind == "hebrew")):
            atime += RelTime(0, hours=6)
    return atime


def get_month_from_name(month_name, current_year):
    """Get the numerical value of a month from the supplied name"""

    month = None
    for allowed_month in current_year.months():
        if allowed_month.__format__('#H').startswith(
                month_name.decode(sys.stdin.encoding) if PY2 else month_name):
            if month is None:
                month = allowed_month.value
            else:
                raise ValueError("Ambiguous month")
    if month is None:
        raise ValueError("Invalid month")
    return month


def reformat(line, formatting_options):
    """ Reformat a Hebrew line for bi-directional output or as html """
    if 'reverse' in formatting_options:
        reformatted = get_display(line, base_dir='R')
    elif 'html' in formatting_options:
        reformatted = line.encode('ascii', 'xmlcharrefreplace').decode('ascii')
    else:
        reformatted = line
    return reformatted


def get_output_line(argv):
    """Generator that returns lines of output as unicode strings.

    Read the configuration file.
    Parse the command line arguments.
    Return the specified date as a unicode string in a requested calendar.
    Return any other requested information (e.g. weekly sedrah).
    """
    args, parser = parse_arguments(argv, get_config())
    try:
        atime = input_time(args)
    except ValueError:
        parser.error("Invalid date")

    for output_type in chain(args.output,
                             [x for x in ['sedrah', 'omer']
                              if getattr(args, x)]):
        output_class = OUTPUT_CLASSES[output_type]
        if (output_class in (HebrewYear, DafYomiCycle)
                and 'phonetics' not in args.format):
            template = HEBREW_TEMPLATES[output_type]
            params = {
                'fmt': '#H',
                'conjunction': VAV,
                'parts': CHALAKIM
            }
        else:
            template = ENGLISH_TEMPLATES[output_type]
            params = {
                'fmt': '',
                'conjunction': 'and ',
                'parts': 'parts'
            }
        if (output_type in ("hebrew", "daf", "omer")
                and 'gematria' in args.format):
            params['qualifier'] = '~'
            params['weekday_code'] = 'a'
            params['conjunction'] = ''
        else:
            params['qualifier'] = '-'
            params['weekday_code'] = 'A'
        try:
            value = get_date_time(atime, OUTPUT_CLASSES[output_type])
            if args.molad:
                template = MOLAD_FORMAT
            else:
                if output_type == 'sedrah':
                    params['sedrah'] = value.date.year.sedrah(value.date.month,
                                                              value.date.date,
                                                              args.israel)
                elif output_type == 'omer':
                    omer = value.date.year.omer_day(value.date.month,
                                                    value.date.date)
                    if omer is None:
                        continue
                    params['suffix'] = ordinal_suffix(omer)
                    if params['qualifier'] == '~':
                        omer = to_letters(omer).format(**HEBREW_LETTERS)
                    params['count'] = omer
            yield reformat(format(value, template.format(**params)),
                           args.format if output_class in (HebrewYear,
                                                           DafYomiCycle)
                           else [])
        except DateBeforeDafYomi:
            # Just skip this output format
            pass


def main(argv=None):
    """ Main code for application.

    Outputs required information a line at a time

    Args:
        argv: command line parameters

    """
    if argv is None:
        argv = sys.argv
    try:
        for output_line in get_output_line(argv):
            print(output_line)
    except (ConfigurationParameterValueError,
            ConfigurationParameterAmbiguousError) as ex:
        print(ex.message, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
