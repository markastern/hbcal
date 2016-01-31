""" Tests for '--[no]molad' and 'molad'.

This module contains tests for the '--molad' and '--nomolad' command line
options and for the 'molad' configuration file option.
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
    """Test command line "--[no]molad" option with no configuration file."""

    def test_default(self):
        """Test default value of --[no]molad option."""
        output = hbcal("hbcal -ih -o civil -- 1 2 5775")
        self.assertEqual('Monday 20 April 2015', output[0])

    def test_molad_option(self):
        """Test --molad option"""
        output = hbcal("hbcal -ih -o civil --molad 1 2 5775")
        self.assertEqual('Sunday 19 April 2015 01:27 and 4 parts', output[0])

    def test_molad_short_option(self):
        """Test -m option"""
        output = hbcal("hbcal -ih -o civil -m 1 2 5775")
        self.assertEqual('Sunday 19 April 2015 01:27 and 4 parts', output[0])

    def test_nomolad_option(self):
        """Test --nomolad option"""
        output = hbcal("hbcal -ih -o civil --nomolad 1 2 5775")
        self.assertEqual('Monday 20 April 2015', output[0])


class TestEmptyConfigFile(TestNoConfigFile):
    """Test empty configuration file."""

    config_data = ConfigurationData.EMPTY


class TestEmptySectionConfigFile(TestNoConfigFile):
    """Test configuration file with empty hbcal section."""

    config_data = ""


class TestMoladTrueInConfigFile(TestNoConfigFile):
    """Test "--molad" option with "molad = true" in configuration file."""

    config_data = "molad = true"

    def test_default(self):
        output = hbcal("hbcal -ih -o civil -- 1 2 5775")
        self.assertEqual('Sunday 19 April 2015 01:27 and 4 parts', output[0])


class TestMoladYesInConfigFile(TestMoladTrueInConfigFile):
    """Test "--molad" option with "molad = yes" in configuration file."""

    config_data = "molad = yes"


class TestMoladFalseInConfigFile(TestNoConfigFile):
    """Test "--molad" option with "molad = false" in configuration file."""

    config_data = "molad = false"


class TestMoladNoInConfigFile(TestMoladFalseInConfigFile):
    """Test "--molad" option with "molad = no" in configuration file."""

    config_data = "molad = no"


class TestMixedCase(TestMoladTrueInConfigFile):
    """Test "molad = trUe" (mixed case) in configuration file."""

    config_data = "molad = trUe"


class TestAbbreviated(TestMoladYesInConfigFile):
    """Test "molad = y" in configuration file."""

    config_data = "molad = y"


class TestAbbreviatedTooMuch(TestCase):
    """Test "molad =" in configuration file."""

    config_data = "molad ="

    def test_default(self):
        """Test default value of --[no]molad option."""
        with self.assertRaises(ConfigurationParameterAmbiguousError):
            hbcal("hbcal -ih -o civil -- 1 2 5775")


class TestInvalidValue(TestCase):
    """Test "--molad" option with "molad = tree" in configuration file.

    "tree" is not a valid value of molad, so the program terminates
    with an error.
    """
    config_data = "molad = tree"

    def test_default(self):
        """Test default value of --[no]molad option."""
        with self.assertRaises(ConfigurationParameterValueError):
            hbcal("hbcal -ih -o civil -- 1 2 5775")


class TestMiscellaneous(TestCase):
    """Miscellaneous molad tests"""

    def test_early_morning(self):
        """Test molad before 6am.

        This was added as a regression test because it used to fail.
        """
        output = hbcal("hbcal -m -ih -oc 1 6 5775")
        self.assertEqual('Saturday 15 August 2015 04:23 and 8 parts',
                         output[0])

if __name__ == "__main__":
    unittest.main()
