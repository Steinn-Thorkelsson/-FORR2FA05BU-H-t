# FORR2 - Tímaverkefni 3 - Steinn Þorkelsson
import random
print("FORR2 - Tímaverkefni 3 - Steinn Þorkelsson")


def verkefni_1(val):
    talna_listi = [random.randrange(200, 300, 1) for i in range(100)]

    gengur_i_niu = [i for i in talna_listi if i % 9 == 0]

    tolur_a_milli_200_og_235 = [i for i in talna_listi if i < 236]
    tolur_a_milli_200_og_235.sort()

    heildar_summa = 0

    for tala in talna_listi:
        heildar_summa += tala

    medaltal = round(heildar_summa / len(talna_listi), 2)

    if val == "1":
        return talna_listi

    elif val == "2":
        strengur = f"Heildar summa talnanna er {heildar_summa} og meðaltalið þeirra {medaltal}"
        return strengur

    elif val == "3":
        strengur = f"Tölur sem níu gengur upp í: \n {gengur_i_niu}"
        return strengur

    elif val == "4":
        strengur = f"Tölur á milli 200 og 235: \n {tolur_a_milli_200_og_235}"
        return strengur


def verkefni_2(val):
    skra = open("Tímaverkefni3.txt", "r", encoding="utf8")
    tolur = skra.read()
    skra.close()

    listi = tolur.split(",")

    int_listi = list(map(int, listi))

    summa = 0
    lengd = 0
    for i in int_listi:
        summa += i
    for a in int_listi:
        lengd += 1

    medaltal = round(summa / len(int_listi), 2)

    if val == "1":

        strengur = f"Innihald skránnar: {tolur}"
        return strengur

    elif val == "2":
        strengur = f"Meðaltal talnnana er: {medaltal}"
        return strengur

    elif val == "3":
        int_listi.sort()
        naest_minnsta = int_listi[1]
        strengur = f"Næst minnsta talan er: {naest_minnsta}"
        return strengur
    elif val == "4":

        baeta_vid_tolu = input("Bættu við tölu í listan: ")
        skra = open("Tímaverkefni3.txt", "a", encoding="utf8")
        skra.write("," + baeta_vid_tolu)

        skra = open("Tímaverkefni3.txt", "r", encoding="utf8")
        tolur = skra.read()

        print(tolur)


# Verkefni 3
class KlasiEitt:
    def __init__(self, tala_1, tala_2, tala_3):
        self.tala_1 = tala_1
        self.tala_2 = tala_2
        self.tala_3 = tala_3

    def deila_med_2(self):
        summa = self.tala_1 + self.tala_2 + self.tala_3
        deiling = round(summa / 2, 2)
        strengur = f"Summa talnanna deilt með 2 er: {deiling}"
        return strengur


class KlasiTvo:
    def __init__(self, reidhjol, girar):
        self.reidhjol = reidhjol
        self.girar = girar

    def __repr__(self):
        strengur = f"Ég er {self.reidhjol} hjól og er með {self.girar} gíra"
        return strengur


on = True

while on:
    print()
    print("1. Verkefni 1")
    print("2. Verkefni 2")
    print("3. Verkefni 3")
    print("4. Hætta í forriti")

    val = input("Veldu verkefni: ")

    if val == "1":
        on_1 = True
        while on_1:

            print()
            print("1. Allar tölur í einni línu")
            print("2. Heildar summa og meðaltal listans")
            print("3. Tölur sem níu gengur upp í")
            print("4. Tölur á bilinu 200 til 235")
            print("5. Hætta í Verkefni 1")

            val_1 = input("Veldu fall: ")

            if val_1 == "5":
                on_1 = False
            else:
                print()
                print(verkefni_1(val_1))

    elif val == "2":
        on_2 = True

        while on_2:
            print()
            print("1: Birta innihald srkánnar")
            print("2. Birta meðaltal talnanna")
            print("3. Birta Næst minnstu töluna")
            print("4. Bæta Tölu við skránna")
            print("5. Hætta í Verkefni 2")

            val_2 = input("Veldu fall: ")

            if val_2 == "5":
                on_2 = False

            else:
                print()
                print(verkefni_2(val_2))

    elif val == "3":
        on_3 = True
        while on_3:
            print()
            print("1. Klasi Eitt")
            print("2. Klasi Tvö")
            print("3. Hætta í Verkefni 3")
            val_3 = input("Veldu Klasa: ")
            if val_3 == "1":
                print()
                listi = []
                for i in range(3):
                    tala = int(input("Sláðu inn tölu: "))
                    listi.append(tala)
                klasi_eitt = KlasiEitt(listi[0], listi[1], listi[2])
                print(klasi_eitt.deila_med_2())

            elif val_3 == "2":
                print()
                gerd = input("Sláðu inn gerð af reiðhjóli: ")
                fjoldi_gira = int(input("Hversu marga gíra er hjólið með: "))
                klasi_tvo = KlasiTvo(gerd, fjoldi_gira)
                print(klasi_tvo)

            elif val_3 == "3":
                on_3 = False

    elif val == "4":
        on = False
