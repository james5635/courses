class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    """
    in c++, the operator* return new object
            the operato*= return *this          
    in python, the __mul__ or __rmul__ return new object
               the __imul__ return self
    """

    def __mul__(self, v: "Vector"):
        new = Vector(self.x * v.x, self.y * v.y)
        return new

    def __truediv__(self, v):
        self.x /= v.x
        self.y /= v.y
        return self


v1 = Vector(1, 2)
v2 = Vector(2, 3)
mul = v1 * v2
div = v1 / v2
print(mul.x, mul.y)
print(div.x, div.y)
