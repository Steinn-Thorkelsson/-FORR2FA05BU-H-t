on = True

while on:
    print('1. Daemi 1')
    print('2. Daemi 2')
    print('3. Daemi 3')
    print('4. Daemi 4')
    print('5. Daemi 5')
    print('6. Haetta')
    val = input("Veldu Daemi: ")

    if val == '1':
        tuuple = ('a', 'b', 'c', 'd', 'e', 'f', 2, 2.5, 'Steinn')
        print(f'Stak nr. 3:  {tuuple[2]}')
        for t in tuuple:
            print(t, end=':')

    elif val == '2':
        listatuple = ([1, 6, 4], [10, 20, 4],
                      [-1, -4, 4], [50, 60, 4])
        print(listatuple)
        print(listatuple[1][1])

    elif val == '3':
        tuuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n')
        print(f'4 Aftasti stafurinn: {tuuple[-4]}')
        print(f'Stafir 2 - 8: {tuuple[1:9]}')

    elif val == '4':
        tuple_1 = (1, 2, 3, 4, 5)
        tuple_2 = ()
        print(tuple_1)
        marg = int(input('Sladu inn tolu til ad margfalda med tuple: '))
        for t in tuple_1:
            tuple_2 = tuple_2 + ((marg * t),)
        print(tuple_2)
    elif val == '5':
        tuplea = ('a', 'b', 'c', 'd', 'e', 'f')
        stafur = input('Sladu inn staf til ad leita af: ')
        if stafur in tuplea:
            print(stafur, 'er i tuple')
        else:
            print('stafur er ekki i tuple')
    elif val == '6':
        on = False
