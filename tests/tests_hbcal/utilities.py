"""Utilities for testing hbcal

Exports:
    set_up_module
    hbcal
    TestCase
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

import os.path
import unittest
from enum import Enum

from hbcal import get_output_line

DIRECTORY_NAME = os.path.join(os.getcwd(), 'home')
FILENAME = os.path.join(DIRECTORY_NAME, '.hbcal.config')


def set_up_module():
    """ Set up for test modules that will use TestCase.

    Create the home directory (if it does not exist). The home directory
    is used to store the configuration file used for testing.

    :return: none
    """
    try:
        os.makedirs(DIRECTORY_NAME)
    except OSError:
        if not os.path.isdir(DIRECTORY_NAME):
            raise


def hbcal(command_line):
    """Get output lines from specified command line string.

    Split the command line into an array of parameters.
    Generate output lines and combine them into a list.
    Parameters:
        command_line: string of command line parameters
    Return:
        list of output strings.
    """
    return list(get_output_line(command_line.split()))


class ConfigurationData(Enum):
    NO_FILE = 1
    EMPTY = 2


class TestCase(unittest.TestCase):
    """Subclass of unittest.TestCase that also sets up configuration file.

    Attributes:
        section_name: The section name to be used in the configuration file
                      (only if config_data is a string)
        config_data:  Data to be stored in configuration file.
                      Values:
                          Instance of string:
                              Configuration file contains a single section
                              containing <config_data> as data
                          ConfigurationData.NO_FILE:
                              There is no configuration file.
                          ConfigurationData.EMPTY:
                              An empty configuration file.
    """
    section_name = 'hbcal'
    config_data = ConfigurationData.NO_FILE

    @classmethod
    def setUpClass(cls):
        if isinstance(cls.config_data, (basestring, ConfigurationData)):
            if cls.config_data == ConfigurationData.NO_FILE:
                if os.path.isfile(FILENAME):
                    os.remove(FILENAME)
            else:
                with open(FILENAME, 'w') as config_file:
                    if cls.config_data != ConfigurationData.EMPTY:
                        config_file.write("[{}]\n{}".format(cls.section_name,
                                                            cls.config_data))
        else:
            raise TypeError("config_data must be an instance of " +
                            "basestring or ConfigurationData")

        os.environ["HOME"] = DIRECTORY_NAME
