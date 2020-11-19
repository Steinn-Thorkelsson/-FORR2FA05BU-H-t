# FORR2 - Tímapróf - Steinn Þorkelsson
import random

# liður 1
# nota list comprehension til thess ad spara tima stafror er key og tala value
stafrof = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
tolur = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, ]
dict_stafrof = {stafrof[i]: tolur[i] for i in range(len(stafrof))}


def dict_checker(ord, val):
    listi = []
    # Dictionary inniheldur lykil og value, stafur er lykillinn og talan er value ef að stafurinn er i dict þa set eg
    # tolu stafsins i listann
    for stafur, tala in dict_stafrof.items():
        if stafur in ord:
            listi.append(tala)
    if val == 1:
        strengur = f" stafirnir i ordinu '{ord}' eru thessir tolustafir: {listi}"
        return strengur
    elif val == 2:
        return listi


def finnasumma(ord):
    listi = dict_checker(ord, 2)
    summa = 0
    for i in listi:
        summa += i
    return summa


def notanda_input():
    listi = []
    summa = []
    for i in range(2):
        ordid = input("Sladu inn ord i med enska stafrofinu: ")
        listi.append(ordid)
    for a in range(2):
        summa.append(finnasumma(listi[a]))
    print(f"Summa fyrir {listi[0]} er {summa[0]}. Summa fyrir {listi[1]} er {summa[1]}")


# lidur 2


def random_tolur():
    listi = []
    for i in range(100):
        listi.append(random.randrange(0, 51))
    return listi


random_listi = random_tolur()


def skrifa_skra(listi, nafntxt):
    skra = open(nafntxt, 'a')
    bil = " "
    for i in range(len(listi)):
        skra.write(str(listi[i]) + bil)
    skra.close()


def lesa_skra(skratxt):
    skra = open(skratxt, 'r')
    tolur = skra.read().split(" ")
    tolur.pop()
    listi = list(map(int, tolur))
    return listi


def finna_summu_listans():
    listi = lesa_skra("skra.txt")
    summa = 0
    for i in listi:
        summa += i
    return summa


# lidur 3
def svor_vid_spurningum(val):
    if val == 1:
        print("1. Hvenær er eðlilegra að nota tuple heldur en lista í forritun og hvers vegna. Hverjir eru kostir og "
              "gallar tuple og lista?")
        print("Ef þú ert með lista sem að Þú vilt að breytist ekki óvart þegar forritið er í gangi þá er betra að"
              "nota tuple() í stað lista[]. Tuple hefur þann eiginleika að ekki sé hægt að breyta honum "
              "eftir að það sé búið að skilgreina hann. Hinsvegar ef þú ert með lista of gögnum sem þarf regluglega að"
              "breyta þá er þæginlegra að nota venjulegan Lista[] í stað tuple()")
    elif val == 2:
        print("2. Hvernig er einföld útskýring á hvað fall er? Hvað einkennir vel gert fall?")
        print("Fall í einföldu máli er forrit innan í forriti, það sem er þæginlegt við föll er að þú getur notað þau"
              "innan í öðrum föllum / formúlum án þess að þurfa að skrifa allan kóðan innan í fallinu aftur."
              "Gott er að hafa föll sem að gera ekki of marga hluti í einu, það er betra að hafa fullt af litlum föllum"
              "í stað þess að hafa eitt stórt fall vegna þess að þá hefur þú sem mestan sveigjanleika með forritin,"
              "sem forritari þá veistu aldrei hvenær þú þarft að nota það eitt sérstakt fall pg það mun spara þér "
              "höfuðverkin "
              "að búta upp fallið í minni föll")


on = True

while on:
    val_listi = ["Tímaverkefni 2: ", "1. Stafróf", "2. Skráarvinnsla", "3. Svör við spurningum", "4. Hætta í forriti"]
    print()
    for i in val_listi:
        print(i)
    val = input("Veldu lið: ")

    if val == "1":
        on1 = True
        while on1:
            val_listi_1 = ["1. Finna tolustafi í orði", "2. Finna summu 2 orða", "3. Hætta"]
            print()
            for i in val_listi_1:
                print(i)
            val1 = input("Veldu forrit: ")
            if val1 == "1":
                print()
                notanda_ord = input("Sláðu inn orð: ").lower()
                print(dict_checker(notanda_ord, 1))
            elif val1 == "2":
                notanda_input()
            elif val1 == "3":
                on1 = False

    elif val == "2":
        on2 = True
        while on2:

            val_listi_2 = ["1. Skrifa randöm tölu lista í skrá og prenta listan út", "2. Finna summu skránnar",
                           "3. Hætta"]
            print()
            for i in val_listi_2:
                print(i)
            val2 = input("Veldu forrit: ")
            if val2 == "1":
                print()
                skrifa_skra(random_listi, "skra.txt")
                print(lesa_skra("skra.txt"))
            elif val2 == "2":
                print()
                print(f"Summa skránnar er: {finna_summu_listans()}")
            elif val2 == "3":
                on2 = False

    elif val == "3":
        print()
        print(svor_vid_spurningum(1))
        print()
        print(svor_vid_spurningum(2))

    elif val == "4":
        on = False
