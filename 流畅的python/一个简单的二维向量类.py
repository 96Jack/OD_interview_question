from math import hypot

class Vector:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        # %r表示用repr()处理， 类似%s是用str()处理
        return "Vector(%r,%r)"%(self.x, self.y)
    
    def __abs__(self):
        return hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y    
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x*scalar, self.y*scalar)

v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1 + v2)