"""
"""

from sigma.core import UnitError


class WhiteListError(UnitError):
    """WhiteList Constraint.
    """
    def __str__(self):
        return ("{}\n"
                "White List: {}\n").format(
            super(WhiteListError, self).__str__(),
            self.option.value
        )


class BlackListError(UnitError):
    """BlackList Constraint.
    """
    def __str__(self):
        return ("{}\n"
                "Black List: {}\n").format(
            super(BlackListError, self).__str__(),
            self.option.value
        )


class LengthError(UnitError):
    """Length Constraint.
    """
    def __str__(self):
        return ("{}\n"
                "length: {}\n"
                "length limitation: {}\n").format(
            super(LengthError, self).__str__(),
            len(self.value),
            self.option.value
        )


class TooShortError(LengthError):
    pass


class TooLongError(LengthError):
    pass


class SizeError(UnitError):
    """Size Constraint.
    """
    def __str__(self):
        return ("{}\n"
                "size limitation: {}\n").format(
            super(SizeError, self).__str__(),
            self.option.value
        )


class OverMaxError(SizeError):
    pass


class OverMinError(SizeError):
    pass


class InvalidTypeError(UnitError):
    """Type Constraint.
    """
    def __str__(self):
        return ("{}\n"
                "expected type: {}\n"
                "actual type: {}\n").format(
            super(InvalidTypeError, self).__str__(),
            self.option.value,
            type(self.value)
        )


class RegExpError(UnitError):
    """RegExp Constraint.
    """
    def __str__(self):
        return ("{}\n"
                "regexp: {}\n").format(
            super(RegExpError, self).__str__(),
            self.option.value
        )
