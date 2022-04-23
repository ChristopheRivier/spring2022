import math #exclude
from tokenize import Number #exclude

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
