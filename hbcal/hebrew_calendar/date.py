# -*- coding: utf-8 -*-
"""This module defines calendar classes (mostly abstract) for hbcal"""

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

from __future__ import division
from abc import ABCMeta, abstractmethod
from enum import IntEnum
import logging

from future.builtins import range
from future.utils import PY2, with_metaclass
try:
    from functools import cached_property
except ImportError:
    from cached_property import cached_property

from .abs_time import RelTime, AbsTime, DAY
from .abstract_attribute import AbstractAttribute
from .weekday import Weekday
from .format_percent_string import FormatPercentString

# Exception Classes


class BadDate(ValueError):
    """An exception class for an invalid Date"""


class DateBeforeCreation(BadDate):
    """An exception class for a date before the creation of the world"""


class MonthNotInRange(BadDate):
    """An exception class for a date whose month is out of range"""


class DateNotInRange(BadDate):
    """An exception class for a date whose date (in month) is out of range"""


class Month(IntEnum):
    """A base class for month classes of different calendars"""
    def name(self):

        """Return the name of the month"""
        return self._name_.replace('_', ' ').title()

    @staticmethod
    @abstractmethod
    def start_year_month():
        """Return the month at the start of which the year changes.

        For Hebrew years, this is not 1."""
        if PY2:
            raise NotImplementedError

    @staticmethod
    @abstractmethod
    def end_year_month():
        """Return the month after which the year changes."""
        if PY2:
            raise NotImplementedError

    def __format__(self, fmt):
        return str(self)

    def format_month_name(self, fmt, year, date):
        """ Return the formatted month name

        The result may depend on the year and date"""
        return format(self, fmt)

    def __str__(self):
        return self.name()


class Date(FormatPercentString):
    """A date class for different calendar types.

    The year attribute is an instance of class Year and determines the
    calendar type.

    Date objects can be formatted using the standard python format command
    to create a string representing the date under the control of an explicit
    format string.

    Format Codes

    Directive   Meaning                             Example

    %a          Weekday as an abbreviated name      Sun, Mon, …, Sat

    %a#H        Weekday as an abbreviated name      יום א׳, יום ב׳, …, שבת
                using Hebrew letters as numbers

    %A          Weekday as full name                Sunday, Monday, …,
                                                    Saturday

    %A#H        Weekday as full Hebrew name         יום ראשון, יום שני, …, שבת

    %B          Month as full name                  January, February, …,
                                                    December
                                                    Nissan, Iyar, …, Ellul

    %B#H        Month as full name in Hebrew        ניסן, אייר, …, אלול
                letters

    %d          Day of the month as a zero-padded   01, 02, …, 31
                decimal number                      002, 003, …, 176 (daf)

    %-d         Day of the month as a decimal       1, 2, …, 31
                number                              2, 3, …, 176 (daf)

    %_d         Day of the month as a space-padded  ' 1', ' 2', …, 31
                decimal number                      '  2', '  3', …, 176 (daf)

    %~d#H       Day of the month using Hebrew       א׳, ב׳, …, ל׳
                letters as numbers                  (daf) ב׳, ג׳, …, קע״ו

    %y          Year without century as a           00, 01, …, 99
                zero-padded decimal number

    %-y         Year without century as a decimal   0, 1, …, 99
                number

    %_y         Year without century as a           ' 0', ' 1', …, 99
                space-padded decimal number

    %~y#H       Year without millenium using        א׳, …, תתקצ״ט ,''
                Hebrew letters as numbers

    %Y          Year as a zero-padded decimal       0000, 0001, …, 9999
                number

    %-Y         Year as a decimal number            0, 1, …, 9999

    %_Y         Year as a space-padded decimal      '   0', '   1', …, 9999
                number

    %~Y#H       Year using Hebrew letters as       א׳, ב׳, ה׳תש״פ, …
                numbers

    %%          A single percent sign              %

    NOTE: '#H' may be specified only once in the formatting string, at its
    end. It will then qualify all format codes within the formatting string.
    It is only valid if the year is a HebrewYear or DafYomiCycle
    """

    SUBFORMATTERS = ('year',)

    def __init__(self, year, month, date=None):
        if isinstance(month, AbsTime):
            if month < AbsTime(0, 0, 6):
                raise BadDate
            year, remainder = year.current_year(month)
            self.year = year
            self.month = year.month_class().start_year_month()
            self.date = year.first_day()
            days = remainder.days_chalakim[0]
            self.__iadd__(days)
        else:
            self.year = year
            (month, self.date) = year.adjust_date(month, date)
            self.month = year.month_class()(month)

    def __eq__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        return (self.year, self.month, self.date) == (other.year,
                                                      other.month,
                                                      other.date)

    def __ne__(self, other):
        return not self == other

    def __iadd__(self, other):
        if isinstance(other, int):
            self.year, self.month, self.date = self.year.add_days(self.month,
                                                                  self.date,
                                                                  other)
            return self
        raise TypeError("unsupported operand type(s) for += : " +
                        "'{0}' and '{1}'".format(self.__class__.__name__,
                                                 other.__class__.__name__))

    def __isub__(self, other):
        if isinstance(other, int):
            self.year, self.month, self.date = self.year.add_days(self.month,
                                                                  self.date,
                                                                  -other)
            return self
        raise TypeError("unsupported operand type(s) for -= : " +
                        "'{0}' and '{1}'".format(self.__class__.__name__,
                                                 other.__class__.__name__))

    def __add__(self, other):
        total = self
        total += other
        return total

    def __sub__(self, other):
        difference = self
        difference -= other
        return difference

    @cached_property
    def day_start(self):
        """Return the absolute time of the start of the current date."""
        return self.year.day_start(self.month, self.date)

    def __repr__(self):
        return "Date({0}, {1}, {2})".format(self.year, self.month, self.date)

    def __str__(self):
        return self.__format__("")

    def format_year(self, fmt):
        """ Return the formatted year"""
        return format(self.year, fmt)

    def format_weekday(self, fmt):
        """ Return the formatted weekday"""
        return format(Weekday(self.day_start.days), fmt)

    def format_month_name(self, fmt):
        """ Return the formatted month name"""
        return self.month.format_month_name(fmt, self.year, self.date)

    def format_day_of_month(self, fmt):
        """ Return the day of the month, formatted as 2 digits """
        return self.year.format_day_of_month(self.date, fmt)

    ESCAPES = {
        'A': 'format_weekday',
        'a': 'format_weekday',
        'B': 'format_month_name',
        'd': 'format_day_of_month'
    }


