import pytest
from project.matrix import Matrix


def test_matrix_addition_with_equal_size():
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5, 6], [7, 8]])
    result = matrix1 + matrix2
    assert result.content == [
        [6, 8],
        [10, 12],
    ], "Результат сложения должен быть [[6, 8], [10, 12]]"

def test_matrix_addition_with_zero_matrix():
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix3 = Matrix([[0, 0], [0, 0]])
    result = matrix1 + matrix3
    assert result.content == [
        [1, 2],
        [3, 4],
    ], "Результат сложения с нулевой матрицей должен быть равен оригинальной матрице"

def test_matrix_addition_with_different_size():
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix4 = Matrix([[1, 2]])
    with pytest.raises(
        Exception,
        match="In order to find the sum of two matrices they must be the same size",
    ):
        matrix1 + matrix4

