from TheGame.Charcter import Charcter
from TheGame.Skills.Skill import *


class Lobo(Charcter):
    def __init__(self):
        Charcter.__init__(self, "Lobo", 11, 13, 0, "IA", 1)
        self.setHa(Zarpazo(self.getLvl()))
        self.setHa(Esquiva(self.getLvl()))
        self.setHa(Aullido(self.getLvl()))

    def aullar(self, ally):
        self.setHP(self.getHp() + self.getHa()[2].aullido(ally))
