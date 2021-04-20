from TheGame.Charcter import Charcter
from TheGame.Skills.Skill import *


class Picaro(Charcter):

    def __init__(self, name, lvl):
        if lvl == 1:
            hp = 11
        elif lvl == 2:
            hp = 19
        elif lvl == 3:
            hp = 27
        else:
            raise ValueError("Nivel introducido no existente")
        Charcter.__init__(self, name, hp, 12, 0, "PJ", lvl)
        self.setHa(Tajo(lvl))
        self.setHa(Esquiva(lvl))
        self.setHa(Furtivo(lvl))
