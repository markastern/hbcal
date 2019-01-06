"""This file contains classes and functions to simplify configuration."""

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
from __future__ import absolute_import
try:
    from configparser import NoSectionError, NoOptionError
except ImportError:
    from ConfigParser import NoSectionError, NoOptionError

from abc import ABCMeta, abstractmethod
import argparse
import sys as _sys
from future.utils import PY2, with_metaclass
from future.builtins import super


class ConfigurationParameterException(Exception):
    """Exception class for errors in the configuration file."""
    pass


class ConfigurationParameterValueError(ConfigurationParameterException):
    """An exception class.

    Raised if a configuration parameter has an invalid value."""
    pass


class ConfigurationParameterDefaultError(ConfigurationParameterException):
    """An exception class.

    Raised if a configuration parameter is supplied with an invalid default
    value."""
    pass


class ConfigurationParameterAmbiguousError(ConfigurationParameterException):
    """An exception class.

    Configuration parameters may be abbreviated. This exception is raised if a
    configuration parameter is supplied with a value that could be one of two
    or more possible allowed values."""
    pass


class AmbiguousKeyError(KeyError):
    """An exception class raised by AbbrevList if the supplied key could be
    used to provide two or more possible values."""
    pass


class AbbrevList(list):
    """This class provides a list with lookup by key (not index). Only the
    start of the key needs to be provided - if it matches one of the keys
    the key is returned. If it matches more than one key, an exception
    (AmbiguousKeyError) is raised."""

    def __getitem__(self, item):
        found = None
        for listitem in self:
            if listitem.startswith(item):
                if found is None:
                    found = listitem
                else:
                    raise AmbiguousKeyError
        if found is None:
            raise KeyError
        return found

    def __contains__(self, item):
        try:
            self[item]
        except KeyError:
            return False
        else:
            return True


class DuplicateError(Exception):
    """Exception class.

    Raised when attempting to modify the string in StringHolder."""
    pass


class RestrictiveList(list):
    """A list that only allows specified values with mutually exclusive groups.

    When the instance is created, it is empty. Elements may be appended,
    provided that they are in the allowed list (may be abbreviated), and
    provided that this would not leave more than one element of a mutually
    exclusive group as elements of the instance.

    Attributes:
        allowed: An AbbrevList specifying the allowed values.
        mutex_groups: A dictionary. Keys are elements in mutually exclusive
            groups. Values are lists of up to one element. All keys in one
            mutually exclusive group share the same value (list).
    """

    def __init__(self, allowed, mutex_groups=None):
        super().__init__()
        self.allowed = allowed
        self.mutex_groups = {}
        for group in mutex_groups if mutex_groups else []:
            holder = []
            for element in group:
                self.mutex_groups[allowed[element]] = holder

    def append(self, p_object):
        """Append an item to the instance.

        Raises:
            DuplicateError: If appending the item would violate a mutually
                exclusive constraint.
        """
        key = self.allowed[p_object]
        if key in self.mutex_groups:
            holder = self.mutex_groups[key]
            if not holder:
                holder.append(key)
            elif holder[0] != key:
                raise DuplicateError
        super().append(key)

    def __delslice__(self, start, stop):
        """Only needed in python 2."""
        self.__delitem__(slice(start, stop))

    def __delitem__(self, key):
        for element in self.__getitem__(key) if isinstance(key, slice) \
                else (self.__getitem__(key), ):
            if element in self.mutex_groups:
                holder = self.mutex_groups[element]
                del holder[0]
        super().__delitem__(key)


class ConfigurationParameter(with_metaclass(ABCMeta, object)):
    """ Abstract base class for parameters in configuration file.

    The values must be from a predefined list. They may be abbreviated.

    Attributes:
        value: The value to be passed as a default to the command line.
               It should be set to the string found in the configuration
               file.
    """

    @abstractmethod
    def _get_value(self):
        """Return the value to be passed as default to command line."""
        pass

    @abstractmethod
    def _set_value(self, config_string):
        """Set the value to be passed as default to command line.

        Parameters:
            config_string: The string read from the configuration file.
        """
        pass

    # The following trick from Geek at Play (www.kylev.com) allows
    # properties to be inherited.
    value = property(fget=lambda self: self._get_value(),
                     fset=lambda self, value: self._set_value(value))

    def parameter_found(self, name, section, config):
        """ Called to handle the parameter when the configuration file has
        been read.

        Parameters:
            name: The name of the parameter
            section: The name of the section in the configuration file
            config: The value (string) obtained from the configuration file

        Returns:
            nothing

        Raises:
            Subclasses of ConfigurationParameterException
        """
        try:
            value = config.get(section, name).lower()
        except (NoSectionError, NoOptionError):
            pass
        else:
            try:
                self.value = value
            except AmbiguousKeyError:
                raise ConfigurationParameterAmbiguousError
            except (KeyError, DuplicateError):
                raise ConfigurationParameterValueError


