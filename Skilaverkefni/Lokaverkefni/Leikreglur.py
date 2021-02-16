# from hermenn_func import bua_til_hermann
import hermenn_func as hermenn

# import time
pessar = hermenn.bua_til_hermann("Pessar")
hettir = hermenn.bua_til_hermann("Hattar")
dreyrar = hermenn.bua_til_hermann("Dreyrar")

aettbalka_listi = [pessar, hettir, dreyrar]

notanda_aettbalkur = []


# for i in aettbalka_listi:
#    for h in i:
#        print(h)


def bardagi(hermadur_1, hermadur_2):
    sigurvegari = 0

    on = True

    while on:
        hermadur_1.meidast(hermadur_2.get_afl())
        hermadur_2.meidast(hermadur_2.get_afl())
        print()
        print(f"{hermadur_1.get_aettbalkur()} og {hermadur_2.get_aettbalkur()} ráðast á hvorn annan")
        print()
        print(
            f"{hermadur_1.get_aettbalkur()} meiðir {hermadur_2.get_aettbalkur()} um {hermadur_1.get_afl()} með {hermadur_1.get_vopn()}")
        print(
            f"{hermadur_2.get_aettbalkur()} meiðir {hermadur_1.get_aettbalkur()} um {hermadur_2.get_afl()} með {hermadur_2.get_vopn()}")

        hermadur_1.missa_afl()
        hermadur_2.missa_afl()
        print()
        print(f"{hermadur_1.get_aettbalkur()} er með {hermadur_1.get_lif()} Lif og {hermadur_1.get_afl()} Afl")
        print(f"{hermadur_2.get_aettbalkur()} er með {hermadur_2.get_lif()} Lif og {hermadur_2.get_afl()} Afl")

        if hermadur_1.daudur():
            on = False
        if hermadur_2.daudur():
            on = False
        # time.sleep(2)
        input("Ýttu á Enter til að halda áfram: ")
    if hermadur_1.get_lif() > hermadur_2.get_lif():
        print()
        print(f"{hermadur_1.get_aettbalkur()} vann bardagann")
        sigurvegari = 1

    elif hermadur_2.get_lif() > hermadur_1.get_lif():
        print()
        print(f"{hermadur_2.get_aettbalkur()} vann bardagann")
        sigurvegari = 2

    else:
        print()
        print(f"{hermadur_1.get_aettbalkur()} og {hermadur_2.get_aettbalkur()} drápust báðir í bardaganum")

    return sigurvegari


# Fall til þess að velja 2 ættbálka og skila lista með báðum ættbálkunum
def velja_keppendur(listi):
    keppanda_listi = []
    on_v = True
    while on_v:
        print()
        print("1. Pessar")
        print("2. Hettir")
        print("3. Dreyrar")

        val = int(input("Veldu lid 1: "))
        val_2 = int(input("Veldu lid 2: "))

        if val == val_2:
            print("Ekki er haegt ad velja sama lidid tvisvar")

        else:
            keppanda_listi.append(listi[val - 1])
            keppanda_listi.append(listi[val_2 - 1])
            on_v = False
    return keppanda_listi


def leikreglur():
    strengur = f"\nHver hermaður fær random afl og líf\n hermaðurinn fær random Vopn sem meiða öll mismunandi \n" \
               f"Exi bætir 1 afl vid, Sverð 2, Spjöt meiðir 3\n \n" \
               f"Leikreglur: \n Báðir hermenn ráðast á hvorn annan á sama tíma, \n" \
               f"Sá sem sigrar bardagan heldur áfram í næsta bardaga"

    return strengur


print(leikreglur())
print()
input("Ýttu á enter til þess að byrja leikinn: ")

keppendur = velja_keppendur(aettbalka_listi)

nofn = [keppendur[0][0].get_aettbalkur(), keppendur[1][0].get_aettbalkur()]

on_l = True

while on_l:
    if keppendur[0] and keppendur[1]:
        bardagi(keppendur[0][0], keppendur[1][0])

        if keppendur[0][0].daudur():
            keppendur[0].pop(0)
        if keppendur[1][0].daudur():
            keppendur[1].pop(0)
        else:
            keppendur[0].pop(0)
            keppendur[1].pop(0)
    else:
        if len(keppendur[0]) > len(keppendur[1]):
            print()
            print(f"{nofn[0]} unnu.")
        elif len(keppendur[1]) > len(keppendur[0]):
            print()
            print(f"{nofn[1]} unnu.")
        else:
            print()
            print(f"{nofn[0]} og {nofn[1]} útrýmdu hvorn annan.")
        on_l = False
