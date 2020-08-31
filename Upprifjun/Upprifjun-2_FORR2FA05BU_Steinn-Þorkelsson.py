# FORR2FA05BU - Upprifjun 2 - Steinn Þorkelson

on = True

while on:
    print("Upprifjun 2")
    print()
    print("1.Dæmi")
    print("2.Dæmi")
    print("3.Dæmi")
    print("4.Dæmi")
    print("5.Dæmi")
    print("6.Hætta í Forriti")

    val = input("Veldu tölu: ")

    if val == "1":
        fyrra1 = input("Sláðu inn Fyrra nafn: ")
        haed1 = int(input("Sláðu inn Hæð í sentimetrum: "))
        fyrra2 = input("Sláðu inn seinna nafn: ")
        haed2 = int(input("Sláðu inn Hæð í sentimetrum: "))
        if haed1 > haed2:
            print(f"{fyrra1} er stærri en {fyrra2}.")
        elif haed1 < haed2:
            print(f"{fyrra2} er stærri en {fyrra1}.")
        else:
            print(f"{fyrra1} og {fyrra2} eru jafnhá.")
    elif val == "2":
        lengd = int(input("Lengd í  metrum: "))
        breidd = int(input("Breidd í metrum: "))
        ekra = lengd * breidd / 4046
        print(f"Þessi reitur er {ekra} ekrur.")
    elif val == "3":
        breidd = int(input("Breidd í metrum: "))
        print(f"10m Lengd = {10 * breidd / 4046} Ekrur.")
        print(f"20m Lengd = {20 * breidd / 4046} Ekrur.")
        print(f"30m Lengd = {30 * breidd / 4046} Ekrur.")
        print(f"40m Lengd = {40 * breidd / 4046} Ekrur.")
        print(f"50m Lengd = {50 * breidd / 4046} Ekrur.")
        print(f"60m Lengd = {60 * breidd / 4046} Ekrur.")
        print(f"70m Lengd = {70 * breidd / 4046} Ekrur.")
        print(f"80m Lengd = {80 * breidd / 4046} Ekrur.")
        print(f"90m Lengd = {90 * breidd / 4046} Ekrur.")
        print(f"100m Lengd = {100 * breidd / 4046} Ekrur.")
        print(f"200m Lengd = {200 * breidd / 4046} Ekrur.")
    elif val == "4":
        afangi = input("Heiti áfanga: ")
        if len(afangi) == 7:
            if afangi[0:3].isupper() and afangi[3:7].isdigit():
                print(f"{afangi} er rétt skammstöfun.")
        else:
            print(f"{afangi} er ekki rétt skammstöfun.")
    elif val == "5":
        heild = int(input("Hver er heildin?: "))
        prosenta = int(input("Hver er %?: "))
        summa = heild * prosenta / 100
        print(f"Niðurstaðan: {summa}")
    elif val == "6":
        print("Bless")
        on = False
    else:
        print("Villa, Reyndu aftur")
        on = True