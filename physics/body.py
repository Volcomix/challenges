from ..geometry.circle import *

class Body(namedtuple('Body', Circle._fields + ('speed', 'mass'))):
    __slots__ = ()

    def move(self):
        return self._replace(position=self.position + self.speed)
