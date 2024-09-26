import math
from project.vector import Vector


def test_vector_length():
    vector1 = Vector([3, 4])
    assert vector1.length() == 5.0, "Длина вектора [3, 4] должна быть 5"

    vector2 = Vector([0, 0])
    assert vector2.length() == 0, "Длина нулевого вектора должна быть 0"

    vector3 = Vector([1, 1, 1])
    assert math.isclose(
        vector3.length(), math.sqrt(3)
    ), "Длина вектора [1, 1, 1] должна быть √3"
