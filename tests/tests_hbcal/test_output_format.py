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
import sys

from hbcal.configuration_utilities import ConfigurationParameterValueError
from .utilities import ConfigurationData, TestCase, hbcal
# Test discovery uses setUpModule, but pylint does not know that.
# pylint: disable=unused-import
from .utilities import set_up_module as setUpModule  # noqa

# pylint: enable=unused-import

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class TestNoConfigFile(TestCase):
    """Test command line "--format" option with no configuration file."""

    def test_default(self):
        """Test default value of --format option."""
        output = hbcal("hbcal -ig -oh 3 8 2019")
        self.assertEqual(u"\u05E9\u05D1\u05EA 2 \u05D0\u05D1 5779", output[0])

    def test_normal_option(self):
        """Test '--format normal' command line option."""
        output = hbcal("hbcal -ig --format normal -oh 3 8 2019")
        self.assertEqual(u"\u05E9\u05D1\u05EA 2 \u05D0\u05D1 5779", output[0])

    def test_reverse_option(self):
        """Test '--format reverse' command line option."""
        output = hbcal("hbcal -ig --format reverse -oh 3 8 2019")
        self.assertEqual(u"5779 \u05D1\u05D0 2 \u05EA\u05D1\u05E9", output[0])

    def test_html_option(self):
        """Test '--format html' command line option."""
        output = hbcal("hbcal -ig --format html -oh 3 8 2019")
        self.assertEqual('&#1513;&#1489;&#1514; 2 &#1488;&#1489; 5779',
                         output[0])

    def test_phonetics_option(self):
        """Test '--format phonetics' command line option."""
        output = hbcal("hbcal -ig --format phonetics -oh 3 8 2019")
        self.assertEqual('Saturday 2 Av 5779', output[0])

    def test_gematria_option(self):
        """Test '--format gematria' command line option."""
        output = hbcal("hbcal -ig --format gematria -oh 3 8 2019")
        self.assertEqual(u"\u05E9\u05D1\u05EA \u05D1\u05F3 \u05D0\u05D1 "
                         + u"\u05EA\u05E9\u05E2\u05F4\u05D8", output[0])

    def test_normal_gematria_options(self):
        """Test '--format normal gematria' command line option."""
        output = hbcal("hbcal -ig --format normal gematria -oh 3 8 2019")
        self.assertEqual(u"\u05E9\u05D1\u05EA \u05D1\u05F3 \u05D0\u05D1 "
                         + u"\u05EA\u05E9\u05E2\u05F4\u05D8", output[0])

    def test_reverse_gematria_options(self):
        """Test '--format reverse gematria' command line option."""
        output = hbcal("hbcal -ig --format reverse gematria -oh 3 8 2019")
        self.assertEqual(u"\u05D8\u05F4\u05E2\u05E9\u05EA \u05D1\u05D0 "
                         + u"\u05F3\u05D1 \u05EA\u05D1\u05E9", output[0])

    def test_html_gematria_options(self):
        """Test '--format normal gematria' command line option."""
        output = hbcal("hbcal -ig --format html gematria -oh 3 8 2019")
        self.assertEqual('&#1513;&#1489;&#1514; &#1489;&#1523; &#1488;&#1489; '
                         + '&#1514;&#1513;&#1506;&#1524;&#1496;', output[0])

    def test_phonetics_gematria_options(self):
        with self.assertRaises(SystemExit):
            hbcal("hbcal -ig --format phonetics gematria -oh 3 8 2019")

    def test_reverse_html_options(self):
        with self.assertRaises(SystemExit):
            hbcal("hbcal -ig --format reverse html -oh 3 8 2019")

    def test_short_option(self):
        """Test '-f' command line option."""
        output = hbcal("hbcal -ig -fhtml -oh 3 8 2019")
        self.assertEqual('&#1513;&#1489;&#1514; 2 &#1488;&#1489; 5779',
                         output[0])

    def test_abbreviated_value(self):
        """Test '--format rev' in command line."""
        output = hbcal("hbcal -ig --format rev -oh 3 8 2019")
        self.assertEqual(u"5779 \u05D1\u05D0 2 \u05EA\u05D1\u05E9", output[0])

    def test_short_option_abbreviated(self):
        """Test '-fp' in command line.

        This tests a short option with an abbreviated value.
        """
        output = hbcal("hbcal -ig -fp -oh 3 8 2019")
        self.assertEqual('Saturday 2 Av 5779', output[0])


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
        output = hbcal("hbcal -ig -oh 3 8 2019")
        self.assertEqual(u"5779 \u05D1\u05D0 2 \u05EA\u05D1\u05E9", output[0])


