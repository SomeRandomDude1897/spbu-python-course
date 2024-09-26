from project.vector import Vector


def test_vector_scalar_product():
    vector1 = Vector([1, 0])
    vector2 = Vector([0, 1])
    assert (
        Vector.scalar_product(vector1, vector2) == 0
    ), "Скалярное произведение [1, 0] и [0, 1] должно быть 0"

    vector3 = Vector([1, 2, 3])
    vector4 = Vector([4, 5, 6])
    assert (
        Vector.scalar_product(vector3, vector4) == 32
    ), "Скалярное произведение [1, 2, 3] и [4, 5, 6] должно быть 32"

    vector5 = Vector([-1, 1])
    vector6 = Vector([1, 1])
    assert (
        Vector.scalar_product(vector5, vector6) == 0
    ), "Скалярное произведение [-1, 1] и [1, 1] должно быть 0"
