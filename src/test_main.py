import pytest
from entity import Hero, position_deplacement
from position import Position


def test_position_hero():
    h = Hero(0, 
            1, 
            0, 
            0, 
            0, 0
            , 0, -1, -1, -1, -1)
    assert h.get_fact_pos_x()==3
    assert h.get_fact_pos_y()==1
    h = Hero(1, 
            1, 
            0, 
            0, 
            0, 0
            , 0, -1, -1, -1, -1)
    assert h.get_fact_pos_x()==2
    assert h.get_fact_pos_y()==2


def test_position_base_hero():
    h = Hero(0, 
            1, 
            0, 
            0, 
            0, 0
            , 0, -1, -1, -1, -1)
    h.set_pos_base(Position(0,0))
    assert h.base_pos.getX()==position_deplacement
    assert h.base_pos.getY()==int(position_deplacement/3)

    h.set_pos_base(Position(17630, 9000))
    assert h.base_pos.getX()==(17630 - position_deplacement)
    assert h.base_pos.getY()==(9000 - int(position_deplacement/3))

    h = Hero(1, 
            1, 
            0, 
            0, 
            0, 0
            , 0, -1, -1, -1, -1)
    h.set_pos_base(Position(0,0))
    assert h.base_pos.getX()==int(position_deplacement*2/3)
    assert h.base_pos.getY()==int(position_deplacement*2/3)



