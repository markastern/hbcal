"""Tests for ordinal_suffix function"""

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

from hbcal import ordinal_suffix
import unittest


class TestOrdinal(unittest.TestCase):
    """Tests for ordinal_suffix function"""

    def test_one(self):
        self.assertEqual("st", ordinal_suffix(1))

    def test_two(self):
        self.assertEqual("nd", ordinal_suffix(2))

    def test_three(self):
        self.assertEqual("rd", ordinal_suffix(3))

    def test_four(self):
        self.assertEqual("th", ordinal_suffix(4))

    def test_ten(self):
        self.assertEqual("th", ordinal_suffix(10))

    def test_eleven(self):
        self.assertEqual("th", ordinal_suffix(11))

    def test_twelve(self):
        self.assertEqual("th", ordinal_suffix(12))

    def test_thirteen(self):
        self.assertEqual("th", ordinal_suffix(13))

    def test_fourteen(self):
        self.assertEqual("th", ordinal_suffix(14))

    def test_twenty(self):
        self.assertEqual("th", ordinal_suffix(20))

    def test_twenty_one(self):
        self.assertEqual("st", ordinal_suffix(21))

    def test_twenty_two(self):
        self.assertEqual("nd", ordinal_suffix(22))

    def test_twenty_three(self):
        self.assertEqual("rd", ordinal_suffix(23))

    def test_twenty_four(self):
        self.assertEqual("th", ordinal_suffix(24))

    def test_thirty(self):
        self.assertEqual("th", ordinal_suffix(30))

    def test_thirty_one(self):
        self.assertEqual("st", ordinal_suffix(31))

    def test_thirty_two(self):
        self.assertEqual("nd", ordinal_suffix(32))

    def test_thirty_three(self):
        self.assertEqual("rd", ordinal_suffix(33))

    def test_thirty_four(self):
        self.assertEqual("th", ordinal_suffix(34))

    def test_hundred(self):
        self.assertEqual("th", ordinal_suffix(100))

    def test_hundred_and_one(self):
        self.assertEqual("st", ordinal_suffix(101))

    def test_hundred_and_two(self):
        self.assertEqual("nd", ordinal_suffix(102))

    def test_hundred_and_three(self):
        self.assertEqual("rd", ordinal_suffix(103))

    def test_hundred_and_four(self):
        self.assertEqual("th", ordinal_suffix(104))

    def test_hundred_and_ten(self):
        self.assertEqual("th", ordinal_suffix(110))

    def test_hundred_and_eleven(self):
        self.assertEqual("th", ordinal_suffix(111))

    def test_hundred_and_twelve(self):
        self.assertEqual("th", ordinal_suffix(112))

    def test_hundred_and_thirteen(self):
        self.assertEqual("th", ordinal_suffix(113))

    def test_hundred_and_fourteen(self):
        self.assertEqual("th", ordinal_suffix(114))

    def test_hundred_and_twenty(self):
        self.assertEqual("th", ordinal_suffix(120))

    def test_hundred_and_twenty_one(self):
        self.assertEqual("st", ordinal_suffix(121))

    def test_hundred_and_twenty_two(self):
        self.assertEqual("nd", ordinal_suffix(122))

    def test_hundred_and_twenty_three(self):
        self.assertEqual("rd", ordinal_suffix(123))

    def test_hundred_and_twenty_four(self):
        self.assertEqual("th", ordinal_suffix(124))

    def test_hundred_and_thirty(self):
        self.assertEqual("th", ordinal_suffix(130))

    def test_hundred_and_thirty_one(self):
        self.assertEqual("st", ordinal_suffix(131))

    def test_hundred_and_thirty_two(self):
        self.assertEqual("nd", ordinal_suffix(132))

    def test_hundred_and_thirty_three(self):
        self.assertEqual("rd", ordinal_suffix(133))

    def test_hundred_and_thirty_four(self):
        self.assertEqual("th", ordinal_suffix(134))

    if __name__ == "__main__":
        unittest.main()
