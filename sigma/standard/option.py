from sigma.core import option

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


@option
def match(self, opt, value):
    if isinstance(opt.value, tuple):
        regexp = opt.value[0]
        args = opt.value[1:]
    else:
        regexp = opt.value
        args = []
    if regexp.match(value, *args):
        return value
    raise RegExpError(opt, value)


@option
def search(self, opt, value):
    if isinstance(opt.value, tuple):
        regexp = opt.value[0]
        args = opt.value[1:]
    else:
        regexp = opt.value
        args = []
    if regexp.search(value, *args):
        return value
    raise RegExpError(opt, value)
