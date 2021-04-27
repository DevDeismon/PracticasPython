from random import randint
from TextController import TextController

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

txtc = TextController()
p = Picaro("Teobaldo", 1)
pa = Paladin("Jhon", 1)
m = Mago("Copernico", 1)
lvl1 = [RataGigante, Lobo, Ladron]
lvl2 = [JefeLadron, LoboGigante]
lvl3 = [Asesino, LoboTerrible]


# Menu principal del Juego
def Menu():
    txtc.intro()
    op = input()
    if op == "1":
        txtc.introPicaro(p)
        op = input("S/N: ")
        if op == "S" or op == "s":
            encuentro(p)
        elif op == "N" or op == "n":
            Menu()
        else:
            print("==============================\nOpción erronea!\n==============================")
            Menu()
    elif op == "2":
        txtc.introPaladin(pa)
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
        txtc.introMago(m)
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


# Controlador de turnos y cuando ha ganado el Jugador o la IA
def encuentro(pj):
    for x in range(3):
        i = 1
        if pj.getLvl() == 1:
            enemy = generarlvl1()
        elif pj.getLvl() == 2:
            enemy = generarlvl2()

        elif pj.getLvl() == 3:
            enemy = generarlvl3()
        txtc.encuentro(pj, enemy)
        while enemy.getHp() > 0 and pj.getHp() > 0:
            print("Turno", str(i))
            if pj.getName() == "Copernico":
                turnoMagico(pj, enemy)
            else:
                turnoPj(pj, enemy, i)
            if enemy.getHp() > 0:
                turnoIA(enemy, pj)
            i = i + 1
        if pj.getHp() <= 0:
            txtc.defeat()
            Menu()
        else:
            txtc.victory()
            if x == 2:
                txtc.end()
                Menu()
            else:
                pj.lvlUp()


# Genera un enemigo según el nivel del Jugador
def generarlvl1():
    enemy = lvl1[randint(0, 2)]
    return enemy()


# Genera un enemigo según el nivel del Jugador
def generarlvl2():
    enemy = lvl2[randint(0, 1)]
    return enemy()


# Genera un enemigo según el nivel del Jugador
def generarlvl3():
    enemy = lvl3[randint(0, 1)]
    return enemy()


# Controlador del turno del Jugador
def turnoPj(pj, enemy, turn):
    if turn == pj.getTiempoLimite():
        pj.setTimeOff(False)
    pj.pullHa()

    op = input("Opción:")
    while op == "2" and pj.getTimeOff():
        print("==============================\nHabilidad en enfriamiento!\n==============================")
        pj.pullHa()
        op = input("Opcion:")

    while op != "1" and op != "2":
        print("==============================\nOpción incorrecta!\n==============================")
        pj.pullHa()
        op = input("Opcion: ")

    if op == "1":
        pj.ataque(enemy, op)
    elif op == "2":
        pj.calcCoolDown(turn)
        pj.ataque(enemy, op)


# Controlador especial del turno del Mago
def turnoMagico(pj, enemy):
    if pj.getPm() < 20:
        pj.setPm(pj.getPm() + 2)
    pj.pullHa()
    op = input("Opción:")
    while op != "1" and op != "2" and op != "3":
        print("==============================\nOpción incorrecta!\n==============================")
        pj.pullHa()
        op = input("Opcion: ")
        print("-----------------------------------\n")
    pj.ataqueMagico(enemy, op)


# Controlador del turno de la IA
def turnoIA(enemy, pj):
    txtc.pullIa(enemy)
    atk = randint(1, 2)
    enemy.ataque(pj, atk)


Menu()
