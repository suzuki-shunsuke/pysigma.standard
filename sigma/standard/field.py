import sigma.core as core


class Field(core.Field):
    def __validate__(self, value):
        if getattr(self, "noneable", False) and value is None:
            return None
        for option in self.__options__.values():
            value = option(self, value)
        return value
