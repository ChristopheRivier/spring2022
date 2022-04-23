from multiprocessing.dummy import Array
import sys
import math
from tokenize import Number #exclude
from wsgiref.headers import tspecials #exclude

debug = True

#--------------------- BEGIN position

class Position:
    x: Number
    y: Number
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distance(self, pos2):
        return math.sqrt((self.x-pos2.getX())**2+(self.y-pos2.getY())**2)
#--------------------- END position

#--------------------- BEGIN entity


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
    pass#--------------------- END entity

#--------------------- BEGIN game

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
#--------------------- END game
        
    
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# base_x: The corner of the map representing your base
base_x, base_y = [int(i) for i in input().split()]
if debug:
    print(f"{base_x} {base_y}", file=sys.stderr, flush=True)
heroes_per_player = int(input())  # Always 3
if debug:
    print(f"{heroes_per_player}", file=sys.stderr, flush=True)
game = Game(base_x, base_y)

# game loop
while True:
    game.init_round()
    for i in range(2):
        # health: Each player's base health
        # mana: Ignore in the first league; Spend ten mana to cast a spell
        health, mana = [int(j) for j in input().split()]
        if i==0:
            game.add_m_health(health, mana)
        else:
            game.add_e_health(health, mana)

    entity_count = int(input())  # Amount of heros and monsters you can see
    for i in range(entity_count):
        # _id: Unique identifier
        # _type: 0=monster, 1=your hero, 2=opponent hero
        # x: Position of this entity
        # shield_life: Ignore for this league; Count down until shield spell fades
        # is_controlled: Ignore for this league; Equals 1 when this entity is under a control spell
        # health: Remaining health of this monster
        # vx: Trajectory of this monster
        # near_base: 0=monster with no target yet, 1=monster targeting a base
        # threat_for: Given this monster's trajectory, is it a threat to 1=your base, 2=your opponent's base, 0=neither
        _id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for = [int(j) for j in input().split()]
        game.addEntity(_id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for)
    game.print(debug)
    game.calcul_move()

#    for i in range(heroes_per_player):

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)


        # In the first league: MOVE <x> <y> | WAIT; In later leagues: | SPELL <spellParams>;
 #       print("WAIT")
