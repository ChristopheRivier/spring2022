import sys
from position import Position #exclude
import math #exclude
from tokenize import Number #exclude

position_deplacement = 6300

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
            print(f'game.addEntity({self.id}, {self._type}, {self.pos.getX()}, {self.pos.getY()}, {self.shield}, {self.is_controlled}, {self.health}, {self.vPos.getX()}, {self.vPos.getY()}, {self.near_base}, {self.threat_for})', file=sys.stderr, flush=True)


class Monster(Entity):
    ponderation: Number
    dist_suppress: Number
    dist_base: Number
    def __init__(self,_id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for) -> None:
        Entity.__init__(self, _id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for)
        self.ponderation=0
        self.dist_suppress=0
        self.dist_base=-1
    def init_pond(self):
        self.ponderation
    def add_ponderation(self, pond: Number):
        self.ponderation+=pond
    def print(self, d):
        super().print(d)
        if d:
            print(f' M {self.id} {self.ponderation} {self.dist_suppress} {self.dist_base}'
                , file=sys.stderr, flush=True)
            


class Hero(Entity):
    base_pos: Position
    def get_fact_pos_x(self):
        return 3-(self.id%3)
    def get_fact_pos_y(self):
        return 1+(self.id%3)
    
    def set_pos_base(self, position_base):
        facteur=-1
        if position_base.getX()==0:
            facteur = 1
        self.base_pos = Position(position_base.getX()+ int(facteur*position_deplacement*self.get_fact_pos_x()/3),
                                 position_base.getY()+int(facteur*position_deplacement*self.get_fact_pos_y()/3))
