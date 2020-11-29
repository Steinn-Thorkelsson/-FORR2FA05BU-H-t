# FORR2 - Lokaverkefni - Steinn Þorkelsson
import random


class Hermadur:
    def __init__(self, aettbalkur, superh=False):

        vopn = ["Sverð", "Spjót", "Exi"]
        aettbalkur_listi = ["Pessar", "Hettir", "Dreyrar"]
        self.aettbalkur = aettbalkur_listi[aettbalkur]
        self.superh = superh
        # ég nota frekar if statement inn í klasanum vegna þess að þegar ég bý til t.d 1 pessa þá þarf ég ekki
        # að skrifa aftur öll random föllin aftur, lífið og aflið breytist líks sjálkrafa ef ég hafa súper hermann
        if self.superh:
            self.vopn = random.choice(vopn)
            self.lif = random.randrange(10, 16)
            self.afl = random.randrange(4, 10)

        else:
            self.vopn = random.choice(vopn)
            self.lif = random.randrange(1, 6)
            self.afl = random.randrange(1, 6)

        self.vopn_afl()

    def __repr__(self):
        hermadur = ""
        if self.superh:
            hermadur = "Súper Hermaður"
        else:
            hermadur = "Venjulegur Hermaður"
        strengur = f"Ættbálkur: {self.aettbalkur}, {hermadur}, Vopn: {self.vopn}, Líf: {self.lif}, Afl: {self.afl}."
        return strengur

    def meidast(self, magn):
        # Kalla á þetta fall í hvert skipti sem hermaður meiðist
        self.lif -= magn

    def missa_afl(self):
        # Kalla á þetta fall í hver skipti sem að súper hermaður meiðir
        self.afl -= 2

    def vopn_afl(self):
        if self.vopn == "Exi":
            self.afl += 1
        elif self.vopn == "Sverð":
            self.afl += 2
        elif self.vopn == "Spjót":
            self.afl += 3


def bua_til_hermann(balkur):
    listi = []
    for h in range(7):
        nyr_hermadur = Hermadur(balkur)
        listi.append(nyr_hermadur)
    for s in range(3):
        nyr_shermadur = Hermadur(balkur, True)
        listi.append(nyr_shermadur)
    stokkad = random.sample(listi, len(listi))
    random.shuffle(stokkad)
    return stokkad


pessar = bua_til_hermann(0)
hettir = bua_til_hermann(1)
dreyrar = bua_til_hermann(2)

aettbalka_listi = [pessar, hettir, dreyrar]

notanda_aettbalkur = []

for i in aettbalka_listi:
    for h in i:
        print(h)
pessi = Hermadur(0)


def bardagi(notandi=False):
    ...


pessar_stig = 0
dreyrar_stig = 0
hettir_stig = 0

sigurvegari = []

while not sigurvegari:
    print()
    print("Velkomin i staersta bardaga sögunnar")
    print("1. Berjast sjálfur")
    print("2. Tölvan berst fyrir þig")

    val = input("Veldu aðgergð: ")

    if val == "1":
        print()
        print("1. Pessar")
        print("2. Hettir")
        print("3. Dreyrar")

        val_1 = input("Veldu ættbálk: ")
        print()
        if val_1 == "1":
            print("Þú hefur valið Pessa.")
            for i in aettbalka_listi[0]:
                notanda_aettbalkur.append(i)

        elif val_1 == "2":
            print("Þú hefur valið Hetti.")
            for i in aettbalka_listi[1]:
                notanda_aettbalkur.append(i)

        elif val_1 == "3":
            print("Þú hefur valið Dreyra.")
            for i in aettbalka_listi[2]:
                notanda_aettbalkur.append(i)

        for i in notanda_aettbalkur:
            print(i)
        bardagi()
    elif val == "2":
        bardagi()
