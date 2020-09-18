import math


def rummalkulu(r):
    utkoma = (4 * math.pi * math.pow(r, 3)) / 3
    return round(utkoma)


def rummalkassa(h, b, l):
    utkoma = (h * b * l)
    return round(utkoma)


def thrihyrningur(b, h):
    utkoma = (b * h) / 2
    return round(utkoma)


on = True
while on:
    print("1. Rúmmál kúlu.")
    print("2. Rúmmál Kassa.")
    print("3. flatarmál þríhyrnings.")
    print("4. Hætta")

    val = input("Veldur forrit: ")

    if val == "1":
        radius = int(input("sladu inn radius kulunnar: "))
        print(rummalkulu(radius))
        print()
    elif val == "2":
        hæd = int(input("hæd kassans: "))
        breidd = int(input("breidd kassans: "))
        lengd = int(input("lengd kassans: "))
        print(rummalkassa(hæd, breidd, lengd))
        print()
    elif val == "3":
        hæd = int(input("Hæd Thríhyrningsins:"))
        breidd = int(input("Breidd Thríhyrningsins: "))
        print(thrihyrningur(breidd, hæd))
        print()
    elif val == "4":
        on = False
    else:
        on = True



