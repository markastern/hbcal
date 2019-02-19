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
from __future__ import absolute_import
from collections import OrderedDict
try:
    from collections.abc import MutableSet
except ImportError:
    from collections import MutableSet


class OrderedSet(MutableSet):
    """ A mutable set that can be subclassed, using an ordered dict

    Order is preserved, but conditional expressions (e.g. ==) disregard it.
    """

    def __init__(self, iterator=None):
        self.mydict = OrderedDict() if iterator is None else OrderedDict(
            [(x, True) for x in iterator])

    def __contains__(self, item):
        return item in self.mydict

    def __iter__(self):
        return iter(self.mydict)

    def __len__(self):
        return len(self.mydict)

    def add(self, value):
        self.mydict[value] = True

    def discard(self, value):
        if value in self.mydict:
            del self.mydict[value]

    def __repr__(self):
        return '{name}({contents!r})'.format(
            name=self.__class__.__name__,
            contents=[item for item in self.mydict])
