from sigma.core import Option
from .error import TooLongError, TooShortError, InvalidTypeError, \
    OverMinError, OverMaxError, NotNoneError, RegExpError, \
    WhiteListError, BlackListError


class noneable(Option):
    __option_name__ = "noneable"

    def __init__(self, noneable):
        self.noneable = noneable

    def __call__(self, field, value):
        if not self.noneable and value is None:
            raise NotNoneError(field, self, value)
        return value


class white_list(Option):
    __option_name__ = "white_list"

    def __init__(self, *args):
        self.white_list = args

    def __call__(self, field, value):
        if value not in self.white_list:
            raise WhiteListError(field, self, value)
        return value


class black_list(Option):
    __option_name__ = "black_list"

    def __init__(self, *args):
        self.black_list = args

    def __call__(self, field, value):
        if value in self.black_list:
            raise BlackListError(field, self, value)
        return value


class length(Option):
    __option_name__ = "length"

    def __init__(self, m=None, M=None):
        self.m = m
        self.M = M

    def __call__(self, field, value):
        length = len(value)
        if self.m and length < self.m:
            raise TooShortError(field, self, value)
        if self.M and length > self.M:
            raise TooLongError(field, self, value)
        return value


class size(Option):
    __option_name__ = "size"

    def __init__(self, m=None, M=None):
        self.m = m
        self.M = M

    def __call__(self, field, value):
        if self.m is not None and value < self.m:
            raise OverMinError(field, self, value)
        if self.M is not None and value > self.M:
            raise OverMaxError(field, self, value)
        return value


class type_(Option):
    __option_name__ = "type_"

    def __init__(self, type_, is_converted=False):
        self.type_ = type_
        self.is_converted = is_converted

    def __call__(self, field, value):
        if self.is_converted:
            if isinstance(value, self.type_):
                return value
            else:
                return self.type_(value)
        else:
            if isinstance(value, self.type_):
                return value
        raise InvalidTypeError(field, self, value)


class Regexp(Option):
    def __init__(self, regexp, pos=0, endpos=None):
        self.regexp = regexp
        if endpos is None:
            self.args = [pos]
        else:
            self.args = [pos, endpos]


class match(Regexp):
    def __call__(self, field, value):
        if self.regexp.match(value, *self.args):
            return value
        raise RegExpError(field, self, value)


class search(Regexp):
    def __call__(self, field, value):
        if self.regexp.search(value, *self.args):
            return value
        raise RegExpError(field, self, value)
