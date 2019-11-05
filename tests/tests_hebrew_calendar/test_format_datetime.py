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
from hbcal.hebrew_calendar.abs_time import AbsTime
from hbcal.hebrew_calendar.date import DateTime

from hbcal.hebrew_calendar.hebrew_year import HebrewYear
from hbcal.hebrew_calendar.civil_year import GregorianYear
from hbcal.hebrew_calendar.daf_yomi import DafYomiCycle
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class TestFormatDateTime(unittest.TestCase):

    def test_weekday_gregorian(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                         AbsTime(301484, 1, 9, 40)), '%A'),
                         'Monday')

    def test_weekday_hebrew_phonetics(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                         AbsTime(301484, 1, 9, 40)), '%A'),
                         'Monday')

    def test_weekday_hebrew_hebrew(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                         AbsTime(301484, 1, 9, 40)), '%A#H'),
                         u'\u05D9\u05D5\u05DD \u05E9\u05E0\u05D9')

    def test_short_weekday_gregorian(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                         AbsTime(301484, 1, 9, 40)), '%a'),
                         'Mon')

    def test_short_weekday_hebrew_phonetics(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                         AbsTime(301484, 1, 9, 40)), '%a'),
                         'Mon')

    def test_short_weekday_hebrew_hebrew(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                         AbsTime(301484, 1, 9, 40)), '%a#H'),
                         u'\u05D9\u05D5\u05DD \u05D1\u05F3')

    def test_month_name_gregorian(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                         AbsTime(301484, 1, 9, 40)), '%B'),
                         'September')

    def test_month_name_hebrew_phonetics(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(301484, 1, 9, 40)), '%B'), 'Ellul')

    def test_month_name_hebrew_hebrew(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                         AbsTime(301484, 1, 9, 40)), '%B#H'),
                         u'\u05D0\u05DC\u05D5\u05DC')

    def test_day_of_month_gregorian(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                AbsTime(301484, 1, 9, 40)), '%D'), '09')

    def test_day_of_month_gregorian_0pad(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                AbsTime(301484, 1, 9, 40)), '%0D'), '09')

    def test_day_of_month_gregorian_spacepad(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                AbsTime(301484, 1, 9, 40)), '%_D'), ' 9')

    def test_day_of_month_gregorian_nopad(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                AbsTime(301484, 1, 9, 40)), '%-D'), '9')

    def test_day_of_month_hebrew(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(301484, 1, 9, 40)), '%D'), '09')

    def test_day_of_month_hebrew_0pad(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(301484, 1, 9, 40)), '%0D'), '09')

    def test_day_of_month_hebrew_spacepad(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(301484, 1, 9, 40)), '%_D'), ' 9')

    def test_day_of_month_hebrew_nopad(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(301484, 1, 9, 40)), '%-D'), '9')

    def test_day_of_month_hebrew_hebrew(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(301484, 1, 9, 40)), '%D#H'), '09')

    def test_day_of_month_hebrew_gematria(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(301484, 1, 9, 40)), '%~D#H'),
                         u'\u05D8\u05F3')

    def test_day_of_month_daf(self):
        self.assertEqual(format(DateTime(DafYomiCycle,
                                         AbsTime(301348, 3, 4, 40)), '%D'),
                         '009')

    def test_day_of_month_daf_0pad(self):
        self.assertEqual(format(DateTime(DafYomiCycle,
                                         AbsTime(301348, 3, 4, 40)), '%0D'),
                         '009')

    def test_day_of_month_daf_spacepad(self):
        self.assertEqual(format(DateTime(DafYomiCycle,
                                         AbsTime(301348, 3, 4, 40)), '%_D'),
                         '  9')

    def test_day_of_month_daf_nopad(self):
        self.assertEqual(format(DateTime(DafYomiCycle,
                                         AbsTime(301348, 3, 4, 40)), '%-D'),
                         '9')

    def test_day_of_month_daf_hebrew(self):
        self.assertEqual(format(DateTime(DafYomiCycle,
                                         AbsTime(301348, 3, 4, 40)), '%D#H'),
                         '009')

    def test_day_of_month_daf_gematria(self):
        self.assertEqual(format(DateTime(DafYomiCycle,
                                         AbsTime(301368, 3, 4, 40)), '%~D#H'),
                         u'\u05E7\u05DE\u05F4\u05D8')

    def test_short_year_gregorian(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                AbsTime(300910, 2, 9, 40)), '%y'), '08')

    def test_short_year_gregorian_0pad(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                AbsTime(300910, 2, 9, 40)), '%0y'), '08')

    def test_short_year_gregorian_spacepad(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                AbsTime(300910, 2, 9, 40)), '%_y'), ' 8')

    def test_short_year_gregorian_nopad(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                AbsTime(300910, 2, 9, 40)), '%-y'), '8')

    def test_short_year_hebrew(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(297780, 1, 9, 40)), '%y'), '08')

    def test_short_year_hebrew_0pad(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(297780, 1, 9, 40)), '%0y'), '08')

    def test_short_year_hebrew_spacepad(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(297780, 1, 9, 40)), '%_y'), ' 8')

    def test_short_year_hebrew_nopad(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(297780, 1, 9, 40)), '%-y'), '8')

    def test_short_year_hebrew_hebrew(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(301484, 1, 9, 40)), '%y#H'), '79')

    def test_short_year_hebrew_gematria(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(301484, 1, 9, 40)), '%~y#H'),
                         u'\u05EA\u05E9\u05E2\u05F4\u05D8')

    def test_short_year_hebrew_gematria_zero(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(312984, 1, 9, 40)), '%~y#H'), '')

    def test_full_year_gregorian(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                AbsTime(196555, 2, 9, 40)), '%Y'), '0008')

    def test_full_year_gregorian_0pad(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                AbsTime(196555, 2, 9, 40)), '%0Y'), '0008')

    def test_full_year_gregorian_spacepad(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                AbsTime(196555, 2, 9, 40)), '%_Y'), '   8')

    def test_full_year_gregorian_nopad(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                AbsTime(196555, 2, 9, 40)), '%-Y'), '8')

    def test_full_year_hebrew(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(364, 6, 9, 40)), '%Y'), '0008')

    def test_full_year_hebrew_0pad(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(364, 6, 9, 40)), '%0Y'), '0008')

    def test_full_year_hebrew_spacepad(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(364, 6, 9, 40)), '%_Y'), '   8')

    def test_full_year_hebrew_nopad(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(364, 6, 9, 40)), '%-Y'), '8')

    def test_full_year_hebrew_hebrew(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(301484, 1, 9, 40)), '%Y#H'), '5779')

    def test_full_year_hebrew_gematria(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(301484, 1, 9, 40)), '%~Y#H'),
                         u'\u05D4\u05F3\u05EA\u05E9\u05E2\u05F4\u05D8')

    def test_hours_gregorian(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                AbsTime(196555, 2, 9, 40)), '%H'), '03')

    def test_hours_gregorian_0pad(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                AbsTime(196555, 2, 9, 40)), '%0H'), '03')

    def test_hours_gregorian_spacepad(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                AbsTime(196555, 2, 9, 40)), '%_H'), ' 3')

    def test_hours_gregorian_nopad(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                AbsTime(196555, 2, 9, 40)), '%-H'), '3')

    def test_hours_hebrew(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(364, 6, 9, 40)), '%H'), '09')

    def test_hours_hebrew_0pad(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(364, 6, 9, 40)), '%0H'), '09')

    def test_hours_hebrew_spacepad(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(364, 6, 9, 40)), '%_H'), ' 9')

    def test_hours_hebrew_nopad(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(364, 6, 9, 40)), '%-H'), '9')

    def test_hours_hebrew_hebrew(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(301484, 1, 9, 40)), '%H#H'), '09')

    def test_minutes_gregorian(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                AbsTime(196555, 2, 9, 40)), '%M'), '02')

    def test_minutes_gregorian_0pad(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                AbsTime(196555, 2, 9, 40)), '%0M'), '02')

    def test_minutes_gregorian_spacepad(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                AbsTime(196555, 2, 9, 40)), '%_M'), ' 2')

    def test_minutes_gregorian_nopad(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                AbsTime(196555, 2, 9, 40)), '%-M'), '2')

    def test_minutes_hebrew(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(364, 6, 9, 40)), '%M'), '02')

    def test_minutes_hebrew_0pad(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(364, 6, 9, 40)), '%0M'), '02')

    def test_minutes_hebrew_spacepad(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(364, 6, 9, 40)), '%_M'), ' 2')

    def test_minutes_hebrew_nopad(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(364, 6, 9, 40)), '%-M'), '2')

    def test_minutes_hebrew_hebrew(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(301484, 1, 9, 40)), '%M#H'), '02')

    def test_remaining_parts_gregorian(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                AbsTime(196555, 2, 9, 40)), '%P'), '04')

    def test_remaining_parts_gregorian_0pad(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                AbsTime(196555, 2, 9, 40)), '%0P'), '04')

    def test_remaining_parts_gregorian_spacepad(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                AbsTime(196555, 2, 9, 40)), '%_P'), ' 4')

    def test_remaining_parts_gregorian_nopad(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                AbsTime(196555, 2, 9, 40)), '%-P'), '4')

    def test_remaining_parts_hebrew(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(364, 6, 9, 40)), '%P'), '04')

    def test_remaining_parts_hebrew_0pad(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(364, 6, 9, 40)), '%0P'), '04')

    def test_remaining_parts_hebrew_spacepad(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(364, 6, 9, 40)), '%_P'), ' 4')

    def test_remaining_parts_hebrew_nopad(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(364, 6, 9, 40)), '%-P'), '4')

    def test_remaining_parts_hebrew_hebrew(self):
        self.assertEqual(format(DateTime(HebrewYear,
                                AbsTime(301484, 1, 9, 40)), '%P#H'), '04')

    def test_string(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                         AbsTime(301484, 1, 9, 40)),
                                'Hello World!'),
                         'Hello World!')

    def test_percent(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                         AbsTime(301484, 1, 9, 40)), '%%'),
                         '%')

    def test_percent_A(self):
        self.assertEqual(format(DateTime(GregorianYear,
                                         AbsTime(301484, 1, 9, 40)), '%%A'),
                         '%A')


if __name__ == '__main__':
    unittest.main()
