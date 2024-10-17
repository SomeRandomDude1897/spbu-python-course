# test_smart_args.py

import pytest
from project.smart_args import smart_args, Evaluated, Isolated
import random


def test_evaluated_argument_evaluation():
    @smart_args
    def func(x):
        return x

    result = func(x=Evaluated(lambda: 42))
    assert result == 42


def test_evaluated_argument_with_function():
    # переписать на неслучайные числа
    def generate_random():
        return random.randint(1, 100000000)

    @smart_args
    def func(x=Evaluated(generate_random)):
        return x

    result1 = func()
    result2 = func()
    assert result1 != result2  # Since random numbers are likely different


def test_mutable_argument_deepcopy():
    @smart_args
    def append_item(lst):
        lst.append(42)
        return lst

    original_list = [1, 2, 3]
    result = append_item(original_list)
    assert result == [1, 2, 3, 42]
    assert original_list == [1, 2, 3]  # original_list should not be modified


def test_non_mutable_argument():
    @smart_args
    def func(x):
        return x * 2

    result = func(5)
    assert result == 10


def test_combination_of_evaluated_and_mutable_arguments():
    @smart_args
    def func(x, lst):
        lst.append(x)
        return lst

    result = func(x=Evaluated(lambda: 10), lst=[1, 2])
    assert result == [1, 2, 10]


def test_evaluated_default_argument():
    @smart_args
    def func(x=Evaluated(lambda: 5)):
        return x * 2

    result = func()
    assert result == 10


def test_smart_args_with_positional_and_keyword_arguments():
    @smart_args
    def func(a, b=Evaluated(lambda: 5)):
        return a + b

    result = func(10)
    assert result == 15
    result = func(10, b=Evaluated(lambda: 7))
    assert result == 17


def test_smart_args_with_multiple_evaluated_arguments():
    @smart_args
    def func(a=Evaluated(lambda: 5), b=Evaluated(lambda: 10)):
        return a + b

    result = func()
    assert result == 15


def test_mutable_default_argument():
    @smart_args
    def func(lst=[]):
        lst.append(1)
        return lst

    result1 = func()
    result2 = func()
    assert result1 == [1]
    assert result2 == [1]  # Each call should get a fresh copy


def test_isolated():
    @smart_args
    @smart_args
    def check_isolation(*, d=Isolated()):
        d["a"] = 0
        return d

    no_mutable = {"a": 10}

    assert check_isolation(d=no_mutable) == {"a": 0}


def test_isolated_evaluated():
    def amogus():
        return "sus"

    @smart_args
    def func(a=Isolated(), b=Evaluated(amogus)):
        return b + str(a)

    assert func(27) == "sus27"


def test_keyword_args():
    def amogus():
        return "sus"

    @smart_args
    def func(*, a=Isolated(), b=Evaluated(amogus)):
        return b + str(a)

    assert func(a=27) == "sus27"
