from random import randint

from Player.Picaro import Picaro
from Player.Paladin import Paladin
from Player.Mago import Mago
from TheGame.IA.Asesino import Asesino
from TheGame.IA.JefeLadron import JefeLadron
from TheGame.IA.Ladron import Ladron
from TheGame.IA.Lobo import Lobo
from TheGame.IA.LoboGigante import LoboGigante
from TheGame.IA.LoboTerrible import LoboTerrible
from TheGame.IA.RataGigante import RataGigante

p = Picaro("Teobaldo", 1)
pa = Paladin("Jhon", 1)
m = Mago("Copernico", 1)
lvl1 = [RataGigante, Lobo, Ladron]
lvl2 = [JefeLadron, LoboGigante]
lvl3 = [Asesino, LoboTerrible]


# Menu principal del Juego
def Menu():
    intro()
    op = input()
    if op == "1":
        introPicaro()
        op = input("S/N: ")
        if op == "S" or op == "s":
            encuentro(p)
        elif op == "N" or op == "n":
            Menu()
        else:
            print("==============================\nOpción erronea!\n==============================")
            Menu()
    elif op == "2":
        introPaladin()
        print("¿Deseas jugar con el Paladin?")
        op = input("S/N: ")
        if op == "S" or op == "s":
            encuentro(pa)
        elif op == "N" or op == "n":
            Menu()
        else:
            print("==============================\nOpción erronea!\n==============================")
            Menu()
    elif op == "3":
        introMago()
        print("¿Deseas jugar con el Mago?")
        op = input("S/N: ")
        if op == "S" or op == "s":
            encuentro(m)
        elif op == "N" or op == "n":
            Menu()
        else:
            print("==============================\nOpción erronea!\n==============================")
            Menu()
    elif op == "4":
        print("Exit")
        exit()
    else:
        print("==============================\nOpción erronea!\n==============================")
        Menu()


# Texto introductorio
def intro():
    print("\nBienvenido a proyecto entornos, este es una pequña demo de un juego de rol por turnos. Es decir "
          "encarnaras\n "
          "a uno de los tres valiente personajes jugables en su pequeña aventura por atravesar un misterios y espeso \n"
          "bosque.\n"
          "\n"
          "Las reglas son sencillas, comenzaras a nivel 1 e iras teniendo encuentros aleatorios con criaturas del "
          "bosque\n "
          "que querran atacarte y matarte. Si pierdes toda tu vida se acabara la partida, pero si consigues vencer a "
          "tus\n "
          "adversarios avanzaras al siguiente encuentro y asi sucesivamente hasta alcanzar el siguiente nivel. Por "
          "ultimo\n "
          "a lo largo del camino hay la posibildad de encontrar o no objetos que te ayuden en tu viaje.\n\n"
          "Los personajes jugables son:\n"
          "1.Picaro\n"
          "2.Paladin\n"
          "3.Mago\n"
          "4.Exit\n"
          "Opcion:", end="")


# -----------------------------------\n
# Texto introductorio para le personaje Picaro
def introPicaro():
    p.resetAll()
    print("\nHas seleccionado al Picaro!\n"
          "Teobaldo es un pillin que vive de los robos y hurtos, actualmente se encuentra huyendo de su ciudad natal\n"
          "tras haber robado al noble que regenta la misma. Comienzas tu aventura en mitad del bosque tras estar\n"
          "huyendo tres dias sin parar.\n\n"
          "Perfil del Personaje:\n"
          "Nombre: ", str(p.getName()), "\n"
                                        "Vida:", str(p.getHp()), "\n"
                                                                 "Habilidades:\n"
          , str(p.getHa()[0].getName()), "-", str(p.getHa()[0].getDesc()), ".\n"
          , str(p.getHa()[1].getName()), "-", str(p.getHa()[1].getDesc()), ". \n"
          , str(p.getHa()[2].getName()), "-", str(p.getHa()[2].getDesc()), ".")
    print("¿Deseas jugar con el Picaro?")


