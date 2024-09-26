import pytest
from project.matrix import Matrix

def test_matrix_multiplication_with_valid_matrices():
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5, 6], [7, 8]])
    result = matrix1 * matrix2
    assert result.content == [
        [19, 22],
        [43, 50],
    ], "Результат умножения должен быть [[19, 22], [43, 50]]"

def test_matrix_multiplication_with_identity_matrix():
    matrix1 = Matrix([[1, 2], [3, 4]])
    identity_matrix = Matrix([[1, 0], [0, 1]])
    result = matrix1 * identity_matrix
    assert result.content == [
        [1, 2],
        [3, 4],
    ], "Результат умножения на единичную матрицу должен быть равен исходной матрице"

def test_matrix_multiplication_with_incompatible_matrices():
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix3 = Matrix([[1, 2, 3], [4, 5, 6]])
    with pytest.raises(Exception, match="Matrix dimensions not fit for multiplication"):
        matrix1 * matrix3
