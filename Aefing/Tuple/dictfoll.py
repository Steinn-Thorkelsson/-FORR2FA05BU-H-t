on = True


def buatildict():
    litadict = {1: "vettel", 2: "hamilton", 3: 'bottas', 4: 'Raikkonen', 5: 'Ricciardo', 6: 'Veerstappen', 7: 'gasly',
                8: 'leclerc', 9: 'albon', 10: 'russel'}
    return litadict


def prentadict(dict1):
    print(dict1)


def eydalit(nr, dict1):
    dict1.pop(nr)
    return dict1


while on:
    print('1. Daemi 1')
    print('2. Daemi 2')
    print('3. Daemi 3')
    print('4. Daemi 4')
    print('5. Daemi 5')
    print('6. Haetta')
    val = input("Veldu Daemi: ")

    if val == '1':
        buatildict()

    elif val == '2':
        prentadict(buatildict())
    elif val == '3':
        nr = int(input('veldu item til thess ad eyda: '))
        eydalit(nr, buatildict())
        print(buatildict())
