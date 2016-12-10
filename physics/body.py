from ..geometry.circle import *

class Body(namedtuple('Body', Circle._fields + ('speed', 'mass'))):
    __slots__ = ()
