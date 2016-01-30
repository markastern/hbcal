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

from hbcal.hebrew_calendar import abs_time


class TestEquality(unittest.TestCase):

    def test_equal(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 12, 123)
        self.assertTrue(abs_time1 == abs_time2)

    def test_unequal_weeks(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(101, 4, 12, 123)
        self.assertFalse(abs_time1 == abs_time2)

    def test_unequal_days(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 5, 12, 123)
        self.assertFalse(abs_time1 == abs_time2)

    def test_unequal_hours(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 13, 123)
        self.assertFalse(abs_time1 == abs_time2)

    def test_unequal_chalakim(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 12, 122)
        self.assertFalse(abs_time1 == abs_time2)

    def test_equal_adjust_weeks(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(99, 11, 12, 123)
        self.assertTrue(abs_time1 == abs_time2)

    def test_equal_adjust_days(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 5, -12, 123)
        self.assertTrue(abs_time1 == abs_time2)

    def test_equal_adjust_hours(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 10, 2283)
        self.assertTrue(abs_time1 == abs_time2)


class TestInequality(unittest.TestCase):
    def test_equal(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 12, 123)
        self.assertFalse(abs_time1 != abs_time2)

    def test_unequal_weeks(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(101, 4, 12, 123)
        self.assertTrue(abs_time1 != abs_time2)

    def test_unequal_days(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 5, 12, 123)
        self.assertTrue(abs_time1 != abs_time2)

    def test_unequal_hours(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 13, 123)
        self.assertTrue(abs_time1 != abs_time2)

    def test_unequal_chalakim(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 12, 122)
        self.assertTrue(abs_time1 != abs_time2)

    def test_equal_adjust_weeks(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(99, 11, 12, 123)
        self.assertFalse(abs_time1 != abs_time2)

    def test_equal_adjust_days(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 5, -12, 123)
        self.assertFalse(abs_time1 != abs_time2)

    def test_equal_adjust_hours(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 10, 2283)
        self.assertFalse(abs_time1 != abs_time2)


class TestLessThan(unittest.TestCase):

    def test_equal(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 12, 123)
        self.assertFalse(abs_time1 < abs_time2)

    def test_unequal_weeks(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(101, 4, 12, 123)
        self.assertTrue(abs_time1 < abs_time2)

    def test_unequal_days(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 5, 12, 123)
        self.assertTrue(abs_time1 < abs_time2)

    def test_unequal_hours(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 13, 123)
        self.assertTrue(abs_time1 < abs_time2)

    def test_unequal_chalakim(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 12, 122)
        self.assertFalse(abs_time1 < abs_time2)

    def test_equal_adjust_weeks(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(99, 11, 12, 123)
        self.assertFalse(abs_time1 < abs_time2)

    def test_equal_adjust_days(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 5, -12, 123)
        self.assertFalse(abs_time1 < abs_time2)

    def test_equal_adjust_hours(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 10, 2283)
        self.assertFalse(abs_time1 < abs_time2)


class TestLessOrEqual(unittest.TestCase):

    def test_equal(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 12, 123)
        self.assertTrue(abs_time1 <= abs_time2)

    def test_unequal_weeks(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(101, 4, 12, 123)
        self.assertTrue(abs_time1 <= abs_time2)

    def test_unequal_days(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 5, 12, 123)
        self.assertTrue(abs_time1 <= abs_time2)

    def test_unequal_hours(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 13, 123)
        self.assertTrue(abs_time1 <= abs_time2)

    def test_unequal_chalakim(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 12, 122)
        self.assertFalse(abs_time1 <= abs_time2)

    def test_equal_adjust_weeks(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(99, 11, 12, 123)
        self.assertTrue(abs_time1 <= abs_time2)

    def test_equal_adjust_days(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 5, -12, 123)
        self.assertTrue(abs_time1 <= abs_time2)

    def test_equal_adjust_hours(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 10, 2283)
        self.assertTrue(abs_time1 <= abs_time2)


class TestGreaterThan(unittest.TestCase):

    def test_equal(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 12, 123)
        self.assertFalse(abs_time1 > abs_time2)

    def test_unequal_weeks(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(101, 4, 12, 123)
        self.assertFalse(abs_time1 > abs_time2)

    def test_unequal_days(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 5, 12, 123)
        self.assertFalse(abs_time1 > abs_time2)

    def test_unequal_hours(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 13, 123)
        self.assertFalse(abs_time1 > abs_time2)

    def test_unequal_chalakim(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 12, 122)
        self.assertTrue(abs_time1 > abs_time2)

    def test_equal_adjust_weeks(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(99, 11, 12, 123)
        self.assertFalse(abs_time1 > abs_time2)

    def test_equal_adjust_days(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 5, -12, 123)
        self.assertFalse(abs_time1 > abs_time2)

    def test_equal_adjust_hours(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 10, 2283)
        self.assertFalse(abs_time1 > abs_time2)


class TestGreaterOrEqual(unittest.TestCase):

    def test_equal(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 12, 123)
        self.assertTrue(abs_time1 >= abs_time2)

    def test_unequal_weeks(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(101, 4, 12, 123)
        self.assertFalse(abs_time1 >= abs_time2)

    def test_unequal_days(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 5, 12, 123)
        self.assertFalse(abs_time1 >= abs_time2)

    def test_unequal_hours(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 13, 123)
        self.assertFalse(abs_time1 >= abs_time2)

    def test_unequal_chalakim(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 12, 122)
        self.assertTrue(abs_time1 >= abs_time2)

    def test_equal_adjust_weeks(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(99, 11, 12, 123)
        self.assertTrue(abs_time1 >= abs_time2)

    def test_equal_adjust_days(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 5, -12, 123)
        self.assertTrue(abs_time1 >= abs_time2)

    def test_equal_adjust_hours(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 10, 2283)
        self.assertTrue(abs_time1 >= abs_time2)


class TestAddSubtract(unittest.TestCase):
    def test_add_abs_abs(self):
        # Adding 2 AbsTime objects is illegal
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(50, 4, 12, 123)
        with self.assertRaises(TypeError):
            abs_time1 + abs_time2

    def test_sub_abs_abs(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(50, 4, 12, 123)
        x = abs_time1 - abs_time2
        self.assertIsInstance(x, abs_time.RelTime)

    def test_add_abs_rel(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        rel_time2 = abs_time.RelTime(50, 4, 12, 123)
        x = abs_time1 + rel_time2
        self.assertIsInstance(x, abs_time.AbsTime)
        self.assertEqual(x, abs_time.AbsTime(151, 2, 0, 246))

    def test_add_rel_abs(self):
        rel_time1 = abs_time.RelTime(50, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 12, 123)
        x = rel_time1 + abs_time2
        self.assertIsInstance(x, abs_time.AbsTime)
        self.assertEqual(x, abs_time.AbsTime(151, 2, 0, 246))

    def test_sub_abs_rel(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        rel_time2 = abs_time.RelTime(50, 4, 12, 123)
        x = abs_time1 - rel_time2
        self.assertIsInstance(x, abs_time.AbsTime)
        self.assertEqual(x, abs_time.AbsTime(50, 0, 0, 0))

    def test_sub_rel_abs(self):
        rel_time1 = abs_time.RelTime(50, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 12, 123)
        with self.assertRaises(TypeError):
            rel_time1 - abs_time2


class TestIncrementDecrement(unittest.TestCase):
    def test_inc_abs_abs(self):
        # Adding 2 AbsTime objects is illegal
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(50, 4, 12, 123)
        with self.assertRaises(TypeError):
            abs_time1 += abs_time2

    def test_dec_abs_abs(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(50, 4, 12, 123)
        abs_time1 -= abs_time2
        self.assertIsInstance(abs_time1, abs_time.RelTime)
        self.assertEqual(50 * 7 * 24 * 1080, abs_time1.chalakim)

    def test_inc_abs_rel(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        rel_time2 = abs_time.RelTime(50, 4, 12, 123)
        abs_time3 = abs_time1
        abs_time1 += rel_time2
        self.assertEqual(abs_time1, abs_time.AbsTime(151, 2, 0, 246))
        # abs_time3 should be unchanged
        self.assertEqual(abs_time.AbsTime(100, 4, 12, 123), abs_time3)

    def test_inc_rel_abs(self):
        rel_time1 = abs_time.RelTime(50, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 12, 123)
        with self.assertRaises(TypeError):
            rel_time1 += abs_time2

    def test_dec_abs_rel(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        rel_time2 = abs_time.RelTime(50, 4, 12, 123)
        abs_time3 = abs_time1
        abs_time1 -= rel_time2
        self.assertEqual(abs_time1, abs_time.AbsTime(50, 0, 0, 0))
        # abs_time3 should unchanged
        self.assertEqual(abs_time.AbsTime(100, 4, 12, 123), abs_time3)

    def test_dec_rel_abs(self):
        rel_time1 = abs_time.RelTime(50, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(100, 4, 12, 123)
        with self.assertRaises(TypeError):
            rel_time1 -= abs_time2


class TestMultiply(unittest.TestCase):
    def test_multiply_abs_int(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time1 * 2
        self.assertEqual(abs_time.AbsTime(201, 2, 0, 246), abs_time2)

    def test_multiply_int_abs(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = 2 * abs_time1
        self.assertEqual(abs_time.AbsTime(201, 2, 0, 246), abs_time2)


class TestMultiplyEquals(unittest.TestCase):
    def test_multiply_abs(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time1
        abs_time1 *= 2
        self.assertEqual(abs_time.AbsTime(201, 2, 0, 246), abs_time1)
        # abs_time2 should be unchanged
        self.assertEqual(abs_time.AbsTime(100, 4, 12, 123), abs_time2)

    def test_multiply_rel(self):
        rel_time1 = abs_time.RelTime(100, 4, 12, 123)
        rel_time2 = rel_time1
        rel_time1 *= 2
        abs_time3 = abs_time.AbsTime(0, 0, 0, 0) + rel_time1
        self.assertEqual(abs_time.AbsTime(201, 2, 0, 246), abs_time3)
        self.assertIs(rel_time1, rel_time2)


class TestCopy(unittest.TestCase):

    def test_same(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time1
        self.assertIs(abs_time1, abs_time2)

    def test_modify(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time1
        abs_time1 += abs_time.RelTime(1, 0, 0, 0)
        self.assertNotEqual(abs_time1, abs_time2)


class TestImmutable(unittest.TestCase):

    def test_modify_weeks(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        with self.assertRaises(AttributeError):
            abs_time1.weeks = 50

    def test_modify_days(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        with self.assertRaises(AttributeError):
            abs_time1.days = 6

    def test_modify_hours(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        with self.assertRaises(AttributeError):
            abs_time1.hours = 18

    def test_modify_chalakim(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        with self.assertRaises(AttributeError):
            abs_time1.chalakim = 150


class TestFormatConstructor(unittest.TestCase):

    def test_empty_format(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(absTime=abs_time1)
        self.assertEqual(abs_time.AbsTime(0), abs_time2)

    def test_weeks_only(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(absTime=abs_time1, weeks=True)
        self.assertEqual(abs_time.AbsTime(100), abs_time2)

    def test_days_only(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(absTime=abs_time1, days=True)
        self.assertEqual(abs_time.AbsTime(0, 4), abs_time2)

    def test_hours_only(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(absTime=abs_time1, hours=True)
        self.assertEqual(abs_time.AbsTime(0, 0, 12), abs_time2)

    def test_chalakim_only(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(absTime=abs_time1, chalakim=True)
        self.assertEqual(abs_time.AbsTime(0, 0, 0, 123), abs_time2)

    def test_weeks_and_days_only(self):
        abs_time1 = abs_time.AbsTime(100, 4, 12, 123)
        abs_time2 = abs_time.AbsTime(absTime=abs_time1, weeks=True, days=True)
        self.assertEqual(abs_time.AbsTime(100, 4), abs_time2)

if __name__ == '__main__':
    unittest.main()
