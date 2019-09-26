"""This module defines a mix-in class for formatting strings"""

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

import logging
from abc import ABCMeta
from future.utils import with_metaclass
from .abstract_attribute import AbstractAttribute


class FormatPercentString(with_metaclass(ABCMeta, object)):
    """A class for formatting strings (typically date and time).

    Most characters are unchanged, but the string may contain an escape
    sequence of the form % [flag] <character> (without spaces). These
    characters will be replaced by the result of a method determined by
    <character>, possibly modified by the optional flag. These are defined
    by the subclass.

    %% is converted to a literal %.

    The string may contain a hash, in which case only characters before the
    hash are processed as above. Any characters after the hash may further
    modify processing (globally, for the entire string."""

    # ESCAPES must be defined as a dictionary mapping option characters to
    # functions that handle them
    ESCAPES = AbstractAttribute("The options valid after an escape (%)")

    FLAGS = frozenset({'-', '_', '0'})

    def __format__(self, fmt):
        fmt1, sep, option = fmt.partition('#')
        formatted, escape, flag = '', False, None
        for char in fmt1:
            if escape:
                if char in self.ESCAPES:
                    formatted += self.ESCAPES[char](self, sep + option,
                                                    flag=flag)
                    escape, flag = False, None
                elif char in self.FLAGS:
                    flag = char
                else:
                    escape = False
                    formatted += '%'
                    if char != '%':
                        if flag:
                            formatted += flag
                        formatted += char
            else:
                if char == '%':
                    escape = True
                else:
                    formatted += char
        return formatted

    def format_number(self, value, places, **kwargs):
        fmt = '0{places}d'.format(places=places)
        if 'flag' in kwargs:
            if kwargs['flag'] == '-':
                fmt = 'd'
            elif kwargs['flag'] == '_':
                fmt = '{places}d'.format(places=places)
        return format(value, fmt)


LOG = logging.getLogger(__name__)
