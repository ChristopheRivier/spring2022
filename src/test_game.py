import pytest

from entity import Hero, position_deplacement
from position import Position
from game import Game

def test_game():
    game = Game(0, 0)
    game.init_round()

    game.add_m_health(3, 0)
    game.add_e_health(3, 0)
    # hero
    game.addEntity(0, 1, 5917, 2473, 0, 0, -1, -1, -1, -1, -1)
    game.addEntity(1, 1, 5670, 2458, 0, 0, -1, -1, -1, -1, -1)
    game.addEntity(2, 1, 4812, 2755, 0, 0, -1, -1, -1, -1, -1)
    
    # monster
    game.addEntity(35, 0, 3250, 2526, 0, 0, 13, -315, -245, 1, 1)
    game.addEntity(36, 0, 5455, 4675, 0, 0, 3, -320, 238, 0, 0)
    game.addEntity(41, 0, 6201, 2743, 0, 0, 12, 77, -392, 0, 0)
    game.addEntity(45, 0, 1513, 5795, 0, 0, 14, -254, -308, 0, 1)


    game.calcul_move()

def test_begin():
    game = Game(0, 0)
    game.init_round()

    game.add_m_health(3, 0)
    game.add_e_health(3, 0)

    game.addEntity(0, 1, 1131, 1131, 0, 0, -1, -1, -1, -1, -1)
    game.addEntity(1, 1, 1414, 849, 0, 0, -1, -1, -1, -1, -1)
    game.addEntity(2, 1, 849, 1414, 0, 0, -1, -1, -1, -1, -1)
    game.calcul_move()

def test_defense():
    game = Game(0, 0)
    game.init_round()

    game.add_m_health(3, 62)
    game.add_e_health(3, 396)

    
    game.addEntity(0, 1, 6300, 2100, 0, 0, -1, -1, -1, -1, -1)
    game.addEntity(1, 1, 1316, 1068, 0, 0, -1, -1, -1, -1, -1)
    game.addEntity(2, 1, 4357, 5426, 0, 0, -1, -1, -1, -1, -1)
    game.addEntity(5, 2, 5765, 5919, 0, 0, -1, -1, -1, -1, -1)
    game.addEntity(47, 0, 1006, 816, 0, 0, 3, -310, -251, 1, 1)
    game.addEntity(54, 0, 1595, 529, 0, 0, 12, -379, -125, 1, 1)
    game.addEntity(60, 0, 7490, 1946, 0, 0, 16, -355, 183, 0, 0)
    game.addEntity(62, 0, 7555, 2991, 0, 0, 17, -126, 379, 0, 0)
    game.addEntity(65, 0, 5765, 5919, 0, 0, 15, 95, -388, 0, 0)
    game.calcul_move()
