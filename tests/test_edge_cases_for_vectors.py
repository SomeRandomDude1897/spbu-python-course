import pytest
from project.vector import Vector


def test_edge_cases_for_vectors():
    vector1 = Vector([0, 0])
    vector2 = Vector([0, 0])

    assert (
        Vector.scalar_product(vector1, vector2) == 0
    ), "Скалярное произведение нулевых векторов должно быть 0"

    vector3 = Vector([1, 1])
    vector4 = Vector([0, 0])
    assert (
        Vector.scalar_product(vector3, vector4) == 0
    ), "Скалярное произведение любого вектора с нулевым должно быть 0"

    with pytest.raises(ZeroDivisionError):
        Vector.get_angle(vector1, vector2)
