def brandari():
    print("Prótein")


brandari()


def brandarar(nrbrandara):
    if nrbrandara == 1:
        print("Speggi")
    elif nrbrandara == 2:
        print("sportbolti")
    elif nrbrandara == 3:
        print("monkey")
    else:
        print("þessi tala er ekki brandari")


brandaraval = int(input("Veldu brandara 1 2 eða 3: "))

brandarar(brandaraval)


def heilsun(kyn):
    if kyn == "KK":
        print("Þú ert karlmaður")
    elif kyn == "KVK":
        print("Þú er ert kvenmaður")
    elif kyn == "HK":
        print("Þú ert kynsegin")


kynval = input("Veldu Kynið þitt KK, KVK eða HK: ").upper()

heilsun(kynval)
