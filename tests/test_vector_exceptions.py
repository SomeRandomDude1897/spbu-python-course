import pytest
from project.vector import Vector


def test_exceptions():
    vector1 = Vector([1, 2])
    vector2 = Vector([1, 2, 3])

    with pytest.raises(Exception, match="vectors must have same amount of dimensions"):
        Vector.scalar_product(vector1, vector2)

    with pytest.raises(Exception, match="vectors must have same amount of dimensions"):
        Vector.get_angle(vector1, vector2)
