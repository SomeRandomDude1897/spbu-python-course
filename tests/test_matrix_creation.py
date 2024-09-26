from project.matrix import Matrix


def test_matrix_creation_with_full_data():
    matrix1 = Matrix([[1, 2], [3, 4]])
    assert matrix1.content == [[1, 2], [3, 4]], "Матрица должна быть создана правильно"


def test_empty_matrix_creation():
    matrix2 = Matrix()
    assert matrix2.content == [], "Пустая матрица должна быть корректно создана"


def test_matrix_creation_with_incomplete_rows():
    matrix3 = Matrix([[1], [2, 3]])
    assert matrix3.content == [[1, 0], [2, 3]], "Матрица должна быть выровнена нулями"
