from typing import Union, List


class Matrix:
    """
    Класс для представления матрицы и выполнения операций с ней.

    Атрибуты:
    ----------
    content : List[List[Union[int, float]]]
        Двумерный список, представляющий содержимое матрицы.
    width : int
        Количество столбцов матрицы (максимальная длина строк).
    height : int
        Количество строк матрицы.

    Методы:
    -------
    __init__(content: List[List[Union[int, float]]] = []) -> None:
        Инициализация матрицы с выравниванием строк до одинаковой длины.

    draw() -> None:
        Выводит содержимое матрицы в консоль.

    __add__(other: 'Matrix') -> 'Matrix':
        Складывает текущую матрицу с другой матрицей и возвращает результат.

    __mul__(other: 'Matrix') -> 'Matrix':
        Умножает текущую матрицу на другую матрицу и возвращает результат.

    trans() -> 'Matrix':
        Транспонирует текущую матрицу (меняет строки на столбцы) и возвращает результат.
    """

    def __init__(self, content: List[List[Union[int, float]]] = []) -> None:
        """
        Инициализирует матрицу.

        Принимает двумерный список (список списков), который представляет матрицу.
        Автоматически выравнивает строки до максимальной длины, добавляя нули в конец
        строк, которые короче других.

        Параметры:
        ----------
        content : List[List[Union[int, float]]], optional
            Двумерный список чисел (int или float), представляющий матрицу. По умолчанию — пустой список.
        """
        self.content: List[List[Union[int, float]]] = content
        self.width: int = 0
        self.height: int = len(self.content)

        for i in range(self.height):
            self.width = max(len(self.content[i]), self.width)
        for i in range(self.height):
            if self.width > len(self.content[i]):
                self.content[i] += [0] * (self.width - len(self.content[i]))

    def draw(self) -> None:
        """
        Выводит содержимое матрицы в консоль.

        Пример вывода:
        [[1, 2, 3], [4, 5, 6]]
        """
        print(self.content)

    def __add__(self, other: "Matrix") -> "Matrix":
        """
        Складывает текущую матрицу с другой матрицей.

        Складывает два объекта класса `Matrix`, проверяя при этом, что их размеры совпадают.
        Возвращает новую матрицу, содержащую сумму соответствующих элементов.

        Параметры:
        ----------
        other : Matrix
            Вторая матрица, с которой нужно произвести сложение.

        Возвращаемое значение:
        ----------------------
        Matrix
            Новая матрица, представляющая собой результат сложения двух матриц.

        Исключения:
        -----------
        Exception
            Если размеры двух матриц не совпадают.
        """
        if self.width != other.width or self.height != other.height:
            raise Exception(
                "In order to find the sum of two matrices they must be the same size"
            )
        return Matrix(
            [
                [self.content[y][x] + other.content[y][x] for x in range(self.width)]
                for y in range(self.height)
            ]
        )

    def __mul__(self, other: "Matrix") -> "Matrix":
        """
        Умножает текущую матрицу на другую матрицу.

        Умножает два объекта класса `Matrix`, проверяя, что число столбцов первой
        матрицы равно числу строк второй матрицы. Возвращает новую матрицу, содержащую
        результат умножения.

        Параметры:
        ----------
        other : Matrix
            Вторая матрица, на которую нужно умножить текущую матрицу.

        Возвращаемое значение:
        ----------------------
        Matrix
            Новая матрица, представляющая собой результат умножения двух матриц.

        Исключения:
        -----------
        Exception
            Если число столбцов первой матрицы не равно числу строк второй.
        """
        if self.height != other.width:
            raise Exception("Matrix dimensions not fit for multiplication")
        return Matrix(
            [
                [
                    sum(
                        self.content[i][k] * other.content[k][j]
                        for k in range(self.width)
                    )
                    for j in range(other.width)
                ]
                for i in range(self.height)
            ]
        )

    def trans(self) -> "Matrix":
        """
        Транспонирует текущую матрицу.

        Меняет строки на столбцы и возвращает новую матрицу.

        Возвращаемое значение:
        ----------------------
        Matrix
            Новая транспонированная матрица.

        Пример:
        -------
        Если исходная матрица:
        [[1, 2, 3], [4, 5, 6]]
        Транспонированная матрица будет:
        [[1, 4], [2, 5], [3, 6]]
        """
        return Matrix(
            [
                [self.content[x][y] for x in range(self.height)]
                for y in range(self.width)
            ]
        )
