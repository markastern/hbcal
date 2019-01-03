"""This file contains classes CivilMonth, CivilYear and subclasses."""

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

from abc import ABCMeta
from .abs_time import AbsTime, DAY
from .date import Month, Date, BadDate, RegularYear, Year


class CivilMonth(Month):
    """An enumeration class for civil months"""
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12

    @staticmethod
    def start_year_month():
        return CivilMonth.JANUARY

    @staticmethod
    def end_year_month():
        return CivilMonth.DECEMBER


class CivilYear(Year):
    """An abstract base class for different variants of civil year"""
    __metaclass__ = ABCMeta

    # The first full civil year
    FIRST_YEAR = -3758

    SHORT_FEBRUARY = 28
    LONG_FEBRUARY = 29
    SHORT_MONTH = 30
    LONG_MONTH = 31

    DAYS_IN_YEAR = 365
    DAYS_IN_LEAP_YEAR = DAYS_IN_YEAR + 1
    MONTHS_IN_YEAR = 12

    @classmethod
    def leap_year(cls, year_value):
        """Return True if year is a leap year, False otherwise.

        This should be an abstract class method, but abstract class methods
        do not work in python 2 (fixed in python 3.4).
        """
        return NotImplementedError

    def days_in_year(self):
        """Return the number of days in the year."""
        return self.DAYS_IN_LEAP_YEAR if self.leap_year(self._value) \
            else self.DAYS_IN_YEAR

    def february_days(self):
        """Return the number of days in February"""
        return self.LONG_FEBRUARY if self.leap_year(self._value) \
            else self.SHORT_FEBRUARY

    MONTH_DAYS = (None, LONG_MONTH, february_days, LONG_MONTH, SHORT_MONTH,
                  LONG_MONTH, SHORT_MONTH, LONG_MONTH, LONG_MONTH,
                  SHORT_MONTH, LONG_MONTH, SHORT_MONTH, LONG_MONTH)

    def days_in_month(self, month):
        """Return the number of days in a given month."""
        month_days = CivilYear.MONTH_DAYS[month]
        return month_days if isinstance(month_days, int) else month_days(self)

    def months_in_year(self):
        """Return the number of months in a year."""
        return self.MONTHS_IN_YEAR

    @staticmethod
    def month_class():
        return CivilMonth


class JulianYear(CivilYear, RegularYear):
    """Subclass of Year for the Julian calendar.

    This calendar was replaced in 1752 (in Britain)
    by the Gregorian calendar."""

    YEARS_IN_CYCLE = 4
    LEAP_YEARS_IN_CYCLE = 1
    START_FIRST_YEAR = AbsTime(0, 102, 6)

    def __init__(self, year):
        if isinstance(year, CivilYear) and \
                hasattr(year.__class__, "LAST_JULIAN_DATE") and \
                year.value <= year.__class__.LAST_JULIAN_DATE.year.value:
            self._value = year.value
            self._start = year.start
        else:
            super(JulianYear, self).__init__(year)

    @classmethod
    def leap_year(cls, year_value):
        """Return a Boolean - True if the lear is a leap year."""
        return year_value % 4 == 0

    # Not all years are the same length, but there is a cycle of 4 years
    # where the length of a cycle is fixed.
    @classmethod
    def _years_per_cycle(cls):
        """Return number of years in a cycle."""
        return cls.YEARS_IN_CYCLE

    @classmethod
    def _cycle_duration(cls):
        """Return length of a cycle (RelTime)."""
        return ((cls.YEARS_IN_CYCLE - cls.LEAP_YEARS_IN_CYCLE) *
                cls.DAYS_IN_YEAR +
                cls.LEAP_YEARS_IN_CYCLE * cls.DAYS_IN_LEAP_YEAR) * DAY


class GregorianYear(CivilYear, RegularYear):
    """Subclass of Year for the Gregorian calendar.

    This calendar replaced the Julian calendar in 1752 (in Britain)."""

    YEARS_IN_CYCLE = 400
    LEAP_YEARS_IN_CYCLE = 97
    START_FIRST_YEAR = AbsTime(0, 132, 6)

    def __init__(self, year):
        if isinstance(year, CivilYear) and \
                hasattr(year.__class__, "FIRST_GREGORIAN_DATE") and \
                year.value >= year.__class__.FIRST_GREGORIAN_DATE.year.value:
            self._value = year.value
            self._start = year.start
            if year.value == year.__class__.FIRST_GREGORIAN_DATE.year.value:
                self._start -= year.__class__.DAYS_SKIPPED * DAY
        else:
            super(GregorianYear, self).__init__(year)

    @classmethod
    def leap_year(cls, year_value):
        """Return a Boolean - True if the lear is a leap year."""
        return (year_value % 4 == 0 and
                year_value % 100 != 0) or year_value % 400 == 0

    # Not all years are the same length, but there is a cycle of 400 years
    # where the length of a cycle is fixed.
    @classmethod
    def _years_per_cycle(cls):
        """Return number of years in a cycle."""
        return cls.YEARS_IN_CYCLE

    @classmethod
    def _cycle_duration(cls):
        """Return length of a cycle (RelTime)."""
        return ((cls.YEARS_IN_CYCLE - cls.LEAP_YEARS_IN_CYCLE) *
                cls.DAYS_IN_YEAR +
                cls.LEAP_YEARS_IN_CYCLE * cls.DAYS_IN_LEAP_YEAR) * DAY


