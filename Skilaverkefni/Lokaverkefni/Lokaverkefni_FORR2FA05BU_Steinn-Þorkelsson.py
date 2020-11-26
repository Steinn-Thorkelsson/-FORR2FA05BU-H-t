# FORR2 - Lokaverkefni - Steinn Þorkelsson
import random


class Pessar:
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

    def __repr__(self):
        hermadur = ""
        if self.superh:
            hermadur = "Súper Hermaður"
        else:
            hermadur = "Venjulegur Hermaður"
        strengur = f"Ættbálkur: {self.aettbalkur}, {hermadur}, Vopn: {self.vopn}, Líf: {self.lif}, Afl: {self.afl}."
        return strengur

    def meidast(self, magn):
        self.lif -= magn


def bua_til_hermann(balkur):
    listi = []
    for h in range(7):
        nyr_hermadur = Pessar(balkur)
        listi.append(nyr_hermadur)
    for s in range(3):
        nyr_shermadur = Pessar(balkur, True)
        listi.append(nyr_shermadur)
    stokkad = random.sample(listi, len(listi))
    random.shuffle(stokkad)
    return stokkad


pessar = bua_til_hermann(0)
hettir = bua_til_hermann(1)
dreyrar = bua_til_hermann(2)

aettbalka_listi = [pessar, hettir, dreyrar]
for i in aettbalka_listi:
    for h in i:
        print(h)
pessi = Pessar(0)
print(pessi.lif)
pessi.meidast(2)
print(pessi.lif)
