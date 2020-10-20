einkunn = "10 2 8 7 5"
skra = open("einkunnir.txt", "w", encoding="utf8")
for x in range(5):
    tala = input("Sladu inn tolu:")
    skra.write(tala+" ")

skra.close()

einkunn = open("einkunnir.txt", "r", encoding="utf8")
utkoma = einkunn.read()
listi = utkoma.split()
skra.close()
einkunn_listi = list(map(int, listi))
print("Einkunnar listi", einkunn_listi)

heildareinnkunn = 0

for i in range(len(einkunn_listi)):
    heildareinnkunn += einkunn_listi[i]

medal_einkunn = heildareinnkunn / len(einkunn_listi)
print("Heildareinkunn", heildareinnkunn)
print("Medaleinkunn", medal_einkunn)
