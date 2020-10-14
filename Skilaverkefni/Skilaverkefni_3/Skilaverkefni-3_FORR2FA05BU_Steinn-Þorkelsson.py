# # FORR2 - Skilaverkefni 3 - Steinn Þorkelsson
import random


# Dæmi 1 ---------------------------------------------------------------------------------------------------------------
def prentatuple(tup):
    for i in tup:
        print(i, end=' ')
    print()


def pararod(tup1, tup2):
    for i in range(0, 6):
        print(f"Par {i + 1}: {tup1[i]} og {tup2[i]}")
    print()


def para_random(tup1, tup2):
    print()
    for i in range(6):
        random_herra = random.choice(tup1)
        random_dama = random.choice(tup2)
        print(f"Random Par {i}: {random_herra} og {random_dama}")


def para_random_stakur(tup1, tup2):
    herra_listi = []
    domu_listi = []
    """á meðan herra/dömu listinn er ekki = 6 þá velur það random nafn, ef að nafnið er núþegar í listanum 
    þá setur það nafnið í listann. Ef það er núþegar í listanum þá velur það random nafn þangað til að það finnst
    nafn sem er ekki núþegar í listanum"""

    while len(herra_listi) != 6:
        random_herra = random.choice(tup1)
        if random_herra not in herra_listi:
            herra_listi.append(random_herra)

    while len(domu_listi) != 6:
        random_dama = random.choice(tup2)
        if random_dama not in domu_listi:
            domu_listi.append(random_dama)
    # nota " i + 1" vegna þess að for loopan telur frá 0 og upp
    for i in range(6):
        print(f"Random par an duplicates {i + 1}: {domu_listi[i]} og {herra_listi[i]}")


def finnanafn(stafur, tup2):
    nafnalisti = []
    for s in tup2:
        if stafur in s:
            nafnalisti.append(s)
    print(nafnalisti)


def byrjar_a(stafur, tup2):
    print()
    nafnalisti = []
    for s in tup2:
        if s[0] == stafur:
            nafnalisti.append(s)
    print(nafnalisti)


def finna_n(tup1, tup2):
    enn = "nn"
    listi = []
    for i in tup2:
        if enn in i:
            listi.append(i)
    for s in tup1:
        if enn in s:
            listi.append(s)
    print(listi)


# Dæmi 2 ---------------------------------------------------------------------------------------------------------------

def finna_sima_nr(dict1, nafn):
    print()
    if nafn in dict1:
        simanumer = dict1[nafn]
        return f"Símanúmerið hjá {nafn} er {simanumer}"
    else:
        return f"{nafn} er ekki i simaskranni"


# Dæmi 3 ---------------------------------------------------------------------------------------------------------------
def skrifa_ut_nemendur(dict1):
    print()
    for i in dict1:
        print(f"{i}, aldur: {dict1[i]}")


def nemendur_yfir_18(dict1):
    teljari = 0
    listi = []
    for i in dict1:
        if dict1[i] >= 18:
            teljari += 1
            listi.append(i)
    print(f"Fjoldi nemenda sem eru yfir 18 eru {teljari} og nofn theirra eru:")
    for i in listi:
        print(i,dict1[i], end=", ")


def finna_medalaldur_heildaraldur(dict1, val):
    heildar_aldur = 0
    for i in dict1:
        heildar_aldur += dict1[i]
    medal_aldur = heildar_aldur / 15
    if val == "medal":
        return medal_aldur
    elif val == "heildar":
        return heildar_aldur


# ----------------------------------------------------------------------------------------------------------------------
on = True

