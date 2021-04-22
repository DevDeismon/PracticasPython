from TheGame.Charcter import Charcter
from TheGame.Skills.Skill import *


class LoboGigante(Charcter):
    def __init__(self):
        Charcter.__init__(self, "Lobo Terrible", 37, 14, 0, "IA", 3)
        self.setHa(Zarpazo(self.getLvl()))
        self.setHa(Aullido(self.getLvl()))
        self.setHa(Esquiva(self.getLvl()))

    def aullar(self, ally):
        cura = self.getHa()[1].aullido(ally)
        self.setHP(self.getHp() + cura)
        return cura
