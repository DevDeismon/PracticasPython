from TheGame.Charcter import Charcter
from TheGame.Skills.Skill import *


class RataGigante(Charcter):
    def __init__(self):
        Charcter.__init__(self, "Rata Gigante", 10, 12, 0, "IA", 1)
        self.setHa(Esquiva(self.getLvl()))
        self.setHa(Mordisco(self.getLvl()))
        self.setHa(Zarpazo(self.getLvl()))