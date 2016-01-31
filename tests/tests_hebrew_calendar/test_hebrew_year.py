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
from hbcal.hebrew_calendar.hebrew_year import HebrewYear, HebrewMonth
from hbcal.hebrew_calendar.abs_time import AbsTime

logging.basicConfig(filename='/dev/stdout', level=logging.DEBUG)


class TestMolad(unittest.TestCase):

    def test_minus1_month(self):
        """ Tests a month value of -1

        This is now valid. It is the last month of the year.
        """
        test_year = HebrewYear(2)
        self.assertEqual(AbsTime(21, 6, 5, 725), test_year.molad(-1))

    def test_minus12_month(self):
        """ Tests a month value of -12

        This is now valid. For negative months we count back from the end of
        the year.
        """
        test_year = HebrewYear(2)
        self.assertEqual(AbsTime(26, 0, 18, 438), test_year.molad(-12))

    def test_large_negative_month(self):
        test_year = HebrewYear(2)
        with self.assertRaises(date.MonthNotInRange):
            test_year.molad(-13)

    def test_minus1_month_leap(self):
        """ Tests a month value of -1 in a leap year

        This is now valid. It is the last month of the year.
        """
        test_year = HebrewYear(3)
        self.assertEqual(AbsTime(76, 5, 3, 234), test_year.molad(-1))

    def test_minus13_month_leap(self):
        """ Tests a month value of -13 in a leap year

        This is now valid. For negative months we count back from the end of
        the year.
        """
        test_year = HebrewYear(3)
        self.assertEqual(AbsTime(80, 6, 15, 1027), test_year.molad(-13))

    def test_large_negative_month_leap(self):
        test_year = HebrewYear(3)
        with self.assertRaises(date.MonthNotInRange):
            test_year.molad(-14)

    def test_zero_month(self):
        with self.assertRaises(ValueError):
            date.Date(HebrewYear(2), 0, 23)

    def test_month_too_high(self):
        test_year = HebrewYear(2)
        with self.assertRaises(date.MonthNotInRange):
            test_year.molad(14)

    def test_year2_month7(self):
        test_year = HebrewYear(2)
        self.assertEqual(AbsTime(0, 5, 14, 0), test_year.molad(7))

    def test_year2_month8(self):
        test_year = HebrewYear(2)
        self.assertEqual(AbsTime(5, 0, 2, 793), test_year.molad(8))

    def test_year2_month12(self):
        test_year = HebrewYear(2)
        self.assertEqual(AbsTime(21, 6, 5, 725), test_year.molad(12))

    def test_year2_month13(self):
        test_year = HebrewYear(2)
        self.assertEqual(AbsTime(21, 6, 5, 725), test_year.molad(13))

    def test_year2_month1(self):
        test_year = HebrewYear(2)
        self.assertEqual(AbsTime(26, 0, 18, 438), test_year.molad(1))

    def test_year2_month6(self):
        test_year = HebrewYear(2)
        self.assertEqual(AbsTime(47, 1, 10, 83), test_year.molad(6))

    def test_year3_month7(self):
        test_year = HebrewYear(3)
        self.assertEqual(AbsTime(51, 2, 22, 876), test_year.molad(7))

    def test_year19_month7(self):
        test_year = HebrewYear(19)
        self.assertEqual(AbsTime(886, 5, 0, 210), test_year.molad(7))

    def test_year20_month7(self):
        test_year = HebrewYear(20)
        self.assertEqual(AbsTime(941, 3, 21, 799), test_year.molad(7))

    def test_year21_month7(self):
        test_year = HebrewYear(21)
        self.assertEqual(AbsTime(992, 1, 6, 595), test_year.molad(7))

    def test_year22_month7(self):
        test_year = HebrewYear(22)
        self.assertEqual(AbsTime(1042, 5, 15, 391), test_year.molad(7))


class TestYearStart(unittest.TestCase):
    def test_year2(self):
        """Verify first, year, postponement to prevent RH on Friday"""
        self.assertEqual(AbsTime(0, 6, 0, 0), HebrewYear(2).start)

    def test_year3(self):
        """Verify postponement to prevent RH on Wednesday"""
        self.assertEqual(AbsTime(51, 4, 0, 0), HebrewYear(3).start)

    def test_year7(self):
        """Verify GaTRaD postponement"""
        self.assertEqual(AbsTime(262, 4, 0, 0), HebrewYear(7).start)

    def test_year8(self):
        """Verify postponement to prevent RH on Sunday"""
        self.assertEqual(AbsTime(313, 1, 0, 0), HebrewYear(8).start)

    def test_year75(self):
        """Verify BTUTKPaT postponement"""
        self.assertEqual(AbsTime(3810, 2, 0, 0), HebrewYear(75).start)

    def test_year_5708(self):
        """Verify fix for erroneous BTUTKPaT postponement in earlier version"""
        self.assertEqual(AbsTime(297728, 1, 0, 0), HebrewYear(5708).start)


