""" This file contains days of the week.

    Exports:
        DAYS_IN_WEEK
        YOM
        WEEKDAY_HEBREW_NAMES
"""


# Copyright 2015, 2019 Mark Stern
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

from enum import IntEnum

from .hebrew_letters import HEBREW_LETTERS
from .gematria import to_letters
from .format_percent_string import format_percent_string

DAYS_IN_WEEK = 7
YOM = u"{YOD}{VAV}{FINAL_MEM}".format(**HEBREW_LETTERS)

WEEKDAY_HEBREW_NAMES = [
    YOM + u" {RESH}{ALEF}{SHIN}{VAV}{FINAL_NUN}".format(**HEBREW_LETTERS),
    YOM + u" {SHIN}{NUN}{YOD}".format(**HEBREW_LETTERS),
    YOM + u" {SHIN}{LAMED}{YOD}{SHIN}{YOD}".format(**HEBREW_LETTERS),
    YOM + u" {RESH}{BET}{YOD}{AYIN}{YOD}".format(**HEBREW_LETTERS),
    YOM + u" {CHET}{MEM}{YOD}{SHIN}{YOD}".format(**HEBREW_LETTERS),
    YOM + u" {SHIN}{YOD}{SHIN}{YOD}".format(**HEBREW_LETTERS),
    u"{SHIN}{BET}{TAV}".format(**HEBREW_LETTERS)]


ESCAPES = {'a': 'format_short_weekday',
           'A': 'format_weekday',
           '-': None,
           '~': None}


class Weekday(IntEnum):
    """An enumeration class for days of the week"""
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6

    def __str__(self):
        return self._name_.title()

    def __format__(self, fmt):
        return format_percent_string(self, ESCAPES, fmt)

    def format_weekday(self, fmt):
        """ Format a weekday as a string """
        _, _, option = fmt.partition('#')
        if option == 'H':
            return WEEKDAY_HEBREW_NAMES[self]
        return self.__str__()

    def format_short_weekday(self, fmt):
        """ Format a weekday as a short string (usually 3 characters) """
        _, _, option = fmt.partition('#')
        if option == "H":
            if self.value == Weekday.SATURDAY:
                name = WEEKDAY_HEBREW_NAMES[self]
            else:
                name = u"{YOM} {day}".format(YOM=YOM,
                                             day=to_letters(self.value + 1))
            return name
        return self.__str__()[:3]
