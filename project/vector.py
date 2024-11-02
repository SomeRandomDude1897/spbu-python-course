from typing import Union, List
import math


class Vector:
    """
    A class to represent a vector and perform operations with it.

    Attributes:
    -----------
    coordinates : List[Union[int, float]]
        A list of vector coordinates (can contain both integers and floating-point numbers).

    Methods:
    --------
    __init__(coordinates: List[Union[int, float]] = []) -> None:
        Initializes the vector with the given coordinates.

    scalar_product(vector1: 'Vector', vector2: 'Vector') -> Union[int, float]:
        Calculates the dot product of two vectors.

    get_angle(vector1: 'Vector', vector2: 'Vector') -> float:
        Calculates the angle between two vectors in degrees.

    length() -> float:
        Calculates the length (Euclidean norm) of the vector.
    """

    @staticmethod
    def scalar_product(vector1: "Vector", vector2: "Vector") -> Union[int, float]:
        """
        Calculates the dot product of two vectors.

        The dot product of two vectors is calculated as the sum of the products
        of their corresponding coordinates.

        Parameters:
        -----------
        vector1 : Vector
            The first vector.
        vector2 : Vector
            The second vector.

        Returns:
        --------
        Union[int, float]
            The result of the dot product of two vectors.

        Exceptions:
        -----------
        Exception
            If the number of dimensions (coordinates) of the vectors does not match.

        Example:
        --------
        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([4, 5, 6])
        >>> Vector.scalar_product(v1, v2)
        32
        """
        if len(vector1.coordinates) != len(vector2.coordinates):
            raise Exception("vectors must have same amount of dimensions")
        product: Union[int, float] = 0
        for i in range(len(vector1.coordinates)):
            product += vector1.coordinates[i] * vector2.coordinates[i]
        return product

    @staticmethod
    def get_angle(vector1: "Vector", vector2: "Vector") -> float:
        """
        Calculates the angle between two vectors in degrees.

        The angle is calculated using the formula:
        cos(theta) = (A * B) / (|A| * |B|), where * is the dot product,
        and |A| and |B| are the lengths of the vectors. The angle is then
        converted to degrees.

        Parameters:
        -----------
        vector1 : Vector
            The first vector.
        vector2 : Vector
            The second vector.

        Returns:
        --------
        float
            The angle between the two vectors in degrees.

        Exceptions:
        -----------
        Exception
            If one of the vectors has a length of zero.

        Example:
        --------
        >>> v1 = Vector([1, 0])
        >>> v2 = Vector([0, 1])
        >>> Vector.get_angle(v1, v2)
        90.0
        """
        return math.degrees(
            math.acos(
                Vector.scalar_product(vector1, vector2)
                / (vector1.length() * vector2.length())
            )
        )

    def __init__(self, coordinates: List[Union[int, float]] = []) -> None:
        """
        Initializes the vector with the given coordinates.

        Parameters:
        -----------
        coordinates : List[Union[int, float]], optional
            A list of vector coordinates, default is an empty list.

        Example:
        --------
        >>> v = Vector([1, 2, 3])
        >>> v.coordinates
        [1, 2, 3]
        """
        self.coordinates: List[Union[int, float]] = coordinates

    def length(self) -> float:
        """
        Calculates the length (Euclidean norm) of the vector.

        The length (magnitude) of the vector is calculated as the square root
        of the sum of the squares of its coordinates.

        Returns:
        --------
        float
            The length (magnitude) of the vector.

        Example:
        --------
        >>> v = Vector([3, 4])
        >>> v.length()
        5.0
        """
        length: float = 0
        for i in range(len(self.coordinates)):
            length += self.coordinates[i] ** 2
        return length**0.5
