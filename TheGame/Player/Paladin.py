from TheGame.Charcter import Charcter
from TheGame.Skills.Skill import *


class Paladin(Charcter):

    def __init__(self, name, lvl):
        Charcter.__init__(self, name, 15, 2, 0, "PJ", lvl)
        self.setHa(Tajo(lvl))
        self.setHa(Estocada(lvl))
        self.setHa(Escudo(lvl))

    def resetHp(self):
        if self.getLvl() == 1:
            self.setHP(15)
        elif self.getLvl() == 2:
            self.setHP(25)
        elif self.getLvl() == 3:
            self.setHP(35)
        else:
            raise ValueError("Nivel introducido no existente")
        self.cubrir()

    def cubrir(self):
        self.setCa(2 + self.getHa()[2].escudo())
