import math
from collections import namedtuple 

class Vector(namedtuple('Vector', 'x y')):
    __slots__ = ()

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    def __floordiv__(self, scalar):
        return Vector(self.x // scalar, self.y // scalar)

    @property
    def length(self):
        return math.hypot(self.x, self.y)

    @property
    def length2(self):
        return self.x * self.x + self.y * self.y

    @property
    def norm(self):
        length = self.length
        if length > 0:
            return Vector(self.x / length, self.y / length)
        return Vector(0, 0)

    def dot(self, other):
        return self.x * other.x + self.y * other.y
