class Charcter(object):
    # Atributos
    __tl = 0
    __name = ""
    __type = ""
    __hp = 0
    __ca = 0
    __pm = 0
    __ha = list()
    __lvl = 0
    __timeoff = False

    # Constructor
    def __init__(self, name, hp, ca, pm, t, lvl):
        self.__name = name
        self.__hp = hp
        self.__ca = ca
        self.__pm = pm
        self.__type = t
        self.__ha = list()
        self.__lvl = lvl

    # Getters/Stters
    def getName(self):
        return self.__name

    def getHp(self):
        return self.__hp

    def getCa(self):
        return self.__ca

    def getPm(self):
        return self.__pm

    def getHa(self):
        return self.__ha

    def getLvl(self):
        return self.__lvl

    def getTimeOff(self):
        return self.__timeoff

    def getType(self):
        return self.__type

    def getTiempoLimite(self):
        return self.__tl

    def setTimeOff(self, Y):
        self.__timeoff = Y

    def setLvl(self, Y):
        self.__lvl = Y

    def setName(self, Y):
        self.__name = Y

    def setHP(self, Y):
        self.__hp = Y

    def setCa(self, Y):
        self.__ca = Y

    def setPm(self, Y):
        self.__pm = Y

    def setHa(self, Y):
        self.__ha.append(Y)

    def setType(self, Y):
        self.__type = Y

    # Other Methods
    def resthp(self, damage):
        self.setHP(self.getHp() - damage)

    def ataque(self, attacked, action):
        op = int(action)
        esquiva = self.__compEsquiva(attacked)
        if op == 1:
            if esquiva == 0:
                if attacked.getType() == "PJ":
                    damage = self.getHa()[0].damage() - attacked.getCa()
                    if damage < 0:
                        damage = 0
                    attacked.resthp(damage)
                    print("-----------------------------------\n", attacked.getName(), " a recibido ", str(damage),
                          " daño reducido por la CA")
                else:
                    damage = self.getHa()[0].damage()
                    attacked.resthp(damage)
                    print("-----------------------------------\n", attacked.getName(), " a recibido ", str(damage),
                          " daño")
            elif esquiva == 1:
                print("-----------------------------------\nAtque esquivado!")
        elif op == 2:
            if esquiva == 0:
                if self.getName() == "Lobo" or self.getName() == "Lobo Gigante" or self.getName() == "Lobo Terrible":
                    print("El lobo se a curado ", str(self.aullar()), " HP\n",
                          "Vida actual:", self.getHp())
                elif attacked.getType() == "PJ":
                    damage = self.getHa()[1].damage() - attacked.getCa()
                    if damage < 0:
                        damage = 0
                    attacked.resthp(damage)
                    print("-----------------------------------\n", attacked.getName(), " a recibido ", str(damage),
                          " daño reducido por la CA")
                else:
                    damage = self.getHa()[1].damage()
                    attacked.resthp(damage)
                    print("-----------------------------------\n", attacked.getName(), " a recibido ", str(damage),
                          " daño")
            elif esquiva == 1:
                print("-----------------------------------\nAtaque esquivado!")

    def calcCoolDown(self, tActual):
        self.__tl = tActual + 3

    def resetAll(self):
        if self.getLvl() >= 1:
            self.setLvl(1)
        self.resetHp()
        for i in range(3):
            self.getHa()[i].setLvl(1)
        self.setTimeOff(False)

    def pullHa(self):
        if self.getTimeOff():
            print("Ataca ", self.getName(), "\n"
                                            "HP actual:", self.getHp(), "\n"
                                                                        "Nivel Actual: ", self.getLvl(), "\n"
                                                                                                         "Hablidades:\n"
                                                                                                         "1.",
                  self.getHa()[0].getName(),
                  "(Activa enfriamiento 1 turno)\n")
        else:
            print("Ataca ", self.getName(), "\n"
                                            "HP actual:", self.getHp(), "\n"
                                                                        "Nivel Actual: ", self.getLvl(), "\n"
                                                                                                         "Hablidades:\n"
                                                                                                         "1.",
                  self.getHa()[0].getName(),
                  "(Activa enfriamiento 1 turno)\n"
                  "2.", self.getHa()[1].getName(),
                  "(Activa enfriamiento 2 turnos)")

    def lvlUp(self):
        self.setLvl(self.getLvl() + 1)
        for i in range(3):
            self.getHa()[i].setLvl(self.getHa()[i].getLvl() + 1)
        self.resetHp()

    def __compEsquiva(self, attacked):
        esquiva = 0
        for i in range(0, len(attacked.getHa())):
            if attacked.getHa()[i].getName() == "Esquiva":
                esquiva = attacked.getHa()[i].esquivar(attacked)
            else:
                esquiva = 0
        return esquiva
