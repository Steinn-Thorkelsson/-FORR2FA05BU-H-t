# FORR2 - Lokaverkefni - Steinn Þorkelsson
import random


class Hermadur:
    def __init__(self, aettbalkur, superh=False):

        vopn = ["Sverð", "Spjót", "Exi"]
        self.aettbalkur = aettbalkur
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

    def vopn_afl(self):
        if self.vopn == "Exi":
            self.afl += 1
        elif self.vopn == "Sverð":
            self.afl += 2
        elif self.vopn == "Spjót":
            self.afl += 3

    def get_aettbalkur(self):
        return self.aettbalkur

    def get_afl(self):
        return self.afl

    def get_lif(self):
        return self.lif

    def get_super(self):
        return self.superh

    def get_vopn(self):
        return self.vopn

    def daudur(self):
        if self.lif > 0:
            return False
        else:
            return True

    def meidast(self, magn):
        # Kalla á þetta fall í hvert skipti sem hermaður meiðist
        self.lif -= magn
        if self.lif < 0:
            self.lif = 0

    def missa_afl(self):
        # Kalla á þetta fall í hver skipti sem að súper hermaður meiðir
        if self.superh:
            self.afl = self.afl - 1

    def __repr__(self):
        hermadur = ""
        if self.superh:
            hermadur = "Súper Hermaður"
        else:
            hermadur = "Venjulegur Hermaður"
        strengur = f"Ættbálkur: {self.aettbalkur}, {hermadur}, Vopn: {self.vopn}, Líf: {self.lif}, Afl: {self.afl}."
        return strengur


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
