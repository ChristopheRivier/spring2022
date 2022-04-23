
from position import Position #exclude
import math #exclude
from tokenize import Number #exclude

class Entity:
    pos: Position
    vPos: Position
    id: Number
    _type: Number
    shield: Number
    is_controlled: Number
    health: Number
    near_base: Number
    threat_for: Number
    def __init__(self,_id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for) -> None:
        self.id=_id
        self._type=_type
        self.pos=Position(x,y)
        self.shield=shield_life
        self.is_controlled=is_controlled
        self.health=health
        self.vPos=Position(vx,vy)
        self.near_base=near_base
        self.threat_for=threat_for
    def get_position(self) -> Position:
        return self.pos
    def print(self, d):
        if d:
            print(f'{self.id} {self._type} {self.pos.getX()} {self.pos.getY()} {self.shield} {self.is_controlled} {self.health} {self.vPos.getX()} {self.vPos.getY()} {self.near_base} {self.threat_for}', file=sys.stderr, flush=True)


class Monster(Entity):
    pass

class Hero(Entity):
    #def get_position_initial():
    pass