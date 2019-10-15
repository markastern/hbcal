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
from future.utils import with_metaclass, iteritems
from future.builtins import super
from cached_property import cached_property
from .abstract_attribute import AbstractAttribute


class UnknownFlagError(TypeError):
    """Raise when an unrecognized flag is encountered in the format argument"""

    def __init__(self, message, flag, *args):
        self.message = message  # without this you may get DeprecationWarning
        self.flag = flag
        super().__init__(message, flag, *args)


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
    SUBFORMATTERS = tuple()

    @cached_property
    def escapes(self):
        """ Collects all the valid escape characters from subformatters """
        escapes = self.ESCAPES.copy()
        for attr_name in self.SUBFORMATTERS:
            attr = getattr(self, attr_name)
            escapes.update((key, "format_" + attr_name if value else value)
                           for key, value in iteritems(attr.escapes))
        return escapes

    def __format__(self, fmt):
        fmt1, sep, option = fmt.partition('#')
        formatted, escape_sequence = '', ''
        for char in fmt1:
            if escape_sequence:
                if char in self.escapes:
                    escape_sequence += char
                    if self.escapes[char] is not None:
                        fmt = escape_sequence + sep + option
                        formatted += getattr(self, self.escapes[char])(fmt)
                        escape_sequence = ''
                else:
                    escape_sequence = ''
                    formatted += char
            else:
                if char == '%':
                    escape_sequence += char
                else:
                    formatted += char
        formatted += escape_sequence
        return formatted

    @staticmethod
    def format_number(value, places, fmt, validate_flag=False):
        """ Formats a number according to a specified format.

        The format is expected to be %[<flag>]<character>,
        but this function only looks at <flag>.

        If the flag is unknown, an exception is (optionally) raised.
        The calling function can catch this exception to process
        other flags. """
        fmt1, _, _ = fmt.partition('#')
        flag = fmt1[1:-1]
        if len(flag) > 1:
            flag = flag[-1]
        fmt = '0{places}d'.format(places=places)
        if flag == '-':
            fmt = 'd'
        elif flag == '_':
            fmt = '{places}d'.format(places=places)
        elif flag not in ('', '0') and validate_flag:
            raise UnknownFlagError("Unknown flag: {flag}".format(flag=flag),
                                   flag=flag)
        return format(value, fmt)


class Formatter:
    """ Decorator that turns a function into an attribute that can be
    formatted (with the format function) by calling the original function.

    Instead of calling the (undecorated) function directly (func(fmt),
    the decorated function can now be called as format(func, fmt).

    It is not currently used (because it does not work properly with
    Python 2.7)."""
    def __init__(self, func):
        self.func = func

    def __format__(self, fmt):
        return self.func(fmt)

    def __get__(self, obj, obj_type=None):
        """ This code is necessary to make the decorator work with methods. """
        if obj is None:
            return self
        new_func = self.func.__get__(obj, obj_type)
        return self.__class__(new_func)


LOG = logging.getLogger(__name__)
