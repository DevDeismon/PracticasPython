from TheGame.Charcter import Charcter
from TheGame.Skills.Skill import *


class LoboTerrible(Charcter):
    def __init__(self):
        Charcter.__init__(self, "Lobo Terrible", 50, 0, 0, "IA", 3)
        self.setHa(Zarpazo(self.getLvl()))
        self.setHa(Aullido(self.getLvl()))
        self.setHa(Esquiva(self.getLvl()))

    def aullar(self):
        cura = self.getHa()[1].aullido()

        if self.getHp() < 50:
            if (self.getHp() + cura) > 50:
                resto = 50 - self.getHp()
                self.setHP(50)
                return resto
            else:
                self.setHP(self.getHp() + cura)
                return cura
        else:
            return 0
