import sigma.core as core

from .error import TooLongError, TooShortError, InvalidTypeError, \
    OverMinError, OverMaxError, NotNoneError, RegExpError, \
    WhiteListError, BlackListError


class Field(core.Field):
    def noneable(self, option, value):
        if not option.value and value is None:
            raise NotNoneError(self, option, value)
        return value

    def white_list(self, option, value):
        if value not in option.value:
            raise WhiteListError(self, option, value)
        return value

    def black_list(self, option, value):
        if value in option.value:
            raise BlackListError(self, option, value)
        return value

    def type(self, option, value):
        if not isinstance(value, option.value):
            raise InvalidTypeError(self, option, value)
        return value

    def length(self, option, value):
        m, M = option.value
        length = len(value)
        if m and length < m:
            raise TooShortError(self, option, value)
        if M and length > M:
            raise TooLongError(self, option, value)
        return value

    def size(self, option, value):
        m, M = option.value
        if m and value < m:
            raise OverMinError(self, option, value)
        if M and value > M:
            raise OverMaxError(self, option, value)
        return value

    def match(self, option, value):
        if isinstance(option.value, tuple):
            regexp = option.value[0]
            args = option[1:]
        else:
            regexp = option.value
            args = []
        if regexp.match(value, *args):
            return value
        raise RegExpError(self, option, value)

    def search(self, option, value):
        if isinstance(option.value, tuple):
            regexp = option.value[0]
            args = option.value[1:]
        else:
            regexp = option.value
            args = []
        if regexp.search(value, *args):
            return value
        raise RegExpError(self, option, value)
