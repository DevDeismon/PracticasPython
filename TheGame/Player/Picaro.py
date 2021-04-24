from TheGame.Charcter import Charcter
from TheGame.Skills.Skill import *


class Picaro(Charcter):
    def __init__(self, name, lvl):
        if lvl == 1:
            hp = 15
        elif lvl == 2:
            hp = 19
        elif lvl == 3:
            hp = 29
        else:
            raise ValueError("Nivel introducido no existente")
        Charcter.__init__(self, name, hp, 2, 0, "PJ", lvl)
        self.setHa(Tajo(lvl))
        self.setHa(Furtivo(lvl))
        self.setHa(Esquiva(lvl))

    def resetHp(self):
        if self.getLvl() == 1:
            self.setHP(11)
        elif self.getLvl() == 2:
            self.setHP(19)
        elif self.getLvl() == 3:
            self.setHP(27)
        else:
            raise ValueError("Nivel introducido no existente")
