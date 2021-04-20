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
        Charcter.__init__(self, name, hp, 16, 0, "PJ", lvl)
        self.setHa(Tajo(lvl))
        self.setHa(Escudo(lvl))
        self.setHa(Estocada(lvl))
