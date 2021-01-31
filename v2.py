with open('travels.txt','r') as f:

    Am = set()
    Bm = set()
    RAS = {}
    PO = {}
    PN = {}
    summa = 0
    fer = 0
    sec = 0
    thir = 0
    rashod = 0
    masL = 0

    for i in f:
        date,month,A,B,km,petrol,kg = i.split()
        Am.add(A)
        Bm.add(B)

        if date+month == '1октября':
            summa += int(km)
            fer += int(kg)
        elif date+month == '2октября':
            sec += int(kg)
        else:
            thir += int(kg)


        rashod += int(petrol)/int(km)


        if B not in PN:
            RAS.update({B:0})
            RAS[B] += rashod
        else:
            RAS[B] += rashod

        rashod = 0



        if B not in PN:
            PN.update({B:0})
            PN[B] += int(kg)
        else:
            PN[B] += int(kg)

        if A not in PO:
            PO.update({A:0})
            PO[A] += int(kg)
        else:
            PO[A] += int(kg)



        if A == 'Липки':
            masL += int(kg)

    if max(fer,sec,thir) == fer:
        datee = '1.10'

    elif max (fer,sec,thir) == sec:
        datee = '2.10'
    else:
        date = '3.10'


    print(' ')
    print(' ')
    print('Суммарное расстояние, которое проехал грузовой транспорт за 1.10 ---', summa)
    print(' ')
    print ('Перевезено больше всего грузов --- ' ,datee ,', суммарным объемом ---',max(fer,sec,thir))
    print(' ')
    print ('Масса отправленных из Липки --- ' ,masL)
    print(' ')
    print('Количество ПО --- ',len(Am),'. Пункты: \n ', PO)
    print(' ')
    print('Количество ПН --- ',len(Bm),'. Пункты: \n ', PN)
    print(' ')
    print('Пункт назначения с наибольшим расходом бензина --- ', max(RAS, key=RAS.get))
