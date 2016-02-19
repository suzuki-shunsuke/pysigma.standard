from sigma.core import option, Option

from .error import TooLongError, TooShortError, InvalidTypeError, \
    OverMinError, OverMaxError, NotNoneError, RegExpError, \
    WhiteListError, BlackListError


@option
def noneable(self, opt, value):
    if not opt.value and value is None:
        raise NotNoneError(opt, value)
    return value


@option
def white_list(self, opt, value):
    if value not in opt.value:
        raise WhiteListError(opt, value)
    return value


@option
def black_list(self, opt, value):
    if value in opt.value:
        raise BlackListError(opt, value)
    return value


@option
def convert_type(self, opt, value):
    type_ = opt.__dict__["value"]
    if isinstance(value, type_):
        return value
    return type_(value)


@option("type")
def type_(self, opt, value):
    if not isinstance(value, opt.value):
        raise InvalidTypeError(opt, value)
    return value


@option
def length(self, opt, value):
    m, M = opt.value
    length = len(value)
    if m and length < m:
        raise TooShortError(opt, value)
    if M and length > M:
        raise TooLongError(opt, value)
    return value


@option
def size(self, opt, value):
    m, M = opt.value
    if m and value < m:
        raise OverMinError(opt, value)
    if M and value > M:
        raise OverMaxError(opt, value)
    return value


class Regexp(Option):
    def __init__(self, *args):
        if not len(args):
            if hasattr(self, "default"):
                args = self.default
        arg = args[0]
        if isinstance(arg, tuple):
            regexp = arg[0]
            args = arg[1:]
        else:
            regexp = arg
            args = []
        self.regexp = regexp
        self.args = args


class Match(Regexp):
    def validate(self, field, value):
        if self.regexp.match(value, *self.args):
            return value
        raise RegExpError(self, value)


class Search(Regexp):
    def validate(self, field, value):
        if self.regexp.search(value, *self.args):
            return value
        raise RegExpError(self, value)
