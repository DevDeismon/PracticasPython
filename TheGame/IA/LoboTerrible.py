from TheGame.Charcter import Charcter
from TheGame.Skills.Skill import *


class LoboGigante(Charcter):
    def __init__(self):
        Charcter.__init__(self, "Lobo Terrible", 37, 14, 0, "IA", 3)
        self.setHa(Zarpazo(self.getLvl()))
        self.setHa(Esquiva(self.getLvl()))
        self.setHa(Aullido(self.getLvl()))

    def aullar(self, ally):
        self.setHP(self.getHp() + self.getHa()[2].aullido(ally))
