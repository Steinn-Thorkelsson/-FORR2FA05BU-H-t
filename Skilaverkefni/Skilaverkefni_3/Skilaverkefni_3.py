import random


def prentatuple(tup):
    for i in tup:
        print(i, end=' ')
    print()


tup_herrar = ("Steinn", "Kolbeinn", "Tryggvi", "Hugi", "Starri", "Bessi")
tup_domur = ("Renata", "Thuridur", "Sigridur", "Maria", "Eilidh", "Nanna")
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


def para_random_stakur(tup1, tup2):
    print()
    herra_listi = []
    domu_listi = []
    while len(herra_listi) != 6:
        random_herra = random.choice(tup1)
        if random_herra not in herra_listi:
            herra_listi.append(random_herra)

    while len(domu_listi) != 6:
        random_dama = random.choice(tup2)
        if random_dama not in domu_listi:
            domu_listi.append(random_dama)
    for i in range(6):
        print(f"Random par an duplicates {i + 1}: {domu_listi[i]} og {herra_listi[i]}")


para_random_stakur(tup_herrar, tup_domur)


def finnanafn(stafur, tup2):
    print()
    nafnalisti = []
    for s in tup2:
        if stafur in s:
            nafnalisti.append(s)
    print(nafnalisti)


finnanafn("n", tup_herrar)


def byrjar_a(stafur, tup2):
    print()
    nafnalisti = []
    for s in tup2:
        if s[0] == stafur:
            nafnalisti.append(s)
    print(nafnalisti)


byrjar_a("R", tup_domur)


def finna_n(tup1, tup2):
    print()
    subs = "nn"
    res = []
    for i in tup2:
        if subs in i:
            res.append(i)
    for s in tup1:
        if subs in s:
            res.append(s)
    print(res)


finna_n(tup_domur, tup_herrar)

simaskra = {"Steinn": 5673890, "Kolbeinn": 6945980, "Tryggvi": 5780967, "Hugi": 8989005, "Starri": 7068957,
            "Renata": 7657989, "Thuridur": 6956830, "Sigridur": 6403230, "Maria": 8589005, "Eilidh": 8486410}


def finna_sima_nr(dict1, nafn):
    print()
    if nafn in dict1:
        simanumer = dict1[nafn]
        return simanumer
    else:
        return "nafnid er ekki i simaskranni"


print(finna_sima_nr(simaskra, "Eilidh"))

bekkur = {"Steinn": 17, "Kolbeinn": 18, "Tryggvi": 19, "Hugi": 16, "Starri": 20, "Bessi":19,
          "Renata": 18, "Thuridur": 20, "Sigridur": 16, "Maria": 19, "Eilidh": 17, "Nanna": 16,
          "Ulfur": 16, "Emma": 17, "Sigmundur": 19 }


def skrifa_ut_nemendur(dict1):
    print()
    for i in dict1:
        print(f"{i}, aldur: {dict1[i]}")


skrifa_ut_nemendur(bekkur)


def nemendur_yfir_18(dict1):
    print()
    teljari = 0
    listi = []
    for i in dict1:
        if dict1[i] >= 18:
            teljari += 1
            listi.append(i)
    print(f"Fjoldi nemenda sem eru yfir 18 eru: {teljari} og nofn theirra eru:")
    for i in listi:
        print(i)


nemendur_yfir_18(bekkur)


def finna_medalaldur(dict1):
    print()
    heildar_aldur = 0
    for i in dict1:
        heildar_aldur += dict1[i]
    medal_aldur = heildar_aldur / 15
    return medal_aldur


print(finna_medalaldur(bekkur))


