# test_curry_explicit.py

import pytest
from project.curry import curry_explicit


def test_curry_explicit_negative_arity():
    with pytest.raises(Exception) as exc_info:

        @curry_explicit(-1)
        def func(a):
            return a

    assert str(exc_info.value) == "Arity must be non-negative"


def test_curry_explicit_single_argument():
    @curry_explicit(1)
    def func(a):
        return a * 2

    assert func(5) == 10


def test_curry_explicit_partial_application():
    @curry_explicit(2)
    def func(a, b):
        return a + b

    curried_func = func(3)
    result = curried_func(4)
    assert result == 7


def test_curry_explicit_multiple_partial_applications():
    @curry_explicit(3)
    def func(a, b, c):
        return a * b + c

    step1 = func(2)
    step2 = step1(3)
    result = step2(4)
    assert result == 10


def test_curry_explicit_multiple_arguments_in_partial():
    @curry_explicit(2)
    def func(a, b):
        return a + b

    partial = func(1)
    with pytest.raises(Exception) as exc_info:
        partial(2, 3)
    assert str(exc_info.value) == "Only one argument can be provided at a time"
