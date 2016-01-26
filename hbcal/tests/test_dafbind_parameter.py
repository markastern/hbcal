""" Tests for '--dafbind'.

This module contains tests for the '--dafbind' and --nodafbind command line
options and for the 'dafbind' configuration file option.
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
from freezegun import freeze_time
from configuration_utilities import ConfigurationParameterValueError, \
    ConfigurationParameterAmbiguousError
from utilities import ConfigurationData, TestCase, hbcal

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

        def test_bind_civil(self):
            """Test --dafbind parameter with civil calendar."""
            output = hbcal("hbcal -id -od --dafbind civil -fphonetics")
            self.assertEqual(1, len(output))
            self.assertEqual('Bava Basra 133', output[0])

        def test_bind_gregorian(self):
            """Test --dafbind parameter with Gregorian calendar."""
            output = hbcal("hbcal -id -od -fphonetics --dafbind gregorian")
            self.assertEqual(1, len(output))
            self.assertEqual('Bava Basra 133', output[0])

        def test_bind_julian(self):
            """Test --dafbind parameter with Julian calendar."""
            output = hbcal("hbcal -id -od --dafbind julian -fphonetics")
            self.assertEqual(1, len(output))
            self.assertEqual('Bava Basra 133', output[0])

        def test_bind_hebrew(self):
            """Test --dafbind parameter with Hebrew calendar."""
            output = hbcal("hbcal -id -od --dafbind hebrew -fphonetics")
            self.assertEqual(1, len(output))
            self.assertEqual('Bava Basra 134', output[0])


@freeze_time("2010-01-01 19:35:35")
class TestNoConfigFile(Wrapper.CommonTests):
    """Test command line "--dafbind" option with no configuration file."""

    def test_default(self):
        """Test default value of --dafbind parameter."""
        output = hbcal("hbcal -id -od -fphonetics")
        self.assertEqual(1, len(output))
        self.assertEqual('Bava Basra 133', output[0])


@freeze_time("2010-01-01 19:35:35")
class TestEmptyConfigFile(Wrapper.CommonTests):
    """Test empty configuration file."""
    config_data = ConfigurationData.EMPTY

    def test_default(self):
        """Test default value of --dafbind parameter."""
        output = hbcal("hbcal -id -od -fphonetics")
        self.assertEqual(1, len(output))
        self.assertEqual('Bava Basra 133', output[0])


@freeze_time("2010-01-01 19:35:35")
class TestEmptySectionConfigFile(Wrapper.CommonTests):
    """Test configuration file with empty hbcal section."""

    config_data = ""

    def test_default(self):
        """Test default value of --dafbind parameter."""
        output = hbcal("hbcal -id -od -fphonetics")
        self.assertEqual(1, len(output))
        self.assertEqual('Bava Basra 133', output[0])


@freeze_time("2010-01-01 19:35:35")
class TestDafBindCivilConfigFile(Wrapper.CommonTests):
    """Test with "dafbind = civil" in configuration file."""

    config_data = "dafbind = civil"

    def test_default(self):
        """Test default value of --dafbind parameter."""
        output = hbcal("hbcal -id -od -fphonetics")
        self.assertEqual(1, len(output))
        self.assertEqual('Bava Basra 133', output[0])


@freeze_time("2010-01-01 19:35:35")
class TestDafBindGregorianConfigFile(Wrapper.CommonTests):
    """Test with "dafbind = gregorian" in configuration file."""

    config_data = "dafbind = gregorian"

    def test_default(self):
        """Test default value of --dafbind parameter."""
        output = hbcal("hbcal -id -od -fphonetics")
        self.assertEqual(1, len(output))
        self.assertEqual('Bava Basra 133', output[0])


@freeze_time("2010-01-01 19:35:35")
class TestDafBindJulianConfigFile(Wrapper.CommonTests):
    """Test with "dafbind = julian" in configuration file."""

    config_data = "dafbind = julian"

    def test_default(self):
        """Test default value of --dafbind parameter."""
        output = hbcal("hbcal -id -od -fphonetics")
        self.assertEqual(1, len(output))
        self.assertEqual('Bava Basra 133', output[0])


@freeze_time("2010-01-01 19:35:35")
class TestDafBindHebrewConfigFile(Wrapper.CommonTests):
    """Test with "dafbind = hebrew" in configuration file."""

    config_data = "dafbind = hebrew"

    def test_default(self):
        """Test default value of --dafbind parameter."""
        output = hbcal("hbcal -id -od -fphonetics")
        self.assertEqual(1, len(output))
        self.assertEqual('Bava Basra 134', output[0])


@freeze_time("2010-01-01 19:35:35")
class TestMixedCase(Wrapper.CommonTests):
    """Test with "dafbind = hebRew" (mixed case) in configuration file."""

    config_data = "dafbind = hebRew"

    def test_default(self):
        """Test default value of --dafbind parameter."""
        output = hbcal("hbcal -id -od -fphonetics")
        self.assertEqual(1, len(output))
        self.assertEqual('Bava Basra 134', output[0])


@freeze_time("2010-01-01 19:35:35")
class TestAbbreviated(Wrapper.CommonTests):
    """Test with "dafbind = heb" (abbreviated) in configuration file."""

    config_data = "dafbind = heb"

    def test_default(self):
        """Test default value of --dafbind parameter."""
        output = hbcal("hbcal -id -od -fphonetics")
        self.assertEqual(1, len(output))
        self.assertEqual('Bava Basra 134', output[0])


@freeze_time("2010-01-01 19:35:35")
class TestAbbreviatedTooMuch(TestCase):
    """Test with "dafbind =" (too abbreviated) in configuration file."""

    config_data = "dafbind ="

    def test_default(self):
        """Test default value of --dafbind parameter."""
        with self.assertRaises(ConfigurationParameterAmbiguousError):
            hbcal("hbcal -id -od -fphonetics")


@freeze_time("2010-01-01 19:35:35")
class TestInvalidValue(TestCase):
    """Test with "dafbind = daf" in the configuration file.

    This is invalid because the daf yomi calendar cannot be bound to itself.
    """

    config_data = "dafbind = daf"

    def test_default(self):
        """Test default value of --dafbind parameter."""
        with self.assertRaises(ConfigurationParameterValueError):
            hbcal("hbcal -id -od -fphonetics")

if __name__ == "__main__":
    unittest.main()
