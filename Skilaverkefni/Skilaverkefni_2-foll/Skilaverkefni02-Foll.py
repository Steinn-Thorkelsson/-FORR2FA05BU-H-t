# Dæmi 1
# Geri return í staðin fyrir print svo að ég ráði hvenær ég vill prenta út útkomunni
def fahren_cel(f):
    c = (f-32) / 1.8
    return round(c, 3)


def cel_fahren(c):
    f = c * 1.8 + 32
    return round(f, 3)
##############################


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
##################################


def reiknaveldi(tala, veldi):
    # ** er til þess að reikna veldi
    utkoma = tala**veldi
    return utkoma


on = True

while on:
    print("1. Celslíus og farenheit")
    print("2. Hraðatakmörk")
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