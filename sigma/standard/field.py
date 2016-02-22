import sigma.core as core

from .option import noneable, white_list, black_list, type_, length, size, \
    match, search


class Field(core.Field):
    def __validate__(self, value):
        if "noneable" in self.__options__ and self.noneable(value) is None:
            return None
        for option in self.__options__.values():
            value = option(self, value)
        return value
