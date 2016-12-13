from collections import namedtuple

from ..geometry.circle import *

class Body(namedtuple('Body', Circle._fields + ('speed', 'mass'))):
    __slots__ = ()

    def move(self):
        return self._replace(position=self.position + self.speed)

    def thrust(self, acceleration):
        return self._replace(speed=self.speed + acceleration)

    def friction(self, value):
        return self._replace(speed=self.speed * value)
    
    def will_collide_circle(self, circle):
        dist = self.position.dist(circle.position)
        sumRadii = self.radius + circle.radius
        dist -= sumRadii
        if self.speed.length < dist:
            return False
        
        N = self.speed.norm()
        C = circle.position - self.position
        D = N.dot(C)

        if D <= 0:
            return False
        
        lengthC = C.length
        F = lengthC * lengthC - D * D

        sumRadiiSquared = sumRadii * sumRadii
        if F >= sumRadiiSquared:
            return False
        
        T = sumRadiiSquared - F

        if T < 0:
            return False
        
        distance = D - math.sqrt(T)
        mag = self.speed.length

        if mag < distance:
            return False
        
        return True
