""" Tests for '--output' and 'output calendar'.

This module contains tests for the '--output' command line option
and for the 'output calendar' configuration file option.
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
from configuration_utilities import ConfigurationParameterValueError
from utilities import ConfigurationData, TestCase, hbcal
# Test discovery uses setUpModule, but pylint does not know that.
# pylint: disable=unused-import
from utilities import set_up_module as setUpModule  # noqa

# pylint: enable=unused-import

logging.basicConfig(filename='/dev/stdout', level=logging.DEBUG)


class TestNoConfigFile(TestCase):
    """Test command line "--output" option with no configuration file."""

    def test_default_2015(self):
        """Test default value of --output parameter after 1752"""
        output = hbcal("hbcal -ic -fphonetics 17 8 2015")
        self.assertEqual('Monday 17 August 2015', output[0])
        self.assertEqual('Monday 2 Ellul 5775', output[1])
        self.assertEqual(2, len(output))

    def test_default_1750(self):
        """Test default value of --output parameter before 1752"""
        output = hbcal("hbcal -ic -fphonetics 17 8 1750")
        self.assertEqual(2, len(output))
        self.assertEqual('Friday 17 August 1750', output[0])
        self.assertEqual('Friday 26 Av 5510', output[1])

    def test_civil_option_2015(self):
        """Test --output with civil calendar after 1752"""
        output = hbcal("hbcal -ic -o civil -fphonetics 17 8 2015")
        self.assertEqual(1, len(output))
        self.assertEqual('Monday 17 August 2015', output[0])

    def test_civil_option_1750(self):
        """Test --output with civil calendar before 1752"""
        output = hbcal("hbcal -ic -o civil -fphonetics 17 8 1750")
        self.assertEqual(1, len(output))
        self.assertEqual('Friday 17 August 1750', output[0])

    def test_gregorian_option_2015(self):
        """Test --output with Gregorian calendar after 1752"""
        output = hbcal("hbcal -ic -o gregorian -fphonetics 17 8 2015")
        self.assertEqual(1, len(output))
        self.assertEqual('Monday 17 August 2015', output[0])

    def test_gregorian_option_1750(self):
        """Test --output with Gregorian calendar after 1752"""
        output = hbcal("hbcal -ic -o gregorian -fphonetics 17 8 1750")
        self.assertEqual(1, len(output))
        self.assertEqual('Friday 28 August 1750', output[0])

    def test_julian_option_2015(self):
        """Test --output with Julian calendar after 1752"""
        output = hbcal("hbcal -ic -o julian -fphonetics 17 8 2015")
        self.assertEqual(1, len(output))
        self.assertEqual('Monday 4 August 2015', output[0])

    def test_julian_option_1750(self):
        """Test --output with Julian calendar before 1752"""
        output = hbcal("hbcal -ic -o julian -fphonetics 17 8 1750")
        self.assertEqual(1, len(output))
        self.assertEqual('Friday 17 August 1750', output[0])

    def test_hebrew_option_5775(self):
        """Test --output with Hebrew calendar"""
        output = hbcal("hbcal -ic -o hebrew -fphonetics 17 8 2015")
        self.assertEqual(1, len(output))
        self.assertEqual('Monday 2 Ellul 5775', output[0])

    def test_daf_option_5775(self):
        """Test --output with Daf Yomi calendar"""
        output = hbcal("hbcal -ic -o daf -fphonetics 17 8 2015")
        self.assertEqual(1, len(output))
        self.assertEqual('Nedarim 85', output[0])

    def test_civil_hebrew_option_2015(self):
        """Test --output specifying civil and Hebrew after 1752."""
        output = hbcal("hbcal -ic -o civil hebrew -fphonetics 17 8 2015")
        self.assertEqual(2, len(output))
        self.assertEqual('Monday 17 August 2015', output[0])
        self.assertEqual('Monday 2 Ellul 5775', output[1])

    def test_civil_hebrew_option_1750(self):
        """Test --output specifying civil and Hebrew before 1752."""
        output = hbcal("hbcal -ic -o civil hebrew -fphonetics 17 8 1750")
        self.assertEqual(2, len(output))
        self.assertEqual('Friday 17 August 1750', output[0])
        self.assertEqual('Friday 26 Av 5510', output[1])

    def test_gregorian_hebrew_option_2015(self):
        """Test --output specifying Gregorian and Hebrew after 1752."""
        output = hbcal("hbcal -ic -o gregorian hebrew -fphonetics 17 8 2015")
        self.assertEqual('Monday 17 August 2015', output[0])
        self.assertEqual('Monday 2 Ellul 5775', output[1])
        self.assertEqual(2, len(output))

    def test_gregorian_hebrew_option_1750(self):
        """Test --output specifying Gregorian and Hebrew before 1752."""
        output = hbcal("hbcal -ic -o gregorian hebrew -fphonetics 17 8 1750")
        self.assertEqual(2, len(output))
        self.assertEqual('Friday 28 August 1750', output[0])
        self.assertEqual('Friday 26 Av 5510', output[1])

    def test_julian_hebrew_option_2015(self):
        """Test --output specifying Julian and Hebrew after 1752."""
        output = hbcal("hbcal -ic -o julian hebrew -fphonetics 17 8 2015")
        self.assertEqual(2, len(output))
        self.assertEqual('Monday 4 August 2015', output[0])
        self.assertEqual('Monday 2 Ellul 5775', output[1])

    def test_julian_hebrew_option_1750(self):
        """Test --output specifying Julian and Hebrew before 1752."""
        output = hbcal("hbcal -ic -o julian hebrew -fphonetics 17 8 1750")
        self.assertEqual(2, len(output))
        self.assertEqual('Friday 17 August 1750', output[0])
        self.assertEqual('Friday 26 Av 5510', output[1])

    def test_civil_daf_option_2015(self):
        """Test --output specifying Civil and Daf Yomi"""
        output = hbcal("hbcal -ic -o civil daf -fphonetics 17 8 2015")
        self.assertEqual(2, len(output))
        self.assertEqual('Monday 17 August 2015', output[0])
        self.assertEqual('Nedarim 85', output[1])

    def test_civil_daf_option_1750(self):
        """Test --output specifying civil and daf before 1752.

        No daf is output because the date precedes the inauguration
        of Daf Yomi.
        """
        output = hbcal("hbcal -ic -o civil daf -fphonetics 17 8 1750")
        self.assertEqual(1, len(output))
        self.assertEqual('Friday 17 August 1750', output[0])

    def test_gregorian_daf_option_2015(self):
        """Test --output specifying Gregorian and Daf Yomi"""
        output = hbcal("hbcal -ic -o gregorian daf -fphonetics 17 8 2015")
        self.assertEqual(2, len(output))
        self.assertEqual('Monday 17 August 2015', output[0])
        self.assertEqual('Nedarim 85', output[1])

    def test_gregorian_daf_option_1750(self):
        """Test --output specifying Gregorian and Daf Yomi before 1752.

        No daf is output because the date precedes the inauguration
        of Daf Yomi.
        """
        output = hbcal("hbcal -ic -o gregorian daf -fphonetics 17 8 1750")
        self.assertEqual(1, len(output))
        self.assertEqual('Friday 28 August 1750', output[0])

    def test_julian_daf_option_2015(self):
        """Test --output specifying Julian and Daf Yomi"""
        output = hbcal("hbcal -ic -o julian daf -fphonetics 17 8 2015")
        self.assertEqual(2, len(output))
        self.assertEqual('Monday 4 August 2015', output[0])
        self.assertEqual('Nedarim 85', output[1])

    def test_julian_daf_option_1750(self):
        """Test --output specifying Julian and Daf Yomi before 1752.

        No daf is output because the date precedes the inauguration
        of Daf Yomi.
        """
        output = hbcal("hbcal -ic -o julian daf -fphonetics 17 8 1750")
        self.assertEqual(1, len(output))
        self.assertEqual('Friday 17 August 1750', output[0])

    def test_hebrew_daf_option_5775(self):
        """Test --output specifying Hebrew and Daf Yomi."""
        output = hbcal("hbcal -ic -o hebrew daf -fphonetics 17 8 2015")
        self.assertEqual(2, len(output))
        self.assertEqual('Monday 2 Ellul 5775', output[0])
        self.assertEqual('Nedarim 85', output[1])

    def test_civil_hebrew_daf_option_2015(self):
        """Test --output specifying civil, Hebrew and Daf Yomi."""
        output = hbcal("hbcal -ic -o civil hebrew daf -fphonetics 17 8 2015")
        self.assertEqual(3, len(output))
        self.assertEqual('Monday 17 August 2015', output[0])
        self.assertEqual('Monday 2 Ellul 5775', output[1])
        self.assertEqual('Nedarim 85', output[2])

    def test_civil_hebrew_daf_option_1750(self):
        """Test --output specifying civil, Hebrew and Daf Yomi before 1752.

        No daf is output because the date precedes the inauguration
        of Daf Yomi.
        """
        output = hbcal("hbcal -ic -o civil hebrew daf -fphonetics 17 8 1750")
        self.assertEqual(2, len(output))
        self.assertEqual('Friday 17 August 1750', output[0])
        self.assertEqual('Friday 26 Av 5510', output[1])

    def test_gregorian_hebrew_daf_option_2015(self):
        """Test --output specifying Gregorian, Hebrew and Daf Yomi."""
        output = hbcal("hbcal -ic -o gregorian hebrew daf -fphonetics" +
                       " 17 8 2015")
        self.assertEqual(3, len(output))
        self.assertEqual('Monday 17 August 2015', output[0])
        self.assertEqual('Monday 2 Ellul 5775', output[1])
        self.assertEqual('Nedarim 85', output[2])

    def test_gregorian_hebrew_daf_option_1750(self):
        """Test --output specifying Gregorian, Hebrew and Daf Yomi before 1752.

        No daf is output because the date precedes the inauguration
        of Daf Yomi.
        """
        output = hbcal("hbcal -ic -o gregorian hebrew daf -fphonetics" +
                       " 17 8 1750")
        self.assertEqual(2, len(output))
        self.assertEqual('Friday 28 August 1750', output[0])
        self.assertEqual('Friday 26 Av 5510', output[1])

    def test_julian_hebrew_daf_option_2015(self):
        """Test --output specifying Julian, Hebrew and Daf Yomi."""
        output = hbcal("hbcal -ic -o julian hebrew daf -fphonetics 17 8 2015")
        self.assertEqual(3, len(output))
        self.assertEqual('Monday 4 August 2015', output[0])
        self.assertEqual('Monday 2 Ellul 5775', output[1])
        self.assertEqual('Nedarim 85', output[2])

    def test_julian_hebrew_daf_option_1750(self):
        """Test --output specifying Julian, Hebrew and Daf Yomi before 1752.

        No daf is output because the date precedes the inauguration
        of Daf Yomi.
        """
        output = hbcal("hbcal -ic -o julian hebrew daf -fphonetics 17 8 1750")
        self.assertEqual(2, len(output))
        self.assertEqual('Friday 17 August 1750', output[0])
        self.assertEqual('Friday 26 Av 5510', output[1])

    def test_long_option(self):
        """Test the long version of --output."""
        output = hbcal("hbcal -ic --output julian -fphonetics 17 8 2015")
        self.assertEqual(1, len(output))
        self.assertEqual('Monday 4 August 2015', output[0])

    def test_long_option_multiple_calendars(self):
        """Test use of one --output option (long) with 2 calendars"""
        output = hbcal("hbcal -ic --output julian hebrew -fphonetics" +
                       " 17 8 2015")
        self.assertEqual(2, len(output))
        self.assertEqual('Monday 4 August 2015', output[0])
        self.assertEqual('Monday 2 Ellul 5775', output[1])

    def test_multiple_short_options(self):
        """Test double use of --output (short version)"""
        output = hbcal("hbcal -ic -o julian -o hebrew -fphonetics 17 8 2015")
        self.assertEqual(2, len(output))
        self.assertEqual('Monday 4 August 2015', output[0])
        self.assertEqual('Monday 2 Ellul 5775', output[1])

    def test_multiple_long_options(self):
        """Test double use of --output (long version)"""
        output = hbcal("hbcal -ic --output julian --output hebrew" +
                       " -fphonetics 17 8 2015")
        self.assertEqual(2, len(output))
        self.assertEqual('Monday 4 August 2015', output[0])
        self.assertEqual('Monday 2 Ellul 5775', output[1])

    def test_abbreviated_option(self):
        """Test use of an abbreviated value of --output option"""
        output = hbcal("hbcal -ic --output jul -fphonetics 17 8 2015")
        self.assertEqual(1, len(output))
        self.assertEqual('Monday 4 August 2015', output[0])

    def test_civil_gregorian_option(self):
        """Test --output specifying Civil and Gregorian calendars.

        These options are incompatible, so the program terminates with an
        error.
        """
        with self.assertRaises(SystemExit):
            hbcal("hbcal -ic -o civil gregorian -fphonetics 17 8 1750")

    def test_civil_julian_option(self):
        """Test --output specifying Civil and Julian calendars.

        These options are incompatible, so the program terminates with an
        error.
        """
        with self.assertRaises(SystemExit):
            hbcal("hbcal -ic -o civil julian -fphonetics 17 8 1750")

    def test_gregorian_julian_option(self):
        """Test --output specifying Gregorian and Julian calendars.

        These options are incompatible, so the program terminates with an
        error.
        """
        with self.assertRaises(SystemExit):
            hbcal("hbcal -ic -o gregorian julian -fphonetics 17 8 1750")


class TestEmptyConfigFile(TestNoConfigFile):
    """Test empty configuration file."""

    config_data = ConfigurationData.EMPTY


class TestEmptySectionConfigFile(TestNoConfigFile):
    """Test configuration file with empty hbcal section."""

    config_data = ""


class TestCivilInConfigFile(TestNoConfigFile):
    """Test "output calendar = civil" in the configuration file."""

    config_data = "output calendar = civil"

    def test_default_2015(self):
        output = hbcal("hbcal -ic -fphonetics 17 8 2015")
        self.assertEqual(1, len(output))
        self.assertEqual('Monday 17 August 2015', output[0])

    def test_default_1750(self):
        output = hbcal("hbcal -ic -fphonetics 17 8 1750")
        self.assertEqual(1, len(output))
        self.assertEqual('Friday 17 August 1750', output[0])


class TestGregorianInConfigFile(TestCivilInConfigFile):
    """Test "output calendar = greorian" in the configuration file."""
    config_data = "output calendar = gregorian"

    def test_default_1750(self):
        output = hbcal("hbcal -ic -fphonetics 17 8 1750")
        self.assertEqual(1, len(output))
        self.assertEqual('Friday 28 August 1750', output[0])


class TestJulianInConfigFile(TestCivilInConfigFile):
    """Test "output calendar = julian" in the configuration file."""

    config_data = "output calendar = julian"

    def test_default_2015(self):
        output = hbcal("hbcal -ic -fphonetics 17 8 2015")
        self.assertEqual(1, len(output))
        self.assertEqual('Monday 4 August 2015', output[0])


class TestHebrewInConfigFile(TestNoConfigFile):
    """Test "output calendar = hebrew" in the configuration file."""

    config_data = "output calendar = hebrew"

    def test_default_2015(self):
        output = hbcal("hbcal -ic -fphonetics 17 8 2015")
        self.assertEqual(1, len(output))
        self.assertEqual('Monday 2 Ellul 5775', output[0])

    def test_default_1750(self):
        output = hbcal("hbcal -ic -fphonetics 17 8 1750")
        self.assertEqual(1, len(output))
        self.assertEqual('Friday 26 Av 5510', output[0])


class TestDafInConfigFile(TestNoConfigFile):
    """Test "output calendar = daf" in the configuration file."""

    config_data = "output calendar = daf"

    def test_default_2015(self):
        output = hbcal("hbcal -ic -fphonetics 17 8 2015")
        self.assertEqual(1, len(output))
        self.assertEqual('Nedarim 85', output[0])

    def test_default_1750(self):
        output = hbcal("hbcal -ic -fphonetics 17 8 1750")
        # No output - before inauguration of Daf Yomi
        self.assertEqual(0, len(output))


class TestCivilHebrewInConfigFile(TestNoConfigFile):
    """Test "output calendar = civil hebrew" in the configuration file.

    This is the default, so no tests need to be overridden.
    """

    config_data = "output calendar = civil hebrew"


class TestGregorianHebrewInConfigFile(TestNoConfigFile):
    """Test "output calendar = gregorian hebrew" in the configuration file."""

    config_data = "output calendar = gregorian hebrew"

    def test_default_1750(self):
        output = hbcal("hbcal -ic -fphonetics 17 8 1750")
        self.assertEqual(2, len(output))
        self.assertEqual('Friday 28 August 1750', output[0])
        self.assertEqual('Friday 26 Av 5510', output[1])


class TestJulianHebrewInConfigFile(TestNoConfigFile):
    """Test "output calendar = julian hebrew" in the configuration file."""

    config_data = "output calendar = julian hebrew"

    def test_default_2015(self):
        output = hbcal("hbcal -ic -fphonetics 17 8 2015")
        self.assertEqual(2, len(output))
        self.assertEqual('Monday 4 August 2015', output[0])
        self.assertEqual('Monday 2 Ellul 5775', output[1])


class TestCivilDafInConfigFile(TestNoConfigFile):
    """Test "output calendar = civil daf" in the configuration file."""

    config_data = "output calendar = civil daf"

    def test_default_2015(self):
        """Test default value of --output parameter after 1752"""
        output = hbcal("hbcal -ic -fphonetics 17 8 2015")
        self.assertEqual(2, len(output))
        self.assertEqual('Monday 17 August 2015', output[0])
        self.assertEqual('Nedarim 85', output[1])

    def test_default_1750(self):
        """Test default value of --output parameter before 1752.

        No daf is output because the date precedes the inauguration
        of Daf Yomi.
        """
        output = hbcal("hbcal -ic -fphonetics 17 8 1750")
        self.assertEqual(1, len(output))
        self.assertEqual('Friday 17 August 1750', output[0])


class TestGregorianDafInConfigFile(TestNoConfigFile):
    """Test "output calendar = greorian daf" in the configuration file."""
    config_data = "output calendar = gregorian daf"

    def test_default_2015(self):
        """Test default value of --output parameter after 1752"""
        output = hbcal("hbcal -ic -fphonetics 17 8 2015")
        self.assertEqual(2, len(output))
        self.assertEqual('Monday 17 August 2015', output[0])
        self.assertEqual('Nedarim 85', output[1])

    def test_default_1750(self):
        """Test default value of --output parameter before 1752.

        No daf is output because the date precedes the inauguration
        of Daf Yomi.
        """
        output = hbcal("hbcal -ic -fphonetics 17 8 1750")
        self.assertEqual(1, len(output))
        self.assertEqual('Friday 28 August 1750', output[0])


class TestJulianDafInConfigFile(TestNoConfigFile):
    """Test "output calendar = julian daf" in the configuration file."""

    config_data = "output calendar = julian daf"

    def test_default_2015(self):
        output = hbcal("hbcal -ic -fphonetics 17 8 2015")
        self.assertEqual(2, len(output))
        self.assertEqual('Monday 4 August 2015', output[0])
        self.assertEqual('Nedarim 85', output[1])

    def test_default_1750(self):
        """Test default value of --output parameter before 1752.

        No daf is output because the date precedes the inauguration
        of Daf Yomi.
        """
        output = hbcal("hbcal -ic -fphonetics 17 8 1750")
        self.assertEqual(1, len(output))
        self.assertEqual('Friday 17 August 1750', output[0])


class TestHebrewDafInConfigFile(TestNoConfigFile):
    """Test "output calendar = hebrew daf" in the configuration file."""

    config_data = "output calendar = hebrew daf"

    def test_default_2015(self):
        """Test default value of --output parameter after 1752"""
        output = hbcal("hbcal -ic -fphonetics 17 8 2015")
        self.assertEqual(2, len(output))
        self.assertEqual('Monday 2 Ellul 5775', output[0])
        self.assertEqual('Nedarim 85', output[1])

    def test_default_1750(self):
        """Test default value of --output parameter before 1752.

        No daf is output because the date precedes the inauguration
        of Daf Yomi.
        """
        output = hbcal("hbcal -ic -fphonetics 17 8 1750")
        self.assertEqual(1, len(output))
        self.assertEqual('Friday 26 Av 5510', output[0])


class TestCivilHebrewDafInConfigFile(TestNoConfigFile):
    """Test "output calendar = civil hebrew daf" in configuration file."""

    config_data = "output calendar = civil hebrew daf"

    def test_default_2015(self):
        output = hbcal("hbcal -ic -fphonetics 17 8 2015")
        self.assertEqual(3, len(output))
        self.assertEqual('Monday 17 August 2015', output[0])
        self.assertEqual('Monday 2 Ellul 5775', output[1])
        self.assertEqual('Nedarim 85', output[2])

    def test_default_1750(self):
        """Test default value of --output parameter before 1752.

        No daf is output because the date precedes the inauguration
        of Daf Yomi.
        """
        output = hbcal("hbcal -ic -fphonetics 17 8 1750")
        self.assertEqual(2, len(output))
        self.assertEqual('Friday 17 August 1750', output[0])
        self.assertEqual('Friday 26 Av 5510', output[1])


class TestGregorianHebrewDafInConfigFile(TestCivilHebrewDafInConfigFile):
    """Test "output calendar = gregorian hebrew daf" in configuration file."""
    config_data = "output calendar = gregorian hebrew daf"

    def test_default_1750(self):
        """Test default value of --output parameter before 1752.

        No daf is output because the date precedes the inauguration
        of Daf Yomi.
        """
        output = hbcal("hbcal -ic -fphonetics 17 8 1750")
        self.assertEqual(2, len(output))
        self.assertEqual('Friday 28 August 1750', output[0])
        self.assertEqual('Friday 26 Av 5510', output[1])


class TestJulianHebrewDafInConfigFile(TestCivilHebrewDafInConfigFile):
    """Test "output calendar = julian hebrew daf" in configuration file."""

    config_data = "output calendar = julian hebrew daf"

    def test_default_2015(self):
        output = hbcal("hbcal -ic -fphonetics 17 8 2015")
        self.assertEqual(3, len(output))
        self.assertEqual('Monday 4 August 2015', output[0])
        self.assertEqual('Monday 2 Ellul 5775', output[1])
        self.assertEqual('Nedarim 85', output[2])


class TestOutputCalendarEmptyInConfigFile(TestNoConfigFile):
    """Test "output calendar =" with no calendar in the configuration file.

    The deafult in this case is that no calendar will be output.
    """
    config_data = "output calendar ="

    def test_default_2015(self):
        output = hbcal("hbcal -ic -fphonetics 17 8 2015")
        self.assertEqual(0, len(output))

    def test_default_1750(self):
        output = hbcal("hbcal -ic -fphonetics 17 8 1750")
        self.assertEqual(0, len(output))


class TestMixedCase(TestHebrewInConfigFile):
    """Test output calendar in configuration file using mixed case."""

    config_data = "output calendar = Hebrew"


class TestAbbreviated(TestNoConfigFile):
    """Test "output calendar = h j" in configuration file.

    This tests using using abbreviated calendar names.
    """
    config_data = "output calendar = h j"

    def test_default_2015(self):
        output = hbcal("hbcal -ic -fphonetics 17 8 2015")
        self.assertEqual(2, len(output))
        self.assertEqual('Monday 2 Ellul 5775', output[0])
        self.assertEqual('Monday 4 August 2015', output[1])

    def test_default_1750(self):
        output = hbcal("hbcal -ic -fphonetics 17 8 1750")
        self.assertEqual(2, len(output))
        self.assertEqual('Friday 26 Av 5510', output[0])
        self.assertEqual('Friday 17 August 1750', output[1])


class TestInvalidValue(TestCase):
    """Test invalid value of output calendar in configuration file."""

    config_data = "output calendar = julien"

    def test_default(self):
        """Test default value of --output parameter."""
        with self.assertRaises(ConfigurationParameterValueError):
            hbcal("hbcal -ic -fphonetics 17 8 2015")


class TestCivilGregorianInConfigFile(TestCase):
    """Test "output calendar = civil gregorian" in configuration file.

    These calendars are incompatible in the output,
    so an error should be generated.
    """
    config_data = "output calendar = civil gregorian"

    def test_default(self):
        """Test default value of --output parameter."""
        with self.assertRaises(ConfigurationParameterValueError):
            hbcal("hbcal -ic -fphonetics 17 8 2015")


class TestCivilJulianInConfigFile(TestCase):
    """Test "output calendar = civil julian" in configuration file.

    These calendars are incompatible in the output,
    so an error should be generated.
    """
    config_data = "output calendar = civil julian"

    def test_default(self):
        """Test default value of --output parameter."""
        with self.assertRaises(ConfigurationParameterValueError):
            hbcal("hbcal -ic -fphonetics 17 8 2015")


class TestGregorianJulianInConfigFile(TestCase):
    """Test "output calendar = greogian julian" in configuration file.

    These calendars are incompatible in the output,
    so an error should be generated.
    """
    config_data = "output calendar = gregorian julian"

    def test_default(self):
        """Test default value of --output parameter."""
        with self.assertRaises(ConfigurationParameterValueError):
            hbcal("hbcal -ic -fphonetics 17 8 2015")


if __name__ == "__main__":
    unittest.main()
