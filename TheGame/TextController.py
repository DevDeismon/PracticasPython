class TextController(object):
    # Texto introductorio
    def intro(self):
        print("************************************************\n"
              "*                                              *\n"
              "*            BIENVENIDO a OAKHURST             *\n"
              "*                                              *\n"
              "************************************************\n"
              "\nEsta es una pequña demo de un juego de rol por turnos. Es decir encarnaras\n"
              "a uno de los tres valiente personajes jugables en su pequeña aventura por \n"
              "atravesar un misterios y espeso bosque.\n\n")
        op = input("Pulsa enter para continuar!\n")
        if op == "":
            print("//////////////////////////////////////////////\n"
                  "/                                            /\n"
                  "/                    REGLAS                  /\n"
                  "/                                            /\n"
                  "//////////////////////////////////////////////\n"
                  "\nComenzaras a nivel 1 e iras teniendo encuentros aleatorios con criaturas del\n"
                  "bosque que querran atacarte y matarte. Si pierdes toda tu vida se acabara la\n"
                  "partida, pero si consigues vencer a tus adversarios avanzaras al siguiente\n"
                  "encuentro y asi sucesivamente hasta alcanzar el siguiente nivel. Por ultimo\n"
                  "a lo largo del camino hay la posibildad de encontrar o no objetos que te ayuden en tu viaje.\n\n"
                  "Los personajes jugables son:\n"
                  "1.Picaro\n"
                  "2.Paladin\n"
                  "3.Mago\n"
                  "4.Exit\n"
                  "Opcion:", end="")
        else:
            print("==============================\nOpción erronea!\n==============================\n")
            self.intro()

    # Texto introductorio para le personaje Picaro

    def introPicaro(slef, pj):
        pj.resetAll()
        print("\nHas seleccionado al Picaro!\n"
              "Teobaldo es un pillin que vive de los robos y hurtos, actualmente se encuentra huyendo de su ciudad natal\n"
              "tras haber robado al noble que regenta la misma. Comienzas tu aventura en mitad del bosque tras estar\n"
              "huyendo tres dias sin parar.\n\n"
              "Perfil del Personaje:\n"
              "Nombre: ", str(pj.getName()), "\n"
                                             "Vida:", str(pj.getHp()), "\n"
                                                                       "Habilidades:\n"
              , str(pj.getHa()[0].getName()), "-", str(pj.getHa()[0].getDesc()), ".\n"
              , str(pj.getHa()[1].getName()), "-", str(pj.getHa()[1].getDesc()), ". \n"
              , str(pj.getHa()[2].getName()), "-", str(pj.getHa()[2].getDesc()), ".")
        print("¿Deseas jugar con el Picaro?")

        # Texto introductorio para le personaje Paladin

    # Texto introductorio para le personaje Paladin
    def introPaladin(self, pj):
        pj.resetAll()
        print("\nHas seleccionado al Paladin!\n"
              "John es una joven promesa que acaba de jurar los votos para su orden de caballeria,y como primera mision se\n"
              "le ha encargado capturar a un ladron que ha robado un objeto muy valioso para un noble de la región. El objeto\n"
              "en cuaestion parece ser una reliquia antigua que lleva mucho tiempo en la familia del noble, pero lo que a john\n"
              "no le termina de convenzer es las prisas con la que le han encargado recuperar la reliquia.¿Por que sera tan importante?\n")

        print("Perfil del Personaje:\n"
              "Nombre: ", str(pj.getName()), "\n"
                                             "Vida:", str(pj.getHp()), "\n"
                                                                       "Habilidades:\n"
              , str(pj.getHa()[0].getName()), "-", str(pj.getHa()[0].getDesc()), ".\n"
              , str(pj.getHa()[1].getName()), "-", str(pj.getHa()[1].getDesc()), ". \n"
              , str(pj.getHa()[2].getName()), "-", str(pj.getHa()[2].getDesc()), ".")

        # Texto introductorio para le personaje Mago

    # Texto introductorio para le personaje Mago
    def introMago(self, pj):
        pj.resetAll()
        print("Sos un mago hermano")

        print("Perfil del Personaje:\n"
              "Nombre: ", str(pj.getName()), "\n"
                                             "Vida:", str(pj.getHp()), "\n"
                                                                       "Puntos de Magia: ", str(pj.getPm()), "\n"
                                                                                                             "Habilidades:\n"
              , str(pj.getHa()[0].getName()), "-", str(pj.getHa()[0].getDesc()), ". (Coste de puntos magicos:)",
              pj.getHa()[0].getPmCost(), "\n"
              , str(pj.getHa()[1].getName()), "-", str(pj.getHa()[1].getDesc()), ". (Coste de puntos magicos:)",
              pj.getHa()[1].getPmCost(), "\n"
              , str(pj.getHa()[2].getName()), "-", str(pj.getHa()[2].getDesc()), ". (Coste de puntos magicos:)",
              pj.getHa()[2].getPmCost())

    # titulo de cada encuentro
    def encuentro(self, pj, enemy):
        print("\n===================================")
        print("    ", pj.getName(), " vs ", enemy.getName())
        print("===================================\n")

    # Text de visctoria
    def victory(self):
        print("######################\n"
              "#                    #\n"
              "#      Victoria!     #\n"
              "#                    #\n"
              "######################\n")

    # Text de derrota
    def defeat(self):
        print("######################\n"
              "#                    #\n"
              "#      Derrota!      #\n"
              "#                    #\n"
              "######################\n")

    # Texto Final de Juego
    def end(self):
        print("Henorabuena has sobrevivido al bosque, proximamente mas historia en proximas versiones\n"
              "======================================================================================\n")

    # Texto de la IA
    def pullIa(self, IA):
        print("*************** TURNO DE LA IA ***************\nAtaca", IA.getName(), "\n"
                                                                                     "HP actual: ", str(IA.getHp()))
