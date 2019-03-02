""" Tests for '--[no]molad' and 'molad'.

This module contains tests for the '--molad' and '--nomolad' command line
options and for the 'molad' configuration file option.
"""
# Copyright 2015, 2016m 2019 Mark Stern
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
import sys
from hbcal.configuration_utilities import ConfigurationParameterValueError, \
    ConfigurationParameterAmbiguousError
from .utilities import ConfigurationData, TestCase, hbcal

# Test discovery uses setUpModule, but pylint does not know that.
# pylint: disable=unused-import
from .utilities import set_up_module as setUpModule  # noqa
# pylint: enable=unused-import

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


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

    def test_hebrew_output(self):
        """Test --molad option"""
        output = hbcal("hbcal -ih -o hebrew --molad 1 2 5775")
        self.assertEqual(u'\u05D9\u05D5\u05DD \u05E8\u05D0\u05E9\u05D5\u05DF '
                         + u'30 \u05E0\u05D9\u05E1\u05DF 5775 07:27 \u05D54 '
                         + u'\u05D7\u05DC\u05E7\u05D9\u05DD', output[0])

    def test_reverse_hebrew_output(self):
        """Test --molad option"""
        output = hbcal("hbcal -ih -o hebrew -freverse --molad 1 2 5775")
        self.assertEqual(u'\u05DD\u05D9\u05E7\u05DC\u05D7 4\u05D5 07:27 5775 '
                         + u'\u05DF\u05E1\u05D9\u05E0 30 '
                         + u'\u05DF\u05D5\u05E9\u05D0\u05E8 '
                         + u'\u05DD\u05D5\u05D9', output[0])

    def test_html_output(self):
        """Test --molad option"""
        output = hbcal("hbcal -ih -o hebrew -fhtml --molad 1 2 5775")
        self.assertEqual('&#1497;&#1493;&#1501; '
                         + '&#1512;&#1488;&#1513;&#1493;&#1503; 30 '
                         + '&#1504;&#1497;&#1505;&#1503; 5775 07:27 &#1493;4 '
                         + '&#1495;&#1500;&#1511;&#1497;&#1501;', output[0])


if __name__ == "__main__":
    unittest.main()
