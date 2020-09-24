import random


# Dæmi 1
# Geri return í staðin fyrir print svo að ég ráði hvenær ég vill prenta út útkomunni
def fahren_cel(f):
    c = (f - 32) / 1.8
    return round(c, 3)


def cel_fahren(c):
    f = c * 1.8 + 32
    return round(f, 3)


##############################################


# Dæmi 2
def hversuhratt(h):
    print(f"Þú ókst á {h}Km hraða")
    if h < 90:
        print("ókilidókílí")
    elif h > 90:
        # nota heiltölu deilingu "//" til þess að sleppa við kommu
        refsistig = (h - 90) // 5
        print(f"Þú ert með {refsistig} refsistig")
        if refsistig >= 12:
            print("þú hefur misst Ökuskírteinið þitt vegna hraðaksturs")


##############################################


# Dæmi 3
def reiknaveldi(tala, veldi):
    # ** er til þess að reikna veldi
    utkoma = tala ** veldi
    return utkoma


##############################################


# Dæmi 4
def reiknabmi(kg, m):
    bmi = round(kg / (m * m), 2)

    if bmi >= 18.4 and bmi < 26:
        return f"Þitt bmi er {bmi}. Þú ert í kjörþyngd"

    elif bmi < 18.5:
        return f"Þitt bmi er {bmi}. Þú ert í undirþyngd"

    elif bmi >= 25 and bmi < 30:
        return f"Þitt bmi er {bmi}. Þú ert í yfirþyngd"

    elif bmi >= 30:
        return f"Þitt bmi er {bmi}. Þú ert í offitu"

    else:
        return "Villa"


##############################################


# Dæmi 5 
def gallon_i_litra(g):
    liter = g * 3.785
    return liter


def litrar_i_gallon(l):
    gallon = l / 3.785
    return gallon


##############################################


# Dæmi 6
def heilsa(n):
    # Nota slicing aðferð til þess að búta nafnið upp í N jafna parta
    if n[-3:] == "son":
        return f"Sæll og blessaður {n}"

    elif n[-6:] == "dóttir":
        return f"Sæl og blessuð {n}"

    else:
        return "Ég þekki ekki þessa endingu"


##############################################


# Dæmi 7
def tkast(hveoft):
    summa = 0
    teljari = 1
    # nota range() til þess að segja forritinu hversu oft ég vil kasta teningnum
    for x in range(hveoft):
        kast = random.randint(1, 6)
        print(f"Kast {teljari}: {kast}")

        teljari += 1
        summa += kast

    return f"Þú kastðir teningnum {hveoft} sinnum og summa kastana er {summa}"


##############################################


# Dæmi 8
def eins(l1, l2, l3):
    l4 = []

    for el in l1:
        if el in l2:
            if el in l3:
                l4.append(el)
    return f"Listi 1,2 og 3 innhalda allar þessa Tölu/r: {l4}"


on = True

while on:
    print("1. Celslíus og farenheit")
    print("2. Hraðatakmörk")
    print("3. Veldisreikningur")
    print("4. BMI")
    print("5. Gallon og Lítrar")
    print("6. Heilsa")
    print("7. Teningakast")
    print("8. Listar")
    print("9. Hætta í forriti")
    print()
    # ég nota ekki int(input("")) til þess að forðast villu meldingu ef að notandinn slær inn char í staðinn fyrir int 
    val = input("Veldu Lið: ")

    if val == "1":
        print("1 = Fahrenheit í Celsíus")
        print("2 = Celsíus Í Fahreinheit")
        graduval = input("Veldu Aðgerð: ")
        if graduval == "1":
            fahren = int(input("Sláðu inn Fahreinheit gráðu: "))
            print(f"{fahren}F eru {fahren_cel(fahren)}C")

        elif graduval == "2":
            cel = int(input("Sláðu inn Celsíus gráðu: "))
            print(f"{cel}C eru {cel_fahren(cel)}f")
    elif val == "2":
        hradi = int(input("Sláðu inn hraðan sem þú ókst á í KM: "))
        hversuhratt(hradi)
        print()

    elif val == "3":
        t = float(input("Sláðu inn tölu með kommu eða ekki: "))
        v = float(input("Sláðu inn veldistölu með kommu eða ekki: "))
        print(reiknaveldi(t, v))
        print()

    elif val == "4":
        w = float(input("Sláðu inn þyngd í kg: "))
        h = float(input("Sláðu inn hæð í metrurm: "))
        print(reiknabmi(w, h))

    elif val == "5":
        print("1. Gallon í Lítra")
        print("2. Lítrar í Gallon")
        val5 = input("Veldu aðgerð: ")
        print()

        if val5 == "1":
            gallon = int(input("Sláðu inn magn í Gallon: "))
            print()
            print(f"{gallon} Gallon er {round(gallon_i_litra(gallon), 2)} Lítrar")
            print()

        if val5 == "2":
            liter = int(input("Sláðu inn magn í Lítrum: "))
            print()
            print(f"{liter} Lítrar er {round(litrar_i_gallon(liter), 2)} Gallon")
            print()

    elif val == "6":
        nafn = input("Sláðu inn fullt nafn: ")
        print(heilsa(nafn))
        print()

    elif val == "7":
        oft = int(input("Hversu oft viltu kasta teningnum?: "))
        print(tkast(oft))
    elif val == "8":
        l1 = [1, 2, 3]
        l2 = [2, 3, 4]
        l3 = [3, 4, 5]
        print(eins(l1, l2, l3))
        print()
    elif val == "9":
        on = False
