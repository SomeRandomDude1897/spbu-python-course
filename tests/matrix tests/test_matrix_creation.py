from project.matrix import Matrix


def test_empty_matrix_creation():
    matrix2 = Matrix()
    assert matrix2.content == [], "Пустая матрица должна быть корректно создана"


def test_matrix_creation():
    matrix3 = Matrix([[1, 4], [2, 3]])
    assert matrix3.content == [[1, 4], [2, 3]], "Матрица должна быть выровнена нулями"

def test_matrix_creation():
    matrix3 = Matrix([[1, 4], [2, 3]])
    assert matrix3.content == [[1, 4], [2, 3]], "Матрица должна быть корректно создана"