# Texto introductorio para le personaje Paladin
def introPaladin():
    pa.resetAll()
    print("\nHas seleccionado al Paladin!\n"
          "John es una joven promesa que acaba de jurar los votos para su orden de caballeria,y como primera mision se\n"
          "le ha encargado capturar a un ladron que ha robado un objeto muy valioso para un noble de la región. El objeto\n"
          "en cuaestion parece ser una reliquia antigua que lleva mucho tiempo en la familia del noble, pero lo que a john\n"
          "no le termina de convenzer es las prisas con la que le han encargado recuperar la reliquia.¿Por que sera tan importante?\n")

    print("Perfil del Personaje:\n"
          "Nombre: ", str(pa.getName()), "\n"
                                         "Vida:", str(pa.getHp()), "\n"
                                                                   "Habilidades:\n"
          , str(pa.getHa()[0].getName()), "-", str(p.getHa()[0].getDesc()), ".\n"
          , str(pa.getHa()[1].getName()), "-", str(p.getHa()[1].getDesc()), ". \n"
          , str(pa.getHa()[2].getName()), "-", str(p.getHa()[2].getDesc()), ".")


# Texto introductorio para le personaje Mago
def introMago():
    m.resetAll()
    print("Sos un mago hermano")

    print("Perfil del Personaje:\n"
          "Nombre: ", str(m.getName()), "\n"
                                        "Vida:", str(m.getHp()), "\n"
                                                                 "Habilidades:\n"
          , str(m.getHa()[0].getName()), "-", str(m.getHa()[0].getDesc()), ". (Coste de puntos magicos:)",
          m.getHa()[0].getPmCost(), "\n"
          , str(m.getHa()[1].getName()), "-", str(m.getHa()[1].getDesc()), ". (Coste de puntos magicos:)",
          m.getHa()[1].getPmCost(), "\n"
          , str(m.getHa()[2].getName()), "-", str(m.getHa()[2].getDesc()), ". (Coste de puntos magicos:)",
          m.getHa()[2].getPmCost())


# Es el controlador de turnos y cuando ha ganado el Jugador o la IA
def encuentro(pj):
    for x in range(3):
        i = 1
        if pj.getLvl() == 1:
            enemy = generarlvl1()
        elif pj.getLvl() == 2:
            enemy = generarlvl2()
        elif pj.getLvl() == 3:
            enemy = generarlvl3()
        print("-----------------------------------")
        print(pj.getName(), " vs ", enemy.getName())
        while enemy.getHp() > 0 and pj.getHp() > 0:
            print("-----------------------------------")
            print("Turno", str(i))
            if pj.getName() == "Copernico":
                turnoMagico(pj, enemy)
            else:
                turnoPj(pj, enemy, i)
            if enemy.getHp() > 0:
                turnoIA(enemy, pj)
            i = i + 1
        if pj.getHp() <= 0:
            print("Derrota!")
            Menu()
        else:
            print("Victoria!")
            if x == 2:
                end()
            else:
                pj.lvlUp()


# Genera un enemigo según el nivel del Jugador
def generarlvl1():
    enemy = lvl1[randint(0, 2)]
    return enemy()


def generarlvl2():
    enemy = lvl2[randint(0, 1)]
    return enemy()


def generarlvl3():
    enemy = lvl3[randint(0, 1)]
    return enemy()


# Controlador del turno del Jugador
def turnoPj(pj, enemy, turn):
    if turn == pj.getTiempoLimite():
        pj.setTimeOff(False)
    pj.pullHa()

    op = input("Opción:")
    print("-----------------------------------\n")
    while op == "2" and pj.getTimeOff():
        print("==============================\nHabilidad en enfriamiento!\n==============================")
        pj.pullHa()
        op = input("Opcion:")
        print("-----------------------------------\n")

    while op != "1" and op != "2":
        print("==============================\nOpción incorrecta!\n==============================")
        pj.pullHa()
        op = input("Opcion: ")
        print("-----------------------------------\n")

    if op == "1":
        pj.ataque(enemy, op)
    elif op == "2":
        pj.calcCoolDown(turn)
        pj.setTimeOff(True)
        pj.ataque(enemy, op)


# Controlador del turno de la IA
def turnoIA(enemy, pj):
    print("HP de", enemy.getName(), ":", enemy.getHp(), "\n",
          enemy.getName(), " realiza un ataque")
    atk = randint(1, 2)
    enemy.ataque(pj, atk)


def turnoMagico(pj, enemy):
    if pj.getPm() < 15:
        pj.setPm(pj.getPm() + 2)
    pj.pullHa()
    op = input("Opción:")
    print("-----------------------------------\n")
    while op != "1" and op != "2" and op != "3":
        print("==============================\nOpción incorrecta!\n==============================")
        pj.pullHa()
        op = input("Opcion: ")
        print("-----------------------------------\n")
    pj.ataqueMagico(enemy, op)


# Texto Final de Juego
def end():
    print("Henorabuena has sobrevivido al bosque, proximamente mas historia en proximas versiones\n"
          "======================================================================================\n")
    Menu()



Menu()
