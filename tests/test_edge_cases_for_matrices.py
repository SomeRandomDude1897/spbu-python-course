from project.matrix import Matrix


def test_edge_cases_for_matrices():
    matrix = Matrix([[1, 2], [3]])
    assert matrix.content == [
        [1, 2],
        [3, 0],
    ], "Матрица должна быть корректно выровнена нулями"

    matrix1 = Matrix([[1, 2], [3, 0]])
    matrix2 = Matrix([[0, 0], [0, 0]])
    result = matrix1 + matrix2
    assert result.content == [
        [1, 2],
        [3, 0],
    ], "Сложение с нулевой матрицей должно вернуть исходную матрицу"
