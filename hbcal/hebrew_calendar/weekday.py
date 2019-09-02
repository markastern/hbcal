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

import re
from enum import IntEnum

from .hebrew_letters import HEBREW_LETTERS
from .gematria import to_letters

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
        fmt1, sep, option = fmt.partition('#')
        if option == "":
            return self.__str__()
        matched = re.match('%~A', fmt1)
        if not matched or self.value == Weekday.SATURDAY:
            return WEEKDAY_HEBREW_NAMES[self]
        day = to_letters(self.value + 1)
        return YOM + ' ' + day
