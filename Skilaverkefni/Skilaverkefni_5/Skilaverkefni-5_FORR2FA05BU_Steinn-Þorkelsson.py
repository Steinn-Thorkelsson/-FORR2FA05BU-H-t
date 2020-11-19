# FORR2 - Skilaverkefni 5 - Steinn Þorkelsson
import math


class Hringur:

    def __init__(self, radius):
        self.radius = radius

    def ummal(self):
        utkoma = math.pi * (2 * self.radius)
        return utkoma

    def flatarmal(self):
        utkoma = 2 * pow(self.radius, 2) * math.pi
        return utkoma

    def rummal(self):
        utkoma = 3 * (pow(self.radius, 3) * math.pi) / 4
        return utkoma


class Eigandi:

    def __init__(self, nafn, innistaeda=0):
        self.nafn = nafn
        self.innistaeda = innistaeda

    def __repr__(self):
        return f"Eigandi: {self.nafn}, Innistæða: {self.innistaeda}"

    def set_innistaeda(self, ny_innistaeda):
        self.innistaeda = ny_innistaeda

    def uttekt(self, upphaed):
        if upphaed > self.innistaeda:
            print("Ekki er naeg innstaeda")
        else:
            self.innistaeda -= upphaed

    def leggja_inna(self, upphaed):
        self.innistaeda += upphaed


class Nemi:

    def __init__(self, nafn, aldur):
        self.nafn = nafn
        self.aldur = aldur

    def __repr__(self):
        return f"Nafn: {self.nafn}, Aldur: {self.aldur}"


def bua_til_nemendur(nofn, naldur):
    nemanda_listi = []
    for el in range(len(nofn)):
        nyr_nemandi = Nemi(nofn[el], naldur[el])
        nemanda_listi.append(nyr_nemandi)
    return nemanda_listi


def reikna_medaltal(listi):
    summa = 0

    for nemi in range(len(listi)):
        summa += listi[nemi].aldur

    return summa / len(listi)


on = True

while on:
    print("1. Hringur.")
    print("2. Bankareikningur.")
    print("3. Nemendur.")
    print("4. Hætta")

    val = input("Veljið Klasa: ")

    if val == "1":
        notanda_radius = int(input("Sladu inn radius hrings í cm: "))
        h1 = Hringur(notanda_radius)
        on_h = True
        while on_h:
            print("-------- Hringur ----------")
            print("1. Reikna ummál hrings.")
            print("2. Reikna flatarmál hrings.")
            print("3. Reikna rúmmál hrings.")
            print("4. Hætta í Klasa")
            val_h = input("Veldu fall: ")

            if val_h == "1":
                print(f"Ummál hringsins er: {round(h1.ummal(), 2)} cm")
            elif val_h == "2":
                print(f"Flatarmál hringsins er: {round(h1.flatarmal(), 2)} cm2")
            elif val_h == "3":
                print(f"Rúmmál hringsins er: {round(h1.rummal(), 2)} cm3")
            elif val_h == "4":
                on_h = False

    elif val == "2":
        nafn = input("Sláðu inn nafnið á eiganda reikingsins: ")
        inneign = int(input("Sláðu inn inneign reikningsins til að byrja með: "))
        reikningur = Eigandi(nafn, inneign)

        on_e = True
        while on_e:
            print("------- Bankareikningur ----------")
            print("1. Leggja inn á reiking.")
            print("2. Taka út af reikning.")
            print("3. Prenta upplýsingar um reikning.")
            print("4. Hætta")
            val_e = input("Veldu fall: ")

            if val_e == "1":
                magn = int(input("Hversu mikið viltu leggja inn á reikningin?: "))
                reikningur.leggja_inna(magn)
                print(reikningur)
            elif val_e == "2":
                upphaed = int(input("Sláðu inn magn til þess að taka út: "))
                reikningur.uttekt(upphaed)
                print(reikningur)
            elif val_e == "3":
                print(reikningur)

            elif val_e == "4":
                on_e = False

    elif val == "3":
        nemendur_aldur = []
        nemendur_nofn = []
        for i in range(5):
            nafn1 = input("Sláðu inn nafn nemandans: ").capitalize()
            naldur = int(input("sláðu inn aldur nemandans: "))
            nemendur_nofn.append(nafn1)
            nemendur_aldur.append(naldur)
        nemendur = bua_til_nemendur(nemendur_nofn, nemendur_aldur)
        on_n = True
        while on_n:
            print("1. Prenta alla nemendur.")
            print("2. Reikna meðalaldur nemenda.")
            print("3. Hætta")
            val_n = input("Veldu fall: ")

            if val_n == "1":
                for nemandi in range(len(nemendur)):
                    print(nemendur[nemandi])
            elif val_n == "2":
                medaltal = reikna_medaltal(nemendur)
                print(f"Meðaltal nemendana er : {medaltal}")
            elif val_n == "3":
                on_n = False
    elif val == "4":
        on = False
