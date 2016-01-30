""" Tests for DateCache class.

This module contains tests for storing and retrieving a date according to
different calendars from a cache.
"""
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
from hbcal.hebrew_calendar.weekday import Weekday
from hbcal.hebrew_calendar.civil_year import GregorianYear, CivilMonth
from hbcal.hebrew_calendar.date import Date
from hbcal import DateCache
from hbcal.hebrew_calendar.hebrew_year import HebrewYear, HebrewMonth


class TestDateCache(unittest.TestCase):
    """ Tests for DateCache class.

    This class contains tests for storing and retrieving a date according to
    different calendars from a cache.
    """
    def setUp(self):
        self.date_cache = DateCache(Date(HebrewYear(5776),
                                         HebrewMonth.TISHRI, 1))

    def test_one_date(self):
        """Test retrieval of the only date in the cache"""
        self.assertEqual(Date(HebrewYear(5776), HebrewMonth.TISHRI, 1),
                         self.date_cache[HebrewYear])

    def test_weekday(self):
        """Test days attribute of DateCache class."""
        self.assertEqual(Weekday.MONDAY, self.date_cache.atime.days)

    def test_conversion(self):
        """Test conversion to another calendar within the cache."""
        self.assertEqual((Date(GregorianYear(2015),
                               CivilMonth.SEPTEMBER, 14)),
                         self.date_cache[GregorianYear])

if __name__ == "__main__":
    unittest.main()
