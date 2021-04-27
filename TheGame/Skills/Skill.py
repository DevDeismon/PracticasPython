from random import *


class Skill:
    # Atributos
    __name = ""
    __desc = ""
    __pMCost = 0
    __damage = 0
    __lvl = 0

    # constructor
    def __init__(self, name, desc, lvl, pM):
        self.__name = name
        self.__desc = desc
        self.__lvl = lvl
        self.__pMCost = pM

    # Getters/Setters

    def getName(self):
        return self.__name

    def getDesc(self):
        return self.__desc

    def getDamage(self):
        return self.__damage

    def getPmCost(self):
        return self.__pMCost

    def setPmCost(self, Y):
        self.__pMCost = Y

    def getLvl(self):
        return self.__lvl

    def setName(self, Y):
        self.__name = Y

    def setDesc(self, Y):
        self.__desc = Y

    def setDamage(self, Y):
        self.__damage = Y

    def setLvl(self, Y):
        self.__lvl = Y

    def probability(self):
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


class Tajo(Skill):
    def __init__(self, lvl):
        Skill.__init__(self, "Tajo", "Corte estandar para atacar al enemigo", lvl, 0)

    def damage(self):
        if self.getLvl() == 1:
            self.setDamage(randint(2, 5))
            return self.getDamage()
        elif self.getLvl() == 2:
            self.setDamage(randint(3, 6))
            return self.getDamage()
        elif self.getLvl() == 3:
            self.setDamage(randint(5, 8))
            return self.getDamage()
        else:
            raise ValueError("Nivel introducido no existente")


class Furtivo(Skill):
    def __init__(self, lvl):
        Skill.__init__(self, "Furtivo", "Puñalada trapera con probabilidad de critico", lvl, 0)

    def damage(self):
        if self.getLvl() == 1:
            # Comprobamos si hay critico.
            if self.probability() == 1:
                print("Critico!")
                self.setDamage(randint(2, 5) + 0.5)
            else:
                self.setDamage(randint(2, 5))
            return self.getDamage()

        elif self.getLvl() == 2:
            if self.probability() == 1:
                print("Critico!")
                self.setDamage(randint(3, 6) + 1)
            else:
                self.setDamage(randint(3, 6))
            return self.getDamage()

        elif self.getLvl() == 3:
            if self.probability() == 1:
                print("Critico!")
                self.setDamage(randint(5, 8) + 1.5)
            else:
                self.setDamage(randint(5, 8))
            return self.getDamage()
        else:
            raise ValueError("Nivel introducido no existente")


class Mordisco(Skill):
    def __init__(self, lvl):
        Skill.__init__(self, "Mordico", "Ataque realizado por un animal para hacer daño", lvl, 0)

    def damage(self):
        if self.getLvl() == 1:
            if self.probability() == 1:
                print("Veneno!")
                self.setDamage(randint(2, 3))
            else:
                self.setDamage(randint(2, 3))
            return self.getDamage()
        elif self.getLvl() == 2:
            if self.probability() == 1:
                print("Veneno!")
                self.setDamage(randint(4, 5))
            else:
                self.setDamage(randint(4, 5))
            return self.getDamage()
        elif self.getLvl() == 3:
            if self.probability() == 1:
                print("Veneno!")
                self.setDamage(randint(6, 7))
            else:
                self.setDamage(randint(6, 7))
            return self.getDamage()
        else:
            raise ValueError("Nivel introducido no existente")


class Zarpazo(Skill):
    def __init__(self, lvl):
        Skill.__init__(self, "Zarpazo", "Ataque realizado por un animal para hacer daño", lvl, 0)

    def damage(self):
        if self.getLvl() == 1:
            self.setDamage(randint(2, 5))
            return self.getDamage()
        elif self.getLvl() == 2:
            self.setDamage(randint(3, 6))
            return self.getDamage()
        elif self.getLvl() == 3:
            self.setDamage(randint(6, 9))
            return self.getDamage()
        else:
            raise ValueError("Nivel introducido no existente")


class Estocada(Skill):
    def __init__(self, lvl):
        Skill.__init__(self, "Estocada", "Ataque en linea recta", lvl, 0)

    def damage(self):
        if self.getLvl() == 1:
            self.setDamage(randint(3, 6))
            return self.getDamage()
        elif self.getLvl() == 2:
            self.setDamage(randint(5, 9))
            return self.getDamage()
        elif self.getLvl() == 3:
            self.setDamage(randint(8, 10))
            return self.getDamage()
        else:
            raise ValueError("Nivel introducido no existente")


