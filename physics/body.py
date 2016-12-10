from ..geometry.circle import *

class Body(namedtuple('Body', Circle._fields + ('speed', 'mass'))):
    __slots__ = ()

    def move(self):
        return self._replace(position=self.position + self.speed)

    def thrust(self, acceleration):
        return self._replace(speed=self.speed + acceleration)

    def friction(self, value):
        return self._replace(speed=self.speed * value)
