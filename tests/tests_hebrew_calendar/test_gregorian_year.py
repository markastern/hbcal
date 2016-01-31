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

from hbcal.hebrew_calendar import date
from hbcal.hebrew_calendar.civil_year import CivilMonth, GregorianYear
from hbcal.hebrew_calendar.abs_time import AbsTime

logging.basicConfig(filename='/dev/stdout', level=logging.DEBUG)


class TestYearStart(unittest.TestCase):
    def test_first_year(self):
        self.assertEqual(AbsTime(18, 6, 6, 0), GregorianYear(-3758).start)

    def test_second_year(self):
        self.assertEqual(AbsTime(71, 0, 6, 0), GregorianYear(-3757).start)

    def test_third_year(self):
        self.assertEqual(AbsTime(123, 1, 6, 0), GregorianYear(-3756).start)

    def test_fourth_year(self):
        self.assertEqual(AbsTime(175, 3, 6, 0), GregorianYear(-3755).start)

    def test_century_year(self):
        self.assertEqual(AbsTime(3097, 2, 6, 0), GregorianYear(-3699).start)

    def test_four_century_year(self):
        self.assertEqual(AbsTime(8315, 1, 6, 0), GregorianYear(-3599).start)


class TestValidate(unittest.TestCase):
    def test_before_creation(self):
        with self.assertRaises(ValueError):
            date.Date(GregorianYear(-3759), 8, 21)

    def test_after_creation(self):
        test_date = date.Date(GregorianYear(-3759), 8, 22)
        self.assertEqual((-3759, 8, 22),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_minus1_month(self):
        """ Tests a month value of -1

        This is now valid. It is the last month of the year.
        """
        test_date = date.Date(GregorianYear(2000), -1, 23)
        self.assertEqual((2000, CivilMonth.DECEMBER, 23),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_minus12_month(self):
        """ Tests a month value of -12

        This is now valid. For negative months we count back from the end of
        the year.
        """
        test_date = date.Date(GregorianYear(2000), -12, 23)
        self.assertEqual((2000, CivilMonth.JANUARY, 23),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_large_negative_month(self):
        with self.assertRaises(ValueError):
            date.Date(GregorianYear(2000), -13, 23)

    def test_zero_month(self):
        with self.assertRaises(ValueError):
            date.Date(GregorianYear(2000), 0, 23)

    def test_month_too_big(self):
        with self.assertRaises(ValueError):
            date.Date(GregorianYear(2000), 13, 23)

    def test_minus1_date(self):
        """ Tests a date value of -1.

        This is now valid. It is the last date of the month.
        """
        test_date = date.Date(GregorianYear(2000), 7, -1)
        self.assertEqual((2000, 7, 31),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_small_negative_date(self):
        """ Tests a small negative value for date.

        This is now valid. For negative dates we count back from the end of
        the month.
        """
        test_date = date.Date(GregorianYear(2000), 7, -7)
        self.assertEqual((2000, 7, 25),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_large_negative_date(self):
        with self.assertRaises(ValueError):
            date.Date(GregorianYear(2000), 7, -32)

    def test_zero_date(self):
        with self.assertRaises(ValueError):
            date.Date(GregorianYear(2000), 7, 0)

    def test_date_too_big(self):
        with self.assertRaises(ValueError):
            date.Date(GregorianYear(2000), 7, 32)

    def test_january_31(self):
        test_date = date.Date(GregorianYear(2000), 1, 31)
        self.assertEqual((2000, 1, 31),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_february_29_regular(self):
        """Tests February 29 in a non-leap year.

        This may become valid in the future
        (and convert to February 28 or March 1)."""
        with self.assertRaises(ValueError):
            date.Date(GregorianYear(2001), 2, 29)

    def test_february_29_leap_year(self):
        test_date = date.Date(GregorianYear(2000), 2, 29)
        self.assertEqual((2000, 2, 29),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_february_30_leap_year(self):
        with self.assertRaises(ValueError):
            date.Date(GregorianYear(2000), 2, 30)

    def test_march_31(self):
        test_date = date.Date(GregorianYear(2000), 3, 30)
        self.assertEqual((2000, 3, 30),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_april_31(self):
        with self.assertRaises(ValueError):
            date.Date(GregorianYear(2000), 4, 31)

    def test_may_31(self):
        test_date = date.Date(GregorianYear(2000), 5, 31)
        self.assertEqual((2000, 5, 31),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_june_31(self):
        with self.assertRaises(ValueError):
            date.Date(GregorianYear(2000), 6, 31)

    def test_july_31(self):
        test_date = date.Date(GregorianYear(2000), 7, 31)
        self.assertEqual((2000, 7, 31),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_august_31(self):
        test_date = date.Date(GregorianYear(2000), 8, 31)
        self.assertEqual((2000, 8, 31),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_september_31(self):
        with self.assertRaises(ValueError):
            date.Date(GregorianYear(2000), 9, 31)

    def test_october_31(self):
        test_date = date.Date(GregorianYear(2000), 10, 31)
        self.assertEqual((2000, 10, 31),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_november_31(self):
        with self.assertRaises(ValueError):
            date.Date(GregorianYear(2000), 11, 31)

    def test_december_31(self):
        test_date = date.Date(GregorianYear(2000), 12, 31)
        self.assertEqual((2000, 12, 31),
                         (test_date.year.value, test_date.month,
                          test_date.date))


class TestCurrentDate(unittest.TestCase):
    def test_start_of_first_year(self):
        self.assertEqual(date.Date(GregorianYear(-3758),
                                   CivilMonth.JANUARY, 1),
                         date.Date(GregorianYear, AbsTime(18, 6, 6, 0)))

    def test_end_first_day(self):
        self.assertEqual(date.Date(GregorianYear(-3758),
                                   CivilMonth.JANUARY, 1),
                         date.Date(GregorianYear, AbsTime(19, 0, 5, 1079)))

    def test_start_second_day(self):
        self.assertEqual(date.Date(GregorianYear(-3758),
                                   CivilMonth.JANUARY, 2),
                         date.Date(GregorianYear, AbsTime(19, 0, 6, 0)))

    def test_last_day_january(self):
        self.assertEqual(date.Date(GregorianYear(-3758),
                                   CivilMonth.JANUARY, 31),
                         date.Date(GregorianYear, AbsTime(23, 1, 6, 0)))

    def test_first_day_february(self):
        self.assertEqual(date.Date(GregorianYear(-3758),
                                   CivilMonth.FEBRUARY, 1),
                         date.Date(GregorianYear, AbsTime(23, 2, 6, 0)))

    def test_last_day_december(self):
        self.assertEqual(date.Date(GregorianYear(-3758),
                                   CivilMonth.DECEMBER, 31),
                         date.Date(GregorianYear, AbsTime(70, 6, 6, 0)))

    def test_first_day_second_year(self):
        self.assertEqual(date.Date(GregorianYear(-3757),
                                   CivilMonth.JANUARY, 1),
                         date.Date(GregorianYear, AbsTime(71, 0, 6, 0)))

    def test_first_day_recent_year(self):
        self.assertEqual(date.Date(GregorianYear(2000),
                                   CivilMonth.JANUARY, 1),
                         date.Date(GregorianYear, AbsTime(300456, 6, 6, 0)))

    # Check that we still get the right answers even if we use a ridiculously
    # low (or high) heuristic for the numbe of weeks in a year.
    def test_first_day_recent_year_low_heuristic(self):
        class GregorianLowDays(GregorianYear):
            @classmethod
            def estimate_current_year(cls, atime):
                return int((atime.weeks * 7 + atime.days) / 300 + 0.5) +\
                    cls.first_year()

        self.assertEqual(date.Date(GregorianLowDays(2000),
                                   CivilMonth.JANUARY, 1),
                         date.Date(GregorianLowDays,
                                   AbsTime(300456, 6, 6, 0)))

    def test_first_day_recent_year_high_heuristic(self):
        class GregorianHighDays(GregorianYear):
            @classmethod
            def estimate_current_year(cls, atime):
                return int((atime.weeks * 7 + atime.days) / 400 + 0.5) +\
                    cls.first_year()

        self.assertEqual(date.Date(GregorianHighDays(2000),
                                   CivilMonth.JANUARY, 1),
                         date.Date(GregorianHighDays,
                                   AbsTime(300456, 6, 6, 0)))


class TestDayStart(unittest.TestCase):
    def test_start_of_first_year(self):
        self.assertEqual(date.Date(GregorianYear(-3758),
                                   CivilMonth.JANUARY, 1).day_start(),
                         AbsTime(18, 6, 6, 0))

    def test_second_day(self):
        self.assertEqual(date.Date(GregorianYear(-3758),
                                   CivilMonth.JANUARY, 2).day_start(),
                         AbsTime(19, 0, 6, 0))

    def test_last_day_january(self):
        self.assertEqual(date.Date(GregorianYear(-3758),
                                   CivilMonth.JANUARY, 31).day_start(),
                         AbsTime(23, 1, 6, 0))

    def test_first_day_february(self):
        self.assertEqual(date.Date(GregorianYear(-3758),
                                   CivilMonth.FEBRUARY, 1).day_start(),
                         AbsTime(23, 2, 6, 0))

    def test_last_day_december(self):
        self.assertEqual(date.Date(GregorianYear(-3758),
                                   CivilMonth.DECEMBER, 31).day_start(),
                         AbsTime(70, 6, 6, 0))

    def test_first_day_second_year(self):
        self.assertEqual(date.Date(GregorianYear(-3757),
                                   CivilMonth.JANUARY, 1).day_start(),
                         AbsTime(71, 0, 6, 0))

    def test_first_day_recent_year(self):
        self.assertEqual(date.Date(GregorianYear(2000),
                                   CivilMonth.JANUARY, 1).day_start(),
                         AbsTime(300456, 6, 6, 0))


if __name__ == '__main__':
    unittest.main()
