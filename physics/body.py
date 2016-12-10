from ..geometry.circle import *
from ..geometry.vector import *

class Body(Circle):
    def __init__(self, x, y, vx, vy, radius, mass):
        super().__init__(x, y, radius)
        self.speed = Vector(vx, vy)
        self.mass = mass
