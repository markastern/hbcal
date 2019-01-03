""" Tests for '--dafbind'.

This module contains tests for the '--dafbind' and --nodafbind command line
options and for the 'dafbind' configuration file option.
"""
# Copyright 2015, 2016, 2019 Mark Stern
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

from future.utils import PY2
import sys
import unittest
import logging
from .utilities import hbcal
# Python 2 also supports io.StringIO, but it would not simulate the bug
# (see http://bugs.python.org/issue9779, fixed in configuration_utilities).
if PY2:
    from cStringIO import StringIO
else:
    from io import StringIO

# Test discovery uses setUpModule, but pylint does not know that.
# pylint: disable=unused-import
from .utilities import set_up_module as setUpModule  # noqa
# pylint: enable=unused-import

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class TestHelp(unittest.TestCase):
    def test_help(self):
        with self.assertRaises(SystemExit):
            stdout_save = sys.stdout
            sys.stdout = StringIO()
            try:
                hbcal("hbcal --help")
            finally:
                sys.stdout = stdout_save


if __name__ == "__main__":
    unittest.main()
