from Subasta.Puja import Puja
from Subasta.Usuari import Usuari


class Subhasta(object):
    # Atributs
    __producto = ""
    __propietario = Usuari("", 0)
    __estado = True
    __pujas = list()
    __pujaAlta = Puja("", 0)

    # Constructor
    def __init__(self, p, pr):
        self.__producto = p
        self.__propietario = pr
        pr.setSubHastas(self)

    # Getters/Setters
    def getProducto(self):
        return self.__producto

    def getPropietario(self):
        return self.__propietario

    def getEstado(self):
        return self.__estado

    def getPujas(self):
        return self.__pujas

    def getPujaAlta(self):
        return self.__pujaAlta

    def setProducto(self, Y):
        self.__producto = Y

    def setPropietario(self, Y):
        self.__propietario = Y

    def setEstado(self, Y):
        self.__estado = Y

    def setPujas(self, Y):
        self.__pujas.append(Y)

    def setPujaAlta(self, Y):
        self.__pujaAlta = Y

    # Others Methos
    def pujar(self, usuari, cantidad):
        if self.__controlError(usuari, cantidad):
            puja = Puja(usuari, cantidad)
            self.setPujas(puja)
            self.setPujaAlta(puja)

    def pujar1(self, usuari):
        cantidad = self.getPujaAlta().getPuja() + 1
        if self.__controlError(usuari, cantidad):
            puja = Puja(usuari, cantidad)
            self.setPujas(puja)
            self.setPujaAlta(puja)

    def executar(self):
        if self.getEstado():
            self.setEstado(False)
            self.getPujaAlta().getUsuario().decrementarCredito(self.getPujaAlta().getPuja())
            self.getPropietario().incrementarCredito(self.getPujaAlta().getPuja())
            print("Se ha cerrado la puja")
            return True
        else:
            print("Ya esta cerrado")
            return False

    def __isPropietario(self, usuari):
        if usuari.getNombre() == self.getPropietario().getNombre():
            return True
        else:
            return False

    def __isSaldo(self, usuari, cantidad):
        if cantidad > usuari.getCredito():
            return True
        else:
            return False

    def __isPujaAlta(self, cantidad):
        num = self.getPujaAlta().getPuja()
        if cantidad > num:
            return True
        else:
            return False

    def __controlError(self, usuari, cantidad):
        if self.__estado:
            if not self.__isPropietario(usuari):
                if not self.__isSaldo(usuari, cantidad):
                    if self.__isPujaAlta(cantidad):
                        print("Cantidad aceptada")
                        return True
                    else:
                        print("Cantidad mas baja que la apuesta actual")
                        return False
                else:
                    print("No hay saldo suficiente")
                    return False
            else:
                print("Eres el propietario")
                return False
        else:
            print("Esta cerrado")
            return False
