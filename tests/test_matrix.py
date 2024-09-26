import pytest
import math
from project.matrix import Matrix

def test_matrix_creation():
    matrix1 = Matrix([[1, 2], [3, 4]])
    assert matrix1.content == [[1, 2], [3, 4]], "Матрица должна быть создана правильно"

    matrix2 = Matrix()
    assert matrix2.content == [], "Пустая матрица должна быть корректно создана"

    matrix3 = Matrix([[1], [2, 3]])
    assert matrix3.content == [[1, 0], [2, 3]], "Матрица должна быть выровнена нулями"


def test_matrix_addition():
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5, 6], [7, 8]])
    result = matrix1 + matrix2
    assert result.content == [[6, 8], [10, 12]], "Результат сложения должен быть [[6, 8], [10, 12]]"

    matrix3 = Matrix([[0, 0], [0, 0]])
    result = matrix1 + matrix3
    assert result.content == [[1, 2], [3, 4]], "Результат сложения с нулевой матрицей должен быть равен оригинальной матрице"

    matrix4 = Matrix([[1, 2]])
    with pytest.raises(Exception, match="In order to find the summ of two matrices they must be the same size"):
        matrix1 + matrix4


def test_matrix_multiplication():
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5, 6], [7, 8]])
    result = matrix1 * matrix2
    assert result.content == [[19, 22], [43, 50]], "Результат умножения должен быть [[19, 22], [43, 50]]"

    identity_matrix = Matrix([[1, 0], [0, 1]])
    result = matrix1 * identity_matrix
    assert result.content == [[1, 2], [3, 4]], "Результат умножения на единичную матрицу должен быть равен исходной матрице"

    matrix3 = Matrix([[1, 2, 3], [4, 5, 6]])
    with pytest.raises(Exception, match="Matrix dimensions not fit for multiplication"):
        matrix1 * matrix3


def test_matrix_transposition():
    matrix1 = Matrix([[1, 2], [3, 4]])
    result = matrix1.trans()
    assert result.content == [[1, 3], [2, 4]], "Транспонированная матрица должна быть [[1, 3], [2, 4]]"

    matrix2 = Matrix([[1, 2, 3], [4, 5, 6]])
    result = matrix2.trans()
    assert result.content == [[1, 4], [2, 5], [3, 6]], "Транспонированная матрица должна быть [[1, 4], [2, 5], [3, 6]]"

    identity_matrix = Matrix([[1, 0], [0, 1]])
    result = identity_matrix.trans()
    assert result.content == [[1, 0], [0, 1]], "Транспонированная единичная матрица должна быть равна самой себе"


def test_edge_cases_for_matrices():
    matrix = Matrix([[1, 2], [3]])
    assert matrix.content == [[1, 2], [3, 0]], "Матрица должна быть корректно выровнена нулями"

    matrix1 = Matrix([[1, 2], [3, 0]])
    matrix2 = Matrix([[0, 0], [0, 0]])
    result = matrix1 + matrix2
    assert result.content == [[1, 2], [3, 0]], "Сложение с нулевой матрицей должно вернуть исходную матрицу"
