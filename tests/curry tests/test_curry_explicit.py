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

    assert func(3)(4) == 7


def test_curry_explicit_multiple_partial_applications():
    @curry_explicit(3)
    def func(a, b, c):
        return a * b + c

    assert func(2)(2)(6) == 10


def test_curry_explicit_multiple_arguments_in_partial():
    @curry_explicit(2)
    def func(a, b, c):
        return a + b + c

    with pytest.raises(Exception) as exc_info:
        func(2)(3, 4)
    print(str(exc_info.value))
    assert str(exc_info.value) == "Only one argument can be provided at a time"


def test_curry_explicit_print():
    assert curry_explicit(3)(max)(1)(2)(3) == 3


def test_curry_explicit_print():
    @curry_explicit(2)
    def new_print(*args, **kwargs):
        return print(*args, **kwargs)

    assert new_print(1)(2) == None


# тест на каррирование встроенной функции, арность принта
