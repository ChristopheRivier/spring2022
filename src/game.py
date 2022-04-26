
from audioop import reverse
from distutils.log import debug
import sys #exclude
from multiprocessing.dummy import Array #exclude
from position import Position #exclude
import math #exclude
from tokenize import Number #exclude
from entity import Monster, Hero #exclude

pond_base = 0.8
pond_base_not_target=1.2

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
            h = Hero(_id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for)
            h.set_pos_base(self.position_base)
            self.mheros.append(h)
        elif _type == 2:
            self.Eheros.append(Hero(_id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for))

    def get_position_base_ennemi(self):
        if self.position_base.getX()==0:
            return Position(17630, 9000)
        else:
            return Position(0, 0)

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
                if m.threat_for==1:
                    dist = dist_courante
                    ret_monster = m
        return ret_monster
    
    def calcul_move(self):

        # in case lot of mana, one hero goes to the middle
        all_hero = 3
        if self.m_health.mana>50:
            all_hero = 2
            hero_attack = self.mheros[0]
            action=0

            for m in self.monsters:
                dist_h=m.get_position().distance(hero_attack.pos)
                if dist_h<2200:
                    print(f'SPELL CONTROL {m.id} {self.get_position_base_ennemi().getX()} {self.get_position_base_ennemi().getY()}')
                    action =1
                    m.add_ponderation(100000)
                    break
            if action==0:
                print(f'MOVE {int(17630/2)} {int(9000/2)}')

        # ponderation for all known monster
        for m in self.monsters:
            # to my base
            dist_base=m.get_position().distance(self.position_base)
            m.dist_suppress = dist_base/400
            m.dist_base = dist_base
            if m.threat_for==1:
                m.add_ponderation(dist_base*pond_base)
            else:
                m.add_ponderation(dist_base*pond_base_not_target)
            m.print(debug)

        def customSort(k):
            return k.ponderation
        self.monsters.sort(key=customSort)

            
        for h in self.mheros[3-all_hero:3]:
            dist = -1
            ret_monster: Monster = None
            for m in self.monsters[0:3]:
                dist_courante = m.get_position().distance(h.pos) 
                # can we attack it
                if m.health>0:
                    attack = 0
                    if dist_courante<800:
                        m.health-=2
                    else:
                        attack = dist_courante/800
                    if m.dist_base>10000:
                        ret_monster=None
                    else:
                        m.health -= (m.dist_suppress-attack)/2
                        ret_monster = m
                        break
                    
            
            if ret_monster is None:
                print(f'MOVE {h.base_pos.getX()} {h.base_pos.getY()}')
            else:
                print(f"MOVE {ret_monster.get_position().getX()} {ret_monster.get_position().getY()}")
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
