from datetime import date, datetime

import sigma.core as core
from .option import type_


class Field(core.Field):
    def __validate__(self, value):
        if getattr(self, "noneable", False) and value is None:
            return None
        for option in self.__options__.values():
            value = option(self, value)
        return value


class Type_(core.Field):
    def __validate__(self, value):
        if getattr(self, "noneable", False) and value is None:
            return None
        value = type_(
            self.type_,
            getattr(self, "converted", False),
            getattr(self, "convert", False)
        )(self, value)
        for option in self.__options__.values():
            value = option(self, value)
        return value


class Integer(Type_):
    type_ = int


class Float(Type_):
    type_ = float


class String(Type_):
    type_ = str


class Date(Type_):
    type_ = date
