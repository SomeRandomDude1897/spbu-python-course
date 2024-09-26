import pytest
import math
from project.vector import Vector

def test_length():
    vector1 = Vector([3, 4])
    assert vector1.length() == 5.0, "Длина вектора [3, 4] должна быть 5"

    vector2 = Vector([0, 0])
    assert vector2.length() == 0, "Длина нулевого вектора должна быть 0"

    vector3 = Vector([1, 1, 1])
    assert math.isclose(vector3.length(), math.sqrt(3)), "Длина вектора [1, 1, 1] должна быть √3"


def test_scalar_product():
    vector1 = Vector([1, 0])
    vector2 = Vector([0, 1])
    assert Vector.scalar_product(vector1, vector2) == 0, "Скалярное произведение [1, 0] и [0, 1] должно быть 0"

    vector3 = Vector([1, 2, 3])
    vector4 = Vector([4, 5, 6])
    assert Vector.scalar_product(vector3, vector4) == 32, "Скалярное произведение [1, 2, 3] и [4, 5, 6] должно быть 32"

    vector5 = Vector([-1, 1])
    vector6 = Vector([1, 1])
    assert Vector.scalar_product(vector5, vector6) == 0, "Скалярное произведение [-1, 1] и [1, 1] должно быть 0"


def test_get_angle():
    vector1 = Vector([1, 0])
    vector2 = Vector([0, 1])
    assert math.isclose(Vector.get_angle(vector1, vector2), 90.0), "Угол между [1, 0] и [0, 1] должен быть 90 градусов"

    vector3 = Vector([1, 1])
    vector4 = Vector([1, 0])
    assert math.isclose(Vector.get_angle(vector3, vector4), 45.0), "Угол между [1, 1] и [1, 0] должен быть 45 градусов"

    vector5 = Vector([1, 1])
    vector6 = Vector([1, 1])
    assert math.isclose(Vector.get_angle(vector5, vector6), 0.0), "Угол между одинаковыми векторами должен быть 0 градусов"


def test_exceptions():
    vector1 = Vector([1, 2])
    vector2 = Vector([1, 2, 3])
    
    with pytest.raises(Exception, match="vectors must have same amount of dimensions"):
        Vector.scalar_product(vector1, vector2)
    
    with pytest.raises(Exception, match="vectors must have same amount of dimensions"):
        Vector.get_angle(vector1, vector2)


def test_edge_cases_for_vectors():
    vector1 = Vector([0, 0])
    vector2 = Vector([0, 0])

    assert Vector.scalar_product(vector1, vector2) == 0, "Скалярное произведение нулевых векторов должно быть 0"

    vector3 = Vector([1, 1])
    vector4 = Vector([0, 0])
    assert Vector.scalar_product(vector3, vector4) == 0, "Скалярное произведение любого вектора с нулевым должно быть 0"

    with pytest.raises(ZeroDivisionError):
        Vector.get_angle(vector1, vector2)


def test_various_vectors():
    vectors = [
        (Vector([1, 2, 3]), Vector([1, 2, 3]), 1.0, 0.0),
        (Vector([5, 0, 0]), Vector([0, 5, 0]), 90.0, 0.0),
        (Vector([1, 1, 0]), Vector([0, 0, 1]), 90.0, 0.0),
    ]

    for vector1, vector2, expected_angle, expected_scalar in vectors:
        assert math.isclose(Vector.get_angle(vector1, vector2), expected_angle), f"Ожидался угол {expected_angle} градусов"
        assert Vector.scalar_product(vector1, vector2) == expected_scalar, f"Ожидалось скалярное произведение {expected_scalar}"

