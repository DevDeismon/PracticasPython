class Charcter(object):
    # Atributos
    __name = ""
    __type = ""
    __hp = 0
    __ca = 0
    __pm = 0
    __ha = list()
    __lvl = 0

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
