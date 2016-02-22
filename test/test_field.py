import pytest

from sigma.standard import Field, NotNoneError, \
    WhiteListError, BlackListError, InvalidTypeError, \
    TooLongError, TooShortError, OverMaxError, OverMinError
import sigma.standard.option as so


def test_noneable():
    name = Field(so.noneable(False))
    name.value = 5
    assert name.value == 5
    with pytest.raises(NotNoneError):
        name.value = None
    assert name.value == 5


def test_white_list():
    name = Field(so.white_list(1))
    name.value = 1
    assert name.value == 1
    with pytest.raises(WhiteListError):
        name.value = 2
    assert name.value == 1


def test_black_list():
    name = Field(so.black_list(2))
    name.value = 1
    assert name.value == 1
    with pytest.raises(BlackListError):
        name.value = 2
    assert name.value == 1


def test_type():
    name = Field(so.type_(int))
    name.value = 1
    assert name.value == 1
    with pytest.raises(InvalidTypeError):
        name.value = "1"
    assert name.value == 1


def test_length():
    name = Field(so.length(None, 1))
    name.value = ""
    assert name.value == ""
    name.value = "1"
    assert name.value == "1"
    with pytest.raises(TooLongError):
        name.value = "12"
    assert name.value == "1"

    name = Field(so.length(1, 2))
    name.value = "12"
    assert name.value == "12"
    with pytest.raises(TooLongError):
        name.value = "123"
    assert name.value == "12"

    name = Field(so.length(1, 5))
    name.value = "1"
    assert name.value == "1"
    with pytest.raises(TooShortError):
        name.value = ""
    assert name.value == "1"

    name = Field(so.length(1, None))
    name.value = "1"
    assert name.value == "1"
    with pytest.raises(TooShortError):
        name.value = ""
    assert name.value == "1"


def test_size():
    name = Field(so.size(None, 5))
    name.value = 5
    assert name.value == 5
    with pytest.raises(OverMaxError):
        name.value = 6
    assert name.value == 5

    name = Field(so.size(1, 5))
    name.value = 5
    assert name.value == 5
    with pytest.raises(OverMaxError):
        name.value = 6
    assert name.value == 5

    name = Field(so.size(1, None))
    name.value = 1
    assert name.value == 1
    with pytest.raises(OverMinError):
        name.value = 0
    assert name.value == 1

    name = Field(so.size(1, 5))
    name.value = 1
    assert name.value == 1
    with pytest.raises(OverMinError):
        name.value = 0
    assert name.value == 1
