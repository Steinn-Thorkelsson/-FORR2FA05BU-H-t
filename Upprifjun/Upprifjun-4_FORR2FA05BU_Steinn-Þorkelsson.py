# FORR2FA05BU - Upprifjun 4 - Steinn Þorkelson
on = True

while on:
    print("Upprifjun 4")
    print()
    print("1.Dæmi")
    print("2.Dæmi")
    print("3.Dæmi")
    print("4.Dæmi")
    print("5.Dæmi")
    print("6. Hætta í forriti")

    val = input("Veldu forrit: ")

    if val == "1":
        texti = input("Sláðu inn setningu: ").upper()
        nstafir = 0
        for n in texti:
            if n == "N":
                nstafir += 1
        print(f"Það eru {nstafir} n bókstafir í setningunni")

    if val == "2":
