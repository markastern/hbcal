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
try:
    from collections.abc import MutableSet
except ImportError:
    from collections import MutableSet


class AmbiguousKeyError(KeyError):
    """An exception class raised by AbbrevSet if the supplied key could be
    used to provide two or more possible values."""
    pass


class Set(MutableSet):
    """ A mutable set that can be subclassed, using an underlying set"""

    def __init__(self, iter=None):
        self.myset = set() if iter is None else set(iter)

    def __contains__(self, item):
        return item in self.myset

    def __iter__(self):
        return iter(self.myset)

    def __len__(self):
        return len(self.myset)

    def add(self, value):
        self.myset.add(value)

    def discard(self, value):
        self.myset.discard(value)

    def __repr__(self):
        return '{name}({contents!r})'.format(
            name=self.__class__.__name__,
            contents=[item for item in self.myset])


class AbbrevSet(Set):
    """This class provides a set with lookup by key. Only the
    start of the key needs to be provided - if it matches one of the keys
    the key is returned. If it matches more than one key, an exception
    (AmbiguousKeyError) is raised."""

    def __getitem__(self, item):
        found = None
        for set_item in self:
            if set_item.startswith(item):
                if found is None:
                    found = set_item
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
