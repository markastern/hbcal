"""This module defines the RelTime and AbsTime classes"""

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
from __future__ import division
import numbers
from .hebrew_letters import HEBREW_LETTERS

CHALAKIM_IN_HOUR = 1080
HOURS_IN_DAY = 24
DAYS_IN_WEEK = 7
MINUTES_IN_HOUR = 60
CHALAKIM_IN_MINUTE = CHALAKIM_IN_HOUR // MINUTES_IN_HOUR

PARTS = u"{CHET}{LAMED}{QOF}{YOD}{FINAL_MEM}".format(**HEBREW_LETTERS)


class RelTime(object):
    """A Relative time - the period between 2 points in time"""
    def __init__(self, weeks, days=0, hours=0, chalakim=0):
        self.chalakim = ((weeks * DAYS_IN_WEEK + days) *
                         HOURS_IN_DAY + hours) * CHALAKIM_IN_HOUR + chalakim

    def __add__(self, other):
        if not isinstance(other, RelTime):
            return NotImplemented
        return RelTime(0, 0, 0, self.chalakim + other.chalakim)

    def __sub__(self, other):
        if not isinstance(other, RelTime):
            return NotImplemented
        return RelTime(0, 0, 0, self.chalakim - other.chalakim)

    def __iadd__(self, other):
        if not isinstance(other, RelTime):
            # Cannot return NotImplemented here because it would fall back to
            # using __add__, and then other.__radd__, which would return a
            # RelTime object if other is an AbstTime object.
            raise TypeError("unsupported operand type(s) for -= : " +
                            "'{0}' and '{1}'".format(self.__class__.__name__,
                                                     other.__class__.__name__))
        self.chalakim += other.chalakim
        return self

    def __isub__(self, other):
        if not isinstance(other, RelTime):
            return NotImplemented

        self.chalakim -= other.chalakim
        return self

    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented

        return RelTime(0, 0, 0, self.chalakim * other)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        if not isinstance(other, int):
            return NotImplemented

        self.chalakim *= other
        return self

    def __truediv__(self, other):
        if isinstance(other, RelTime):
            return self.chalakim / other.chalakim
        if isinstance(other, numbers.Real):
            return RelTime(0, 0, 0, self.chalakim / other)
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, RelTime):
            return self.chalakim // other.chalakim
        if isinstance(other, numbers.Real):
            return RelTime(0, 0, 0, self.chalakim // other)
        return NotImplemented

    def __mod__(self, other):
        if isinstance(other, RelTime):
            return RelTime(0, 0, 0, self.chalakim % other.chalakim)
        if isinstance(other, numbers.Real):
            return RelTime(0, 0, 0, self.chalakim % other)
        return NotImplemented

    def __divmod__(self, other):
        if isinstance(other, RelTime):
            quotient, remainder = divmod(self.chalakim, other.chalakim)
            return quotient, RelTime(0, 0, 0, remainder)
        if isinstance(other, numbers.Real):
            quotient, remainder = divmod(self.chalakim, other)
            return RelTime(0, 0, 0, quotient), RelTime(0, 0, 0, remainder)
        return NotImplemented

    def __repr__(self):
        return "RelTime({0})".format(self.chalakim)

    def __format__(self, fmt):
        fmt1, _, option = fmt.partition('#')
        if fmt1 != 'hmp':
            return self.__repr__()

        minutes, chalakim = divmod(self.chalakim, CHALAKIM_IN_MINUTE)
        hours, minutes = divmod(minutes, MINUTES_IN_HOUR)
        hours = hours % HOURS_IN_DAY
        result = "{0:0>2d}:{1:0>2d}".format(hours, minutes)
        if option == "":
            result += " and {} parts".format(chalakim)
        elif option == "H":
            result += u" {VAV}{0} {PARTS}".format(chalakim,
                                                  PARTS=PARTS,
                                                  **HEBREW_LETTERS)
        elif option == "R":
            result = u"{PARTS} {0}{VAV} ".format(chalakim,
                                                 PARTS=PARTS[::-1],
                                                 **HEBREW_LETTERS) + result
        return result

    @property
    def weeks(self):
        """Returns number of weeks in RelTime object."""
        return self.chalakim // (DAYS_IN_WEEK * HOURS_IN_DAY *
                                 CHALAKIM_IN_HOUR)

    @property
    def days(self):
        """Returns number of days (including weeks) in RelTime object."""
        return self.chalakim // (HOURS_IN_DAY * CHALAKIM_IN_HOUR)

    @property
    def days_chalakim(self):
        """Returns a tuple comprising days and leftover chalakim."""
        return divmod(self.chalakim, HOURS_IN_DAY * CHALAKIM_IN_HOUR)


DAY = RelTime(0, 1)


