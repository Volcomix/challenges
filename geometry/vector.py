import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return 'Vector(x={0}, y={1})'.format(self.x, self.y)
    
    def clone(self):
        return Vector(self.x, self.y)

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

    def norm(self):
        length = self.length
        if length > 0:
            return Vector(self.x / length, self.y / length)
        return Vector(0, 0)
    
    def normalize(self):
        length = self.length
        if length > 0:
            self.x /= length
            self.y /= length
        else:
            self.x = 0
            self.y = 0

    def dot(self, other):
        return self.x * other.x + self.y * other.y
