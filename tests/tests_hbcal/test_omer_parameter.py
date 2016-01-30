""" Tests for '--[no]omer' and 'omer'.

This module contains tests for the '--omer' and '--noomer' command line
options and for the 'omer' configuration file option.
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
from utilities import ConfigurationData, TestCase, hbcal

# Test discovery uses setUpModule, but pylint does not know that.
# pylint: disable=unused-import
from utilities import set_up_module as setUpModule  # noqa
# pylint: enable=unused-import

logging.basicConfig(filename='/dev/stdout', level=logging.DEBUG)


class TestNoConfigFile(TestCase):
    """Test command line "--[no]israel" option with no configuration file."""

    def test_default(self):
        """Test default value of --[no]omer option."""
        output = hbcal("hbcal -ih -o -fphonetics 1 2 5775")
        self.assertEqual(0, len(output))

    def test_omer_option(self):
        """Test --omer option."""
        output = hbcal("hbcal -ih -o --omer -fphonetics 1 2 5775")
        self.assertEqual(1, len(output))
        self.assertEqual('16th day of the omer', output[0])

    def test_noomer_option(self):
        """Test --noomer option."""
        output = hbcal("hbcal -ih -o --noomer -fphonetics 1 2 5775")
        self.assertEqual(0, len(output))

    def test_omer_short_option(self):
        """Test -O option."""
        output = hbcal("hbcal -ih -o -O -fphonetics 1 2 5775")
        self.assertEqual(1, len(output))
        self.assertEqual('16th day of the omer', output[0])


class TestEmptyConfigFile(TestNoConfigFile):
    """Test "--[no]omer" option with empty configuration file."""

    config_data = ConfigurationData.EMPTY


class TestEmptySectionConfigFile(TestNoConfigFile):
    """Test configuration file with empty hbcal section."""

    config_data = ""


class TestOmerTrueInConfigFile(TestNoConfigFile):
    """Test "omer = true" in configuration file."""

    config_data = "omer = true"

    def test_default(self):
        output = hbcal("hbcal -ih -o -fphonetics 1 2 5775")
        self.assertEqual(1, len(output))
        self.assertEqual('16th day of the omer', output[0])


class TestOmerYesInConfigFile(TestOmerTrueInConfigFile):
    """Test "omer = yes" in configuration file."""

    config_data = "omer = yes"


class TestOmerFalseInConfigFile(TestNoConfigFile):
    """Test "omer = false" in configuration file."""

    config_data = "omer = false"


class TestOmerNoInConfigFile(TestOmerFalseInConfigFile):
    """Test "omer = no" in configuration file."""

    config_data = "omer = no"


class TestMixedCase(TestOmerTrueInConfigFile):
    """Test "omer = trUe" (mixed case) in configuration file."""

    config_data = "omer = trUe"


class TestAbbreviated(TestOmerYesInConfigFile):
    """Test "omer = y" in configuration file."""

    config_data = "omer = y"


class TestAbbreviatedTooMuch(TestCase):
    """Test "omer =" (too abbreviated) in configuration file."""

    config_data = "omer ="

    def test_default(self):
        """Test default value of --[no]omer option."""
        with self.assertRaises(ConfigurationParameterAmbiguousError):
            hbcal("hbcal -ih -o -fphonetics 1 2 5775")


class InvalidValue(TestCase):
    """Test "omer = tree" (invalid) in the configuration file."""

    config_data = "omer = tree"

    def test_default(self):
        """Test default value of --[no]omer option."""
        with self.assertRaises(ConfigurationParameterValueError):
            hbcal("hbcal -ih -o -fphonetics 1 2 5775")

if __name__ == "__main__":
    unittest.main()
