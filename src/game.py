from multiprocessing.dummy import Array #exclude
from position import Position #exclude
import math #exclude
from tokenize import Number #exclude
from entity import Monster, Hero #exclude

class Health:
    health :Number =0
    mana :Number=0
    def __init__(self, health, mana) -> None:
        self.health=health
        self.mana=mana
    def print(self, d):
        if d:
            print(f'{self.health} {self.mana}', file=sys.stderr, flush=True)

class Game:
    m_health: Health
    e_health: Health
    position_base: Position
    mheros: Array = []
    Eheros: Array = []
    monsters: Array = []

    def __init__(self, base_x, base_y) -> None:
        self.position_base = Position(base_x,base_y)

    def init_round(self):
        self.monsters = []
        self.mheros = []
        self.Eheros = []
    def addEntity(self, _id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for):
        if _type == 0:
            self.monsters.append(Monster(_id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for))
        elif _type == 1:
            self.mheros.append(Hero(_id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for))
        elif _type == 2:
            self.Eheros.append(Hero(_id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for))

    def add_m_health(self, health, mana):
        self.m_health = Health(health, mana)
    def add_e_health(self, health, mana):
        self.e_health = Health(health, mana)
    def get_nearest_monster(self, Hero):
        dist = -1
        ret_monster: Monster = None

        for m in self.monsters:
            dist_courante = m.get_position().distance(self.position_base) 
            if dist==-1 or dist_courante < dist:
                dist = dist_courante
                ret_monster = m
        return ret_monster
    
    def calcul_move(self):
        for h in self.mheros:
            m = self.get_nearest_monster(h)
            if m is None:
                print("WAIT")
            else:
                print("MOVE "+str(m.get_position().getX())+" "+str(m.get_position().getY()))
    def print(self, d):
        self.m_health.print(d)
        self.e_health.print(d)
        if d:
            print(f'{len(self.monsters)+len(self.mheros)+len(self.Eheros)}', file=sys.stderr, flush=True)
            for h in self.mheros:
                h.print(d)
            for e in self.Eheros:
                e.print(d)
            for m in self.monsters:
                m.print(d)
