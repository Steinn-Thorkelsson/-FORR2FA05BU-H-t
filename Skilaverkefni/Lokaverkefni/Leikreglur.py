# from hermenn_func import bua_til_hermann
import hermenn_func as hermenn
import time

pessar = hermenn.bua_til_hermann("Pessi")
hettir = hermenn.bua_til_hermann("Hattur")
dreyrar = hermenn.bua_til_hermann("Dreyri")
print(pessar[1].get_afl())

aettbalka_listi = [pessar, hettir, dreyrar]

notanda_aettbalkur = []

for i in aettbalka_listi:
    for h in i:
        print(h)


def bardagi(hermadur_1, hermadur_2):
    sigurvegari = 0

    on = True

    while on:
        hermadur_1.meidast(hermadur_2.get_afl())
        hermadur_2.meidast(hermadur_2.get_afl())

        print(f"{hermadur_1.get_aettbalkur()} og {hermadur_2.get_aettbalkur()} ráðast á hvorn annan")
        print(
            f"{hermadur_1.get_aettbalkur()} meiðir {hermadur_2.get_aettbalkur()} um {hermadur_1.get_afl()} með {hermadur_1.get_vopn()}")
        print(
            f"{hermadur_2.get_aettbalkur()} meiðir {hermadur_1.get_aettbalkur()} um {hermadur_2.get_afl()} með {hermadur_2.get_vopn()}")

        hermadur_1.missa_afl()
        hermadur_2.missa_afl()

        print(f"{hermadur_1.get_aettbalkur()} er með {hermadur_1.get_lif()} Lif og {hermadur_1.get_afl()} Afl")
        print(f"{hermadur_2.get_aettbalkur()} er með {hermadur_2.get_lif()} Lif og {hermadur_2.get_afl()} Afl")

        if hermadur_1.daudur():
            on = False
        if hermadur_2.daudur():
            on = False
        time.sleep(2)

    if hermadur_1.get_lif() > hermadur_2.get_lif():

        print(f"{hermadur_1.get_aettbalkur()} vann bardagann")
        sigurvegari = 1

    elif hermadur_2.get_lif() > hermadur_1.get_lif():

        print(f"{hermadur_2.get_aettbalkur()} vann bardagann")
        sigurvegari = 2

    else:
        print(f"{hermadur_1.get_aettbalkur()} og {hermadur_2.get_aettbalkur()} drápust báðir í bardaganum")

    return sigurvegari


keppendur = []
bardagi(pessar[0], hettir[2])
print(pessar[0].daudur())
# while len(keppendur[0]) > 0 or len(keppendur[1]) > 0:
#     print()
#     print("Velkomin i staersta bardaga sögunnar")
#     print("1. Berjast sjálfur")
#     print("2. Tölvan berst fyrir þig")
#
#     val = input("Veldu aðgergð: ")
#
#     if val == "1":
#         print()
#         print("1. Pessar")
#         print("2. Hettir")
#         print("3. Dreyrar")
#
#         val_1 = input("Veldu ættbálk: ")
#         print()
#         if val_1 == "1":
#             print("Þú hefur valið Pessa.")
#             for i in aettbalka_listi[0]:
#                 notanda_aettbalkur.append(i)
#
#         elif val_1 == "2":
#             print("Þú hefur valið Hetti.")
#             for i in aettbalka_listi[1]:
#                 notanda_aettbalkur.append(i)
#
#         elif val_1 == "3":
#             print("Þú hefur valið Dreyra.")
#             for i in aettbalka_listi[2]:
#                 notanda_aettbalkur.append(i)
#
#         for i in notanda_aettbalkur:
#             print(i)
#         bardagi()
#     elif val == "2":
#         bardagi()
