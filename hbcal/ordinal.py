"""This module contains the ordinal_suffix function."""

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

SUFFIX = ['th', 'st', 'nd', 'rd']


def ordinal_suffix(number):
    """Return the ordinal suffix of a given number.

    Parameters:
        number (int): Specified number
    Return:
        suffix needed to turn the specified number into an ordinal number.
    """
    number %= 100
    if number >= 20:
        number %= 10
    if number >= 4:
        number = 0
    return SUFFIX[number]
