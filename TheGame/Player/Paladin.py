from TheGame.Charcter import Charcter
from TheGame.Skills.Skill import *


class Paladin(Charcter):

    def __init__(self, name, lvl):
        if lvl == 1:
            hp = 13
        elif lvl == 2:
            hp = 22
        elif lvl == 3:
            hp = 31
        else:
            raise ValueError("Nivel introducido no existente")
        Charcter.__init__(self, name, hp, 2, 0, "PJ", lvl)
        self.setHa(Tajo(lvl))
        self.setHa(Estocada(lvl))
        self.setHa(Escudo(lvl))

    def resetHp(self):
        if self.getLvl() == 1:
            self.setHP(13)
        elif self.getLvl() == 2:
            self.setHP(22)
        elif self.getLvl() == 3:
            self.setHP(31)
        else:
            raise ValueError("Nivel introducido no existente")
        self.cubrir()

    def cubrir(self):
        self.setCa(2 + self.getHa()[2].escudo())
