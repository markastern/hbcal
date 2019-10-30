# Copyright 2019 Mark Stern
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
from hbcal.hebrew_calendar.date import Date

from hbcal.hebrew_calendar.hebrew_year import HebrewYear, HebrewMonth
from hbcal.hebrew_calendar.civil_year import GregorianYear, CivilMonth
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class TestFormatDate(unittest.TestCase):

    def test_weekday_gregorian(self):
        self.assertEqual(format(Date(GregorianYear(2019),
                                     CivilMonth.SEPTEMBER, 9), '%A'),
                         'Monday')

    def test_weekday_hebrew_phonetics(self):
        self.assertEqual(format(Date(HebrewYear(5779),
                                     HebrewMonth.ELLUL, 9), '%A'),
                         'Monday')

    def test_weekday_hebrew_hebrew(self):
        self.assertEqual(format(Date(HebrewYear(5779),
                                     HebrewMonth.ELLUL, 9), '%A#H'),
                         u'\u05D9\u05D5\u05DD \u05E9\u05E0\u05D9')

    def test_short_weekday_gregorian(self):
        self.assertEqual(format(Date(GregorianYear(2019),
                                     CivilMonth.SEPTEMBER, 9), '%a'),
                         'Mon')

    def test_short_weekday_hebrew_phonetics(self):
        self.assertEqual(format(Date(HebrewYear(5779),
                                     HebrewMonth.ELLUL, 9), '%a'),
                         'Mon')

    def test_short_weekday_hebrew_hebrew(self):
        self.assertEqual(format(Date(HebrewYear(5779),
                                     HebrewMonth.ELLUL, 9), '%a#H'),
                         u'\u05D9\u05D5\u05DD \u05D1\u05F3')

    def test_month_name_gregorian(self):
        self.assertEqual(format(Date(GregorianYear(2019),
                                     CivilMonth.SEPTEMBER, 9), '%B'),
                         'September')

    def test_month_name_hebrew_phonetics(self):
        self.assertEqual(format(Date(HebrewYear(5779),
                                     HebrewMonth.ELLUL, 9), '%B'),
                         'Ellul')

    def test_month_name_hebrew_hebrew(self):
        self.assertEqual(format(Date(HebrewYear(5779),
                                     HebrewMonth.ELLUL, 9), '%B#H'),
                         u'\u05D0\u05DC\u05D5\u05DC')

    def test_day_of_month_gregorian(self):
        self.assertEqual(format(Date(GregorianYear(2019),
                                     CivilMonth.SEPTEMBER, 9), '%D'),
                         '09')

    def test_day_of_month_gregorian_0pad(self):
        self.assertEqual(format(Date(GregorianYear(2019),
                                     CivilMonth.SEPTEMBER, 9), '%0D'),
                         '09')

    def test_day_of_month_gregorian_spacepad(self):
        self.assertEqual(format(Date(GregorianYear(2019),
                                     CivilMonth.SEPTEMBER, 9), '%_D'),
                         ' 9')

    def test_day_of_month_gregorian_nopad(self):
        self.assertEqual(format(Date(GregorianYear(2019),
                                     CivilMonth.SEPTEMBER, 9), '%-D'),
                         '9')

    def test_day_of_month_hebrew(self):
        self.assertEqual(format(Date(HebrewYear(5779),
                                     HebrewMonth.ELLUL, 9), '%D'),
                         '09')

    def test_day_of_month_hebrew_0pad(self):
        self.assertEqual(format(Date(HebrewYear(5779),
                                     HebrewMonth.ELLUL, 9), '%0D'),
                         '09')

    def test_day_of_month_hebrew_spacepad(self):
        self.assertEqual(format(Date(HebrewYear(5779),
                                     HebrewMonth.ELLUL, 9), '%_D'),
                         ' 9')

    def test_day_of_month_hebrew_nopad(self):
        self.assertEqual(format(Date(HebrewYear(5779),
                                     HebrewMonth.ELLUL, 9), '%-D'),
                         '9')

    def test_day_of_month_hebrew_hebrew(self):
        self.assertEqual(format(Date(HebrewYear(5779),
                                     HebrewMonth.ELLUL, 9), '%D#H'),
                         '09')

    def test_day_of_month_hebrew_gematria(self):
        self.assertEqual(format(Date(HebrewYear(5779),
                                     HebrewMonth.ELLUL, 9), '%~D#H'),
                         u'\u05D8\u05F3')

    def test_short_year_gregorian(self):
        self.assertEqual(format(Date(GregorianYear(2008),
                                     CivilMonth.SEPTEMBER, 9), '%y'),
                         '08')

    def test_short_year_gregorian_0pad(self):
        self.assertEqual(format(Date(GregorianYear(2008),
                                     CivilMonth.SEPTEMBER, 9), '%0y'),
                         '08')

    def test_short_year_gregorian_spacepad(self):
        self.assertEqual(format(Date(GregorianYear(2008),
                                     CivilMonth.SEPTEMBER, 9), '%_y'),
                         ' 8')

    def test_short_year_gregorian_nopad(self):
        self.assertEqual(format(Date(GregorianYear(2008),
                                     CivilMonth.SEPTEMBER, 9), '%-y'),
                         '8')

    def test_short_year_hebrew(self):
        self.assertEqual(format(Date(HebrewYear(5708),
                                     HebrewMonth.ELLUL, 9), '%y'),
                         '08')

    def test_short_year_hebrew_0pad(self):
        self.assertEqual(format(Date(HebrewYear(5708),
                                     HebrewMonth.ELLUL, 9), '%0y'),
                         '08')

    def test_short_year_hebrew_spacepad(self):
        self.assertEqual(format(Date(HebrewYear(5708),
                                     HebrewMonth.ELLUL, 9), '%_y'),
                         ' 8')

    def test_short_year_hebrew_nopad(self):
        self.assertEqual(format(Date(HebrewYear(5708),
                                     HebrewMonth.ELLUL, 9), '%-y'),
                         '8')

    def test_short_year_hebrew_hebrew(self):
        self.assertEqual(format(Date(HebrewYear(5779),
                                     HebrewMonth.ELLUL, 9), '%y#H'),
                         '79')

    def test_short_year_hebrew_gematria(self):
        self.assertEqual(format(Date(HebrewYear(5779),
                                     HebrewMonth.ELLUL, 9), '%~y#H'),
                         u'\u05EA\u05E9\u05E2\u05F4\u05D8')

    def test_full_year_gregorian(self):
        self.assertEqual(format(Date(GregorianYear(8),
                                     CivilMonth.SEPTEMBER, 9), '%Y'),
                         '0008')

    def test_full_year_gregorian_0pad(self):
        self.assertEqual(format(Date(GregorianYear(8),
                                     CivilMonth.SEPTEMBER, 9), '%0Y'),
                         '0008')

    def test_full_year_gregorian_spacepad(self):
        self.assertEqual(format(Date(GregorianYear(8),
                                     CivilMonth.SEPTEMBER, 9), '%_Y'),
                         '   8')

    def test_full_year_gregorian_nopad(self):
        self.assertEqual(format(Date(GregorianYear(8),
                                     CivilMonth.SEPTEMBER, 9), '%-Y'),
                         '8')

    def test_full_year_hebrew(self):
        self.assertEqual(format(Date(HebrewYear(8),
                                     HebrewMonth.ELLUL, 9), '%Y'),
                         '0008')

    def test_full_year_hebrew_0pad(self):
        self.assertEqual(format(Date(HebrewYear(8),
                                     HebrewMonth.ELLUL, 9), '%0Y'),
                         '0008')

    def test_full_year_hebrew_spacepad(self):
        self.assertEqual(format(Date(HebrewYear(8),
                                     HebrewMonth.ELLUL, 9), '%_Y'),
                         '   8')

    def test_full_year_hebrew_nopad(self):
        self.assertEqual(format(Date(HebrewYear(8),
                                     HebrewMonth.ELLUL, 9), '%-Y'),
                         '8')

    def test_full_year_hebrew_hebrew(self):
        self.assertEqual(format(Date(HebrewYear(5779),
                                     HebrewMonth.ELLUL, 9), '%Y#H'),
                         '5779')

    def test_full_year_hebrew_gematria(self):
        self.assertEqual(format(Date(HebrewYear(5779),
                                     HebrewMonth.ELLUL, 9), '%~Y#H'),
                         u'\u05D4\u05F3\u05EA\u05E9\u05E2\u05F4\u05D8')

    def test_string(self):
        self.assertEqual(format(Date(GregorianYear(2019),
                                     CivilMonth.SEPTEMBER, 9), 'Hello World!'),
                         'Hello World!')

    def test_percent(self):
        self.assertEqual(format(Date(GregorianYear(2019),
                                     CivilMonth.SEPTEMBER, 9), '%%'),
                         '%')

    def test_percent_A(self):
        self.assertEqual(format(Date(GregorianYear(2019),
                                     CivilMonth.SEPTEMBER, 9), '%%A'),
                         '%A')


if __name__ == '__main__':
    unittest.main()
