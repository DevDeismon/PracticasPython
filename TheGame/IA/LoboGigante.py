from TheGame.Charcter import Charcter
from TheGame.Skills.Skill import *


class LoboGigante(Charcter):
    def __init__(self):
        Charcter.__init__(self, "Lobo Gigante", 37, 0, 0, "IA", 2)
        self.setHa(Zarpazo(self.getLvl()))
        self.setHa(Aullido(self.getLvl()))
        self.setHa(Esquiva(self.getLvl()))

    def aullar(self):
        cura = self.getHa()[1].aullido()

        if self.getHp() < 37:
            if (self.getHp() + cura) > 37:
                resto = 37 - self.getHp()
                self.setHP(37)
                return resto
            else:
                self.setHP(self.getHp() + cura)
                return cura
        else:
            return 0