class BritishYear(CivilYear):
    """Combination of JulianYear and GregorianYear, as used in Britain.

    The calendar used the Julian calendar upto and including 2nd September
    1752, after which it jumped to 14th September (Gregorian calendar)."""

    LAST_JULIAN_DATE = Date(JulianYear(1752), 9, 2)
    FIRST_GREGORIAN_DATE = Date(GregorianYear(1752), 9, 14)
    YEAR_AFTER_CHANGEOVER = FIRST_GREGORIAN_DATE.year + 1
    DAYS_SKIPPED = 11  # Do we need this?

    FIRST_YEAR = JulianYear.FIRST_YEAR
    START_FIRST_YEAR = JulianYear.START_FIRST_YEAR

    def __init__(self, year):
        if isinstance(year, JulianYear) and \
                year.value <= self.LAST_JULIAN_DATE.year.value:
            self._value = year.value
            self._start = year.start
        elif isinstance(year, GregorianYear) and \
                year.value > self.FIRST_GREGORIAN_DATE.year.value:
            self._value = year.value
            self._start = year.start
        else:
            super(BritishYear, self).__init__(year)

    def adjust_date(self, month, date):
        """Check if the month and date supplied are valid for the current year.

        Returns a tuple comprising the month and date, adjusted if necessary
        to make them valid. """

        # Allow negative values of date (count back from end of month)
        # Most cases are handled by the base class, but we need to handle
        # September 1752 here (before the changeover)
        if ((self.FIRST_GREGORIAN_DATE.year.value == self._value and
             self.FIRST_GREGORIAN_DATE.month == month and
             date < self.FIRST_GREGORIAN_DATE.date -
             self.last_day(month) - 1)):
            date -= self.DAYS_SKIPPED

        if (self.LAST_JULIAN_DATE.year.value,
                self.LAST_JULIAN_DATE.month,
                self.LAST_JULIAN_DATE.date) < \
                (self._value, month, date) < \
                (self.FIRST_GREGORIAN_DATE.year.value,
                 self.FIRST_GREGORIAN_DATE.month,
                 self.FIRST_GREGORIAN_DATE.date):
            raise BadDate("Dates from 3rd to 13th September 1752 are invalid")
        else:
            return super(BritishYear, self).adjust_date(month, date)

    @classmethod
    def _base_year(cls, year_value):
        """Return the corresponding class for the specified year.

        :param year_value:
        :return:A subclass of CivilYear (JulianYear or GregorianYear)
        """
        return JulianYear if year_value <= cls.LAST_JULIAN_DATE.year.value \
            else GregorianYear

    @Year.value.setter
    def value(self, value):
        old_class = self._base_year(self.value)
        new_class = self._base_year(value)
        year = new_class(self if old_class == new_class
                         else new_class.FIRST_YEAR)
        year.value = value
        self.__init__(year)

    @classmethod
    def leap_year(cls, year_value):
        return cls._base_year(year_value).leap_year(year_value)

    @classmethod
    def current_year(cls, atime):
        cls2 = JulianYear if atime < cls.YEAR_AFTER_CHANGEOVER.start \
            else GregorianYear
        year, remainder = cls2.current_year(atime)
        return cls(year), remainder

    def day_start(self, month, date):
        """Return the start (AbsTime) of the specified month and date."""
        cls = JulianYear if ((self._value, month, date) <=
                             (self.LAST_JULIAN_DATE.year.value,
                              self.LAST_JULIAN_DATE.month,
                              self.LAST_JULIAN_DATE.date)) \
            else GregorianYear
        return cls.day_start(cls(self), month, date)

    def add_days(self, month, date, days):
        julian_old = (self._value, month, date) <= \
                     (self.LAST_JULIAN_DATE.year.value,
                      self.LAST_JULIAN_DATE.month,
                      self.LAST_JULIAN_DATE.date)
        self.year, month, date = super(BritishYear,
                                       self).add_days(month, date, days)
        if julian_old:
            if (self._value, month, date) > \
                    (self.LAST_JULIAN_DATE.year.value,
                     self.LAST_JULIAN_DATE.month,
                     self.LAST_JULIAN_DATE.date):
                (self.year,
                 month, date) = super(BritishYear,
                                      self).add_days(month, date,
                                                     self.DAYS_SKIPPED)
        else:
            if (self._value, month, date) < \
                    (self.FIRST_GREGORIAN_DATE.year.value,
                     self.FIRST_GREGORIAN_DATE.month,
                     self.FIRST_GREGORIAN_DATE.date):
                (self.year,
                 month, date) = super(BritishYear,
                                      self).add_days(month, date,
                                                     -self.DAYS_SKIPPED)
        return self.year, month, date
