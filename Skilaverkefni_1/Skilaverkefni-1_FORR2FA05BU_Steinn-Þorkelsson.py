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
        nofn = input("Sláðun inn 5 nöfn með millibili: ")

        nafnalisti = []
        temp = ''
        for c in nofn:
            if c == ' ':
                nafnalisti.append(temp)
                temp = ''
            else:
                temp += c

        # fyrir síðasta orðið
        if temp:
            nafnalisti.append(temp)
        print()

        on1 = True
        while on1:
            print("Hvað viltu gera við nöfnin?")
            print("1.Birta nöfnin óraðað.")
            print("2.Raða nöfnunum í stafrófsröð og birta.")
            print("3.Raða nöfnunum í öfuga stafrófsröð og birta.")
            print("4.Birta eitt nafn eftir því hvaða númer 1-5 var valið.")
            print("5. Hætta í forriti.")
            val1 = input("Veldu aðgerð: ")

            if val == "1":
                print(nafnalisti)
            if val == "2":
                radad = sorted(nafnalisti)
                print(radad)
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

    elif val == "3":
        nemendur = int(input("Hvað er margir í forr2 áfanganum?"))
        nofn = input("Nöfn nemendana: ")

        nafnalisti = []
        tmp = ''
        for c in nofn:
            if c == ' ':
                nafnalisti.append(tmp)
                tmp = ''
            else:
                tmp += c

        # fyrir síðasta orðið
        if tmp:
            nafnalisti.append(tmp)
        print()

        #nýr listi með nöfnunum raðað eftir stafrófsröð
        radadnafn = sorted(nafnalisti)

        # prenta listan eitt orð í einu
        print(*nafnalisti, sep="\n")
        print()

        eyda = input("Veldu nafn til þess að eyða út: ")
        nafnalisti.remove(eyda)
        print(nafnalisti)

        vidbot = input("Bættu við nafni í listan")
        nafnalisti.append(vidbot)
        print(nafnalisti)








