# Copyright 2015 Mark Stern
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

import unittest
import logging
import sys

from hbcal.hebrew_calendar import date
from hbcal.hebrew_calendar.civil_year import CivilMonth

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class YearCounts(date.Year):

    def days_in_month(self, month):
        return 30

    def months_in_year(self):
        return 12

    def days_in_year(self):
        return 365


class YearRest(date.Year):

    START_FIRST_YEAR = 0

    @classmethod
    def month_class(cls):
        return CivilMonth

    @date.Year.value.setter
    def value(self, value):
        self._value = value


class YearNoDaysInMonth(YearRest):

    def months_in_year(self):
        return 12

    def days_in_year(self):
        return 365


class YearNoMonthsInYear(YearRest):

    def days_in_month(self, month):
        return 30

    def days_in_year(self):
        return 365


class YearNoDaysInYear(YearRest):

    def days_in_month(self, month):
        return 30

    def months_in_year(self):
        return 12


class YearNoFirstYear(YearCounts):

    FIRST_YEAR = 0

    @classmethod
    def month_class(cls):
        return CivilMonth

    @date.Year.value.setter
    def value(self, value):
        self._value = value


class TestAbstractYear(unittest.TestCase):
    def test_year_instance(self):
        with self.assertRaises(TypeError):
            date.Year(1)


class TestNoDaysInMonth(unittest.TestCase):
    def test_year_instance(self):
        with self.assertRaises(TypeError):
            YearNoDaysInMonth(1)


class TestNoMonthsInYear(unittest.TestCase):
    def test_year_instance(self):
        with self.assertRaises(TypeError):
            YearNoMonthsInYear(1)


class TestNoDaysInYear(unittest.TestCase):
    def test_year_instance(self):
        with self.assertRaises(TypeError):
            YearNoDaysInYear(1)


class TestYearNoFirstYear(unittest.TestCase):
    def test_year_instance(self):
        with self.assertRaises(TypeError):
            YearNoFirstYear(1)


if __name__ == '__main__':
    unittest.main()
