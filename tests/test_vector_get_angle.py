import math
from project.vector import Vector


def test_vector_get_angle_90_degrees():
    vector1 = Vector([1, 0])
    vector2 = Vector([0, 1])
    assert math.isclose(
        Vector.get_angle(vector1, vector2), 90.0, abs_tol=1e-5
    ), "Угол между [1, 0] и [0, 1] должен быть 90 градусов"

def test_vector_get_angle_45_degrees():
    vector3 = Vector([1, 1])
    vector4 = Vector([1, 0])
    assert math.isclose(
        Vector.get_angle(vector3, vector4), 45.0, abs_tol=1e-5
    ), "Угол между [1, 1] и [1, 0] должен быть 45 градусов"

def test_vector_get_angle_0_degrees():
    vector5 = Vector([1, 1])
    vector6 = Vector([1, 1])
    assert math.isclose(
        Vector.get_angle(vector5, vector6), 0.0, abs_tol=1e-5
    ), "Угол должен быть 0"
