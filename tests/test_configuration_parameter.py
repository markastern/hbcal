"""Tests for ConfigurationParmater class and subclasses"""

# Copyright 2015, 2016 Mark Stern
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
from configuration_utilities import AbbrevList, AmbiguousKeyError,\
    SingleConfigurationParameter, MultiConfigurationParameter,\
    ConfigurationParameterDefaultError

logging.basicConfig(filename='/dev/stdout', level=logging.DEBUG)


class TestSingleDefault(unittest.TestCase):

    def test_default_not_allowed(self):
        with self.assertRaises(ConfigurationParameterDefaultError):
            SingleConfigurationParameter(AbbrevList(['value1', 'value2']),
                                         'value3')

    def test_default_ambiguous(self):
        with self.assertRaises(ConfigurationParameterDefaultError):
            SingleConfigurationParameter(AbbrevList(['value1', 'value2']),
                                         'value')

    def test_default_valid(self):
        parameter = SingleConfigurationParameter(AbbrevList(['value1',
                                                             'value2']),
                                                 'value2')
        self.assertEqual(parameter.value, ['value2'])


class TestMultiDefault(unittest.TestCase):

    def test_default_not_allowed(self):
        with self.assertRaises(KeyError):
            MultiConfigurationParameter(AbbrevList(['value1', 'value2']),
                                        ['value2', 'value3'])

    def test_default_ambiguous(self):
        with self.assertRaises(AmbiguousKeyError):
            MultiConfigurationParameter(AbbrevList(['value1', 'value2']),
                                        ['value'])

    def test_default_valid(self):
        parameter = MultiConfigurationParameter(AbbrevList(['value1',
                                                            'value2']),
                                                ['value2'])
        self.assertEqual(parameter.value, ['value2'])

    def test_multi_default_valid(self):
        parameter = MultiConfigurationParameter(AbbrevList(['value1',
                                                            'value2']),
                                                ['value2', 'value1'])
        self.assertEqual(parameter.value, ['value2', 'value1'])
