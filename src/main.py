from multiprocessing.dummy import Array
import sys
import math
from tokenize import Number #exclude
from wsgiref.headers import tspecials #exclude

debug = True

from position import Position

from entity import Entity, Monster, Hero

from aciton import Action 

from game import Game
        
    
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
