from project.matrix import Matrix


def test_matrix_transposition_of_square_matrix():
    matrix1 = Matrix([[1, 2], [3, 4]])
    result = matrix1.trans()
    assert result.content == [
        [1, 3],
        [2, 4],
    ], "Транспонированная матрица должна быть [[1, 3], [2, 4]]"


def test_matrix_transposition_of_rectangular_matrix():
    matrix2 = Matrix([[1, 2, 3], [4, 5, 6]])
    result = matrix2.trans()
    assert result.content == [
        [1, 4],
        [2, 5],
        [3, 6],
    ], "Транспонированная матрица должна быть [[1, 4], [2, 5], [3, 6]]"


def test_transposition_of_identity_matrix():
    identity_matrix = Matrix([[1, 0], [0, 1]])
    result = identity_matrix.trans()
    assert result.content == [
        [1, 0],
        [0, 1],
    ], "Транспонированная единичная матрица должна быть равна самой себе"
