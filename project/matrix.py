from typing import Union, List


class Matrix:
    """
    A class to represent a matrix and perform operations with it.

    Attributes:
    -----------
    content : List[List[Union[int, float]]]
        A two-dimensional list representing the matrix content.
    width : int
        The number of columns in the matrix (the maximum length of rows).
    height : int
        The number of rows in the matrix.

    Methods:
    --------
    __init__(content: List[List[Union[int, float]]] = []) -> None:
        Initializes a matrix, aligning the rows to have the same length.

    draw() -> None:
        Prints the matrix content to the console.

    __add__(other: 'Matrix') -> 'Matrix':
        Adds the current matrix with another matrix and returns the result.

    __mul__(other: 'Matrix') -> 'Matrix':
        Multiplies the current matrix with another matrix and returns the result.

    trans() -> 'Matrix':
        Transposes the current matrix (swaps rows with columns) and returns the result.
    """

    def __init__(self, content: List[List[Union[int, float]]] = []) -> None:
        """
        Initializes a matrix.

        Takes a two-dimensional list (a list of lists) that represents the matrix.
        Automatically aligns the rows to the maximum length by adding zeros to the end
        of rows that are shorter than others.

        Parameters:
        -----------
        content : List[List[Union[int, float]]], optional
            A two-dimensional list of numbers (int or float) representing the matrix. Defaults to an empty list.
        """
        self.content: List[List[Union[int, float]]] = content
        self.width: int = 0
        self.height: int = len(self.content)

        for i in range(self.height):
            self.width = max(len(self.content[i]), self.width)
        for i in range(self.height):
            if self.width > len(self.content[i]):
                self.content[i] += [0] * (self.width - len(self.content[i]))

    def __add__(self, other: "Matrix") -> "Matrix":
        """
        Adds the current matrix with another matrix.

        Adds two `Matrix` objects, checking that their sizes match.
        Returns a new matrix containing the sum of the corresponding elements.

        Parameters:
        -----------
        other : Matrix
            The second matrix to be added.

        Returns:
        --------
        Matrix
            A new matrix representing the result of adding the two matrices.

        Exceptions:
        -----------
        Exception
            If the sizes of the two matrices do not match.
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
        Multiplies the current matrix with another matrix.

        Multiplies two `Matrix` objects, checking that the number of columns in the first
        matrix matches the number of rows in the second matrix. Returns a new matrix containing
        the result of the multiplication.

        Parameters:
        -----------
        other : Matrix
            The second matrix to multiply with the current matrix.

        Returns:
        --------
        Matrix
            A new matrix representing the result of multiplying the two matrices.

        Exceptions:
        -----------
        Exception
            If the number of columns in the first matrix does not match the number of rows in the second.
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
        Transposes the current matrix.

        Swaps rows with columns and returns a new matrix.

        Returns:
        --------
        Matrix
            A new transposed matrix.

        Example:
        --------
        If the original matrix is:
        [[1, 2, 3], [4, 5, 6]]
        The transposed matrix will be:
        [[1, 4], [2, 5], [3, 6]]
        """
        return Matrix(
            [
                [self.content[x][y] for x in range(self.height)]
                for y in range(self.width)
            ]
        )
