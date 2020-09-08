# FORR2FA05BU - Skilaverkefni 1 - Steinn Þorkelsson

on = True
import random
while on:
    print("1.Dæmi - Nöfn")
    print("2.Dæmi")
    print("3.Dæmi")
    print("4.Dæmi")
    print("5.Dæmi")
    print("Hætta í forriti")

    val = input("Veldu Forrit: ")
    if val == "1":
        nafn = input("Sláðun inn 5 nöfn með millibili: ")
        on1 = True
        while on1:
            print("Hvað viltu gera við nöfnin?")
            print("1.Birta nöfnin óraðað.")
            print("2.Raða nöfnunum í stafrófsröð og birta.")
            print("3.Raða nöfnunum í öfuga stafrófsröð og birta.")
            print("4.Birta eitt nafn eftir því hvaða númer 1-5 var valið.")
            print("5. Hætta í forriti.")
            val1 = input("Veldu aðgerð: ")
            listi = nafn.split(" ")

            if val1 == "1":
                print(nafn)

            elif val1 == "2":
                radad = sorted(listi)
                print(radad)
            elif val1 == "3":
                ofugt = sorted(listi, reverse=True)
                print(ofugt)
            elif val1 == "4":
                tala = int(input("Veldu tölu frá 1-5: "))
                print(listi[tala - 1])
            elif val1 == "5":
                on1 = False

    elif val == "2":
        random = random.sample(range(0, 501), 70)
        print(random)
        for i in range(0, len(random), 4):
            print(*random[i:i+4], sep=' ')

        print("Stærsta talan og Lægsta talan:")
        print(f"{max(random)} {min(random)}")
        random.reverse()
        for i in range(0, len(random), 6):
            print(*random[i:i+4], sep=' ')
        teljari = 1
            for x in listi:
                if teljari % 6 == 0:
                    print(x)


    elif val == "4":
        oftlisti = []
        oft = int(input("Hversu oft viltu kasta teningi 1?: "))
        teningakast = []








