import sigma.core as core

from .option import white_list, black_list, type_, length, size, \
    match, search


class Field(core.Field):
    def __validate__(self, value):
        if getattr(self, "noneable", False) and value is None:
            return None
        for option in self.__options__.values():
            value = option(self, value)
        return value
