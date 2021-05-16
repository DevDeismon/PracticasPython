class Puja(object):
    __usuario = ""
    __puja = 0

    def __init__(self, usuario, puja):
        self.__puja = puja
        self.__usuario = usuario

    def getPuja(self):
        return self.__puja

    def getUsuario(self):
        return self.__usuario

    def getUserName(self):
        return self.__usuario.getNombre()
