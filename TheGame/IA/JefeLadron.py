from TheGame.Charcter import Charcter
from TheGame.Skills.Skill import *


class JefeLadron(Charcter):

    def __init__(self):
        Charcter.__init__(self, "Jefe Ladron", 37, 0, 0, "IA", 2)
        self.setHa(Tajo(self.getLvl()))
        self.setHa(Furtivo(self.getLvl()))
        self.setHa(Esquiva(self.getLvl()))
