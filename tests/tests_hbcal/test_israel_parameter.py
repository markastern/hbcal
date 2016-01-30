""" Tests for '--[no]israel' and 'israel'.

This module contains tests for the '--israel' and '--noisrael' command line
options and for the 'israel' configuration file option.
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
from utilities import ConfigurationData, hbcal, TestCase
# Test discovery uses setUpModule, but pylint does not know that.
# pylint: disable=unused-import
from utilities import set_up_module as setUpModule  # noqa

# pylint: enable=unused-import

logging.basicConfig(filename='/dev/stdout', level=logging.DEBUG)


class TestNoConfigFile(TestCase):
    """Test command line "--[no]israel" option with no configuration file."""

    def test_default(self):
        """Test default value of --[no]israel option."""
        output = hbcal("hbcal -s -ih -o -fphonetics 23 7 5775")
        self.assertEqual('Vzoth Haberachah', output[0])

    def test_israel_option(self):
        """Test --israel option."""
        output = hbcal("hbcal -s -ih -o --israel -fphonetics 23 7 5775")
        self.assertEqual('Bereshith', output[0])

    def test_noisrael_option(self):
        """Test --noisrael option."""
        output = hbcal("hbcal -s -ih -o --noisrael -fphonetics 23 7 5775")
        self.assertEqual('Vzoth Haberachah', output[0])

    def test_israel_short_option(self):
        """Test -I option."""
        output = hbcal("hbcal -s -ih -o -I -fphonetics 23 7 5775")
        self.assertEqual('Bereshith', output[0])


class TestEmptyConfigFile(TestNoConfigFile):
    """Test "--[no]israel" option with empty configuration file."""

    config_data = ConfigurationData.EMPTY


class TestEmptySectionConfigFile(TestNoConfigFile):
    """Test configuration file with empty hbcal section."""

    config_data = ""


class TestIsraelTrueInConfigFile(TestNoConfigFile):
    """Test "israel = true" in configuration file."""

    config_data = "israel = true"

    def test_default(self):
        output = hbcal("hbcal -s -ih -o -fphonetics 23 7 5775")
        self.assertEqual('Bereshith', output[0])


class TestIsraelYesInConfigFile(TestIsraelTrueInConfigFile):
    """Test "israel = yes" in configuration file."""

    config_data = "israel = yes"


class TestIsraelFalseInConfigFile(TestNoConfigFile):
    """Test "israel = false" in configuration file."""

    config_data = "israel = false"


class TestIsraelNoInConfigFile(TestIsraelFalseInConfigFile):
    """Test "israel = no" in configuration file."""

    config_data = "israel = no"


class TestMixedCase(TestIsraelTrueInConfigFile):
    """Test "israel = trUe" (mixed case) in configuration file."""

    config_data = "israel = trUe"


class TestAbbreviated(TestIsraelYesInConfigFile):
    """Test "israel = y" in configuration file."""

    config_data = "israel = y"


class TestAbbreviatedTooMuch(TestCase):
    """Test "israel =" (too abbreviated) in configuration file."""

    config_data = "israel ="

    def test_default(self):
        """Test default value of --[no]israel option."""
        with self.assertRaises(ConfigurationParameterAmbiguousError):
            hbcal("hbcal -s -ih -o -fphonetics 23 7 5775")


class InvalidValue(TestCase):
    """Test "israel = tree" (invalid) in the configuration file."""

    config_data = "israel = tree"

    def test_default(self):
        """Test default value of --[no]israel option."""
        with self.assertRaises(ConfigurationParameterValueError):
            hbcal("hbcal -s -ih -o -fphonetics 23 7 5775")


if __name__ == "__main__":
    unittest.main()
