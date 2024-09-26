import pytest
from project.vector import Vector


def test_scalar_product_of_zero_vectors():
    vector1 = Vector([0, 0])
    vector2 = Vector([0, 0])

    assert (
        Vector.scalar_product(vector1, vector2) == 0
    ), "Скалярное произведение нулевых векторов должно быть 0"

def test_scalar_product_with_zero_vector():
    vector3 = Vector([1, 1])
    vector4 = Vector([0, 0])
    
    assert (
        Vector.scalar_product(vector3, vector4) == 0
    ), "Скалярное произведение любого вектора с нулевым должно быть 0"

def test_get_angle_with_zero_vectors():
    vector1 = Vector([0, 0])
    vector2 = Vector([0, 0])
    
    with pytest.raises(ZeroDivisionError):
        Vector.get_angle(vector1, vector2)
