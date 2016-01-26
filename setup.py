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

from setuptools import setup, find_packages
exec(open('hbcal/version.py').read())
setup(name='hbcal',
      version=__version__,  # noqa
      description='Hebrew Calendar Date Converter',
      author='Mark Stern',
      author_email='markalexstern@gmail.com',
      url='https://github.com/markastern/hbcal',
      packages=find_packages(),
      package_data={'hbcal': ['templates/*']},
      py_modules=['configuration_utilities'],
      entry_points={'console_scripts': ['hbcal = hbcal.main:main']},
      install_requires=['enum34'],
      tests_require=['freezegun'],
      test_suite='discover_tests')
