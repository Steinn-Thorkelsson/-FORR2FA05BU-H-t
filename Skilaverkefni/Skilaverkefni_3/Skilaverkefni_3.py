import random


def prentatuple(tup):
    for i in tup:
        print(i, end=' ')
    print()


tup_herrar = ("Steinn", "Kolbeinn", "Tryggvi", "Hugi", "Starri", "Bessi")
tup_domur = ("Renata", "Thuridur", "Sigridur", "Maria", "Eilidh", "Mamma")
prentatuple(tup_herrar)
prentatuple(tup_domur)


def pararod(tup1, tup2):
    print("Samkvaemis dansnamskeid: ")
    for i in range(0, 6):
        print(f"Par {i + 1}: {tup1[i]} og {tup2[i]}")


pararod(tup_herrar, tup_domur)


def para_random(tup1, tup2):
    print()
    for i in range(6):
        random_herra = random.choice(tup1)
        random_dama = random.choice(tup2)
        print(f"Random Par {i}: {random_herra} og {random_dama}")


para_random(tup_domur, tup_herrar)

def para_random_stakur(tup1,tup2):
    print()
    herra_listi = []
    domu_listi = []
    for i in range(20):
        random_herra = random.choice(tup1)
        random_dama = random.choice(tup2)
        # orugglega til audveldari leid en thetta
        # nota thessa adferd til thess ad pass thad ad listin se ekki minni ne meiri en 6
        if len(herra_listi) <= 5:
            if random_herra not in herra_listi:
                herra_listi.append(random_herra)
        else:
            pass
        if len(domu_listi) <= 5:
            if random_dama not in domu_listi:
                domu_listi.append(random_dama)
        else:
            pass

    for i in range(0, 6):
        print(f"par {i}: {domu_listi[i]} og {herra_listi[i]}")


para_random_stakur(tup_herrar, tup_domur)