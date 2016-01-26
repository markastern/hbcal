""" This module is used by setup.py to find the tests to run for the
    'test' command.
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

from os.path import abspath, dirname
import unittest


def additional_tests():
    """ Return a test suite containing all tests. """
    return unittest.defaultTestLoader.discover(abspath(dirname(__file__)))
