from project.matrix import Matrix


def test_matrix_creation():
    matrix1 = Matrix([[1, 2], [3, 4]])
    assert matrix1.content == [[1, 2], [3, 4]], "Матрица должна быть создана правильно"

    matrix2 = Matrix()
    assert matrix2.content == [], "Пустая матрица должна быть корректно создана"

    matrix3 = Matrix([[1], [2, 3]])
    assert matrix3.content == [[1, 0], [2, 3]], "Матрица должна быть выровнена нулями"
