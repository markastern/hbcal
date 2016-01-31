""" Tests for '--input' and 'input calendar'.

This module contains tests for the '--input' command line option and
for the 'input calendar' configuration file option.
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
from configuration_utilities import ConfigurationParameterAmbiguousError, \
    ConfigurationParameterValueError
from utilities import TestCase, hbcal, ConfigurationData
# Test discovery uses setUpModule, but pylint does not know that.
# pylint: disable=unused-import
from utilities import set_up_module as setUpModule  # noqa

# pylint: enable=unused-import

logging.basicConfig(filename='/dev/stdout', level=logging.DEBUG)


class Wrapper(object):
    """Wrapper class for CommonTests.

    The wrapper class hides the tests in CommonTests from test discovery,
    so that they will only be run when running tests from subclasses.
    """

    class CommonTests(TestCase):
        """Class containing tests for every configuration file."""

        def test_civil_option_2015(self):
            """Test --input parameter with civil calendar after 1752"""
            output = hbcal("hbcal --input civil -oc 17 8 2015")
            self.assertEqual(output[0], 'Monday 17 August 2015')

        def test_civil_option_1750(self):
            """Test --input parameter with civil calendar before 1752."""
            output = hbcal("hbcal --input civil -oc 17 8 1750")
            self.assertEqual(output[0], 'Friday 17 August 1750')

        def test_gregorian_option_2015(self):
            """Test --input parameter with Gregorian calendar after 1752."""
            output = hbcal("hbcal --input gregorian -oc 17 8 2015")
            self.assertEqual(output[0], 'Monday 17 August 2015')

        def test_gregorian_option_1750(self):
            """Test --input parameter with Gregorian calendar before 1752."""
            output = hbcal("hbcal --input gregorian -oc 17 8 1750")
            self.assertEqual(output[0], 'Monday 6 August 1750')

        def test_julian_option_2015(self):
            """Test --input parameter with Julian calendar after 1752."""
            output = hbcal("hbcal --input julian -oc 17 8 2015")
            self.assertEqual(output[0], 'Sunday 30 August 2015')

        def test_julian_option_1750(self):
            """Test --input parameter with Julian calendar before 1752."""
            output = hbcal("hbcal --input julian -oc 17 8 1750")
            self.assertEqual(output[0], 'Friday 17 August 1750')

        def test_hebrew_option_5775(self):
            """Test --input parameter with Hebrew calendar."""
            output = hbcal("hbcal --input hebrew -oc 2 6 5775")
            self.assertEqual(output[0], 'Monday 17 August 2015')

        def test_daf_option(self):
            """Test --input parameter with Daf Yomi calendar."""
            output = hbcal("hbcal --input daf -oc 85 16 13")
            self.assertEqual(output[0], 'Monday 17 August 2015')

        def test_option_value_abbreviated(self):
            """Test --input parameter with input calendar abbreviated."""
            output = hbcal("hbcal --input heb -oc 2 6 5775")
            self.assertEqual(output[0], 'Monday 17 August 2015')

        def test_short_option(self):
            """Test -i parameter."""
            output = hbcal("hbcal -ihebrew -oc 2 6 5775")
            self.assertEqual(output[0], 'Monday 17 August 2015')

        def test_short_option_abbreviated(self):
            """Test -i parameter with input calendar abbreviated."""
            output = hbcal("hbcal -iheb -oc 2 6 5775")
            self.assertEqual(output[0], 'Monday 17 August 2015')


class TestNoConfigFile(Wrapper.CommonTests):
    """Test command line "--input" option with no configuration file."""

    def test_default_2015(self):
        """Test default value of --input parameter for a date after 1752"""
        output = hbcal("hbcal -oc 17 8 2015")
        self.assertEqual(output[0], 'Monday 17 August 2015')

    def test_default_1750(self):
        """Test default value of --input parameter for a date before 1752"""
        output = hbcal("hbcal -oc 17 8 1750")
        self.assertEqual(output[0], 'Friday 17 August 1750')


class TestEmptyConfigFile(TestNoConfigFile):
    """Test command line "--input" option with an empty configuration file."""

    config_data = ConfigurationData.EMPTY


class TestEmptySectionConfigFile(TestNoConfigFile):
    """Test an empty 'hbcal' section in configuration file."""

    config_data = ""


class TestCivilInConfigFile(TestNoConfigFile):
    """Test "--input" with "input calendar = civil" in configuration file."""

    config_data = "input calendar = civil"


class TestGregorianInConfigFile(TestNoConfigFile):
    """Test "input calendar = gregorian" in configuration file."""

    config_data = "input calendar = gregorian"

    def test_default_1750(self):
        """Test default value of --input parameter for a date before 1752."""
        output = hbcal("hbcal -oc 17 8 1750")
        self.assertEqual(output[0], 'Monday 6 August 1750')


class TestJulianInConfigFile(TestNoConfigFile):
    """Test "input calendar = julian" in configuration file."""

    config_data = "input calendar = julian"

    def test_default_2015(self):
        """Test default value of --input parameter for a date after 1752."""
        output = hbcal("hbcal -oc 17 8 2015")
        self.assertEqual(output[0], 'Sunday 30 August 2015')


class TestHebrewInConfigFile(Wrapper.CommonTests):
    """Test "input calendar = hebrew" in configuration file."""

    config_data = "input calendar = hebrew"

    def test_default(self):
        """Test default value of --input parameter."""
        output = hbcal("hbcal -oc 2 6 5775")
        self.assertEqual(output[0], 'Monday 17 August 2015')


class TestDafInConfigFile(Wrapper.CommonTests):
    """Test "input calendar = daf" in configuration file."""

    config_data = "input calendar = daf"

    def test_default(self):
        """Test default value of --input parameter."""
        output = hbcal("hbcal -oc 85 16 13")
        self.assertEqual(output[0], 'Monday 17 August 2015')


class TestMixedCase(TestHebrewInConfigFile):
    """Test "input calendar" in configuration file using mixed case."""

    config_data = "input calendar = Hebrew"


class TestAbbreviated(TestHebrewInConfigFile):
    """Test "input calendar = h" in configuration file."""

    config_data = "input calendar = h"


class TestAbbreviatedTooMuch(TestCase):
    """Test "input calendar =" (too abbreviated) in configuration file."""

    config_data = "input calendar ="

    def test_default(self):
        """Test default value of --input parameter."""
        with self.assertRaises(ConfigurationParameterAmbiguousError):
            hbcal("hbcal -ih -oc 2 6 5775")


class TestInvalidValue(TestCase):
    """Test an invalid value of input calendar in the configuration file."""

    config_data = "input calendar = julien"

    def test_default(self):
        """Test default value of --input parameter."""
        with self.assertRaises(ConfigurationParameterValueError):
            hbcal("hbcal -ih -oc 2 6 5775")


if __name__ == "__main__":
    unittest.main()
