"""This module contains functions (mostly internal) for
   converting numbers to Hebrew letters with equivalent values. """

# Copyright 2019 Mark Stern
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

from .hebrew_letters import HEBREW_LETTERS

HUNDREDS = ['', HEBREW_LETTERS['QOF'], HEBREW_LETTERS['RESH'],
            HEBREW_LETTERS['SHIN']]

TENS = ['', HEBREW_LETTERS['YOD'], HEBREW_LETTERS['KAF'],
        HEBREW_LETTERS['LAMED'], HEBREW_LETTERS['MEM'], HEBREW_LETTERS['NUN'],
        HEBREW_LETTERS['SAMECH'], HEBREW_LETTERS['AYIN'],
        HEBREW_LETTERS['PE'], HEBREW_LETTERS['TZADE']]

UNITS = ['', HEBREW_LETTERS['ALEF'], HEBREW_LETTERS['BET'],
         HEBREW_LETTERS['GIMEL'], HEBREW_LETTERS['DALET'],
         HEBREW_LETTERS['HE'], HEBREW_LETTERS['VAV'], HEBREW_LETTERS['ZAYIN'],
         HEBREW_LETTERS['CHET'], HEBREW_LETTERS['TET']]


def to_letters(value, abbreviate=True):
    """ Convert number to Hebrew letters with equivalent values

    Args:
        value: number to convert
        abbreviate: If true, thousands will be abbreviated
        e.g. Bet Geresh Shin Mem Gershayim He for 2345 instead of
        Tav Tav Tav Tav Tav Shin Mem Gershayim He.

        A single letter followed by a geresh is potentially ambiguous
        e.g. Alef geresh could mean 1 or 1000. To avoid the ambiguity,
        1000 (but not 1001) will be output in full.
        Similarly, 3000 will be output with the last thousand in full
        (Bet Geresh Tav Tav Gershayim Resh). This is non-standard,
        but clear and unambiguous.

    Returns:
        string:
    """
    return _to_letters(value, abbreviate=abbreviate)


def _to_letters(value, abbreviate=True, force=False):
    """ Convert number to Hebrew letters with equivalent values

    Args:
        value: number to convert
        abbreviate: If true, thousands will be abbreviated
        e.g. Bet Geresh Shin Mem Gershayim He for 2345 instead of
        Tav Tav Tav Tav Tav Shin Mem Gershayim He.
        force: If true, force abbreviation of thousands (see below)

        A single letter followed by a geresh is potentially ambiguous
        e.g. Alef geresh could mean 1 or 1000. To avoid the ambiguity,
        1000 (but not 1001) will be output in full, unless the force
        parameter is set to True.
        Similarly, 3000 will be output with the last thousand in full
        (Bet Geresh Tav Tav Gershayim Resh). This is non-standard,
        but clear and unambiguous. Use of the force parameter is
        intended for internal use only.

    Returns:
        string:
    """

    if not isinstance(value, int) or value <= 0:
        raise ValueError(
            "invalid positive integer: {value}".format(value=value))

    if abbreviate:
        quotient, value = divmod(value, 1000)
        if quotient > 0:
            return _abbreviate_thousands(force, quotient, value)

    quotient, value = divmod(value, 400)
    result = HEBREW_LETTERS['TAV'] * quotient

    quotient, value = divmod(value, 100)
    result += HUNDREDS[quotient]

    quotient, value = divmod(value, 10)
    if quotient == 1 and value in (5, 6):
        result += HEBREW_LETTERS['TET']
        value += 1
    else:
        result += TENS[quotient]
    result += UNITS[value]
    if len(result) == 1:
        result += HEBREW_LETTERS['GERESH']
    else:
        result = result[:-1] + HEBREW_LETTERS['GERSHAYIM'] + result[-1]
    return result


def _abbreviate_thousands(force, quotient, value):
    thousands = _to_letters(quotient, force=True)
    if thousands[-1] == HEBREW_LETTERS['GERESH'] and quotient % 1000:
        if not force and value == 0:
            quotient -= 1
            value += 1000
            if quotient:
                thousands = _to_letters(quotient, force=True)
                if thousands[-1] != HEBREW_LETTERS['GERESH']:
                    thousands += HEBREW_LETTERS['GERESH']
            else:
                thousands = ''
    else:
        thousands += HEBREW_LETTERS['GERESH']
    return thousands + (_to_letters(value, False) if value else '')
