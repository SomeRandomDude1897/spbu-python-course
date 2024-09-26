from typing import Union, List

class Matrix:

    def __init__(self, content: List[List[Union[int, float]]] =[]) -> None:
        self.content: List[List[Union[int, float]]] = content
        self.width: int = 0
        self.height: int = len(self.content)
        for i in range(self.height):
            self.width = max(len(self.content[i]), self.width)
        for i in range(self.height):
            if self.width > len(self.content[i]):
                self.content[i] += [0] * (self.width - len(self.content[i]))

    def draw(self) -> None:
        print(self.content)

    def __add__(self, other: 'Matrix') -> 'Matrix':
        if self.width != other.width or self.height != other.height:
            raise Exception(
                "In order to find the summ of two matrices they must be the same size"
            )
        return Matrix(
            [
                [self.content[y][x] + other.content[y][x] for x in range(self.width)]
                for y in range(self.height)
            ]
        )

    def __mul__(self, other: 'Matrix') -> 'Matrix':
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

    def trans(self) -> 'Matrix':
        return Matrix(
            [
                [self.content[x][y] for x in range(self.height)]
                for y in range(self.width)
            ]
        )
