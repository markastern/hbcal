""" Tests for '--sedrah' and '--nosedrah'.

This module contains tests for the '--sedrah' and '--nosedrah' command
line options and for the 'sedrah' configuration file option.
"""
# Copyright 2016 Mark Stern
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
    """Test command line "--sedrah" option with no configuration file."""

    def test_default(self):
        """Test default value of '--sedrah' option."""
        output = hbcal("hbcal -ih -o -fphonetics 1 8 5775")
        self.assertEqual(0, len(output))

    def test_sedrah_option(self):
        """Test '--sedrah' option."""
        output = hbcal("hbcal -ih -o --sedrah -fphonetics 1 8 5775")
        self.assertEqual(1, len(output))
        self.assertEqual(output[0], 'Noach')

    def test_nosedrah_option(self):
        """Test '--nosedrah' option."""
        output = hbcal("hbcal -ih -o --nosedrah -fphonetics 1 8 5775")
        self.assertEqual(0, len(output))

    def test_sedrah_short_option(self):
        """Test '-s' option."""
        output = hbcal("hbcal -ih -o -s -fphonetics 1 8 5775")
        self.assertEqual(1, len(output))
        self.assertEqual(output[0], 'Noach')


class TestEmptyConfigFile(TestNoConfigFile):
    """Test "--[no]sedrah" option with empty configuration file."""

    config_data = ConfigurationData.EMPTY


class TestEmptySectionConfigFile(TestNoConfigFile):
    """Test configuration file with empty hbcal section."""

    config_data = ""


class TestSedrahTrueInConfigFile(TestNoConfigFile):
    """Test "sedrah = true" in configuration file."""

    config_data = "sedrah = true"

    def test_default(self):
        output = hbcal("hbcal -ih -o -fphonetics 1 8 5775")
        self.assertEqual(1, len(output))
        self.assertEqual(output[0], 'Noach')


class TestSedrahYesInConfigFile(TestSedrahTrueInConfigFile):
    """Test "sedrah = yes" in configuration file."""

    config_data = "sedrah = yes"


class TestSedrahFalseInConfigFile(TestNoConfigFile):
    """Test "sedrah = false" in configuration file."""

    config_data = "sedrah = false"


class TestSedrahNoInConfigFile(TestSedrahFalseInConfigFile):
    """Test "sedrah = no" in configuration file."""

    config_data = "sedrah = no"


class TestMixedCase(TestSedrahTrueInConfigFile):
    """Test "sedrah = trUe" (mixed case) in configuration file."""

    config_data = "sedrah = trUe"


class TestAbbreviated(TestSedrahYesInConfigFile):
    """Test "sedrah = y" (abbreviated) in configuration file."""

    config_data = "sedrah = y"


class TestAbbreviatedTooMuch(TestCase):
    """Test "sedrah =" (too abbreviated) in configuration file."""

    config_data = "sedrah ="

    def test_default(self):
        """Test default value of '--sedrah' option."""
        with self.assertRaises(ConfigurationParameterAmbiguousError):
            hbcal("hbcal -ih -o -fphonetics 1 8 5775")


class InvalidValue(TestCase):
    """Test "sedrah = tree" (invalid value) in configuration file."""

    config_data = "sedrah = tree"

    def test_default(self):
        """Test default value of '--sedrah' option."""
        with self.assertRaises(ConfigurationParameterValueError):
            hbcal("hbcal -ih -o -fphonetics 1 8 5775")


if __name__ == "__main__":
    unittest.main()