LOG = logging.getLogger(__name__)


class Year(with_metaclass(ABCMeta, FormatPercentString)):
    """Abstract base class for defining the year of different calendar types"""

    MIN_DATE = None
    FIRST_YEAR = AbstractAttribute("The value of the first year")
    START_FIRST_YEAR = AbstractAttribute("The start of the first year")

    def __init__(self, year):
        if isinstance(year, int):
            self._value = self.FIRST_YEAR
            self._start = self.START_FIRST_YEAR
            self.value = year
        elif isinstance(year, self.__class__):
            # pylint: disable=protected-access
            self._value = year.value
            self._start = year._start
        else:
            raise TypeError("unsupported operand type for " +
                            "{0}(): '{1}'".format(self.__class__.__name__,
                                                  year.__class__.__name__))

    @property
    def value(self):
        """Return the year value (integer)."""
        return self._value

    @value.setter
    @abstractmethod
    def value(self, value):
        """Set year value.

        :param value: The year value (int)
        :return: None
        """
        raise NotImplementedError

    @property
    def start(self):
        """Return the start of the year (AbsTime).

        For Hebrew Years, this returns Molad Tishri rather than the actual
        start of the year.
        """
        return self._start

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and
                isinstance(self, other.__class__) and
                self._value == other.value)

    def __ne__(self, other):
        return not self == other

    @abstractmethod
    def days_in_month(self, month):
        """Return the number of days in the specified month."""

    @staticmethod
    def first_day():
        """Return the first day of the month."""
        return 1

    def last_day(self, month):
        """Return the last day of the month."""
        return self.days_in_month(month)

    @abstractmethod
    def months_in_year(self):
        """Return the number of months in the year."""
        raise NotImplementedError

    def months(self):
        """A generator for the months of the current year."""
        for month in range(self.month_class().start_year_month(),
                           self.months_in_year() + 1):
            yield self.month_class()(month)

    @abstractmethod
    def days_in_year(self):
        """Return the number of days in the current year."""
        raise NotImplementedError

    def duration(self):
        """Return the duration (RelTime) of the current year."""
        return self.days_in_year() * DAY

    def adjust_date(self, month, date):
        """Check if the month and date supplied are valid for the current year.

        Returns a tuple comprising the month and date, adjusted if necessary
        to make them valid. If the month and date are still invalid,
        an exception is thrown."""

        min_date = self.min_date()
        if (self._value, month, date) < (min_date.year.value, min_date.month,
                                         min_date.date):
            raise DateBeforeCreation()

        # Allow negative months (count back from end of year
        if -self.months_in_year() <= month <= -1:
            month += self.months_in_year() + 1

        # Check if the month is nonsense
        if month not in self.months():
            raise MonthNotInRange()

        # Allow negative values of date (count back from end of month)
        if -self.days_in_month(month) <= date <= -1:
            date += self.last_day(month) + 1

        # Check if date is valid
        if not self.first_day() <= date <= self.last_day(month):
            raise DateNotInRange()

        return (month, date)

    def __iadd__(self, other):
        self.value += other
        return self

    def __isub__(self, other):
        self.value -= other
        return self

    def __add__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        new_year = self.__class__(self)
        return new_year.__iadd__(other)

    def __sub__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        new_year = self.__class__(self)
        return new_year.__isub__(other)

    def add_days(self, month, date, days):
        """ Adds the specified number of days to a date in the current year.

        :param month: the current month
        :param date: the current date (of the month)
        :param days: number of days to add
        :return: A 3-tuple comprising:
                A (possibly new) year object
                The month after addition
                The date after addition
        """
        date += days
        cls = self.month_class()
        if date > self.last_day(month):
            while date > self.last_day(month):
                date -= self.days_in_month(month)
                month = cls(month + 1 if month < self.months_in_year() else 1)
                if month == cls.start_year_month():
                    self += 1
        else:
            while date < self.first_day():
                if month == cls.start_year_month():
                    self -= 1
                month = cls(month - 1 if month > 1 else self.months_in_year())
                date += self.days_in_month(month)
        return (self, month, date)

    @classmethod
    def current_year(cls, atime):
        """Return a 2-tuple for the year containing the specified time atime.

        The tuple comprises:
        The year containing atime (an instance of cls, a subclass of Year)
        A RelTime object containing the difference between atime and the
        start of the year.

        This should be an abstract class method, but abstract class methods
        do not work in python 2 (fixed in python 3.4).
        """
        raise NotImplementedError

    def day_start(self, month, date):
        """Return the start (AbsTime) of the specified month and date."""
        day_count = 0
        for month_count in self.months():
            if month == month_count:
                day_count += date - self.first_day()
                break
            else:
                day_count += self.days_in_month(month_count)
        return self.start + RelTime(0, day_count)

    def __repr__(self):
        return "{0}({1})".format(type(self).__name__, self._value)

    def __str__(self):
        return "{0}".format(self._value)

    @classmethod
    def month_class(cls):
        """Return the associated class (subclass of Month) for months.

        This should be an abstract class method, but abstract class methods
        do not work in python 2 (fixed in python 3.4).
        """
        raise NotImplementedError

    def format_short_year(self, fmt):
        """ Format year (excluding hundreds) as a 2 digit number """
        return self.format_number(self.value % 100, 2, fmt)

    def format_full_year(self, fmt):
        """ Format year as a 4+ digit number """
        return self.format_number(self.value, 4, fmt)

    def format_day_of_month(self, day_of_month, fmt):
        """ Return the day of the month, formatted as 2 digits """
        return self.format_number(day_of_month, 2, fmt)

    @classmethod
    def min_date(cls):

        """Calculate the minimum date for this class.

        We only need to do it once per class."""
        if cls.MIN_DATE is None:
            cls.MIN_DATE = Date(cls, AbsTime(0, 0, 6))
        return cls.MIN_DATE

    ESCAPES = {
        'y': 'format_short_year',
        'Y': 'format_full_year',
        '_': None,
        '-': None,
        '0': None
    }


