# test_uncurry_explicit.py

import pytest
from project.curry import uncurry_explicit, curry_explicit


def test_uncurry_explicit_negative_arity():
    with pytest.raises(Exception) as exc_info:

        @uncurry_explicit(-1)
        def func(a):
            return a

    assert str(exc_info.value) == "Arity must be non-negative"


def test_uncurry_explicit_single_argument():
    @uncurry_explicit(1)
    @curry_explicit(1)
    def func(a):
        return a * 2

    assert func(5) == 10


def test_uncurry_explicit_multiple_arguments():
    @uncurry_explicit(2)
    @curry_explicit(2)
    def func(a, b):
        return a + b

    result = func(3, 4)
    assert result == 7


def test_uncurry_explicit_incomplete_arguments():
    @uncurry_explicit(2)
    @curry_explicit(2)
    def func(a, b):
        return a + b

    with pytest.raises(TypeError) as exc_info:
        func(3)
    assert str(exc_info.value) == "Expected 2 arguments, got 1"


def test_uncurry_explicit_excess_arguments():
    @uncurry_explicit(2)
    @curry_explicit(2)
    def func(a, b):
        return a + b

    with pytest.raises(TypeError) as exc_info:
        func(3, 4, 5)
    assert str(exc_info.value) == "Expected 2 arguments, got 3"


def test_uncurry_explicit_with_non_curried_function():
    @uncurry_explicit(2)
    def func(a):
        return lambda b: a + b

    result = func(3, 4)
    assert result == 7
