import math

from .vector import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return 'Point(x={0}, y={1})'.format(self.x, self.y)
    
    def clone(self):
        return Point(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def dist(self, other):
        return math.hypot(other.x - self.x, other.y - self.y)

    def dist2(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        return dx * dx + dy * dy