class RegularYear(Year):
    """Abstract subclass of Year with a regular cycle of years.

    Not all years are the same length, but there is usually a cycle of
    a fixed number of years, where the length of a cycle is fixed. For
    Hebrew years this is only true of the Molad used to calculate
    the start of the year (so cycles are not exactly the same length).
    """

    @classmethod
    def _years_per_cycle(cls):
        """Return number of years in a cycle."""
        raise NotImplementedError

    @classmethod
    def _cycle_duration(cls):
        """Return length of a cycle (RelTime)."""
        raise NotImplementedError

    @classmethod
    def estimate_current_year(cls, atime):
        """Return an estimate of the year containing the specified time.

        The calling function must allow for the possibility that it is not
        exactly correct."""
        return ((atime - cls.START_FIRST_YEAR) * cls._years_per_cycle() //
                cls._cycle_duration()) + cls.FIRST_YEAR

    @Year.value.setter
    def value(self, value):
        difference = value - self._value
        cycles = (difference + self._years_per_cycle() // 2) // \
            self._years_per_cycle()
        self._start += self._cycle_duration() * cycles
        self._value += self._years_per_cycle() * cycles
        while self._value < value:
            self._start += self.duration()
            self._value += 1
        while self._value > value:
            self._value -= 1
            self._start -= self.duration()

    @classmethod
    def current_year(cls, atime):
        estimate = cls.estimate_current_year(atime)
        year = cls(estimate)

        # now adjust it until it is exactly right.
        while year.start > atime:
            year -= 1

        while year.start + year.days_in_year() * DAY <= atime:
            year += 1

        if estimate != year.value:
            LOG.debug("Calculating year for %s, estimated %s actual %s",
                      atime, estimate, year.value)

        # We now have the right year.
        return year, atime - year.start


class DateTime(FormatPercentString):
    """A class comprising a Date object and a RelTime object.

    The object represents an instant in time. It comprises a Date object and
    a RelTime object (the latter should comprise only hours and chalakim).

    DateTime objects can be formatted using the standard python format command
    to create a string representing the date and time under the control of an
    explicit format string.

    Format Codes

    Directive   Meaning                             Example

    %a          Weekday as an abbreviated name      Sun, Mon, …, Sat

    %a#H        Weekday as an abbreviated name      יום א׳, יום ב׳, …, שבת
                using Hebrew letters as numbers

    %A          Weekday as full name                Sunday, Monday, …,
                                                    Saturday

    %A#H        Weekday as full Hebrew name         יום ראשון, יום שני, …, שבת

    %B          Month as full name                  January, February, …,
                                                    December
                                                    Nissan, Iyar, …, Ellul

    %B#H        Month as full name in Hebrew        ניסן, אייר, …, אלול
                letters

    %d          Day of the month as a zero-padded   01, 02, …, 31
                decimal number                      002, 003, …, 176 (daf)

    %-d         Day of the month as a decimal       1, 2, …, 31
                number                              2, 3, …, 176 (daf)

    %_d         Day of the month as a space-padded  ' 1', ' 2', …, 31
                decimal number                      ' 2', ' 3', …, 176 (daf)

    %~d#H       Day of the month using Hebrew       א׳, ב׳, …, ל׳
                letters as numbers                  (daf) ב׳, ג׳, …, קע״ו

    %H          Hour of the day as a zero-padded    00, 01, …, 23
                decimal number

    %-H         Hour of the day as a decimal        0, 1, …, 23
                number

    %_H         Hour of the day as a space-padded   ' 0', ' 1', …, 23
                decimal number

    %M          Minute of the hour as a             01, 02, …, 59
                zero-padded decimal number

    %-M         Minute of the hour as a decimal     1, 2, …, 59
                number

    %_M         Minute of the hour as a             ' 1', ' 2', …, 59
                space-padded decimal number

    %P          Part (1/18) of the minute as a      00, 01, …, 17
                zero-padded decimal number

    %-P         Part (1/18) of the minute as a      0, 1, …, 17
                decimal number

    %_P         Part (1/18) of the minute as a      ' 0', ' 1', …, 17
                space-padded decimal number

    %y          Year without century as a           00, 01, …, 99
                zero-padded decimal number

    %-y         Year without century as a decimal   0, 1, …, 99
                number

    %_y         Year without century as a           ' 0', ' 1', …, 99
                space-padded decimal number

    %~y#H       Year without millenium using        א׳, …, תתקצ״ט ,''
                Hebrew letters as numbers

    %Y          Year as a zero-padded decimal       0000, 0001, …, 9999
                number

    %-Y         Year as a decimal number            0, 1, …, 9999

    %_Y         Year as a space-padded decimal      '   0', '   1', …, 9999
                number

    %~Y#H       Year using Hebrew letters as       א׳, ב׳, ה׳תש״פ, …
                numbers

    %%          A single percent sign                   %

    NOTE: '#H' may be specified only once in the formatting string, at its
    end. It will then qualify all format codes within the formatting string.
    It is only valid if the year is a HebrewYear or DafYomiCycle.
    """

    SUBFORMATTERS = ('date', )

    def __init__(self, cls, atime):
        """ Construct a DateTime object

        :param cls: A subclass of Year
        :param atime: An AbsTime object (a point in time)
        """
        year, remainder = cls.current_year(atime)
        month = year.month_class().start_year_month()
        self.date = Date(year, month, year.first_day())
        days, remainder = remainder.days_chalakim
        self.date += days
        self.time = RelTime(0, 0, 0, remainder)
        self.date.day_start = atime - self.time

    def format_date(self, fmt):
        """ Format date according to format specified by fmt """
        return format(self.date, fmt)

    def format_hours(self, fmt):
        """ Format hours as a 2 digit number """
        return self.format_number(self.time.hours, 2, fmt)

    def format_minutes(self, fmt):
        """ Format minutes (excluding hours) as a 2 digit number """
        return self.format_number(self.time.minutes, 2, fmt)

    def format_chalakim(self, fmt):
        """ Format chalakim (excluding minutes) as a 2 digit number """
        return self.format_number(self.time.parts, 2, fmt)

    ESCAPES = {
        'H': 'format_hours',
        'M': 'format_minutes',
        'P': 'format_chalakim'
    }
