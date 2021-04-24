from TheGame.Charcter import Charcter
from TheGame.Skills.Skill import *


class Lobo(Charcter):
    def __init__(self):
        Charcter.__init__(self, "Lobo", 11, 0, 0, "IA", 1)
        self.setHa(Zarpazo(self.getLvl()))
        self.setHa(Aullido(self.getLvl()))
        self.setHa(Esquiva(self.getLvl()))

    def aullar(self):
        cura = self.getHa()[1].aullido()

        if self.getHp() < 11:
            if (self.getHp() + cura) > 11:
                resto = 11 - self.getHp()
                self.setHP(11)
                return resto
            else:
                self.setHP(self.getHp() + cura)
                return cura
        else:
            return 0
