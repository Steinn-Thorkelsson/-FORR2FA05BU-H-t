

listi = [1, 2, 3, 4, 5, 20]
def skrifaut(listi):
    print("listinn: ", end=" ")
    for i in range(0, len(listi)):

        print(listi[i], end=" ")




def staersta(listi):
    storasta = listi[0]
    for tala in listi:
        if tala > storasta:
            storasta = tala
    return storasta




def minnsta(listi):
    minnsta = listi[0]
    for tala in listi:
        if tala < minnsta:
            minnsta = tala
    return minnsta





def summa(listi):
    summur = 0
    for i in listi:
        summur += i
    return summur




def medaltal(listi):
    summan = summa(listi)
    lengd = 0
    for i in listi:
        lengd += 1
    average = summan / lengd
    return average



def setning(nafn='konni', action='sefur', hlutur='rólega', stadur='Reykjavik'):
    print(nafn, action, hlutur, 'í', stadur)



setning(nafn='Steinn', action='hoppar', hlutur='æstur', )


def medaltalfjolda(listi):
    summan = summa(listi)
    lengd = 0
    for i in listi:
        lengd += 1
    average = summan / lengd
    return round(average, 3)

print(medaltalfjolda(listi))

def setning2(nafn='', setning='', ):
    print(nafn, setning)


setning2("steinn", 'datt á rassinn')

on = True

while on:
    print('lidur 1 ')
    print('lidur 2')
    val = input('veldu forrit')

    if val == "1":
        skrifaut(listi)
        print('stærsta talan', staersta(listi))
        print('minnsta talan er', minnsta(listi))
        print('summa listans er', summa)
        print('medaltal listans er', medaltal)
    if val == '2':
        nafn = input(' sladu inn nafn')
        action = input('sladu inn adgerd')
        hlutur = input('sladu inn hlut')
        stadur = input('sladu inn adgerd')
        print(setning(nafn, action, hlutur, stadur))
