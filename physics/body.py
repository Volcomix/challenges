import math
from collections import namedtuple

from ..geometry.circle import *
from entities.checkpoint import *

class Body(Circle):
    def __init__(self, position, radius, speed, mass):
        super().__init__(position, radius)
        self.speed = speed
        self.mass = mass

    def move(self):
        self.position.x += self.speed.x
        self.position.y += self.speed.y

    def thrust(self, angle, value):
        self.angle += angle
        self.speed.x += math.cos(self.angle) * value
        self.speed.y += math.sin(self.angle) * value
    
    def friction(self, value):
        self.speed.x *= value
        self.speed.y *= value

    def will_collide_circle(self, circle):
        dist = self.position.dist(circle.position)
        sum_radii = self.radius + circle.radius
        dist -= sum_radii
        if self.speed.length < dist:
            return False
        
        N = self.speed.norm()
        C = circle.position - self.position
        D = N.dot(C)

        if D <= 0:
            return False
        
        length_c = C.length
        F = length_c * length_c - D * D

        sum_radii_squared = sum_radii * sum_radii
        if F >= sum_radii_squared:
            return False
        
        T = sum_radii_squared - F

        if T < 0:
            return False
        
        distance = D - math.sqrt(T)
        mag = self.speed.length

        if mag < distance:
            return False
        
        return True

    def will_reach_circle(self, circle):
        dist = self.position.dist(circle.position)
        dist -= circle.radius
        if self.speed.length < dist:
            return False
        
        N = self.speed.norm()
        C = circle.position - self.position
        D = N.dot(C)

        if D <= 0:
            return False
        
        length_c = C.length
        F = length_c * length_c - D * D

        radius_squared = circle.radius * circle.radius
        if F >= radius_squared:
            return False
        
        T = radius_squared - F

        if T < 0:
            return False
        
        distance = D - math.sqrt(T)
        mag = self.speed.length

        if mag < distance:
            return False
        
        return True
