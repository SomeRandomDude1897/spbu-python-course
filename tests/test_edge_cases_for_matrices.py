from project.matrix import Matrix


def test_matrix_alignment():
    matrix = Matrix([[1, 2], [3]])
    expected = [[1, 2], [3, 0]]
    assert matrix.content == expected, "Матрица должна быть корректно выровнена нулями"

def test_add_zero_matrix():
    matrix1 = Matrix([[1, 2], [3, 0]])
    matrix2 = Matrix([[0, 0], [0, 0]])
    result = matrix1 + matrix2
    expected = [[1, 2], [3, 0]]
    assert result.content == expected, "Сложение с нулевой матрицей должно вернуть исходную матрицу"