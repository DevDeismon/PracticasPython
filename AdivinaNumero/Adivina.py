import random


class Adivina:
    """Atributos"""
    __intentos = 5
    numeroRandom = 0
    __saldoJ = 10
    __saldoG = 50
    __menuOp = 0
    __inputJ = 0
    __numsPLayer = []

    """Construcor"""
    """Getters/Setters"""
    def get_intentos(self):
        return self.__intentos

    def get_numeroRandom(self):
        return self.__numeroRandom

    def get_saldoJ(self):
        return self.__saldoJ

    def get_saldoG(self):
        return self.__saldoG

    def get_menuOp(self):
        return self.__menuOp

    def get_inputJ(self):
        return self.__inputJ

    def set_intentos(self):
        self.__intentos = 5

    def set_saldoJ(self):
        self.__saldoJ = 10

    def set_inputJ(self):
        self.__inputJ = int(input("esperando respuesta: "))

    def set_menuOp(self):
        self.__menuOp = int(input("Esperando respuesta: "))

    """Methods"""

    def randomNum(self):
        if self.get_menuOp(self) == 1:
            self.__numeroRandom = random.randint(1, 10)
        else:
            self.__numeroRandom = random.randint(1, 100)

    def mainMenu(self):
        exit = False
        while not exit:
            if self.get_saldoJ(self) < 10 or self.get_saldoJ(self) > 10:
                self.set_saldoJ()
            print("--------------------------------\n" +
                  "¡Bienvenido a ADIVINA EL NUMERO!\n" +
                  "--------------------------------\n" +
                  "REGLAS:\n" +
                  "El juego consiste en adivinar el numero dentro de un rango, para adivinarlo tendras 5 \n" +
                  "intentos, tras los 5 intentos tendras que pagar un euro para recibir un intento extra.\n" +
                  "Tras Adivinar el numero recibiras un premio segun el modo de juego selecionado,Ademas hay\n" +
                  "un bonus si se adivina el numero a la primera. Para poder iniciar el juego por favor introduce \n" +
                  "un euro.\n"
                  + "--------------------------------")
            self.set_inputJ(self)
            if self.get_inputJ(self) == 1:
                self.__saldoJ -= 1
                self.__saldoG += 1
                self.gameMenu(self)
            elif self.get_inputJ(self) == 0:
                print("Ganancias de hoy: " + str(self.get_saldoJ(self)) + "€\n" +
                      "Adios")
                exit = True

    def gameMenu(self):
        exit = False
        while not exit:
            print("Saldo del jugador: " + str(self.get_saldoJ(self)) + "€\n" +
                  "¡Elige el modo de juego!\n" +
                  "Opcion 1: Adivina un numero entre el 1 y el 10\n" +
                  "Opcion 2: Adivina un numero entre el 1 y el 100\n" +
                  "Opcion 3: Salir")
            self.set_menuOp(self)
            if self.get_menuOp(self) == 1:
                print("Adivina el numero entre 1 y 10. Premio 3€. Bonus 5€\n"
                      "----------------------")
                self.adivinaFacil(self)
            elif self.get_menuOp(self) == 2:
                print("Adivina el numero entre 1 y 100. Premio 5€. Bonus 10€\n" +
                      "Este modo de juego tiene una peuqeña ayuda.\n"
                      "----------------------")
                self.adivinaDificil(self)
            elif self.get_menuOp(self) == 3:
                print("Saldo final: " + str(self.set_saldoJ(self)) + "€\n" +
                      "Hasta la proxima")
                exit = True
            else:
                print("Error")

    def adivinaFacil(self):
        self.randomNum(self)
        exit = False
        contador = 0
        if self.get_intentos(self) < 5:
            self.set_intentos()
        while not exit:
            if self.get_saldoJ(self) < 0:
                print("Te has quedado sin dinero")
                exit = True
            else:
                while not (self.get_inputJ(self) == self.get_numeroRandom(self)) and not (self.get_intentos(self) == 0):
                    self.set_inputJ(self)
                    if 1 <= self.get_inputJ(self) <= 10:
                        if self.get_inputJ(self) == self.get_numeroRandom(self):
                            self.endGame(self)
                            exit = True
                        else:
                            self.__numsPLayer.insert(contador, self.get_inputJ(self))
                            contador += 1
                            self.__intentos -= 1
                            print("Te quedan " + str(self.get_intentos(self)) + " intentos")
                    else:
                        print("Error")
            if self.get_intentos(self) == 0:
                otro = ""
                print("Has perdido, deseas volver a intentarlo?\n" +
                      "Paga 1€, en caso contrario pulsa n")
                otro = input("(s/n): ")
                if otro == "s":
                    self.__saldoJ -= 1
                    self.__saldoG += 1
                    self.__intentos += 1
                else:
                    exit = True
                    self.endGame(self)

    def adivinaDificil(self):
        self.randomNum(self)
        exit = False
        contador = 0
        if self.get_intentos(self) < 5:
            self.set_intentos(self)
        while not exit:
            if self.get_saldoJ(self) < 0:
                print("Te has quedado sin dinero")
                exit = True
            else:
                while not (self.get_inputJ(self) == self.get_numeroRandom(self)) and not (self.get_intentos(self) == 0):
                    self.set_inputJ(self)
                    if 1<= self.get_inputJ(self)<=100:

                        if self.get_inputJ(self) == self.get_numeroRandom(self):
                            self.endGame(self)
                            exit = True

                        else:
                            self.__numsPLayer.insert(contador, self.get_inputJ(self))
                            contador += 1
                            self.__intentos -= 1
                            print("Te quedan " + str(self.get_intentos(self)) + " intentos")
                            if self.get_inputJ(self)<self.get_numeroRandom(self):
                                print("El numero oculto es mayor de "+str(self.get_inputJ(self)))
                            elif self.get_inputJ(self)>self.get_numeroRandom(self):
                                print("El numero oculto es menor de "+str(self.get_inputJ(self)))
                    else:
                        print("Error")

            if self.get_intentos(self) == 0:
                otro = ""
                print("Has perdido, deseas volver a intentarlo?\n" +
                      "Paga 1€, en caso contrario pulsa n")
                otro = input("(s/n): ")
                if otro == "s":
                    self.__saldoJ -= 1
                    self.__saldoG += 1
                    self.__intentos += 1
                else:
                    exit = True
                    self.endGame(self)

    def endGame(self):
        pass


jugador = Adivina
jugador.mainMenu(Adivina)
