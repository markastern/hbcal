"""Test for converting date based on all or part of the current date."""

# Copyright 2015 Mark Stern
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

import logging
from freezegun import freeze_time
import unittest
from utilities import TestCase, hbcal

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
        """Class containing tests that are run for both day and night."""
        def test_today(self):
            output = hbcal("hbcal -ic -fphonetics")
            self.assertEqual(2, len(output))
            self.assertEqual('Friday 1 January 2010', output[0])
            self.assertEqual('Friday 15 Teveth 5770', output[1])

        def test_today_gregorian(self):
            output = hbcal("hbcal -ig -fphonetics")
            self.assertEqual(2, len(output))
            self.assertEqual('Friday 1 January 2010', output[0])
            self.assertEqual('Friday 15 Teveth 5770', output[1])

        def test_today_julian(self):
            output = hbcal("hbcal -ij -fphonetics")
            self.assertEqual(2, len(output))
            self.assertEqual('Friday 1 January 2010', output[0])
            self.assertEqual('Friday 15 Teveth 5770', output[1])

        def test_today_daf(self):
            output = hbcal("hbcal -id -fphonetics")
            self.assertEqual(2, len(output))
            self.assertEqual('Friday 1 January 2010', output[0])
            self.assertEqual('Friday 15 Teveth 5770', output[1])

        def test_same_month(self):
            output = hbcal("hbcal -ic -fphonetics 21")
            self.assertEqual(2, len(output))
            self.assertEqual('Thursday 21 January 2010', output[0])
            self.assertEqual('Thursday 6 Shevat 5770', output[1])

        def test_same_month_gregorian(self):
            output = hbcal("hbcal -ig -fphonetics 21")
            self.assertEqual(2, len(output))
            self.assertEqual('Thursday 21 January 2010', output[0])
            self.assertEqual('Thursday 6 Shevat 5770', output[1])

        def test_same_month_julian(self):
            output = hbcal("hbcal -ij -fphonetics 21")
            self.assertEqual(2, len(output))
            self.assertEqual('Sunday 3 January 2010', output[0])
            self.assertEqual('Sunday 17 Teveth 5770', output[1])

        def test_same_year(self):
            output = hbcal("hbcal -ic -fphonetics 21 4")
            self.assertEqual(2, len(output))
            self.assertEqual('Wednesday 21 April 2010', output[0])
            self.assertEqual('Wednesday 7 Iyar 5770', output[1])

        def test_same_year_gregorian(self):
            output = hbcal("hbcal -ig -fphonetics 21 4")
            self.assertEqual(2, len(output))
            self.assertEqual('Wednesday 21 April 2010', output[0])
            self.assertEqual('Wednesday 7 Iyar 5770', output[1])

        def test_same_year_julian(self):
            output = hbcal("hbcal -ij -fphonetics 21 4")
            self.assertEqual(2, len(output))
            self.assertEqual('Monday 4 May 2009', output[0])
            self.assertEqual('Monday 10 Iyar 5769', output[1])

        def test_same_month_zero_date(self):
            with self.assertRaises(SystemExit):
                hbcal("hbcal -ic -fphonetics 0")

        def test_same_month_minus_date(self):
            output = hbcal("hbcal -ic -fphonetics -1")
            self.assertEqual(2, len(output))
            self.assertEqual('Sunday 31 January 2010', output[0])
            self.assertEqual('Sunday 16 Shevat 5770', output[1])

        def test_minus_month(self):
            output = hbcal("hbcal -ic -fphonetics 21 -1")
            self.assertEqual(2, len(output))
            self.assertEqual('Tuesday 21 December 2010', output[0])
            self.assertEqual('Tuesday 14 Teveth 5771', output[1])


@freeze_time("2010-01-01 14:35:35")
class TestCurrentDateDay(Wrapper.CommonTests):
    """Class containing tests run during the day (before 6pm)."""

    def test_today_hebrew(self):
        output = hbcal("hbcal -ih -fphonetics")
        self.assertEqual(2, len(output))
        self.assertEqual('Friday 1 January 2010', output[0])
        self.assertEqual('Friday 15 Teveth 5770', output[1])

    def test_today_daf_hebrew(self):
        """Test daf yomi input calendar when bound to Hebrew calendar"""
        output = hbcal("hbcal -id --dafbind hebrew -fphonetics")
        self.assertEqual(2, len(output))
        self.assertEqual('Friday 1 January 2010', output[0])
        self.assertEqual('Friday 15 Teveth 5770', output[1])

    def test_same_month_hebrew(self):
        output = hbcal("hbcal -ih -fphonetics 21")
        self.assertEqual(2, len(output))
        self.assertEqual('Thursday 7 January 2010', output[0])
        self.assertEqual('Thursday 21 Teveth 5770', output[1])

    def test_same_tractate(self):
        output = hbcal("hbcal -id -fphonetics 21")
        self.assertEqual(2, len(output))
        self.assertEqual('Friday 11 September 2009', output[0])
        self.assertEqual('Friday 22 Ellul 5769', output[1])

    def test_same_year_hebrew(self):
        output = hbcal("hbcal -ih -fphonetics 21 4")
        self.assertEqual(2, len(output))
        self.assertEqual('Saturday 3 July 2010', output[0])
        self.assertEqual('Saturday 21 Tammuz 5770', output[1])

    def test_same_daf_yomi_cycle(self):
        output = hbcal("hbcal -id -fphonetics 21 4")
        self.assertEqual(2, len(output))
        self.assertEqual('Tuesday 7 February 2006', output[0])
        self.assertEqual('Tuesday 9 Shevat 5766', output[1])


