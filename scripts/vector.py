import math


class Vector:

    @staticmethod
    def scalar_product(vector1=None, vector2=None):
        if len(vector1.coordinates) != len(vector2.coordinates):
            raise Exception("vectors must have same amount of dimensions")
        product = 0
        for i in range(len(vector1.coordinates)):
            product += vector1.coordinates[i] * vector2.coordinates[i]
        return product

    @staticmethod
    def get_angle(vector1=None, vector2=None):
        return math.degrees(
            math.acos(
                Vector.scalar_product(vector1, vector2)
                / (vector1.length() * vector2.length())
            )
        )

    def __init__(self, coordinates=[]) -> None:
        self.coordinates = coordinates

    def length(self):
        length = 0
        for i in range(len(self.coordinates)):
            length += self.coordinates[i] ** 2
        return length**0.5
