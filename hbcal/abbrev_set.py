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
from hbcal.my_collections import OrderedSet


class AmbiguousKeyError(KeyError):
    """An exception class raised by AbbrevSet if the supplied key could be
    used to provide two or more possible values."""
    pass


class AbbrevSet(OrderedSet):
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
