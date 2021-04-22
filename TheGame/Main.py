from random import randint
from TheGame.IA import LoboTerrible
from TheGame.IA.Asesino import Asesino
from TheGame.IA.JefeLadron import JefeLadron
from TheGame.IA.Ladron import Ladron
from TheGame.IA.Lobo import Lobo
from TheGame.IA.LoboGigante import LoboGigante
from TheGame.IA.RataGigante import RataGigante
from TheGame.Player.Picaro import Picaro
from TheGame.Player.Paladin import Paladin
from TheGame.Player.Mago import Mago
from TheGame.GameController import GameController

gm = GameController()
p = Picaro("Teobaldo", 1)
pa = Paladin("Jhon", 1)
m = Mago("Gandalf the green", 1)
lvl1 = [RataGigante, Lobo, Ladron]
lvl2 = [JefeLadron, LoboGigante]
lvl3 = {Asesino, LoboTerrible}


def intro():
    print("Bienvenido a proyecto entornos, este es una pequña demo de un juego de rol por turnos. Es decir encarnaras\n"
          "a uno de los tres valiente personajes jugables en su pequeña aventura por atravesar un misterios y espeso \n"
          "bosque.\n"
          "\n"
          "Las reglas son sencillas, comenzaras a nivel 1 e iras teniendo encuentros aleatorios con criaturas del bosque\n"
          "que querran atacarte y matarte. Si pierdes toda tu vida se acabara la partida, pero si consigues vencer a tus\n"
          "adversarios avanzaras al siguiente encuentro y asi sucesivamente hasta alcanzar el siguiente nivel. Por ultimo\n"
          "a lo largo del camino hay la posibildad de encontrar o no objetos que te ayuden en tu viaje.\n\n"
          "Los personajes jugables son:\n"
          "1.Picaro\n"
          "2.Paladin\n"
          "3.Mago\n"
          "4.Exit\n"
          "Opcion:", end="")


def introPicaro():
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


def introPaladin():
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


def introMago():
    print("Sos un mago hermano")

    print("Perfil del Personaje:\n"
          "Nombre: ", str(m.getName()), "\n"
                                        "Vida:", str(m.getHp()), "\n"
                                                                 "Habilidades:\n"
          , str(m.getHa()[0].getName()), "-", str(m.getHa()[0].getDesc()), ".\n"
          , str(m.getHa()[1].getName()), "-", str(m.getHa()[1].getDesc()), ". \n"
          , str(m.getHa()[2].getName()), "-", str(m.getHa()[2].getDesc()), ".")


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
            print("------------\nOpción erronea!\n------------")
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
            print("------------\nOpción erronea!\n------------")
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
            print("------------\nOpción erronea!\n------------")
            Menu()
    elif op == "4":
        print("Exit")
        exit()
    else:
        print("------------\nOpción erronea!\n------------")
        Menu()


def generarlvl1():
    enemy = lvl1[randint(0, 2)]
    return enemy()


def generarlvl2():
    enemy = lvl1[randint(0, 2)]
    return enemy()


def generarlvl3():
    enemy = lvl1[randint(0, 2)]
    return enemy()


def encuentro(pj):
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
        print("------------------------")
        print("Turno", str(i))
        turnoPj(pj, enemy)
        if enemy.getHp() > 0:
            turnoEnemy(enemy, pj)
        i = i + 1
    if pj.getHp() <= 0:
        print("Derrota!")
    else:
        print("Victoria!")


def atkNormal(attacker, attacked, action):
    op = int(action)
    for i in range(0, len(attacked.getHa())):
        if attacked.getHa()[i].getName() == "Esquiva":
            esquiva = attacked.getHa()[i].esquivar()
    if op == 1:
        if esquiva == 0:
            damage = attacker.getHa()[0].damage()
            attacked.resthp(damage)
            return print(attacked.getName(), " a recibido ", str(damage), " daño")
        elif esquiva == 1:
            return print("Atque esquivado!")
    if op == 2:
        if esquiva == 0:
            if attacker.getHa()[1].getName() == "Aullido":
                cura = attacker.aullar(0)
                return print(attacker.getName(), " aulla y se cura ", str(cura))
            else:
                damage = attacker.getHa()[1].damage()
                attacked.resthp(damage)
                return print(attacked.getName(), " a recibido ", str(damage), " daño")

        elif esquiva == 1:
            return print("Atque esquivado!")


def turnoPj(pj, enemy):
    pj.pullHa()
    op = input("Opción:")
    atkNormal(pj, enemy, op)


def turnoEnemy(enemy, pj):
    print("-----------------------------\n"
          "Ataca ", enemy.getName(), "\n"
                                     "HP de", enemy.getName(), enemy.getHp())
    atk = randint(1, 2)
    atkNormal(enemy, pj, atk)


Menu()