while on:
    print("1. Danspörin")
    print("2. Símaskrá")
    print("3. Skráning í bekk")
    print("4. Hætta í forriti")
    val = input("Val: ")

    if val == "1":
        tup_herrar = ("Steinn", "Kolbeinn", "Tryggvi", "Hugi", "Starri", "Bessi")
        tup_domur = ("Renata", "Thuridur", "Sigridur", "Maria", "Eilidh", "Nanna")
        on1 = True

        while on1:
            print()
            print("--Danspörin--")
            print("1. Prenta Tuple-in")
            print("2. Para saman dömur og herra")
            print("3. Para saman random pör")
            print("4. Para saman pör án tvíbura")
            print("5. Finna nafn sem innihalda staf")
            print("6. Fyrsti stafur í nafni")
            print("7. Fleiri en eitt n í nafninu")
            print("8. Hætta")
            val1 = input("Veldu fall: ")
            print()
            if val1 == "1":
                print()
                print("Dömur:")
                prentatuple(tup_domur)
                print("Herrar:")
                prentatuple(tup_herrar)

            elif val1 == "2":
                print()
                print("Pararöð")
                pararod(tup_herrar, tup_domur)

            elif val1 == "3":
                print()
                print("Random pör: ")
                para_random(tup_herrar, tup_domur)

            elif val1 == "4":
                print()
                print("Random pör án tvíbura: ")
                para_random_stakur(tup_herrar, tup_domur)

            elif val1 == "5":
                print()
                stafa_val = input("sláðu inn staf til að leita af: ")
                print(f"Dömur sem innihalda stafinn {stafa_val}:")
                finnanafn(stafa_val, tup_domur)
                print(f"Herra sem innihalda stafinn {stafa_val}:")
                finnanafn(stafa_val, tup_herrar)

            elif val1 == "6":
                print()
                stafa_val = input("sláðu inn staf til að leita af: ")
                print(f"Dömur sem byrja á stafinum {stafa_val}")
                byrjar_a(stafa_val, tup_domur)
                print(f"Herrar sem byrja á stafinum {stafa_val}")
                byrjar_a(stafa_val, tup_herrar)

            elif val1 == "7":
                print()
                print("Nöfn sem innihalda meiri en eitt n")
                finna_n(tup_domur, tup_herrar)

            elif val1 == "8":
                on1 = False

    elif val == "2":
        simaskra = {"Steinn": 5673890, "Kolbeinn": 6945980, "Tryggvi": 5780967, "Hugi": 8989005, "Starri": 7068957,
                    "Renata": 7657989, "Thuridur": 6956830, "Sigridur": 6403230, "Maria": 8589005, "Eilidh": 8486410}
        nafn1 = input("Sláðu inn nafn til að finna í símaskránni: ").capitalize()
        print(finna_sima_nr(simaskra, nafn1))
        print()

    elif val == "3":
        bekkur = {"Steinn": 17, "Kolbeinn": 18, "Tryggvi": 19, "Hugi": 16, "Starri": 20, "Bessi": 19,
                  "Renata": 18, "Thuridur": 20, "Sigridur": 16, "Maria": 19, "Eilidh": 17, "Nanna": 16,
                  "Ulfur": 16, "Emma": 17, "Sigmundur": 19}
        on3 = True
        while on3:
            print()
            print("------Skráning í bekk------")
            print("1. Skrifa út alla nemendur")
            print("2. Allir nemendur sem eru 18 ára og yfir")
            print("3. Meðalaldur bekkjarins")
            print("4. Heildaraldur bekkjarins")
            print("5. Hætta")
            val3 = input("Veldu fall: ")
            if val3 == "1":
                print()
                print("Allir nemendurnir:")
                skrifa_ut_nemendur(bekkur)

            elif val3 == "2":
                print()
                print("Nemendur 18 ára og yfir:")
                nemendur_yfir_18(bekkur)
                print()
            elif val3 == "3":
                print()
                print("Meðalaldur bekkjarins er:", finna_medalaldur_heildaraldur(bekkur, "medal"))

            elif val3 == "4":
                print()
                print("Heildaraldur bekkjarins er:", finna_medalaldur_heildaraldur(bekkur, "heildar"))

            elif val3 == "5":
                on3 = False

    elif val == "4":
        print("Bless :)")
        on = False
