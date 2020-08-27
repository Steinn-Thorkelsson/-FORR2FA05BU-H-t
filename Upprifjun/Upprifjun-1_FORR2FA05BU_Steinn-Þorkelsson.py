# FORR2FA05BU - Upprifjun 1 - Steinn Þorkelsson

on = True

while on:
    print("1. Samlagning")
    print("2. Heilsa")
    print("3. Km í M")
    print("4. Laun reiknivél")
    print("5. Laun reiknivél með skatt")
    print("6. Gráður")
    print("7. Hætta")
    val = input("Veldu Forrit: ")

    if val == "1":
        tala1 = float(input("Tala 1: "))
        tala2 = float(input("Tala 2: "))
        summa = tala1 + tala2
        print(f"{tala1} + {tala2} = {summa} ")
    elif val == "2":
        fornafn = input("Fornafn?: ")
        eftirnafn = input("Eftirnafn?: ")
        print(f" Halló {fornafn} {eftirnafn}")
    elif val == "3":
        km = float(input("Lengd í Kílómetrum?: "))
        m = km * 1000
        print(f"{km} Kílómetrar eru {m} Metrar")
    elif val == "4":
        laun = int(input("Laun á Klukkustund: "))
        timi = int(input("Fjöldi klukkustunda sem unni er?: "))
        heildarlaun = laun * timi
        print(f"Heildarlaun eru þá Kr. {heildarlaun}")
    elif val == "5":
        laun = int(input("Laun á Klukkustund: "))
        timi = int(input("Fjöldi klukkustunda sem unni er?: "))
        heildarlaun = laun * timi
        if heildarlaun < 30000:
            print(f"Heildarlaun eru þá Kr. {heildarlaun}")
        elif heildarlaun > 30000:
            skattur = heildarlaun * 0.80
            print(f"Heildarlaun eru þá Kr. {skattur}")
    elif val == "6":
        gradur = int(input("Hversu margar gráður?: "))
        hringur = gradur / 360
        print(f"{gradur} eru {hringur} hringur/hringir")
    elif val == "7":
        on = False