class SingleConfigurationParameter(ConfigurationParameter):
    """ A subclass of ConfigurationParameter where a single value is required.
    """

    def __init__(self, allowed, default):
        super().__init__()
        self._allowed = AbbrevList(allowed)
        try:
            self._value = self._allowed[default]
        except KeyError:
            raise ConfigurationParameterDefaultError

    def _get_value(self):
        return [self._value]

    def _set_value(self, config_string):
        self._value = self._allowed[config_string]


class BinaryConfigurationParameter(ConfigurationParameter):
    """ A subclass of ConfigurationParameter where a binary value is required.

    The allowed values in the configuration file are:
    true
    yes
    false
    no
    (or abbreviation of those)
    """
    def __init__(self):
        self._value = False
        super().__init__()
        self._allowed = AbbrevList(("true", "yes", "false", "no"))

    def _get_value(self):
        """Return default value for use in CLI."""
        return self._value

    def _set_value(self, config_string):
        self._value = self._allowed[config_string] in ("true", "yes")


class MultiConfigurationParameter(ConfigurationParameter):
    """ A subclass of ConfigurationParameter where a list of values is required.
    """

    def __init__(self, allowed, default, mutex_groups=None):
        super().__init__()
        self._value = RestrictiveList(AbbrevList(allowed), mutex_groups)
        for item in default:
            self._value.append(item)

    def _get_value(self):
        """Return default value for use in CLI."""
        return self._value

    def _set_value(self, config_string):
        del self._value[:]
        items = config_string.split()
        for item in items:
            self._value.append(item)


class StoreRestrictiveList(argparse.Action):
    """ Stores command line parameter values in a RestrictiveList object.

    This class is an Action class for argparse.

    Attributes:
        allowed: The allowed options (instance of AbbrevList)
        mutex_groups: List of mutually exclusive groups
        restrictive_list: The RestrictiveList object
    """

    def __init__(self, option_strings, choices, mutex_groups=None,
                 *args, **kwargs):
        """
        Parameters:
            option_strings: the option strings provided that caused this
                action to be invoked
            choices: list of choices for this option
            mutex_groups: list of mutually exclusive groups
            args: Remaining positional arguments
            kwargs: Remaining keyword arguments
        """
        self.allowed = AbbrevList(choices)
        self.mutex_groups = mutex_groups
        super().__init__(option_strings=option_strings,
                         choices=self.allowed, *args, **kwargs)
        self.restrictive_list = None

    def __call__(self, parser, namespace, values, option_string=None):
        if self.restrictive_list is None:
            self.restrictive_list = RestrictiveList(self.allowed,
                                                    self.mutex_groups)
        setattr(namespace, self.dest, self.restrictive_list)
        for value in [self.allowed[x] for x in values]:
            self.restrictive_list.append(value)


class ArgumentParser(argparse.ArgumentParser):
    """Python 2 version that outputs UTF-8 properly

    Standard ArgumentParser in argparse outputs help messages without
    converting to UTF-8. This fails if the message is a unicode string
    containing non-ASCII characters and output is redirected (to a
    pipe or a file). Unredirected output seems OK. See
    http://bugs.python.org/issue9779
    This class fixes it. It is not needed in Python 3.
    """
    if PY2:
        def _print_message(self, message, _file=None):
            """Output message to file, encoded as UTF-8 """
            if message:
                if _file is None:
                    _file = _sys.stderr
                _file.write(message.encode('utf-8'))


def add_negatable_option(parser, short_option, long_option, default, **kwargs):
    """Adds 2 mututally exclusive binary options to an ArgumentParser object.

    Positional Parameters:
        parser: The argparse.ArgumentParser object
        short_option: The short command line option (positive only) e.g. "-f"
        long_option: The long command line option (positive) e.g. "--foo".
            The corresponding negative option would be "--nofoo"
        default: The default value if neither option is specified.

    Keyword Parameters:
        help: The help to be displayed for the positive option with "--help".
            A corresponding help for the negative option will be generated
            automatically.
    Returns:
        The mutually exclusive group (an instance of _MutuallyExclusiveGroup)
    """
    help_text = kwargs['help']
    group = parser.add_mutually_exclusive_group()
    group.add_argument(short_option, long_option, action="store_true",
                       help=help_text, default=default)
    group.add_argument('--no' + long_option[2:], action="store_false",
                       dest=long_option[2:], help="do not " + help_text,
                       default=default)
    return group
