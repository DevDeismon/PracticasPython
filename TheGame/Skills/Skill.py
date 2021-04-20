from random import *


class Skill:
    # Atributos
    __name = ""
    __desc = ""
    __pMCost = 0
    __cooldown = 0
    __damage = 0
    __lvl = 0

    # constructor
    def __init__(self, name, desc, lvl, Pm, coolDown):
        self.__name = name
        self.__desc = desc
        self.__lvl = lvl
        self.__cooldown = coolDown
        self.__pMCost = Pm

    # Getters/Setters
    def getName(self):
        return self.__name

    def getDesc(self):
        return self.__desc

    def getDamage(self):
        return self.__damage

    def getCooldown(self):
        return self.__cooldown

    def getPmCost(self):
        return self.__pMCost

    def getLvl(self):
        return self.__lvl

    def setName(self, Y):
        self.__name = Y

    def setDesc(self, Y):
        self.__desc = Y

    def setDamage(self, Y):
        self.__damage = Y

    def setCooldown(self, Y):
        self.__cooldown = Y


class Tajo(Skill):
    def __init__(self, lvl):
        Skill.__init__(self, "Tajo", "Corte estandar para atacar al enemigo", lvl, 0, 1)

    def damage(self):
        if self.getLvl() == 1:
            self.setDamage(randint(2, 5))
            return self.getDamage()
        elif self.getLvl() == 2:
            self.setDamage(randint(3, 6))
            return self.getDamage()
        elif self.getLvl() == 3:
            self.setDamage(randint(4, 7))
            return self.getDamage()
        else:
            raise ValueError("Nivel introducido no existente")


class Esquiva(Skill):
    def __init__(self, lvl):
        Skill.__init__(self, "Esquiva", "Probabilidad de evitar el daño", lvl, 0, 0)

    def esquivar(self):
        if self.getLvl() == 1:
            r = uniform(0, 1)
            if r <= 0.75:
                return 0
            elif r >= 0.76:
                return 1
        elif self.getLvl() == 2:
            r = uniform(0, 1)
            if r <= 0.50:
                return 0
            elif r >= 0.51:
                return 1
        elif self.getLvl() == 3:
            r = uniform(0, 1)
            if r <= 0.24:
                return 0
            elif r >= 0.25:
                return 1
        else:
            raise ValueError("Nivel introducido no existente")


class Furtivo(Skill):
    def __init__(self, lvl):
        Skill.__init__(self, "Furtivo", "Puñalada trapera con probabilidad de critico", lvl, 0, 2)

    def furtivo(self):
        if self.getLvl() == 1:
            self.setDamage(randint(3, 6))
            r = uniform(0, 1)
            if r <= 0.75:
                return 0
            elif r >= 0.76:
                return 1
        elif self.getLvl() == 2:
            self.setDamage(randint(4, 7))
            r = uniform(0, 1)
            if r <= 0.50:
                return 0
            elif r >= 0.51:
                return 1
        elif self.getLvl() == 3:
            self.setDamage(randint(5, 8))
            r = uniform(0, 1)
            if r <= 0.24:
                return 0
            elif r >= 0.25:
                return 1
        else:
            raise ValueError("Nivel introducido no existente")


class Mordisco(Skill):
    def __init__(self, lvl):
        Skill.__init__(self, "Mordico", "Ataque realizado por un animal para hacer daño", lvl, 0, 1)

    def mordisco(self):
        if self.getLvl() == 1:
            self.setDamage(randint(2, 3))
            r = uniform(0, 1)
            if r <= 0.75:
                return 0
            elif r >= 0.76:
                return 1
        elif self.getLvl() == 2:
            self.setDamage(randint(4, 5))
            r = uniform(0, 1)
            if r <= 0.50:
                return 0
            elif r >= 0.51:
                return 1
        elif self.getLvl() == 3:
            self.setDamage(randint(6, 7))
            r = uniform(0, 1)
            if r <= 0.24:
                return 0
            elif r >= 0.25:
                return 1
        else:
            raise ValueError("Nivel introducido no existente")


class Zarpazo(Skill):
    def __init__(self, lvl):
        Skill.__init__(self, "Zarpazo", "Ataque realizado por un animal para hacer daño", lvl, 0, 1)

    def zarpazo(self):
        if self.getLvl() == 1:
            self.setDamage(randint(4, 5))
            return self.getDamage()
        elif self.getLvl() == 2:
            self.setDamage(randint(6, 7))
            return self.getDamage()
        elif self.getLvl() == 3:
            self.setDamage(randint(8, 9))
            return self.getDamage()
        else:
            raise ValueError("Nivel introducido no existente")


class Aullido(Skill):
    def __init__(self, lvl):
        Skill.__init__(self, "Aullido", "Habildad usada para curarse", lvl, 0, 0)

    def aullido(self, ally):
        if self.getLvl() == 1:
            return 1 + ally
        elif self.getLvl() == 2:
            return 2 + ally
        elif self.getLvl() == 3:
            return 3 + ally
        else:
            raise ValueError("Nivel introducido no existente")


class Escudo(Skill):
    def __init__(self, lvl):
        Skill.__init__(self, "Escudo", "Aumenta ligeramente la Ca", lvl, 0, 0)

    def escudo(self):
        if self.getLvl() == 1:
            return 1
        elif self.getLvl() == 2:
            return 2
        elif self.getLvl() == 3:
            return 3
        else:
            raise ValueError("Nivel introducido no existente")


class Estocada(Skill):
    def __init__(self, lvl):
        Skill.__init__(self, "Estocada", "Ataque en linea recta", lvl, 0, 2)

    def estocada(self):
        if self.getLvl() == 1:
            self.setDamage(randint(2, 9))
            return self.getDamage()
        elif self.getLvl() == 2:
            self.setDamage(randint(3, 10))
            return self.getDamage()
        elif self.getLvl() == 3:
            self.setDamage(randint(4, 11))
            return self.getDamage()
        else:
            raise ValueError("Nivel introducido no existente")


class ArmaduradeAgahtis(Skill):
    def __init__(self, lvl):
        Skill.__init__(self, "Armadura de Agahtis", "Armadura magica que umenta la vida y produce daño a los enemigos",
                       lvl, 5, 1)

    def armadura(self):
        print("")


class LlamaSagrada(Skill):
    def __init__(self, lvl):
        Skill.__init__(self, "Llama Sagrada", "Ataque incenciario", lvl, 5, 0)


class BoladeFuego(Skill):
    def __init__(self, lvl):
        Skill.__init__(self, "Bola de fuego", "Ataque incendiario que hace mucho daño", lvl, 15, 0)
