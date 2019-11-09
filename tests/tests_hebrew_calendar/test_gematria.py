"""Tests for to_letters function"""

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

from hbcal.hebrew_calendar.gematria import to_letters
import unittest


class TestToLetters(unittest.TestCase):
    """Tests for converting numbers to Hebrew letters"""

    def test_one(self):
        self.assertEqual(u"\u05D0\u05F3", to_letters(1))

    def test_two(self):
        self.assertEqual(u"\u05D1\u05F3", to_letters(2))

    def test_three(self):
        self.assertEqual(u"\u05D2\u05F3", to_letters(3))

    def test_four(self):
        self.assertEqual(u"\u05D3\u05F3", to_letters(4))

    def test_five(self):
        self.assertEqual(u"\u05D4\u05F3", to_letters(5))

    def test_six(self):
        self.assertEqual(u"\u05D5\u05F3", to_letters(6))

    def test_seven(self):
        self.assertEqual(u"\u05D6\u05F3", to_letters(7))

    def test_eight(self):
        self.assertEqual(u"\u05D7\u05F3", to_letters(8))

    def test_nine(self):
        self.assertEqual(u"\u05D8\u05F3", to_letters(9))

    def test_ten(self):
        self.assertEqual(u"\u05D9\u05F3", to_letters(10))

    def test_eleven(self):
        self.assertEqual(u"\u05D9\u05F4\u05D0", to_letters(11))

    def test_twelve(self):
        self.assertEqual(u"\u05D9\u05F4\u05D1", to_letters(12))

    def test_thirteen(self):
        self.assertEqual(u"\u05D9\u05F4\u05D2", to_letters(13))

    def test_forteen(self):
        self.assertEqual(u"\u05D9\u05F4\u05D3", to_letters(14))

    def test_fifteen(self):
        self.assertEqual(u"\u05D8\u05F4\u05D5", to_letters(15))

    def test_sixteen(self):
        self.assertEqual(u"\u05D8\u05F4\u05D6", to_letters(16))

    def test_seventeen(self):
        self.assertEqual(u"\u05D9\u05F4\u05D6", to_letters(17))

    def test_eighteen(self):
        self.assertEqual(u"\u05D9\u05F4\u05D7", to_letters(18))

    def test_nineteen(self):
        self.assertEqual(u"\u05D9\u05F4\u05D8", to_letters(19))

    def test_twenty(self):
        self.assertEqual(u"\u05DB\u05F3", to_letters(20))

    def test_twenty_one(self):
        self.assertEqual(u"\u05DB\u05F4\u05D0", to_letters(21))

    def test_twenty_five(self):
        self.assertEqual(u"\u05DB\u05F4\u05D4", to_letters(25))

    def test_thirty(self):
        self.assertEqual(u"\u05DC\u05F3", to_letters(30))

    def test_forty(self):
        self.assertEqual(u"\u05DE\u05F3", to_letters(40))

    def test_fifty(self):
        self.assertEqual(u"\u05E0\u05F3", to_letters(50))

    def test_sixty(self):
        self.assertEqual(u"\u05E1\u05F3", to_letters(60))

    def test_seventy(self):
        self.assertEqual(u"\u05E2\u05F3", to_letters(70))

    def test_eighty(self):
        self.assertEqual(u"\u05E4\u05F3", to_letters(80))

    def test_ninety(self):
        self.assertEqual(u"\u05E6\u05F3", to_letters(90))

    def test_hundred(self):
        self.assertEqual(u"\u05E7\u05F3", to_letters(100))

    def test_hundred_and_one(self):
        self.assertEqual(u"\u05E7\u05F4\u05D0", to_letters(101))

    def test_hundred_and_fifteen(self):
        self.assertEqual(u"\u05E7\u05D8\u05F4\u05D5", to_letters(115))

    def test_hundred_and_twenty_five(self):
        self.assertEqual(u"\u05E7\u05DB\u05F4\u05D4", to_letters(125))

    def test_two_hundred(self):
        self.assertEqual(u"\u05E8\u05F3", to_letters(200))

    def test_three_hundred(self):
        self.assertEqual(u"\u05E9\u05F3", to_letters(300))

    def test_four_hundred(self):
        self.assertEqual(u"\u05EA\u05F3", to_letters(400))

    def test_four_hundred_and_one(self):
        self.assertEqual(u"\u05EA\u05F4\u05D0", to_letters(401))

    def test_five_hundred(self):
        self.assertEqual(u"\u05EA\u05F4\u05E7", to_letters(500))

    def test_five_hundred_and_one(self):
        self.assertEqual(u"\u05EA\u05E7\u05F4\u05D0", to_letters(501))

    def test_six_hundred(self):
        self.assertEqual(u"\u05EA\u05F4\u05E8", to_letters(600))

    def test_six_hundred_and_one(self):
        self.assertEqual(u"\u05EA\u05E8\u05F4\u05D0", to_letters(601))

    def test_seven_hundred(self):
        self.assertEqual(u"\u05EA\u05F4\u05E9", to_letters(700))

    def test_seven_hundred_and_one(self):
        self.assertEqual(u"\u05EA\u05E9\u05F4\u05D0", to_letters(701))

    def test_eight_hundred(self):
        self.assertEqual(u"\u05EA\u05F4\u05EA", to_letters(800))

    def test_eight_hundred_and_one(self):
        self.assertEqual(u"\u05EA\u05EA\u05F4\u05D0", to_letters(801))

    def test_nine_hundred(self):
        self.assertEqual(u"\u05EA\u05EA\u05F4\u05E7", to_letters(900))

    def test_nine_hundred_and_one(self):
        self.assertEqual(u"\u05EA\u05EA\u05E7\u05F4\u05D0", to_letters(901))

    def test_one_thousand(self):
        """ Aleph geresh would be ambiguous, so do it the long way """
        self.assertEqual(u"\u05EA\u05EA\u05F4\u05E8", to_letters(1000))

    def test_one_thousand_and_one(self):
        self.assertEqual(u"\u05D0\u05F3\u05D0\u05F3", to_letters(1001))

    def test_one_thousand_and_eleven(self):
        self.assertEqual(u"\u05D0\u05F3\u05D9\u05F4\u05D0", to_letters(1011))

    def test_one_thousand_and_fifteen(self):
        self.assertEqual(u"\u05D0\u05F3\u05D8\u05F4\u05D5", to_letters(1015))

    def test_two_thousand(self):
        self.assertEqual(u"\u05D0\u05F3\u05EA\u05EA\u05F4\u05E8",
                         to_letters(2000))

    def test_ten_thousand(self):
        self.assertEqual(u"\u05D8\u05F3\u05EA\u05EA\u05F4\u05E8",
                         to_letters(10000))

    def test_eleven_thousand(self):
        self.assertEqual(u"\u05D9\u05F4\u05D0\u05F3", to_letters(11000))

    def test_eleven_thousand_and_one(self):
        self.assertEqual(u"\u05D9\u05F4\u05D0\u05F3\u05D0\u05F3",
                         to_letters(11001))

    def test_four_hundred_thousand(self):
        self.assertEqual(
            u"\u05E9\u05E6\u05F4\u05D8\u05F3\u05EA\u05EA\u05F4\u05E8",
            to_letters(400000))

    def test_four_hundred_thousand_and_one(self):
        self.assertEqual(u"\u05EA\u05F3\u05D0\u05F3", to_letters(400001))

    def test_one_million(self):
        self.assertEqual(u"\u05D0\u05F3\u05F3", to_letters(1000000))

    def test_one_million_and_one(self):
        self.assertEqual(u"\u05D0\u05F3\u05F3\u05D0\u05F3",
                         to_letters(1000001))

    def test_one_million_and_eleven(self):
        self.assertEqual(u"\u05D0\u05F3\u05F3\u05D9\u05F4\u05D0",
                         to_letters(1000011))

    def test_one_million_and_fifteen(self):
        self.assertEqual(u"\u05D0\u05F3\u05F3\u05D8\u05F4\u05D5",
                         to_letters(1000015))

    def test_one_million_one_thousand(self):
        self.assertEqual(u"\u05D0\u05F3\u05EA\u05EA\u05F4\u05E8",
                         to_letters(1001000))

    def test_one_million_one_thousand_and_one(self):
        self.assertEqual(u"\u05D0\u05F3\u05D0\u05F3\u05D0\u05F3",
                         to_letters(1001001))

    def test_ten_million(self):
        self.assertEqual(u"\u05D9\u05F3\u05F3", to_letters(10000000))

    def test_zero(self):
        with self.assertRaises(ValueError):
            to_letters(0)

    def test_minus_one(self):
        with self.assertRaises(ValueError):
            to_letters(-1)

    def test_half(self):
        with self.assertRaises(ValueError):
            to_letters(0.5)


if __name__ == "__main__":
    unittest.main()
