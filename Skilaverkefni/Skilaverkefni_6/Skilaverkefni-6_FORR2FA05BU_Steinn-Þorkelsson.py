# FORR2 - Skilaverkefni 6 - Steinn Þorkelsson
import random


class Spilastokkur:
    def __init__(self, spil, tegund):
        self.spil = spil
        self.tegund = tegund

    def __repr__(self):
        spiltala = ""
        if self.spil == 11:
            spiltala = "Gosi"
        elif self.spil == 12:
            spiltala = "Drottning"
        elif self.spil == 13:
            spiltala = "Kóngur"
        elif self.spil == 14:
            spiltala = "Ás"
        else:
            spiltala = self.spil
        strengur = f"Spil: {spiltala}, Tegund: {self.tegund}"
        return strengur


spil_listi = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
tegund_listi = ("Spaði", "Lauf", "Hjarta", "Tígull")


def bua_til_spilastokk(spilin, tegundir):
    spilastokkur = []
    for t in tegundir:

        for s in spilin:
            nytt_spil = Spilastokkur(s, t)
            spilastokkur.append(nytt_spil)

    return spilastokkur


spilin = bua_til_spilastokk(spil_listi, tegund_listi)

# Stokka spil
stokkud_spil = random.sample(spilin, len(spilin))
random.shuffle(stokkud_spil)

# Skipta spilastokknum í 2 hluta
spil_tolvu = [stokkud_spil[spil] for spil in range(len(stokkud_spil) - 26)]
spil_notanda = [stokkud_spil[spil] for spil in range(len(stokkud_spil) - 26, len(stokkud_spil))]

# print("Tolvu spil", len(spil_tolvu), spil_tolvu)
# print("Notanda spil", len(spil_notanda), spil_notanda)


lotur = 0

slagir_not = 0
slagir_tol = 0

tol_vinnur = "Tölvan vann þessa lotu"
not_vinnur = "Þú vannst þessa lotu"

while lotur < 26:
    print()
    print(f"--------Lota nr.{lotur + 1}--------")

    if lotur % 2 == 0:
        print("Notandi leikur fyrst.")
    else:
        print("Tölvan leikur fyrst")

    tromp = random.choice(tegund_listi)
    tromp_strengur = f"Trompið er: {tromp}"

    var_tromp = False

    print(tromp_strengur)
    print()

    hendi_not = spil_notanda.pop()
    hendi_tol = spil_tolvu.pop()

    print(f"Spilið þitt er {hendi_not}")
    print(f"Spil tölvunnar er {hendi_tol}")
    print()

    if hendi_not.tegund == tromp or hendi_tol.tegund == tromp:
        var_tromp = True
        if hendi_not.tegund == tromp and hendi_tol.tegund == tromp:
            if hendi_not.spil > hendi_tol.spil:
                print(not_vinnur)
                slagir_not += 1
            else:
                print(tol_vinnur)
                slagir_tol += 1

        elif hendi_not.tegund == tromp and hendi_tol.tegund != tromp:
            print(not_vinnur)
            slagir_not += 1

        elif hendi_not.tegund != tromp and hendi_tol.tegund == tromp:
            print(tol_vinnur)
            slagir_tol += 1

    # Ég nota var_tromp til þess að tékka hvort að tromp hafi verið í lotunni, ef ég myndi ekki gera það þá myndu þessi
    # if statements samt keyra sig þótt að það hafir verið tromp og rugla í stigunum
    elif lotur % 2 == 0 and not var_tromp:
        # Notandi ræður

        if hendi_not.tegund == hendi_tol.tegund:

            if hendi_not.spil > hendi_tol.spil:
                print(not_vinnur)
                slagir_not += 1
            else:
                print(tol_vinnur)
                slagir_tol += 1
        else:
            print(not_vinnur)
            slagir_not += 1

    elif lotur % 2 != 0 and not var_tromp:
        # Tölvan ræður
        if hendi_tol.tegund == hendi_not.tegund:

            if hendi_tol.spil > hendi_not.spil:
                print(tol_vinnur)
                slagir_tol += 1
            else:
                print(not_vinnur)
                slagir_not += 1
        else:
            print(tol_vinnur)
            slagir_tol += 1

    lotur += 1
    print()
    print(f"Stigin hjá Notanda eru {slagir_not} og hjá Tölvunni {slagir_tol}")
    afram = input("Ýttu á enter til að halda áfram: ")

print()
if slagir_not > slagir_tol:
    print(f"Þú vannst leikin {slagir_not}:{slagir_tol}")
elif slagir_not < slagir_tol:
    print(f"Tölvan vann leikin {slagir_tol}:{slagir_not}")
else:
    print("Það var jafntefli")
