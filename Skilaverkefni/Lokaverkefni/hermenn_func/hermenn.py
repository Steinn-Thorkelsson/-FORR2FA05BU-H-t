# FORR2 - Lokaverkefni - Steinn Þorkelsson
import random


class Hermadur:
    def __init__(self, aettbalkur, superh=False):

        vopn = ["Sverð", "Spjöt", "Exi"]
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
        elif self.vopn == "Spjöt":
            self.afl += 3

    def get_aettbalkur(self):
        # Sjá ættbálk hermannsins
        return self.aettbalkur

    def get_afl(self):
        # Sjá afl hermannsins
        return self.afl

    def get_lif(self):
        # Sjá lí hermannsins
        return self.lif

    def get_super(self):
        # Skilar True ef að hermaðurinn er súper hermaður annars skilar það False
        return self.superh

    def get_vopn(self):
        # Skilar vopni hermannsins
        return self.vopn

    def daudur(self):
        # Skilar True ef að hermaðurinn er dauður annars skilar það False
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


def bua_til_hermann(balkur, venj_fjoldi=7, super_fjoldi=3):
    listi = []
    # Búa til 7 venjulega hermenn
    for h in range(venj_fjoldi):
        nyr_hermadur = Hermadur(balkur)
        listi.append(nyr_hermadur)
    # Búa til 3 súper hermenn
    for s in range(super_fjoldi):
        nyr_shermadur = Hermadur(balkur, True)
        listi.append(nyr_shermadur)
    stokkad = random.sample(listi, len(listi))
    random.shuffle(stokkad)
    return stokkad
