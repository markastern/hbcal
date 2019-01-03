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

from .hebrew_letters import HebrewString

DAYS_IN_WEEK = 7
YOM = HebrewString(u"{YOD}{VAV}{FINAL_MEM}")

WEEKDAY_HEBREW_NAMES = [
    YOM + u" {RESH}{ALEF}{SHIN}{VAV}{FINAL_NUN}",
    YOM + u" {SHIN}{NUN}{YOD}",
    YOM + u" {SHIN}{LAMED}{YOD}{SHIN}{YOD}",
    YOM + u" {RESH}{BET}{YOD}{AYIN}{YOD}",
    YOM + u" {CHET}{MEM}{YOD}{SHIN}{YOD}",
    YOM + u" {SHIN}{YOD}{SHIN}{YOD}",
    u"{SHIN}{BET}{TAV}"]


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
        return (self.__str__() if fmt == ""
                else HebrewString(WEEKDAY_HEBREW_NAMES[self]).__format__(fmt))
