class Matrix:

    def __init__(self, content=[]) -> None:
        self.content = content
        self.width = 0
        self.height = len(self.content)
        for i in range(self.height):
            self.width = max(len(self.content[i]), self.width)
        for i in range(self.height):
            if self.width > len(self.content[i]):
                self.content += [0] * (self.width - len(self.content[i]))

    def draw(self):
        print(self.content)

    def __add__(self, other):
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

    def __mul__(self, other):
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

    def trans(self):
        return Matrix(
            [
                [self.content[x][y] for x in range(self.height)]
                for y in range(self.height)
            ]
        )
