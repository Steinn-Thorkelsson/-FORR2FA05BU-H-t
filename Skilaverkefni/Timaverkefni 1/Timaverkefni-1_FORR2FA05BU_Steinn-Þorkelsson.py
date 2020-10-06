# FORR2 - Timaverkefni 1 - Steinn Þorkelsson
import random


# dæmi 1
def randomlisti(fjlisti, randbyrjun, randendir):
    listi = random.sample(range(randbyrjun, randendir), fjlisti)
    return listi


def saman(listi1, listi2):
    print("listi1", listi1, "listi2", listi2)
    print()
    set1 = set(listi1)
    set2 = set(listi2)

    list_2_not_in_list1 = list(set2 - set1)
    sameinad = list_2_not_in_list1 + listi1

    return "sameinad an duplicates", sameinad


def talnalisti():
    tlisti = [*range(999, 3001, 1)]
    return tlisti


def jafnartolur(listi):
    for i in listi[:]:
        if i % 2 != 0:
            listi.remove(i)
    return listi


# daemi 2
def midja(strengur):
    n = 3
    chunks = [strengur[i:i + n] for i in range(0, len(strengur), n)]

    return chunks[1]


# daemi 3
def flatarmal(lengd, breidd):
    mal = lengd * breidd
    return mal


def heildarflatarmal(h1, h2, h3, h4):
    heild = h1 + h2 + h3 + h4
    return heild


on = True

while on:
    print("1. Listi")
    print("2. strengur")
    print("3. flatarmal")
    print("4. exit")

    val = input("Veldu forrit: ")

    if val == "1":
        print("listi með 20 random tölum frá 20 - 60: ", randomlisti(20, 19, 61, ))
        print()
        #
        print("2 listar með tölum frá 30 - 60", saman(randomlisti(20, 29, 61), randomlisti(20, 29, 61)))
        print()

        print("listi med tolum fra 999 - 3000:", talnalisti())
        print("sami listi bara med jofnum tolum:", jafnartolur(talnalisti()))
        print()

    if val == "2":
        strengur = input("sladu inn streng sem er 7 stafir ad lengd og er oddatala: ")
        if len(strengur) >= 7:
            if len(strengur) % 2 != 0:
                print(midja(strengur))
        else:
            print("Villa reyndu aftur")

    if val == "3":
        print(f"Herbergi 1: {flatarmal(3, 20)} fermetrar")
        print(f"Herbergi 2: {flatarmal(7, 30)} fermetrar")
        print(f"Herbergi 3: {flatarmal(10, 20)} fermetrar")
        print(f"Herbergi 4: {flatarmal(5, 15)} fermetrar")
        print()
        print("heildar flatarmalid er:", heildarflatarmal(flatarmal(3, 20), flatarmal(7, 30), flatarmal(10, 20),
                                                          flatarmal(5, 15)))
        medaltal = heildarflatarmal(flatarmal(3, 20), flatarmal(7, 30), flatarmal(10, 20),
                                    flatarmal(5, 15)) / 4
        print("medaltal allra herbergja", medaltal)
        print()

        if medaltal > 15:
            print("va stor herbergi")
        elif medaltal >= 7 or medaltal <= 15:
            print("medaltad Medaltal")
        elif medaltal <= 6:
            print("hvilikar kompur")
        print()

    if val == "4":
        print("Bless :'( ")
        on = False