class TestValidate(unittest.TestCase):

    def test_negative_year(self):
        with self.assertRaises(ValueError):
            date.Date(HebrewYear(-1), 3, 23)

    def test_zero_year(self):
        with self.assertRaises(ValueError):
            date.Date(HebrewYear(0), 3, 23)

    def test_year_one_before_creation(self):
        with self.assertRaises(ValueError):
            date.Date(HebrewYear(1), 6, 23)

    def test_year_one_after_creation(self):
        test_date = date.Date(HebrewYear(1), 6, 24)
        self.assertEqual((1, 6, 24),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_minus1_month(self):
        """ Tests a month value of -1

        This is now valid. It is the last month of the year.
        """
        test_date = date.Date(HebrewYear(2), -1, 23)
        self.assertEqual((2, HebrewMonth.ADAR_RISHON, 23),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_minus12_month(self):
        """ Tests a month value of -12

        This is now valid. For negative months we count back from the end of
        the year.
        """
        test_date = date.Date(HebrewYear(2), -12, 23)
        self.assertEqual((2, HebrewMonth.NISSAN, 23),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_large_negative_month(self):
        with self.assertRaises(ValueError):
            date.Date(HebrewYear(2), -13, 23)

    def test_minus1_month_leap(self):
        """ Tests a month value of -1 in a leap year

        This is now valid. It is the last month of the year.
        """
        test_date = date.Date(HebrewYear(3), -1, 23)
        self.assertEqual((3, HebrewMonth.ADAR_SHENI, 23),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_minus13_month_leap(self):
        """ Tests a month value of -13 in a leap year

        This is now valid. For negative months we count back from the end of
        the year.
        """
        test_date = date.Date(HebrewYear(3), -13, 23)
        self.assertEqual((3, HebrewMonth.NISSAN, 23),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_large_negative_month_leap(self):
        with self.assertRaises(ValueError):
            date.Date(HebrewYear(3), -14, 23)

    def test_zero_month(self):
        with self.assertRaises(ValueError):
            date.Date(HebrewYear(2), 0, 23)

    def test_month_too_big(self):
        with self.assertRaises(ValueError):
            date.Date(HebrewYear(2), 14, 23)

    def test_adar2_regular_year(self):
        test_date = date.Date(HebrewYear(2), 13, 23)
        self.assertEqual((2, 12, 23),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_adar2_leap_year(self):
        test_date = date.Date(HebrewYear(3), 13, 23)
        self.assertEqual((3, 13, 23),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_minus1_date(self):
        """ Tests a date value of -1.

        This is now valid. It is the last date of the month.
        """
        test_date = date.Date(HebrewYear(2), 7, -1)
        self.assertEqual((2, 7, 30),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_small_negative_date(self):
        """ Tests a small negative value for date.

        This is now valid. For negative dates we count back from the end of
        the month.
        """
        test_date = date.Date(HebrewYear(2), 7, -7)
        self.assertEqual((2, 7, 24),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_large_negative_date(self):
        with self.assertRaises(ValueError):
            date.Date(HebrewYear(2), 7, -31)

    def test_zero_date(self):
        with self.assertRaises(ValueError):
            date.Date(HebrewYear(2), 7, 0)

    def test_date_too_big(self):
        with self.assertRaises(ValueError):
            date.Date(HebrewYear(2), 7, 31)

    def test_tishri_30(self):
        test_date = date.Date(HebrewYear(2), 7, 30)
        self.assertEqual((2, 7, 30),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_cheshvan_30_long(self):
        test_date = date.Date(HebrewYear(2), 8, 30)
        self.assertEqual((2, 8, 30),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_cheshvan_30_short(self):
        test_date = date.Date(HebrewYear(3), 8, 30)
        self.assertEqual((3, 9, 1),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_kislev_30_long(self):
        test_date = date.Date(HebrewYear(2), 9, 30)
        self.assertEqual((2, 9, 30),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_kislev_30_short(self):
        test_date = date.Date(HebrewYear(3), 9, 30)
        self.assertEqual((3, 10, 1),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_teveth_30(self):
        with self.assertRaises(ValueError):
            date.Date(HebrewYear(2), 10, 30)

    def test_shevat_30(self):
        test_date = date.Date(HebrewYear(2), 11, 30)
        self.assertEqual((2, 11, 30),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_adar_30(self):
        test_date = date.Date(HebrewYear(2), 12, 30)
        self.assertEqual((2, 1, 1),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_adar1_30(self):
        test_date = date.Date(HebrewYear(3), 12, 30)
        self.assertEqual((3, 12, 30),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_adar2_30(self):
        with self.assertRaises(ValueError):
            date.Date(HebrewYear(3), 13, 30)

    def test_nissan_30(self):
        test_date = date.Date(HebrewYear(2), 1, 30)
        self.assertEqual((2, 1, 30),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_iyar_30(self):
        with self.assertRaises(ValueError):
            date.Date(HebrewYear(2), 2, 30)

    def test_sivan_30(self):
        test_date = date.Date(HebrewYear(2), 3, 30)
        self.assertEqual((2, 3, 30),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_tammuz_30(self):
        with self.assertRaises(ValueError):
            date.Date(HebrewYear(2), 4, 30)

    def test_av_30(self):
        test_date = date.Date(HebrewYear(2), 5, 30)
        self.assertEqual((2, 5, 30),
                         (test_date.year.value, test_date.month,
                          test_date.date))

    def test_ellul_30(self):
        with self.assertRaises(ValueError):
            date.Date(HebrewYear(2), 6, 30)


class TestCurrentDate(unittest.TestCase):
    def test_start_of_first_year(self):
        self.assertEqual(date.Date(HebrewYear(2), HebrewMonth.TISHRI, 1),
                         date.Date(HebrewYear, AbsTime(0, 6, 0, 0)))

    def test_end_first_day(self):
        self.assertEqual(date.Date(HebrewYear(2), HebrewMonth.TISHRI, 1),
                         date.Date(HebrewYear, AbsTime(0, 6, 23, 1079)))

    def test_start_second_day(self):
        self.assertEqual(date.Date(HebrewYear(2), HebrewMonth.TISHRI, 2),
                         date.Date(HebrewYear, AbsTime(1, 0, 0, 0)))

    def test_last_day_tishri(self):
        self.assertEqual(date.Date(HebrewYear(2), HebrewMonth.TISHRI, 30),
                         date.Date(HebrewYear, AbsTime(5, 0, 0, 0)))

    def test_first_day_cheshvan(self):
        self.assertEqual(date.Date(HebrewYear(2), HebrewMonth.CHESHVAN, 1),
                         date.Date(HebrewYear, AbsTime(5, 1, 0, 0)))

    def test_last_day_ellul(self):
        self.assertEqual(date.Date(HebrewYear(2), HebrewMonth.ELLUL, 29),
                         date.Date(HebrewYear, AbsTime(51, 3, 6, 0)))

    def test_first_day_second_year(self):
        self.assertEqual(date.Date(HebrewYear(3), HebrewMonth.TISHRI, 1),
                         date.Date(HebrewYear, AbsTime(51, 4, 6, 0)))

    def test_first_day_recent_year(self):
        self.assertEqual(date.Date(HebrewYear(5775), HebrewMonth.TISHRI, 1),
                         date.Date(HebrewYear, AbsTime(301225, 4, 6, 0)))

    # Check that we still get the right answers even if we use a ridiculously
    # low (or high) heuristic for the numbe of weeks in a year.
    def test_first_day_recent_year_low_heuristic(self):

        class HebrewYearLowWeeks(HebrewYear):
            @classmethod
            def estimate_current_year(cls, atime):
                return int((atime.weeks * 7 + atime.days) / 100 + 0.5) +\
                    cls.first_year()

        self.assertEqual(date.Date(HebrewYearLowWeeks(5775),
                                   HebrewMonth.TISHRI, 1),
                         date.Date(HebrewYearLowWeeks,
                                   AbsTime(301225, 4, 6, 0)))

    def test_first_day_recent_year_high_heuristic(self):

        class HebrewYearHighWeeks(HebrewYear):
            @classmethod
            def estimate_current_year(cls, atime):
                return int((atime.weeks * 7 + atime.days) / 1000 + 0.5) +\
                    cls.first_year()

        self.assertEqual(date.Date(HebrewYearHighWeeks(5775),
                                   HebrewMonth.TISHRI, 1),
                         date.Date(HebrewYearHighWeeks,
                                   AbsTime(301225, 4, 6, 0)))


class TestDayStart(unittest.TestCase):
    def test_start_of_first_year(self):
        self.assertEqual(date.Date(HebrewYear(2),
                                   HebrewMonth.TISHRI, 1).day_start(),
                         AbsTime(0, 6, 0, 0))

    def test_second_day(self):
        self.assertEqual(date.Date(HebrewYear(2),
                                   HebrewMonth.TISHRI, 2).day_start(),
                         AbsTime(1, 0, 0, 0))

    def test_last_day_tishri(self):
        self.assertEqual(date.Date(HebrewYear(2),
                                   HebrewMonth.TISHRI, 30).day_start(),
                         AbsTime(5, 0, 0, 0))

    def test_first_day_cheshvan(self):
        self.assertEqual(date.Date(HebrewYear(2),
                                   HebrewMonth.CHESHVAN, 1).day_start(),
                         AbsTime(5, 1, 0, 0))

    def test_last_day_ellul(self):
        self.assertEqual(date.Date(HebrewYear(2),
                                   HebrewMonth.ELLUL, 29).day_start(),
                         AbsTime(51, 3, 0, 0))

    def test_first_day_second_year(self):
        self.assertEqual(date.Date(HebrewYear(3),
                                   HebrewMonth.TISHRI, 1).day_start(),
                         AbsTime(51, 4, 0, 0))

    def test_first_day_recent_year(self):
        self.assertEqual(date.Date(HebrewYear(5775),
                                   HebrewMonth.TISHRI, 1).day_start(),
                         AbsTime(301225, 4, 0, 0))


if __name__ == '__main__':
    unittest.main()