class AbsTime(object):
    """An absolute time - a point in time"""
    def __init__(self, weeks=0, days=0, hours=0, chalakim=0, **kwargs):
        """ Construct an AbsTime object.

        :param weeks:
            If absTime parameter is not set, the number of weeks
            from the start of the first day of creation.
            If absTime parameter is set and weeks has a True value,
            the number of weeks is taken from the absTime parameter.
            If absTime parameter is set and weeks has a False value,
            the number of weeks is zero.
        :param days:
            If absTime parameter is not set, the number of days
            from the start of the week.
            If absTime parameter is set and days has a True value,
            the number of days is taken from the absTime parameter.
            If absTime parameter is set and days has a False value,
            the number of days is zero.
        :param hours:
            If absTime parameter is not set, the number of hours
            from the start of the day.
            If absTime parameter is set and hours has a True value,
            the number of hours is taken from the absTime parameter.
            If absTime parameter is set and hours has a False value,
            the number of hours is zero.
        :param chalakim:
            If absTime parameter is not set, the number of chalakim
            from the start of the hour.
            If absTime parameter is set and chalakim has a True value,
            the number of chalakim is taken from the absTime parameter.
            If absTime parameter is set and chalakim has a False value,
            the number of chalakim is zero.
        :param kwargs:
            May contain optional parameter absTime (another AbsTime object,
            see above).

        Note that the input parameter need not be normalised
        e.g. weeks = 1, days = 8 is valid and will be converted to
        weeks = 2, days = 1.
        """
        if 'absTime' in kwargs:
            abs_time = kwargs['absTime']
            self._weeks = abs_time.weeks if weeks else 0
            self._days = abs_time.days if days else 0
            self._hours = abs_time.hours if hours else 0
            self._chalakim = abs_time.chalakim if chalakim else 0
        else:
            self._weeks = weeks
            self._days = days
            self._hours = hours
            self._chalakim = chalakim
            self.normalise()

    @property
    def weeks(self):
        """Return number of weeks since start of first day of creation."""
        return self._weeks

    @property
    def days(self):
        """Return number of days since start of week."""
        return self._days

    @property
    def hours(self):
        """Return number of hours since start of day."""
        return self._hours

    @property
    def chalakim(self):
        """Return number of chalakim since start of hour.

        1 hour = 1080 chalakim.
        """
        return self._chalakim

    def __repr__(self):
        return "AbsTime({0}, {1}, {2}, {3})".format(self._weeks,
                                                    self._days,
                                                    self._hours,
                                                    self._chalakim)

    def __format__(self, fmt):
        fmt1, _, option = fmt.partition('#')
        if fmt1 != 'hmp':
            return self.__repr__()

        result = "{0:0>2d}:{1:0>2d}".format(self._hours,
                                            self._chalakim //
                                            CHALAKIM_IN_MINUTE)
        if option == "":
            result += " and {} parts".format(self._chalakim %
                                             CHALAKIM_IN_MINUTE)
        elif option == "H":
            result += u" {VAV}{0} {PARTS}".format(self._chalakim %
                                                  CHALAKIM_IN_MINUTE,
                                                  PARTS=PARTS,
                                                  **HEBREW_LETTERS)
        elif option == "R":
            result = u"{PARTS} {0}{VAV} ".format(self._chalakim %
                                                 CHALAKIM_IN_MINUTE,
                                                 PARTS=PARTS[::-1],
                                                 **HEBREW_LETTERS) + result
        return result

    # Implement all the rich comparision operators.
    def __eq__(self, other):
        return ((self._weeks, self._days, self._hours, self._chalakim) ==
                (other.weeks, other.days, other.hours, other.chalakim))

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return ((self._weeks, self._days, self._hours, self._chalakim) <
                (other.weeks, other.days, other.hours, other.chalakim))

    def __gt__(self, other):
        return ((self._weeks, self._days, self._hours, self._chalakim) >
                (other.weeks, other.days, other.hours, other.chalakim))

    def __le__(self, other):
        return self == other or self < other

    def __ge__(self, other):
        return self == other or self > other

    def normalise(self):
        """Normalises an AbsTime object.

        This ensures that:
            0 <= days < DAYS_IN_WEEK
            0 <= hours < HOURS_IN_DAY
            0 <= chalakim < CHALAKIM_IN_HOUR

        For consistency, all AbsTime objects must be normalised."""

        hours, self._chalakim = divmod(self._chalakim, CHALAKIM_IN_HOUR)
        self._hours += hours

        days, self._hours = divmod(self._hours, HOURS_IN_DAY)
        self._days += days

        weeks, self._days = divmod(self._days, DAYS_IN_WEEK)
        self._weeks += weeks

        if self._chalakim < 0:
            self._chalakim += CHALAKIM_IN_HOUR
            self._hours -= 1

        if self._hours < 0:
            self._hours += HOURS_IN_DAY
            self._days -= 1

        if self._days < 0:
            self._days += DAYS_IN_WEEK
            self._weeks -= 1

    def __add__(self, other):
        if not isinstance(other, RelTime):
            return NotImplemented

        return AbsTime(self._weeks,
                       self._days,
                       self._hours,
                       self._chalakim + other.chalakim)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, AbsTime):
            return RelTime(self._weeks - other.weeks,
                           self._days - other.days,
                           self._hours - other.hours,
                           self._chalakim - other.chalakim)
        if isinstance(other, RelTime):
            return AbsTime(self._weeks,
                           self._days,
                           self._hours,
                           self._chalakim - other.chalakim)

        return NotImplemented

    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented

        return AbsTime(self._weeks * other,
                       self._days * other,
                       self._hours * other,
                       self._chalakim * other)

    def __rmul__(self, other):
        return self * other
