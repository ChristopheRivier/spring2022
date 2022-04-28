
from audioop import reverse
from distutils.log import debug
import sys #exclude
from multiprocessing.dummy import Array #exclude
from position import Position #exclude
import math #exclude
from tokenize import Number #exclude
from entity import Monster, Hero #exclude
from aciton import Action #exclude

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
    def get_nearest_monster(self, hero, lst_monster):
        dist = -1
        ret_monster: Monster = None
        for m in lst_monster:
            dist_courante = m.get_position().distance(hero.pos) 
            if dist==-1 or dist_courante < dist:
                if m.threat_for==1:
                    dist = dist_courante
                    ret_monster = m
        return ret_monster

    def get_nearest_hero(self, monster, lst_hero, lst_act):
        dist = -1
        ret_hero: Monster = None
        for h in lst_hero:
            if lst_act[h.id%3] is not None:
                continue
            dist_courante = h.get_position().distance(monster.pos) 
            if dist==-1 or dist_courante < dist:
                dist = dist_courante
                ret_hero = h
        return ret_hero

    def calcul_move(self):
        act:Array=[]
        act1=None
        monster_in_base = 0
        hero_attack = self.mheros[0]
        action=0
        # by default define action move default
        for h in self.mheros:
            act.append(None)
        
        for m in self.monsters:
            dist_base=m.get_position().distance(self.position_base)
            m.dist_suppress = dist_base/400
            m.dist_base = dist_base
            dist_h=m.get_position().distance(hero_attack.pos)
            if monster_in_base<5000:
                monster_in_base+=1
            if action == 0 and dist_h<1280 and  m.dist_base<5000:
                act1 = Action(self.get_position_base_ennemi(),"WIND", m.id)
                action =1
                m.add_ponderation(100000)
            elif action == 0 and dist_h<2200 and m.dist_base>5000 and m.threat_for!=2:
                act1 = Action(self.get_position_base_ennemi(),"CONTROL", m.id)
                action =1
                m.add_ponderation(100000)
                
            if m.threat_for==1:
                m.add_ponderation(dist_base*pond_base)
            else:
                m.add_ponderation(dist_base*pond_base_not_target)

        # in case lot of mana, one hero goes to the middle
        all_hero = 3
    
        if self.m_health.mana>50:
            if act1 is None and monster_in_base<3:
                act1 = Action(self.get_position_base_ennemi(),"MOVE", 0)
        else:
            act1=None

        if act1 is not None :
            act[0] = act1
            all_hero=2

        def customSort(k):
            return k.ponderation
        self.monsters.sort(key=customSort)

        for m in self.monsters[0:3]:
            ret_monster = None
            h = self.get_nearest_hero(m, self.mheros[3-all_hero:3], act)
            if h is None:
                continue
            dist_courante = m.get_position().distance(h.pos) 
            # can we attack it
            if m.health>0:
                attack = 0
                if dist_courante<800:
                    m.health-=2
                else:
                    attack = dist_courante/800
                # take a little margin instead of 800 take 1000
                if m.dist_base<1000 and dist_courante<1280:
                    # pchit
                    act[h.id%3] = Action(self.get_position_base_ennemi(),"WIND",0, "Pchit")
                elif m.dist_base<10000:
                    m.health -= (m.dist_suppress-attack)/2
                    ret_monster = m
                    if act[h.id%3] is None:
                        act[h.id%3] = Action(ret_monster.get_position(),"MOVE",0)
        # by default define action move default
        for h in self.mheros:
            if act[h.id%3] is None:
                act[h.id%3] = Action(h.base_pos,"MOVE",0)

        for a in act:
            a.print()

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