class ArmaduradeAgahtis(Skill):
    __isDamage = False

    def __init__(self, lvl):
        Skill.__init__(self, "Armadura de Agahtis", "Armadura magica que umenta la vida y produce daño a los enemigos",
                       lvl, 5)

    def getDamageOn(self):
        return self.__isDamage

    def setDamageOn(self, Y):
        self.__isDamage = Y

    def armadura(self, player):
        if self.getLvl() == 1:
            player.setHP(player.getHp() + 5)
        elif self.getLvl() == 2:
            player.setHP(player.getHp() + 7)
        elif self.getLvl() == 3:
            player.setHP(player.getHp() + 9)
        self.setDamageOn(True)

    def damage(self):
        if self.getLvl() == 1:
            self.setDamage(randint(1, 4))
            return self.getDamage()
        elif self.getLvl() == 2:
            self.setDamage(randint(3, 6))
            return self.getDamage()
        elif self.getLvl() == 3:
            self.setDamage(randint(5, 8))
            return self.getDamage()
        else:
            raise ValueError("Nivel introducido no existente")


class LlamaSagrada(Skill):
    def __init__(self, lvl):
        Skill.__init__(self, "Llama Sagrada", "Ataque incenciario", lvl, 0)

    def damage(self):
        if self.getLvl() == 1:
            self.setDamage(randint(3, 6))
            return self.getDamage()
        elif self.getLvl() == 2:
            self.setDamage(randint(5, 8))
            return self.getDamage()
        elif self.getLvl() == 3:
            self.setDamage(randint(7, 10))
            return self.getDamage()
        else:
            raise ValueError("Nivel introducido no existente")


class BoladeFuego(Skill):
    def __init__(self, lvl):
        Skill.__init__(self, "Bola de fuego", "Ataque incendiario que hace mucho daño", lvl, 15)

    def damage(self):
        if self.getLvl() == 1:
            self.setDamage(randint(5, 8))
            return self.getDamage()
        elif self.getLvl() == 2:
            self.setDamage(randint(7, 10))
            return self.getDamage()
        elif self.getLvl() == 3:
            self.setDamage(randint(9, 12))
            return self.getDamage()
        else:
            raise ValueError("Nivel introducido no existente")


class Esquiva(Skill):
    def __init__(self, lvl):
        Skill.__init__(self, "Esquiva", "Probabilidad de evitar el daño", lvl, 0)

    def __probability(self, chracter):
        if chracter.getType() == "IA":
            if self.getLvl() == 1:
                self.r = uniform(0, 1)
                if self.r <= 0.85:
                    return 0
                elif self.r >= 0.86:
                    return 1
            elif self.getLvl() == 2:
                self.r = uniform(0, 1)
                if self.r <= 0.70:
                    return 0
                elif self.r >= 0.71:
                    return 1
            elif self.getLvl() == 3:
                self.r = uniform(0, 1)
                if self.r <= 0.44:
                    return 0
                elif self.r >= 0.45:
                    return 1
            else:
                raise ValueError("Nivel introducido no existente")
        else:
            if self.getLvl() == 1:
                self.r = uniform(0, 1)
                if self.r <= 0.75:
                    return 0
                elif self.r >= 0.76:
                    return 1
            elif self.getLvl() == 2:
                self.r = uniform(0, 1)
                if self.r <= 0.50:
                    return 0
                elif self.r >= 0.51:
                    return 1
            elif self.getLvl() == 3:
                self.r = uniform(0, 1)
                if self.r <= 0.24:
                    return 0
                elif self.r >= 0.25:
                    return 1
            else:
                raise ValueError("Nivel introducido no existente")

    def esquivar(self, character):
        self.esquiva = self.__probability(character)
        return self.esquiva


class Aullido(Skill):
    def __init__(self, lvl):
        Skill.__init__(self, "Aullido", "Habildad usada para curarse", lvl, 0)

    def aullido(self):
        if self.getLvl() == 1:
            return 2
        elif self.getLvl() == 2:
            return 3
        elif self.getLvl() == 3:
            return 5
        else:
            raise ValueError("Nivel introducido no existente")


class Escudo(Skill):
    def __init__(self, lvl):
        Skill.__init__(self, "Escudo", "Aumenta ligeramente la Ca", lvl, 0)

    def escudo(self):
        if self.getLvl() == 1:
            return 1
        elif self.getLvl() == 2:
            return 2
        elif self.getLvl() == 3:
            return 3
        else:
            raise ValueError("Nivel introducido no existente")
