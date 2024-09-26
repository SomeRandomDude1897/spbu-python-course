from vector import Vector
from matrix import Matrix

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5 , 6], [7, 8]])

m1 *= m2

m1.draw()

m2.trans().draw()