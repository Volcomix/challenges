import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def dist(self, other):
        return math.hypot(other.x - self.x, other.y - self.y)

    def dist2(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        return dx * dx + dy * dy