class TestHtmlInConfigFile(TestNoConfigFile):
    """Test 'format = html' in configuration file."""

    config_data = "format = html"

    def test_default(self):
        output = hbcal("hbcal -ig -oh 3 8 2019")
        self.assertEqual('&#1513;&#1489;&#1514; 2 &#1488;&#1489; 5779',
                         output[0])


class TestPhoneticsInConfigFile(TestNoConfigFile):
    """Test 'format = phonetics' in configuration file."""

    config_data = "format = phonetics"

    def test_default(self):
        output = hbcal("hbcal -ig -oh 3 8 2019")
        self.assertEqual('Saturday 2 Av 5779', output[0])


class TestGematriaInConfigFile(TestNoConfigFile):
    """Test 'format = gematria' in configuration file."""

    config_data = "format = gematria"

    def test_default(self):
        output = hbcal("hbcal -ig -oh 3 8 2019")
        self.assertEqual(u"\u05E9\u05D1\u05EA \u05D1\u05F3 \u05D0\u05D1 "
                         + u"\u05EA\u05E9\u05E2\u05F4\u05D8", output[0])


class TestNormalGematriaInConfigFile(TestNoConfigFile):
    """Test 'format = normal gematria' in configuration file."""

    config_data = "format = normal gematria"

    def test_default(self):
        output = hbcal("hbcal -ig -oh 3 8 2019")
        self.assertEqual(u"\u05E9\u05D1\u05EA \u05D1\u05F3 \u05D0\u05D1 "
                         + u"\u05EA\u05E9\u05E2\u05F4\u05D8", output[0])


class TestReverseGematriaInConfigFile(TestNoConfigFile):
    """Test 'format = reverse gematria' in configuration file."""

    config_data = "format = reverse gematria"

    def test_default(self):
        output = hbcal("hbcal -ig -oh 3 8 2019")
        self.assertEqual(u"\u05D8\u05F4\u05E2\u05E9\u05EA \u05D1\u05D0 "
                         + u"\u05F3\u05D1 \u05EA\u05D1\u05E9", output[0])


class TestHtmlGematriaInConfigFile(TestNoConfigFile):
    """Test 'format = html' in configuration file."""

    config_data = "format = html gematria"

    def test_default(self):
        output = hbcal("hbcal -ig -oh 3 8 2019")
        self.assertEqual('&#1513;&#1489;&#1514; &#1489;&#1523; &#1488;&#1489; '
                         + '&#1514;&#1513;&#1506;&#1524;&#1496;', output[0])


class TestPhoneticsGematriaInConfigFile(TestCase):
    """Test 'format = phonetics gematria' in configuration file."""

    config_data = "format = phonetics gematria"

    def test_default(self):
        with self.assertRaises(ConfigurationParameterValueError) as cm_e:
            hbcal('-ig -oh 3 8 2019')
        self.assertEqual("Configuration parameter 'format' has invalid value "
                         + "'phonetics gematria'", cm_e.exception.message)


class TestReverseHtmlInConfigFile(TestCase):
    """Test 'format = reverse html' in configuration file."""

    config_data = "format = reverse html"

    def test_default(self):
        with self.assertRaises(ConfigurationParameterValueError) as cm_e:
            hbcal('-ig -oh 3 8 2019')
        self.assertEqual("Configuration parameter 'format' has invalid value "
                         + "'reverse html'", cm_e.exception.message)


class TestMixedCase(TestReverseInConfigFile):
    """Test 'format = Reverse' (mixed case in configuration file."""

    config_data = "format = Reverse"


