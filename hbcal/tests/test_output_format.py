""" Tests for '--format' and 'format'.

This module contains tests for the '--format' command line option
and for the 'format' configuration file option.
"""
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
from configuration_utilities import ConfigurationParameterValueError, \
    ConfigurationParameterAmbiguousError
from utilities import ConfigurationData, TestCase, hbcal
# Test discovery uses setUpModule, but pylint does not know that.
# pylint: disable=unused-import
from utilities import set_up_module as setUpModule  # noqa

# pylint: enable=unused-import

logging.basicConfig(filename='/dev/stdout', level=logging.DEBUG)


class TestNoConfigFile(TestCase):
    """Test command line "--format" option with no configuration file."""

    def test_default(self):
        """Test default value of --format option."""
        output = hbcal("hbcal -ih -o -s 1 8 5775")
        self.assertEqual(u"\u05E0\u05D7", output[0])

    def test_normal_option(self):
        """Test '--format normal' command line option."""
        output = hbcal("hbcal -ih -o -s --format normal 1 8 5775")
        self.assertEqual(u"\u05E0\u05D7", output[0])

    def test_reverse_option(self):
        """Test '--format reverse' command line option."""
        output = hbcal("hbcal -ih -o -s --format reverse 1 8 5775")
        self.assertEqual(u"\u05D7\u05E0", output[0])

    def test_html_option(self):
        """Test '--format html' command line option."""
        output = hbcal("hbcal -ih -o -s --format html 1 8 5775")
        self.assertEqual('&#1504;&#1495;', output[0])

    def test_phonetics_option(self):
        """Test '--format phonetics' command line option."""
        output = hbcal("hbcal -ih -o -s --format phonetics 1 8 5775")
        self.assertEqual('Noach', output[0])

    def test_short_option(self):
        """Test '-f' command line option."""
        output = hbcal("hbcal -ih -o -s -fhtml 1 8 5775")
        self.assertEqual('&#1504;&#1495;', output[0])

    def test_abbreviated_value(self):
        """Test '--format rev' in command line."""
        output = hbcal("hbcal -ih -o -s --format rev 1 8 5775")
        self.assertEqual(u"\u05D7\u05E0", output[0])

    def test_short_option_abbreviated(self):
        """Test '-fp' in command line.

        This tests a short option with an abbreviated value.
        """
        output = hbcal("hbcal -ih -o -s -fp 1 8 5775")
        self.assertEqual('Noach', output[0])


class TestEmptyConfigFile(TestNoConfigFile):
    """Test "--format" option with empty configuration file."""

    config_data = ConfigurationData.EMPTY


class TestEmptySectionConfigFile(TestNoConfigFile):
    """Test configuration file with empty hbcal section."""

    config_data = ""


class TestNormalInConfigFile(TestNoConfigFile):
    """Test 'format = normal' in configuration file."""

    config_data = "format = normal"


class TestReverseInConfigFile(TestNoConfigFile):
    """Test 'format = reverse' in configuration file."""

    config_data = "format = reverse"

    def test_default(self):
        output = hbcal("hbcal -ih -o -s 1 8 5775")
        self.assertEqual(u"\u05D7\u05E0", output[0])


class TestHtmlInConfigFile(TestNoConfigFile):
    """Test 'format = html' in configuration file."""

    config_data = "format = html"

    def test_default(self):
        output = hbcal("hbcal -ih -o -s 1 8 5775")
        self.assertEqual('&#1504;&#1495;', output[0])


class TestPhoneticsInConfigFile(TestNoConfigFile):
    """Test 'format = phonetics' in configuration file."""

    config_data = "format = phonetics"

    def test_default(self):
        output = hbcal("hbcal -ih -o -s 1 8 5775")
        self.assertEqual('Noach', output[0])


class TestMixedCase(TestReverseInConfigFile):
    """Test 'format = Reverse' (mixed case in configuration file."""

    config_data = "format = Reverse"


class TestAbbreviated(TestReverseInConfigFile):
    """Test 'formar = r' in configuration file."""

    config_data = "format = r"


class TestAbbreviatedTooMuch(TestCase):
    """Test "format =" (too abbreviated) in configuration file."""

    config_data = "format ="

    def test_default(self):
        """Test default value of --format option."""
        with self.assertRaises(ConfigurationParameterAmbiguousError):
            hbcal("hbcal -ih -o -s 1 8 5775")


class TestInvalidValue(TestCase):
    """Test "format = hebrew" (invalid) in configuration file."""

    config_data = "format = hebrew"

    def test_default(self):
        """Test default value of --format option."""
        with self.assertRaises(ConfigurationParameterValueError):
            hbcal("hbcal -ih -o -s 1 8 5775")


class TestMiscellaneous(TestCase):
    """Miscellaneous output format tests"""

    def test_adar_reverse_option(self):
        """ Tests a bug fix. Adar was coming out as 'Alef Geresh' """
        output = hbcal("hbcal -ih -oh -freverse 1 12 2")
        self.assertEqual(u"2 \u05E8\u05D3\u05D0 1 \u05D9\u05E0\u05E9 " +
                         u"\u05DD\u05D5\u05D9", output[0])


if __name__ == "__main__":
    unittest.main()
