# test_curry_uncurry_combination.py

import pytest
from project.curry import curry_explicit, uncurry_explicit


def test_curry_then_uncurry():
    @uncurry_explicit(2)
    @curry_explicit(2)
    def func(a, b):
        return a * b

    result = func(3, 4)
    assert result == 12


def test_uncurry_then_curry():
    @curry_explicit(2)
    @uncurry_explicit(2)
    @curry_explicit(2)
    def func(a, b):
        return a * b

    curried_func = func(3)
    result = curried_func(4)
    assert result == 12


def test_curry_uncurry_negative_arity():
    with pytest.raises(Exception) as exc_info:

        @uncurry_explicit(-1)
        @curry_explicit(-1)
        def func(a):
            return a

    assert str(exc_info.value) == "Arity must be non-negative"
