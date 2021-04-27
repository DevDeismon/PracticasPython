from TheGame.Charcter import *
from TheGame.Skills.Skill import *


class Asesino(Charcter):

    def __init__(self):
        Charcter.__init__(self, "Asesino", 55, 0, 0, "IA", 3)
        self.setHa(Tajo(self.getLvl()))
        self.setHa(Furtivo(self.getLvl()))
        self.setHa(Esquiva(self.getLvl()))
