"""Tests for setup script"""

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

import os.path
import shutil
import unittest

from setup import get_version

DIRECTORY_NAME = os.path.join(os.getcwd(), 'dummy')
FILENAME = os.path.join(DIRECTORY_NAME, 'version.py')


def setUpModule():
    """ Create a dummy package. """
    try:
        os.makedirs(DIRECTORY_NAME)
    except OSError:
        if not os.path.isdir(DIRECTORY_NAME):
            raise


def tearDownModule():
    """ Delete the dummy package. """
    shutil.rmtree(DIRECTORY_NAME, ignore_errors=True)


class TestCase(unittest.TestCase):
    """Subclass of unittest.TestCase that also sets up version file.

    Attributes:
        version_data:  Data to be stored in version file.
                       If None, there is no file.
                       Values:
    """
    version_data = None

    @classmethod
    def setUpClass(cls):
        if cls.version_data is None:
            if os.path.isfile(FILENAME):
                os.remove(FILENAME)
        else:
            with open(FILENAME, 'w') as version_file:
                version_file.write(cls.version_data)


class TestValidVersion(TestCase):
    """Test a valid version number with an epoch."""

    version_data = "__version__ = '1.2.3'\n"

    def test_get_version(self):
        self.assertEqual('1.2.3', get_version("dummy"))


class TestEpochVersion(TestCase):
    """Test a valid version number with an epoch."""

    version_data = "__version__ = '2!2016.1.27rc2'\n"

    def test_get_version(self):
        self.assertEqual('2!2016.1.27rc2', get_version("dummy"))


class TestDoubleQuotes(TestCase):
    """Test a version number enclosed by double quotes."""

    version_data = '__version__ = "1.2.3"\n'

    def test_get_version(self):
        self.assertEqual('1.2.3', get_version("dummy"))


class TestTripleQuotes(TestCase):
    """Test a version number enclosed by triple quotes."""

    version_data = '__version__ = """1.2.3"""\n'

    def test_get_version(self):
        self.assertEqual('1.2.3', get_version("dummy"))


class TestRawString(TestCase):
    """Test a version number enclosed by a raw quoted string."""

    version_data = "__version__ = r'1.2.3'\n"

    def test_get_version(self):
        self.assertEqual('1.2.3', get_version("dummy"))


class TestMismatchedQuotes(TestCase):
    """Test a version number enclosed by mismatched quotes.

    In this case the version number is invalid and get_version
    returns None.
    """

    version_data = '__version__ = "1.2.3\'\n'

    def test_get_version(self):
        self.assertIsNone(get_version("dummy"))


if __name__ == "__main__":
    unittest.main()
