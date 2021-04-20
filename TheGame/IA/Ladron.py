from TheGame.Charcter import Charcter
from TheGame.Skills.Skill import *


class Ladron(Charcter):

    def __init__(self):
        Charcter.__init__(self, "Ladron", 11, 12, 0, "IA", 1)
        self.setHa(Tajo(self.getLvl()))
        self.setHa(Esquiva(self.getLvl()))
        self.setHa(Furtivo(self.getLvl()))
