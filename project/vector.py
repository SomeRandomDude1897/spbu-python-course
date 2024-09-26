from typing import Union, List
import math


class Vector:
    """
    Класс для представления вектора и выполнения операций с ним.

    Атрибуты:
    ----------
    coordinates : List[Union[int, float]]
        Список координат вектора (может содержать как целые числа, так и числа с плавающей точкой).

    Методы:
    -------
    __init__(coordinates: List[Union[int, float]] = []) -> None:
        Инициализирует вектор с заданными координатами.

    scalar_product(vector1: 'Vector', vector2: 'Vector') -> Union[int, float]:
        Вычисляет скалярное произведение двух векторов.

    get_angle(vector1: 'Vector', vector2: 'Vector') -> float:
        Вычисляет угол между двумя векторами в градусах.

    length() -> float:
        Вычисляет длину вектора (его евклидову норму).
    """

    @staticmethod
    def scalar_product(vector1: "Vector", vector2: "Vector") -> Union[int, float]:
        """
        Вычисляет скалярное произведение двух векторов.

        Скалярное произведение двух векторов рассчитывается как сумма произведений
        их соответствующих координат.

        Параметры:
        ----------
        vector1 : Vector
            Первый вектор.
        vector2 : Vector
            Второй вектор.

        Возвращаемое значение:
        ----------------------
        Union[int, float]
            Результат скалярного произведения двух векторов.

        Исключения:
        -----------
        Exception
            Если количество измерений (координат) у векторов не совпадает.

        Пример:
        -------
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
        Вычисляет угол между двумя векторами в градусах.

        Угол рассчитывается с использованием формулы:
        cos(theta) = (A * B) / (|A| * |B|), где * - скалярное произведение,
        а |A| и |B| - длины векторов. Затем угол переводится в градусы.

        Параметры:
        ----------
        vector1 : Vector
            Первый вектор.
        vector2 : Vector
            Второй вектор.

        Возвращаемое значение:
        ----------------------
        float
            Угол между двумя векторами в градусах.

        Исключения:
        -----------
        Exception
            Если один из векторов имеет нулевую длину.

        Пример:
        -------
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
        Инициализирует вектор с заданными координатами.

        Параметры:
        ----------
        coordinates : List[Union[int, float]], optional
            Список координат вектора, по умолчанию пустой список.

        Пример:
        -------
        >>> v = Vector([1, 2, 3])
        >>> v.coordinates
        [1, 2, 3]
        """
        self.coordinates: List[Union[int, float]] = coordinates

    def length(self) -> float:
        """
        Вычисляет длину вектора (его евклидову норму).

        Длина (модуль) вектора рассчитывается как квадратный корень
        из суммы квадратов его координат.

        Возвращаемое значение:
        ----------------------
        float
            Длина (модуль) вектора.

        Пример:
        -------
        >>> v = Vector([3, 4])
        >>> v.length()
        5.0
        """
        length: float = 0
        for i in range(len(self.coordinates)):
            length += self.coordinates[i] ** 2
        return length**0.5
