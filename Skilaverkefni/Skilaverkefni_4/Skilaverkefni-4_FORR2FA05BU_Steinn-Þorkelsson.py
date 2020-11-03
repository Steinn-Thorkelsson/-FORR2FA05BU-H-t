# FORR2 - Skilaverkefni 3 - Steinn Þorkelsson

# Lidur 1 --------------------------------------------------------------------------------------------------------------
# 1A

def sletttolu_listi():
    tolulisti = []
    for t in range(2, 1001, 2):
        tolulisti.append(t)
    return tolulisti


# 1B
def skrifaiskra(listi, nafntxt):
    skra = open(nafntxt, 'w', encoding="utf8")
    for x in listi:
        skra.write(str(x) + " ")
    skra.close()


# 1C
def lesa_skra(skratxt):
    skra = open(skratxt, 'r')
    tolur = skra.read().split(" ")
    tolur.pop()
    tolur = list(map(int, tolur))
    return tolur


# 1D
def prenta(listi):
    print(listi)


# 1E
def medaltal(listi):
    # lengd = len(listi)
    # heildarstaerd = 0
    # for i in listi:
    #     heildarstaerd += i
    # medaltal = heildarstaerd / lengd
    utkoma = sum(listi) / len(listi)

    return round(utkoma, 2)


# 1F
def gengur_i_8(listi):
    nyr_listi = []
    for x in listi:
        if x % 8 == 0:
            nyr_listi.append(x)
    return nyr_listi


# 1G
def prenta_tiu(listi):
    teljari = 1
    for x in listi:
        if teljari % 10 == 0:
            print(x)
        else:
            print(x, end=" ")
        teljari += 1


# Liður 2 --------------------------------------------------------------------------------------------------------------
# 2A
def primtolu_listi():
    prim_listi = []
    for num in range(0, 101):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prim_listi.append(num)

    return prim_listi


primtolur = primtolu_listi()
skrifaiskra(primtolur, "primtolur.txt")

lesa_primtolur = lesa_skra("primtolur.txt")
prenta(lesa_primtolur)


def inniheldur_7(listi):
    nyr_listi = []
    str_listi = [str(i) for i in listi]
    for i in str_listi:
        if '7' in i:
            nyr_listi.append(i)
    int_nyr_listi = [int(i) for i in nyr_listi]
    print(int_nyr_listi)


inniheldur_7(lesa_primtolur)


def fjorda_hver_tala(listi):
    fjorda_hver_listi = []
    for i in range(3, len(listi), 3):
        fjorda_hver_listi.append(listi[i])
    return fjorda_hver_listi


fjorda_hver_tala_listi = fjorda_hver_tala(lesa_primtolur)
skrifaiskra(fjorda_hver_tala_listi, "fjorda.txt")

print(fjorda_hver_tala(lesa_primtolur))

on = True

while on:
    val_listi = ["------ Skilaverkefni 4 -------", '1. Sléttartölur', '2. Prímtölur', '3. Tuple skrá', '4. Dictionary',
                 '5. Hætta í forriti']
    print()
    for x in val_listi:
        print(x)
    print()
    val = input("Veldu Lið: ")

    if val == "1":
        on1 = True
        while on1:
            val1_listi = ['------ Liður 1 ------', '------Sléttar tölur ------', '1. Prenta sléttölur upp í þúsund',
                          "2. Prenta Meðaltal skránnar",
                          '3. Búa til nýja lista með tölum sem 8 gengur upp í og prenta',
                          "4. Prenta fyrri listann með 10 tölum í hverri röð", "5 Hætta í Lið 1"]
            print()
            for x in val1_listi:
                print(x)
            print()
            val1 = input("Veldu fall: ")

            lesa_skra_listi = lesa_skra("slettolur.txt")

            if val1 == "1":

                slettartolulisti = sletttolu_listi()
                skrifaiskra(slettartolulisti, "slettolur.txt")

                print()
                print("Slétttölur upp í þúsund")
                prenta(lesa_skra_listi)

            elif val1 == "2":

                print()
                print('Meðaltal skránnar:')
                print(medaltal(lesa_skra_listi))

            elif val1 == "3":

                print()
                print('Nýr listi með tölum sem talan 8 gengur upp í:')
                gengur_i_8_listi = gengur_i_8(lesa_skra_listi)
                skrifaiskra(gengur_i_8_listi, "sumartolur.txt")
                lesa_8_listi = lesa_skra("sumartolur.txt")
                prenta(lesa_8_listi)

            elif val1 == "4":
                print()
                print('Tíu tölur í hverri röð: ')
                prenta_tiu(lesa_skra_listi)

            elif val1 == "5":
                on1 = False

    elif val == "2":

        primtolur = primtolu_listi()
        skrifaiskra(primtolur, "primtolur.txt")

        on2 = True
        while on2:
            val2_listi = ["------ Liður 2 -----", "------ Prímtölur ------", "1. Búa til Prímtölu lista og prenta",
                          "2. Finna allar prímtölur sem innihalda töluna 7 ", "3. Finna 4 hverja prímtölu", "4. Hætta"]
            print()
            for i in val2_listi:
                print(i)
            print()
            val2 = input("Veldu fall: ")
            print()

            if val2 == "1":
                print()
                lesa_primtolur = lesa_skra("primtolur.txt")
                prenta(lesa_primtolur)

            elif val2 == "2":
                print()
                inniheldur_7(lesa_primtolur)

            elif val2 == "3":
                fjorda_hver_tala_listi = fjorda_hver_tala(lesa_primtolur)
                skrifaiskra(fjorda_hver_tala_listi, "fjorda.txt")

                print(fjorda_hver_tala(lesa_primtolur))
            elif val2 == "4":
                on2 = False

    elif val == "3":
        pass

    elif val == "4":
        pass

    elif val == "5":
        break
