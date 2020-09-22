# FORR2FA05BU - Skilaverkefni 1 - Steinn Þorkelsson
import random

on = True
while on:
    print("1. Nöfn")
    print("2. Random Tölur")
    print("3. Skráning í áfanga")
    print("4. Listi fyrir tölur")
    print("5. Teningakast")
    print("6. Hætta í forriti")

    val = input("Veldu Forrit: ")
    if val == "1":
        nofn = input("Sláðu inn 5 nöfn með millibili: ")

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
            print("1. Birta nöfnin óraðað.")
            print("2. Raða nöfnunum í stafrófsröð og birta.")
            print("3. Raða nöfnunum í öfuga stafrófsröð og birta.")
            print("4. Birta eitt nafn eftir því hvaða númer 1-5 var valið.")
            print("5. Hætta í Dæmi 1.")
            val1 = input("Veldu aðgerð: ")
            print()

            if val1 == "1":
                print(nafnalisti)
                print()
            elif val1 == "2":
                radad = sorted(nafnalisti)
                print(radad)
                print()
            elif val1 == "3":
                ofugt = sorted(nafnalisti, reverse=True)
                print(ofugt)
                print()
            elif val1 == "4":
                val = int(input("Veldu nafn til að birta: "))
                # það er -1 vegna þess að fyrsta orðið í listanum er nr.0 og síðasta er nr.4

                print(nafnalisti[val - 1])
                print()
            elif val1 == "5":
                on1 = False

    elif val == "2":
        random = random.sample(range(0, 501), 70)
        print(f"random tölur: {random}")
        print()
        on1 = True
        while on1:
            print("1. Birta tölurnar 4 í línu:")
            print("2. Stærsta og lægsta talan í listanum")
            print("3. Birta listann í öfugri röð 6 tölur í línu")
            print("4. Hversu margar eru frá bilinu 1-250 og 251-500")
            print("5. Hætta í Dæmi 2")
            val1 = input("Veldu aðgerð: ")

            if val1 == "1":
                for i in range(0, len(random), 4):
                    print(*random[i:i+4], sep=' ')
            elif val1 == "2":
                print()
                print("Stærsta talan og Lægsta talan:")
                print(f"{max(random)} {min(random)}")
                print()
            elif val1 == "3":
                ofugt = random.copy()
                ofugt.reverse()
                print(ofugt)
                for i in range(0, len(ofugt), 4):
                    print(*ofugt[i:i:4], sep=' ')
            elif val1 == "4":
                minni = 0
                staerri = 0
                for m in random:
                    if 251 > m > 0:
                        minni += 1
                for s in random:
                    if 501 > s > 250:
                        staerri += 1
                print()
                print(f"Það eru {minni} tölur á bilinu 1-250 og {staerri} tölur á bilinu 251-500")
                print()
            elif val1 == "5":
                on1 = False
    elif val == "3":
        nemendur = int(input("Hvað er margir í forr2 áfanganum?"))
        nofn = input("Nöfn nemendana: ")
        print()

        # 1 setja nöfnin í lista með for lykkju
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

        # 2 nýr listi með nöfnunum raðað eftir stafrófsröð
        radadnafn = sorted(nafnalisti)

        # 3 prenta listan eitt orð í einu
        print(*nafnalisti, sep="\n")
        print()
        # 4 eyða nafni
        # nýr listi til þess að sá upprunalegi breytist ekki fyrir síðasta liðinni í dæminu
        nynofn = nafnalisti.copy()
        eyda = input("Veldu nafn til þess að eyða út: ")
        nynofn.remove(eyda)
        print(nynofn)
        print()

        # 5 bæta við nafni í listann
        vidbot = input("Bættu við nafni í listan: ")
        nynofn.append(vidbot)
        print(nynofn)
        print()
        # 6 Prenta upprunalega listann
        print(f"Upprunalegu nemendurnir: {nafnalisti}")
        print()
    elif val == "4":
        on1 = True
        while on1:
            tolur = input("Sláðu inn 7 tölur með millibili eða 'x' til að hætta: ")

            if tolur != "x":

                bil = 0
                for b in tolur:
                    if b == ' ':
                        bil += 1

                if bil == 6:
                    strengjalisti = []
                    temp = ''
                    for c in tolur:
                        if c == ' ':
                            strengjalisti.append(temp)
                            temp = ''
                        else:
                            temp += c

                    # fyrir síðustu töluna
                    if temp:
                        strengjalisti.append(temp)
                    # print(strengjalisti)
                    # breyta strengjalistanum í tölur
                    talnalisti = [int(i) for i in strengjalisti]
                    #  print(talnalisti)
                    # stærsta og lægsta talan í listanum
                    print(f"Stærsta talan er {max(talnalisti)} og minnsta talan er {min(talnalisti)}")
                    print(f"Meðaltal talnanna er {sum(talnalisti) / len(talnalisti)}")
                    print(f"Summa talnanna er {sum(talnalisti)}")

                    print(f"Tölurnar eftir stærðarröð: {sorted(talnalisti, reverse=True)}")
                    for t in range(len(talnalisti)):
                        print(talnalisti[t], end="; ")
                    print()
                else:
                    print("Villa Reyndu aftur")
                    on1 = True
            else:
                on1 = False

    elif val == "5":
        oftlisti = []
        oft = int(input("Hversu of viltu kasta teningnunum?: "))
        teningakast = []
        for x in range(oft):
            kast1 = random.randint(1, 6)
            kast2 = random.randint(1, 6)
            print(f"Kast nr.{x + 1}: T1 = {kast1} T2 = {kast2}")
            teningakast.append(kast1)
            teningakast.append(kast2)
        print(sorted(teningakast))
        print()
        for x in range(1, 7):
            oftlisti.append(teningakast.count(x))
            print(f" {x} kom upp {teningakast.count(x)}")
        oftast = max(oftlisti)
        print(f"Talan sem kom oftast er: {oftlisti.index(oftast)+1}")
        print(f"Talan sem kom sjaldnast er: {oftlisti.index(min(oftlisti))+1}")
    elif val == "6":
        on = False
    else:
        print("Villa, reyndu aftur")
        print()
        on = True
