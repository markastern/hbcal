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
try:
    from collections.abc import MutableSet
except ImportError:
    from collections import MutableSet
import argparse
import sys as _sys
from future.utils import PY2, with_metaclass
from future.builtins import super
from .abbrev_set import AbbrevSet, AmbiguousKeyError


class ConfigurationParameterException(Exception):
    """Exception class for errors in the configuration file."""
    def __init__(self, value, problem, name=None):
        named_part = '' if name is None else "'{name}' ".format(name=name)
        self.message = ("Configuration parameter {name}"
                        + "has {problem} '{value}'").format(name=named_part,
                                                            value=value,
                                                            problem=problem)
        super().__init__(name, value, problem)


class ConfigurationParameterValueError(ConfigurationParameterException):
    """An exception class.

    Raised if a configuration parameter has an invalid value."""
    def __init__(self, name, value):
        super().__init__(value, 'invalid value', name)


class ConfigurationParameterDefaultError(ConfigurationParameterException):
    """An exception class.

    Raised if a configuration parameter is supplied with an invalid default
    value."""
    def __init__(self, value):
        super().__init__(value, 'invalid default value')


class ConfigurationParameterAmbiguousError(ConfigurationParameterException):
    """An exception class.

    Configuration parameters may be abbreviated. This exception is raised if a
    configuration parameter is supplied with a value that could be one of two
    or more possible allowed values."""
    def __init__(self, name, value):
        super().__init__(value, 'ambiguous value', name)


class DuplicateError(Exception):
    """Exception class.

    Raised when a mutually exclusive constraint would be violated."""
    def __init__(self, mutex_group):
        self.mutex_group = mutex_group
        super().__init__()


class AllowedOnlySet(MutableSet):
    """ A set with membership restrictions

    Elements of the set must be from the allowed group.
    Mutually exclusive groups may be specified, in which case the set may
    contain at most one element from each mutually exclusive group.
    """
    def __init__(self, iter=None, *args, **kwargs):
        for kwarg in ('allowed', 'mutex_groups'):
            if kwarg in kwargs:
                value = kwargs[kwarg]
                setattr(self, kwarg,
                        value if kwarg == 'allowed' or value is None
                        else tuple(frozenset(elem for elem in group)
                                   for group in value))
                del kwargs[kwarg]
            else:
                setattr(self, kwarg, None)
        super().__init__(**kwargs)
        if iter is not None:
            for value in iter:
                self.add(value)

    def add(self, value):
        if self.allowed is not None:
            try:
                value = self.allowed[value]
            except TypeError:
                pass
            if value not in self.allowed:
                raise KeyError
        if self.mutex_groups is not None:
            for group in self.mutex_groups:
                if value in group:
                    for element in group:
                        if element != value and element in self:
                            raise DuplicateError(group)
        super().add(value)

    def __repr__(self):
        return '{}({!r}, allowed = {!r}, mutex_groups = {!r})'.format(
            self.__class__.__name__,
            [item for item in self],
            self.allowed,
            self.mutex_groups)


class RestrictiveSet(AllowedOnlySet, AbbrevSet):
    """A set that only allows specified values with mutually exclusive groups.

    When the instance is created, it is empty. Elements may be appended,
    provided that they are in the allowed set (may be abbreviated), and
    provided that this would not leave more than one element of a mutually
    exclusive group as elements of the instance

    Attributes:
        allowed: A set specifying the allowed values.
        mutex_groups: A collection of groups of elements. At most one element
            from each group may be added to the set.
    """

    pass


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
                raise ConfigurationParameterAmbiguousError(name, value)
            except (KeyError, DuplicateError):
                raise ConfigurationParameterValueError(name, value)

    def __repr__(self):
        return '{name}({contents!r})'.format(
            name=self.__class__.__name__,
            contents=self.value)


class SingleConfigurationParameter(ConfigurationParameter):
    """ A subclass of ConfigurationParameter where a single value is required.
    """

    def __init__(self, allowed, default):
        super().__init__()
        self._allowed = AbbrevSet(allowed)
        try:
            self._value = self._allowed[default]
        except KeyError:
            raise ConfigurationParameterDefaultError(default)

    def _get_value(self):
        return set([self._value])

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
        self._allowed = AbbrevSet(("true", "yes", "false", "no"))

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
        self._value = RestrictiveSet(default,
                                     allowed=AbbrevSet(allowed),
                                     mutex_groups=mutex_groups)

    def _get_value(self):
        """Return default value for use in CLI."""
        return self._value

    def _set_value(self, config_string):
        self._value.clear()
        items = config_string.split()
        for item in items:
            self._value.add(item)


class StoreRestrictiveSet(argparse.Action):
    """ Stores command line parameter values in a RestrictiveSet object.

    This class is an Action class for argparse.

    Attributes:
        allowed: The allowed options (instance of AbbrevSet)
        mutex_groups: List of mutually exclusive groups
        restrictive_set: The RestrictiveSet object
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
        self.allowed = AbbrevSet(choices)
        self.mutex_groups = mutex_groups
        super().__init__(option_strings=option_strings,
                         choices=self.allowed, *args, **kwargs)
        self.restrictive_set = None

    def __call__(self, parser, namespace, values, option_string=None):
        if self.restrictive_set is None:
            self.restrictive_set = RestrictiveSet(
                allowed=self.allowed,
                mutex_groups=self.mutex_groups)
        setattr(namespace, self.dest, self.restrictive_set)
        for value in [self.allowed[x] for x in values]:
            try:
                self.restrictive_set.add(value)
            except DuplicateError as error:
                parser.error(("No more than one of {elements} may be "
                              + "specified with {option}").format(
                                  elements=', '.join(
                                      x for x in error.mutex_group),
                                  option=self.option_strings[-1]))


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
