import sigma.core as core

from .option import noneable, white_list, black_list, type_, length, size, \
    match, search


class Field(core.Field):
    noneable = noneable
    white_list = white_list
    black_list = black_list
    type = type_
    length = length
    size = size
    match = match
    search = search

    def __validate__(self, value):
        if "noneable" in self.__options__:
            if self.noneable(value) is None:
                return None
        for option in self.__options__.values():
            value = option(self, value)
        return value
