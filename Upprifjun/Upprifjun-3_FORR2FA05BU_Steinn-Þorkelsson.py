# FORR2FA05BU - Upprifjun 3 - Steinn Þorkelson

import datetime
import math
on = True

while on:
    print("Upprifjun 3")
    print()
    print("1.Dæmi")
    print("2.Dæmi")
    print("3.Dæmi")
    print("4.Dæmi")
    print("5.Dæmi")
    print("6.Dæmi")
    print("7.Dæmi")
    print("8.Hætta í Forriti")

    val = input("Veldu Forrit: ")

    if val == "1":

        tala1 = int(input("Sláðu inn tölu 1: "))
        tala2 = int(input("Sláðu inn tölu 2: "))
        tala3 = int(input("Sláðu inn tölu 3: "))

        listi = [tala1, tala2, tala3]
        print(sorted(listi))

    if val == "2":
        nafn = input("Nafnið þitt?: ")
        aldur = int(input("Aldur?: "))
        now = datetime.datetime.now()
        aldamot = 2100 - now.year + aldur
        print(f"{nafn}, um næstu aldamot verður þú {aldamot} ára.")

    if val == "3":
        tolur = 1
        teljari = 0
        summa = 0
        while tolur != 0:
            tolur = int(input("sláðu inn tölu: "))
            summa += tolur
            teljari += 1
        medaltal = summa / (teljari - 1)
        print(f"Summa talnanna {summa}")
        print(f"fjoldi talna {teljari}")
        print(f"medaltal talna {medaltal}")

    if val == "4":

        radius = float(input("Radís Kúlunnar?: "))
        flatarmal = 4 * 3.14159 * radius**2
        rummal = (4 * radius**3 * 3.14159) / 3
        print(f"Flatarmál kúlunnar er {flatarmal}")
        print(f" Rúmmal Kúlunnar er {rummal}")
    if val == "5":
        print("bilað")

    if val == "6":

        texti = input("Sláðu inn texta: ")
        hastafir = 0
        lagstafir = 0
        for h in texti:
            if h.isupper():
                hastafir += 1
        for l in texti:
            if l.islower():
                lagstafir += 1
        print(f"Í þessum texta eru {hastafir} hástafir og {lagstafir} lágstafir")

    if val == "7":
        tala1 = int(input("Sláðu inn tölu 1: "))
        tala2 = int(input("Sláðu inn tölu 2: "))

        print(math.gcd(tala1, tala2))
    if val == "8":
        on = False
    else:
        print("villa")
        on = True





