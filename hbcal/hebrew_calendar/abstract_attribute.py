# This file is based on a code recipe by Eric Snow and is licensed
# under the MIT licence.

class AbstractAttribute:
    """An abstract class attribute.

    Use this instead of an abstract property when you don't expect the
    attribute to be implemented by a property.

    """

    __isabstractmethod__ = True

    def __init__(self, doc=""):
        self.__doc__ = doc
    def __get__(self, obj, cls):
        return self