class TestAbbreviated(TestReverseInConfigFile):
    """Test 'formar = r' in configuration file."""

    config_data = "format = r"


class TestFormatEmptyInConfigFile(TestNoConfigFile):
    """Test "format =" with no value in the configuration file.

    The default in this case is equivalent to 'normal'.
    """
    config_data = "format ="


class TestInvalidValue(TestCase):
    """Test "format = hebrew" (invalid) in configuration file."""

    config_data = "format = hebrew"

    def test_default(self):
        """Test default value of --format option."""
        with self.assertRaises(ConfigurationParameterValueError) as cm_e:
            hbcal("hbcal -ih -o -s 1 8 5775")
        self.assertEqual("Configuration parameter 'format' has invalid value "
                         + "'hebrew'", cm_e.exception.message)


class TestMiscellaneous(TestCase):
    """Miscellaneous output format tests"""

    def test_adar_reverse_option(self):
        """ Tests a bug fix. Adar was coming out as 'Adar Alef Geresh' """
        output = hbcal("hbcal -ih -oh -freverse 1 12 2")
        self.assertEqual(u"2 \u05E8\u05D3\u05D0 1 \u05D9\u05E0\u05E9 " +
                         u"\u05DD\u05D5\u05D9", output[0])

    def test_meilah_2(self):
        """ Tests output of daf yomi for meilah """
        output = hbcal("hbcal -od -freverse 19 9 2019")
        self.assertEqual(u"2 \u05D4\u05DC\u05D9\u05E2\u05DE", output[0])

    def test_meilah_22(self):
        """ Tests output of daf yomi for meilah """
        output = hbcal("hbcal -od -freverse 9 10 2019")
        self.assertEqual(u"22 (\u05DD\u05D9\u05E0\u05E7/"
                         + u"\u05D4\u05DC\u05D9\u05E2\u05DE) "
                         + u"\u05D4\u05DC\u05D9\u05E2\u05DE", output[0])

    def test_meilah_23(self):
        """ Tests output of daf yomi for meilah """
        output = hbcal("hbcal -od -freverse 10 10 2019")
        self.assertEqual(u"23 (\u05DD\u05D9\u05E0\u05E7) "
                         + u"\u05D4\u05DC\u05D9\u05E2\u05DE", output[0])

    def test_meilah_24(self):
        """ Tests output of daf yomi for meilah """
        output = hbcal("hbcal -od -freverse 11 10 2019")
        self.assertEqual(u"24 (\u05DD\u05D9\u05E0\u05E7) "
                         + u"\u05D4\u05DC\u05D9\u05E2\u05DE", output[0])

    def test_meilah_25(self):
        """ Tests output of daf yomi for meilah """
        output = hbcal("hbcal -od -freverse 12 10 2019")
        self.assertEqual(u"25 (\u05D3\u05D9\u05DE\u05EA/"
                         + u"\u05DD\u05D9\u05E0\u05E7) "
                         + u"\u05D4\u05DC\u05D9\u05E2\u05DE", output[0])

    def test_meilah_26(self):
        """ Tests output of daf yomi for meilah """
        output = hbcal("hbcal -od -freverse 13 10 2019")
        self.assertEqual(u"26 (\u05D3\u05D9\u05DE\u05EA) "
                         + u"\u05D4\u05DC\u05D9\u05E2\u05DE", output[0])

    def test_meilah_33(self):
        """ Tests output of daf yomi for meilah """
        output = hbcal("hbcal -od -freverse 20 10 2019")
        self.assertEqual(u"33 (\u05D3\u05D9\u05DE\u05EA) "
                         + u"\u05D4\u05DC\u05D9\u05E2\u05DE", output[0])

    def test_meilah_34(self):
        """ Tests output of daf yomi for meilah """
        output = hbcal("hbcal -od -freverse 21 10 2019")
        self.assertEqual(u"34 (\u05EA\u05D5\u05D3\u05DE) "
                         + u"\u05D4\u05DC\u05D9\u05E2\u05DE", output[0])


if __name__ == "__main__":
    unittest.main()
