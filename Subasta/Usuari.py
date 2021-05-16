class Usuari(object):
    __credito = 0
    __nombre = ""
    __subhastas = list()

    def __init__(self, nombre, credito):
        self.__nombre = nombre
        self.__credito = credito

    def incrementarCredito(self, c):
        self.setCredito(self.getCredito() + c)

    def decrementarCredito(self, c):
        self.setCredito(self.getCredito() - c)

    def getNombre(self):
        return self.__nombre

    def getCredito(self):
        return self.__credito

    def setCredito(self, Y):
        self.__credito = Y

    def getSubHastas(self):
        return self.__subhastas

    def setSubHastas(self, Y):
        self.__subhastas.append(Y)
