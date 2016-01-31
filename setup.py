#!/usr/bin/env python
""" Setup script based on setuptools

    See https://pythonhosted.org/setuptools/setuptools.html for
    more information.
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

from __future__ import print_function
import re
import sys

from setuptools import setup, find_packages


def get_version(package_name):
    """Extract the version number from the specified package.

    The version number should be in a file version.py at the top level
    of the package and should contain a line:

    __version__ = 'version number'

    Quotes may be single or double. A triple quoted string is valid.
    The quote may be a raw string.
    """
    pattern = re.compile(r'''\A                # start of string
                             __version__
                             \s+               # one or more spaces
                             =
                             \s+               # one or more spaces
                             r?                # r is optional (but pointless)
                             (                 # capture full quote string
                               (['"])          # single or double quote
                               (?:\2\2)?       # optionally triple the quote
                             )                 # end capture
                             (                 # capture version number string
                               [0-9A-Za-z!.]+  # one or more alphanumeric,
                                               # bang, dot
                             )                 # end capture
                             \1                # repeat quote string
                             $''',  # end of string (before newline)
                         flags=re.MULTILINE | re.DOTALL | re.VERBOSE)
    with open(package_name + '/version.py') as version:
        for line in version:
            matched = pattern.match(line)
            if matched:
                return matched.group(3)
            else:
                return None

# ===========================================================================

if __name__ == "__main__":
    __version__ = get_version('hbcal')
    if __version__ is not None:
        print("all packages")
        print(find_packages())
        print("all packages except tests")
        print(find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]))
        setup(name='hbcal',
              version=__version__,
              description='Hebrew Calendar Date Converter',
              author='Mark Stern',
              author_email='markalexstern@gmail.com',
              url='https://github.com/markastern/hbcal',
              packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
              package_data={'hbcal': ['templates/*']},
              py_modules=['configuration_utilities'],
              entry_points={'console_scripts': ['hbcal = hbcal.main:main']},
              install_requires=['enum34'],
              tests_require=['freezegun'],
              test_suite='tests')
    else:
        print("Error: Version number is invalid", file=sys.stderr)
        sys.exit(1)
