texti = "Bilbo"
skra = open("kennsla.txt", "w", encoding="utf8")
skra.write(texti)
skra.close()

skra = open("kennsla.txt", "r", encoding="utf8")
utkoma = skra.read()
skra.close()
print(utkoma)
