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
from hbcal.hebrew_calendar.date import DateNotInRange

from hbcal.hebrew_calendar.hebrew_year import HebrewYear, HebrewMonth
logging.basicConfig(filename='/dev/stdout', level=logging.DEBUG)


class TestOmer(unittest.TestCase):

    def test_other_month(self):
        self.assertIsNone(HebrewYear(2000).omer_day(HebrewMonth.ADAR_RISHON,
                                                    15))

    def test_before_omer(self):
        self.assertIsNone(HebrewYear(2000).omer_day(HebrewMonth.NISSAN, 15))

    def test_first_day(self):
        self.assertEqual(HebrewYear(2000).omer_day(HebrewMonth.NISSAN,
                                                   16), 1)

    def test_second_day(self):
        self.assertEqual(HebrewYear(2000).omer_day(HebrewMonth.NISSAN,
                                                   17), 2)

    def test_end_of_nissan(self):
        self.assertEqual(HebrewYear(2000).omer_day(HebrewMonth.NISSAN,
                                                   30), 15)

    def test_start_of_iyar(self):
        self.assertEqual(HebrewYear(2000).omer_day(HebrewMonth.IYAR,
                                                   1), 16)

    def test_end_of_iyar(self):
        self.assertEqual(HebrewYear(2000).omer_day(HebrewMonth.IYAR,
                                                   29), 44)

    def test_start_of_sivan(self):
        self.assertEqual(HebrewYear(2000).omer_day(HebrewMonth.SIVAN,
                                                   1), 45)

    def test_last_day(self):
        self.assertEqual(HebrewYear(2000).omer_day(HebrewMonth.SIVAN, 5), 49)

    def test_after_omer(self):
        self.assertIsNone(HebrewYear(2000).omer_day(HebrewMonth.SIVAN, 6))

    def test_invalid_date(self):
        with self.assertRaises(DateNotInRange):
            HebrewYear(2000).omer_day(HebrewMonth.SIVAN, 0)


if __name__ == '__main__':
    unittest.main()
