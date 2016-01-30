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

from __future__ import division
import unittest

from hbcal.hebrew_calendar import abs_time


class TestAddSubtract(unittest.TestCase):

    def test_add_rel(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        rel_time2 = abs_time.RelTime(50, 4, 12, 123)
        self.assertEqual(abs_time.RelTime(150, 8, 24, 246).chalakim,
                         rel_time1.chalakim + rel_time2.chalakim)

    def test_add_int(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        with self.assertRaises(TypeError):
            rel_time1 + 6

    def test_radd_int(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        with self.assertRaises(TypeError):
            6 + rel_time1

    def test_sub_rel(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        rel_time2 = abs_time.RelTime(50, 4, 12, 123)
        self.assertEqual(abs_time.RelTime(50, 0, 0, 0).chalakim,
                         rel_time1.chalakim - rel_time2.chalakim)

    def test_sub_int(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        with self.assertRaises(TypeError):
            rel_time1 - 6

    def test_rsub_int(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        with self.assertRaises(TypeError):
            6 - rel_time1


class TestIncrementDecrement(unittest.TestCase):

    def test_iadd_rel(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        rel_time2 = abs_time.RelTime(50, 4, 12, 123)
        rel_time1 += rel_time2
        self.assertEqual(abs_time.RelTime(150, 8, 24, 246).chalakim,
                         rel_time1.chalakim)

    def test_iadd_int(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        with self.assertRaises(TypeError):
            rel_time1 += 6

    def test_isub_rel(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        rel_time2 = abs_time.RelTime(50, 4, 12, 123)
        rel_time1 -= rel_time2
        self.assertEqual(abs_time.RelTime(50, 0, 0, 0).chalakim,
                         rel_time1.chalakim)

    def test_isub_int(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        with self.assertRaises(TypeError):
            rel_time1 -= 6


class TestMultiply(unittest.TestCase):

    def test_multiply_int(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        rel_time2 = rel_time1 * 2
        self.assertEqual(abs_time.RelTime(200, 8, 24, 246).chalakim,
                         rel_time2.chalakim)

    def test_rmultiply_int(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        rel_time2 = 2 * rel_time1
        self.assertEqual(abs_time.RelTime(200, 8, 24, 246).chalakim,
                         rel_time2.chalakim)

    def test_imultiply_int(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        rel_time2 = rel_time1
        rel_time1 *= 2
        self.assertEqual(abs_time.RelTime(200, 8, 24, 246).chalakim,
                         rel_time2.chalakim)

    def test_multiply(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        rel_time2 = abs_time.RelTime(50, 4, 12, 123)
        with self.assertRaises(TypeError):
            rel_time1 * rel_time2

    def test_imultiply(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        rel_time2 = abs_time.RelTime(50, 4, 12, 123)
        with self.assertRaises(TypeError):
            rel_time1 *= rel_time2

    def test_floor_divide_int(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        self.assertEqual(abs_time.RelTime(20, 0, 21, 672).chalakim,
                         (rel_time1 // 5).chalakim)

    def test_ifloor_divide_int(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        rel_time1 //= 5
        self.assertEqual(abs_time.RelTime(20, 0, 21, 672).chalakim,
                         rel_time1.chalakim)

    def test_floor_divide(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        rel_time2 = abs_time.RelTime(50, 4, 12, 123)
        self.assertEqual(1, rel_time1 // rel_time2)

    def test_ifloor_divide(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        rel_time2 = abs_time.RelTime(50, 4, 12, 123)
        rel_time1 //= rel_time2
        self.assertEqual(1, rel_time1)

    def test_floor_divide_string(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        with self.assertRaises(TypeError):
            rel_time1 // "Hell World"

    def test_ifloor_divide_string(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        with self.assertRaises(TypeError):
            rel_time1 //= "Hell World"

    def test_true_divide_int(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        self.assertAlmostEqual(3652152.6, (rel_time1 / 5).chalakim, 10)

    def test_itrue_divide_int(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        rel_time1 /= 5
        self.assertAlmostEqual(3652152.6, rel_time1.chalakim, 10)

    def test_true_divide(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        rel_time2 = abs_time.RelTime(50, 4, 12, 123)
        self.assertAlmostEqual(1.987, rel_time1 / rel_time2, 3)

    def test_itrue_divide(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        rel_time2 = abs_time.RelTime(50, 4, 12, 123)
        rel_time1 /= rel_time2
        self.assertAlmostEqual(1.987, rel_time1, 3)

    def test_itrue_divide_string(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        with self.assertRaises(TypeError):
            rel_time1 //= "Hell World"

    def test_mod_int(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        self.assertEqual(abs_time.RelTime(0, 0, 0, 3).chalakim,
                         (rel_time1 % 5).chalakim)

    def test_imod_int(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        rel_time1 %= 5
        self.assertEqual(abs_time.RelTime(0, 0, 0, 3).chalakim,
                         rel_time1.chalakim)

    def test_mod(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        rel_time2 = abs_time.RelTime(50, 4, 12, 123)
        self.assertEqual(abs_time.RelTime(50, 0, 0, 0).chalakim,
                         (rel_time1 % rel_time2).chalakim)

    def test_imod(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        rel_time2 = abs_time.RelTime(50, 4, 12, 123)
        rel_time1 %= rel_time2
        self.assertEqual(abs_time.RelTime(50, 0, 0, 0).chalakim,
                         rel_time1.chalakim)

    def test_mod_string(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        with self.assertRaises(TypeError):
            rel_time1 % "Hell World"

    def test_imod_string(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        with self.assertRaises(TypeError):
            rel_time1 %= "Hell World"

    def test_divmod_int(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        rel_time2, rel_time3 = divmod(rel_time1, 5)
        self.assertEqual((abs_time.RelTime(20, 0, 21, 672).chalakim,
                          abs_time.RelTime(0, 0, 0, 3).chalakim),
                         (rel_time2.chalakim, rel_time3.chalakim))

    def test_divmod(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        rel_time2 = abs_time.RelTime(50, 4, 12, 123)
        quotient, rel_time3 = divmod(rel_time1, rel_time2)
        self.assertEqual((1, abs_time.RelTime(50, 0, 0, 0).chalakim),
                         (quotient, rel_time3.chalakim))


class TestProperties(unittest.TestCase):

    def test_weeks(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        self.assertEqual(100, rel_time1.weeks)

    def test_days(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        self.assertEqual(704, rel_time1.days)

    def test_days_xxx(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        self.assertEqual((704, 12 * 1080 + 123), rel_time1.days_chalakim)


if __name__ == '__main__':
    unittest.main()
