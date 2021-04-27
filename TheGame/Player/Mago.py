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
        Charcter.__init__(self, name, hp, 0, 20, "PJ", lvl)

        self.setHa(LlamaSagrada(lvl))
        self.setHa(ArmaduradeAgahtis(lvl))
        self.setHa(BoladeFuego(lvl))

    def pullHa(self):
        print("Ataca ", self.getName(), "\n"
                                        "HP actual:", self.getHp(), "\n"
                                                                    "Nivel Actual: ", self.getLvl(), "\n"
                                                                                                     "Puntos Magicos: ",
              self.getPm(), "\n"
                            "Hablidades:\n"
                            "1.",
              self.getHa()[0].getName(),
              "(Coste de Mana:)", self.getHa()[0].getPmCost(), "\n"
                                                               "2.", self.getHa()[1].getName(),
              "(Coste de Mana:)", self.getHa()[1].getPmCost(), "\n"
                                                               "3.", self.getHa()[2].getName(),
              "(Coste de Mana:)", self.getHa()[2].getPmCost())

    def resetHp(self):
        if self.getLvl() == 1:
            self.setHP(9)
        elif self.getLvl() == 2:
            self.setHP(16)
        elif self.getLvl() == 3:
            self.setHP(23)
        else:
            raise ValueError("Nivel introducido no existente")

    def ataqueMagico(self, target, action):
        op = int(action)
        if op == 1:

            esquiva = self.compEsquiva(target)
            if esquiva == 1:
                print("Ataque esquivado!\n")
            else:
                damage = self.getHa()[0].damage()
                target.resthp(damage)
                print(target.getName(), " a recibido ", str(damage), " daño\n")
        elif op == 2 and self.getPm() >= self.getHa()[1].getPmCost():
            self.restPm(1)
            self.getHa()[1].armadura(self)
            print("Armadura magica aplicada. HP actual: ", str(self.getHp()), "\n")
        elif op == 3 and self.getPm() >= self.getHa()[2].getPmCost():
            self.restPm(2)
            esquiva = self.compEsquiva(target)
            if esquiva == 1:
                print("Ataque esquivado!")
            else:
                damage = self.getHa()[2].damage()
                target.resthp(damage)
                print(target.getName(), " a recibido ", str(damage), "daño\n")
        else:
            print("==============================\nNo tienes suficiente puntos Magicos\n==============================")
            self.pullHa()
            op = input("Opcion:")
            self.ataqueMagico(target, op)

    def restPm(self, x):
        self.setPm(self.getPm() - self.getHa()[x].getPmCost())

    def passivDamage(self, target):
        if self.getHa()[1].getDamageOn():
            damage = self.getHa()[1].damage()
            target.resthp(damage)
            print(target.getName(), " a recibido ", str(damage), " daño por armadura magica")
