from TheGame.Charcter import Charcter
from TheGame.Skills.Skill import *


class Mago(Charcter):

    def __init__(self, name, lvl):
        if lvl == 1:
            hp = 9
        elif lvl == 2:
            hp = 16
        elif lvl == 3:
            hp = 23
        else:
            raise ValueError("Nivel introducido no existente")
        Charcter.__init__(self, name, hp, 10, 0, "PJ", lvl)
        self.setHa(ArmaduradeAgahtis(lvl))
        self.setHa(LlamaSagrada(lvl))
        self.setHa(BoladeFuego(lvl))
