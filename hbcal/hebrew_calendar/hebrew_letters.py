""" This file contains unicode codes for Hebrew letters.

Exports:
    hebrew_letters
    HebrewString
"""

# Copyright 2015, 2019 Mark Stern
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

HEBREW_LETTERS = {'ALEF': u"\u05D0", 'BET': u"\u05D1", 'GIMEL': u"\u05D2",
                  'DALET': u"\u05D3", 'HE': u"\u05D4", 'VAV': u"\u05D5",
                  'ZAYIN': u"\u05D6", 'CHET': u"\u05D7", 'TET': u"\u05D8",
                  'YOD': u"\u05D9", 'FINAL_KAF': u"\u05DA", 'KAF': u"\u05DB",
                  'LAMED': u"\u05DC", 'FINAL_MEM': u"\u05DD", 'MEM': u"\u05DE",
                  'FINAL_NUN': u"\u05DF", 'NUN': u"\u05E0",
                  'SAMECH': u"\u05E1", 'AYIN': u"\u05E2",
                  'FINAL_PE': u"\u05E3", 'PE': u"\u05E4",
                  'FINAL_TZADE': u"\u05E5", 'TZADE': u"\u05E6",
                  'QOF': u"\u05E7", 'RESH': u"\u05E8", 'SHIN': u"\u05E9",
                  'TAV': u"\u05EA", 'GERESH': u"\u05F3"}


class HebrewString(unicode if PY2 else str):
    """ A class for formatting Hebrew strings in different ways."""

    def __format__(self, fmt):
        """ Formats the string according to the requested option
        :param fmt: The requested format (usually after':' in the string)
            Valid formats are:
            '#H': Output Hebrew characters according to the order of the
                string. This is intended for terminal emulators that support
                bi-directional mode.
            '#R': Output the string in reverse order. This is intended for
                terminal emulators that output everything from left to right,
                so it is necessary to output the text reversed for it to
                appear correct.
            'h': Output the string as HTML codes for unicode. This is intended
                for use in web scripts.
        :return: The formatted string.
        """
        hebrew_format = self.format(**HEBREW_LETTERS)
        if fmt == "#H":
            return hebrew_format
        elif fmt == "#R":
            return hebrew_format[::-1]
        elif fmt == "#h":
            return hebrew_format.encode('ascii',
                                        'xmlcharrefreplace').decode('ascii')
        else:
            raise NotImplementedError
