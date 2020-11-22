import random


class Spilastokkur:
    def __init__(self, spil, tegund):
        self.spil = spil
        self.tegund = tegund

    def __repr__(self):
        strengur = f"Spil: {self.spil}, Tegund: {self.tegund}"
        return strengur


spil_listi = (
    'Tvistur', "Þristur", "Fjarki", "Fimma", "Sexa", "Sjöa", "Átta", "Nía", "Tía", "Gosi", "Drotting", "Kóngur", "Ás")
tegund_listi = ("Spaði", "Lauf", "Hjarta", "Tígull")


def bua_til_spilastokk(spilin, tegundir):
    spilastokkur = []
    for t in range(len(tegundir)):

        for s in range(len(spilin)):

            nytt_spil = Spilastokkur(spilin[s], tegundir[t])
            spilastokkur.append(nytt_spil)

    return spilastokkur


spilin = bua_til_spilastokk(spil_listi, tegund_listi)

stokkud_spil = random.sample(spilin, len(spilin))
random.shuffle(stokkud_spil)

tolvu_spil = [stokkud_spil[spil] for spil in range(len(stokkud_spil)-26)]
notanda_spil = [stokkud_spil[spil] for spil in range(len(stokkud_spil)-26, len(stokkud_spil))]

print("Tolvu spil",len(tolvu_spil), tolvu_spil)
print("Notanda spil",len(notanda_spil), notanda_spil)