@freeze_time("2010-01-01 19:35:35")
class TestCurrentDateNight(Wrapper.CommonTests):
    """Class containing tests run at night (between 6pm and midnight).

    If the input calendar (configuration file or command line) is Hebrew
    (or Daf Yomi and dafbind is set to Hebrew), the next day is assumed.
    """

    def test_today_hebrew(self):
        output = hbcal("hbcal -ih -fphonetics")
        self.assertEqual(2, len(output))
        self.assertEqual('Saturday 2 January 2010', output[0])
        self.assertEqual('Saturday 16 Teveth 5770', output[1])

    def test_today_daf(self):
        output = hbcal("hbcal -id -fphonetics")
        self.assertEqual(2, len(output))
        self.assertEqual('Friday 1 January 2010', output[0])
        self.assertEqual('Friday 15 Teveth 5770', output[1])

    def test_today_daf_hebrew(self):
        """Test daf yomi input calendar when bound to Hebrew calendar"""
        output = hbcal("hbcal -id --dafbind hebrew -fphonetics")
        self.assertEqual(2, len(output))
        self.assertEqual('Saturday 2 January 2010', output[0])
        self.assertEqual('Saturday 16 Teveth 5770', output[1])

    def test_same_month_hebrew(self):
        output = hbcal("hbcal -ih -fphonetics 21")
        self.assertEqual(2, len(output))
        self.assertEqual('Thursday 7 January 2010', output[0])
        self.assertEqual('Thursday 21 Teveth 5770', output[1])

    def test_same_tractate(self):
        output = hbcal("hbcal -id -fphonetics 21")
        self.assertEqual(2, len(output))
        self.assertEqual('Friday 11 September 2009', output[0])
        self.assertEqual('Friday 22 Ellul 5769', output[1])

    def test_same_year_hebrew(self):
        output = hbcal("hbcal -ih -fphonetics 21 4")
        self.assertEqual(2, len(output))
        self.assertEqual('Saturday 3 July 2010', output[0])
        self.assertEqual('Saturday 21 Tammuz 5770', output[1])

    def test_same_daf_yomi_cycle(self):
        output = hbcal("hbcal -id -fphonetics 21 4")
        self.assertEqual(2, len(output))
        self.assertEqual('Tuesday 7 February 2006', output[0])
        self.assertEqual('Tuesday 9 Shevat 5766', output[1])


@freeze_time('2015-12-14 13:45:32')
class TestSameTractateDay(TestCase):

    def test_same_tractate(self):
        """Test daf yomi input calendar at the start/end of a tractate.

        The current date is the last civil date of the tractate.
        The daf yomi calendar is bound to the Hebrew calendar (command line
        options). However, the time is before 6pm. Therefore the requested
        date is for daf 21 of the old tractate.
        """
        output = hbcal("hbcal -id --dafbind hebrew -fphonetics 21")
        self.assertEqual(2, len(output))
        self.assertEqual('Monday 16 November 2015', output[0])
        self.assertEqual('Monday 4 Kislev 5776', output[1])


@freeze_time('2015-12-14 18:45:32')
class TestSameTractateNight(TestCase):

    def test_same_tractate(self):
        """Test daf yomi input calendar at the start/end of a tractate.

        The current date is the last civil date of the tractate.
        The daf yomi calendar is bound to the Hebrew calendar (command line
        options) and the time is after 6pm. Therefore the requested date is
        daf 21 of the new tractate.
        """

        output = hbcal("hbcal -id --dafbind hebrew -fphonetics 21")
        self.assertEqual(2, len(output))
        self.assertEqual('Sunday 3 January 2016', output[0])
        self.assertEqual('Sunday 22 Teveth 5776', output[1])


@freeze_time('2012-08-02 13:45:32')
class TestSameDafYomiCycleDay(TestCase):

    def test_same_daf_yomi_cycle(self):
        """Test daf yomi input calendar at the start/end of a cycle.

        The current date is the last civil date of the cycle.
        The daf yomi calendar is bound to the Hebrew calendar (command line
        options). However, the time is before 6pm. Therefore the requested
        date is for Pesachim 21 of the old cycle.
        """
        output = hbcal("hbcal -id --dafbind hebrew -fphonetics 21 4")
        self.assertEqual(2, len(output))
        self.assertEqual('Tuesday 7 February 2006', output[0])
        self.assertEqual('Tuesday 9 Shevat 5766', output[1])


@freeze_time('2012-08-02 18:45:32')
class TestSameDafYomiCycleNight(TestCase):

    def test_same_daf_yomi_cycle(self):
        """Test daf yomi input calendar at the start/end of a tractate.

        The current date is the last civil date of the tractate.
        The daf yomi calendar is bound to the Hebrew calendar (command line
        options) and the time is after 6pm. Therefore the requested date is
        for Pesachim 21 of the new cycle.
        """

        output = hbcal("hbcal -id --dafbind hebrew -fphonetics 21 4")
        self.assertEqual(2, len(output))
        self.assertEqual('Thursday 11 July 2013', output[0])
        self.assertEqual('Thursday 4 Av 5773', output[1])

if __name__ == "__main__":
    unittest.main()
