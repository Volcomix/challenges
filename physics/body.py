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
    
    def cancel_move(self):
        self.position.x -= self.speed.x
        self.position.y -= self.speed.y

    def thrust(self, angle, value):
        self.angle += angle

        """x = self.angle
        if x < -3.14159265:
            x += 6.28318531
        elif x > 3.14159265:
            x -= 6.28318531

        if x < 0:
            sin = 1.27323954 * x + 0.405284735 * x * x
        else:
            sin = 1.27323954 * x - 0.405284735 * x * x

        x += 1.57079632
        if x >  3.14159265:
            x -= 6.28318531

        if x < 0:
            cos = 1.27323954 * x + 0.405284735 * x * x
        else:
            cos = 1.27323954 * x - 0.405284735 * x * x"""

        self.speed.x += math.cos(self.angle) * value
        self.speed.y += math.sin(self.angle) * value
    
    def friction(self, value):
        self.speed.x *= value
        self.speed.y *= value
    
    def is_on_circle(self, circle):
        if (
            abs(self.position.x - circle.position.x) < circle.radius and
            abs(self.position.y - circle.position.y) < circle.radius
        ):
            return self.position.dist2(circle.position) < circle.radius * circle.radius
        return False
    
    def did_collide(self, other):
        sum_radius = self.radius + other.radius
        if (
            abs(self.position.x - other.position.x) < sum_radius and
            abs(self.position.y - other.position.y) < sum_radius
        ):
            dist2 = self.position.dist2(other.position)
            return dist2 <= sum_radius * sum_radius
        return False
    
    def bounce(self, other):
        n = self.position - other.position
        n.normalize()

        a1 = self.speed.dot(n)
        a2 = other.speed.dot(n)

        optimized_p = 2 * (a1 - a2) / (self.mass + other.mass)
        self.speed -= optimized_p * other.mass * n
        other.speed += optimized_p * self.mass * n

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
