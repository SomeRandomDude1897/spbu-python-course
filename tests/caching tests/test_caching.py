import pytest
from project.cache import cache


def test_cache_single_argument():
    @cache(storage_size=2)
    def square(x):
        return x * x

    result = square(3)
    assert result == 9


def test_cache_reuse_cached_value():
    @cache(storage_size=2)
    def square(x):
        return x * x

    square(4)  # First call, value is computed and cached
    result = square(4)  # Second call, value should be retrieved from cache
    assert result == 16


def test_cache_eviction():
    @cache(storage_size=2)
    def square(x):
        return x * x

    square(5)  # Cache: {5: 25}
    square(6)  # Cache: {5: 25, 6: 36}
    square(7)  # Cache exceeds size, oldest entry (5) should be evicted
    result = square(5)  # Should recompute since 5 was evicted
    assert result == 25


def test_cache_multiple_arguments():
    @cache(storage_size=2)
    def add(a, b):
        return a + b

    result = add(2, 3)
    assert result == 5


def test_cache_with_kwargs():
    @cache(storage_size=2)
    def greet(greeting, name="World"):
        return f"{greeting}, {name}!"

    result = greet("Hello", name="Alice")
    assert result == "Hello, Alice!"
