"""Tests for OrderedSet class"""

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
from hbcal.my_collections import OrderedSet


class TestOrderedSet(unittest.TestCase):

    def setUp(self):
        self.set1 = OrderedSet(['eggs', 'cheese', 'spam'])

    def test_init_preserves_order(self):
        self.assertEqual(tuple(self.set1), ('eggs', 'cheese', 'spam'))

    def test_contains(self):
        self.assertTrue('eggs' in self.set1)

    def test_not_contains(self):
        self.assertTrue('chicken' not in self.set1)

    def test_length(self):
        self.assertEqual(len(self.set1), 3)

    def test_add(self):
        self.set1.add('chicken')
        self.assertEqual(tuple(self.set1),
                         ('eggs', 'cheese', 'spam', 'chicken'))

    def test_add_duplicate(self):
        self.set1.add('eggs')
        self.assertEqual(tuple(self.set1), ('eggs', 'cheese', 'spam'))

    def test_discard(self):
        self.set1.discard('cheese')
        self.assertEqual(tuple(self.set1), ('eggs', 'spam'))

    def test_discard_missing(self):
        self.set1.discard('chicken')
        self.assertEqual(tuple(self.set1), ('eggs', 'cheese', 'spam'))

    def test_subset(self):
        set2 = OrderedSet(['spam', 'eggs'])
        self.assertTrue(set2 <= self.set1)

    def test_subset_equal(self):
        set2 = OrderedSet(['spam', 'eggs', 'cheese'])
        self.assertTrue(set2 <= self.set1)

    def test_not_subset(self):
        set2 = OrderedSet(['spam', 'chicken'])
        self.assertFalse(set2 <= self.set1)

    def test_superset(self):
        set2 = OrderedSet(['spam', 'eggs'])
        self.assertTrue(self.set1 >= set2)

    def test_superset_equal(self):
        set2 = OrderedSet(['spam', 'eggs', 'cheese'])
        self.assertTrue(set2 >= self.set1)

    def test_not_superset(self):
        set2 = OrderedSet(['spam', 'chicken'])
        self.assertFalse(self.set1 >= set2)

    def test_proper_subset(self):
        set2 = OrderedSet(['spam', 'eggs'])
        self.assertTrue(set2 < self.set1)

    def test_not_proper_subset_equal(self):
        set2 = OrderedSet(['spam', 'eggs', 'cheese'])
        self.assertFalse(set2 < self.set1)

    def test_not_proper_subset(self):
        set2 = OrderedSet(['spam', 'chicken'])
        self.assertFalse(set2 < self.set1)

    def test_proper_superset(self):
        set2 = OrderedSet(['spam', 'eggs'])
        self.assertTrue(self.set1 > set2)

    def test_not_proper_superset_equal(self):
        set2 = OrderedSet(['spam', 'eggs', 'cheese'])
        self.assertFalse(set2 > self.set1)

    def test_not_proper_superset(self):
        set2 = OrderedSet(['spam', 'chicken'])
        self.assertFalse(self.set1 >= set2)

    def test_union(self):
        set2 = OrderedSet(['spam', 'chicken'])
        self.assertEqual(tuple(self.set1 | set2),
                         ('eggs', 'cheese', 'spam', 'chicken'))

    def test_intersection(self):
        set2 = OrderedSet(['spam', 'chicken'])
        self.assertEqual(self.set1 & set2, set(['spam']))

    def test_difference(self):
        set2 = OrderedSet(['spam', 'chicken'])
        self.assertEqual(tuple(self.set1 - set2),
                         ('eggs', 'cheese'))

    def test_symmetric_difference(self):
        set2 = OrderedSet(['spam', 'chicken'])
        self.assertEqual(tuple(self.set1 ^ set2),
                         ('eggs', 'cheese', 'chicken'))


if __name__ == "__main__":
    unittest.main()
