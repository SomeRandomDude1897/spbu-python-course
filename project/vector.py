from typing import Union, List
import math

class Vector:

    @staticmethod
    def scalar_product(vector1: 'Vector', vector2: 'Vector'):
        if len(vector1.coordinates) != len(vector2.coordinates):
            raise Exception("vectors must have same amount of dimensions")
        product: Union[int, float] = 0
        for i in range(len(vector1.coordinates)):
            product += vector1.coordinates[i] * vector2.coordinates[i]
        return product

    @staticmethod
    def get_angle(vector1: 'Vector', vector2: 'Vector'):
        return math.degrees(
            math.acos(
                Vector.scalar_product(vector1, vector2)
                / (vector1.length() * vector2.length())
            )
        )

    def __init__(self, coordinates: List[Union[int, float]] = []) -> None:
        self.coordinates: List[Union[int, float]] = coordinates

    def length(self):
        length: int = 0
        for i in range(len(self.coordinates)):
            length += self.coordinates[i] ** 2
        return length**0.5