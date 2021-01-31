with open('travels.txt','r') as f:
    travels = list(0 for i in range(117))

    for i in range(117):
        travels[i] = dict.fromkeys(['date','A','B','km','petrol','kg'])
    n = 0
    fi = 0
    rast = 0
    s = 0
    t = 0
    d = 0

    for i in f:
        n = n+1
        date,month,A,B,km,petrol,kg = i.split()
        l = [date,month,A,B,km,petrol,kg]

        travels[n-1]['date'] = date+month
        travels[n-1]['A'] = A
        travels[n-1]['B'] = B
        travels[n-1]['km'] = km
        travels[n-1]['petrol'] = petrol
        travels[n-1]['kg'] = kg

    print('\n'.join(str(value) for value in travels))


    setpunkts = set([travels[i]['A'] for i in range(117) ])
    punkts = list(setpunkts)
    dpunkts = dict.fromkeys([i for i in punkts], 0)

    setnaznach = set([travels[i]['B'] for i in range(117) ])
    naznach = list(setnaznach)
    dnaznach = dict.fromkeys([i for i in naznach],0)
    drashod = dict.fromkeys([i for i in naznach],0)

    for i in range(117):

        if travels[i]['date'] == '1октября':
            fi=fi+int(travels[i]['kg'])
            rast += int(travels[i]['km'])
        elif travels[i]['date'] == '2октября':
            s=s+int(travels[i]['kg'])
        else:
            t=t+int(travels[i]['kg'])



        for g in punkts:
            if travels[i]['A'] == g:

                dpunkts[g] += int(travels[i]['kg'])





        for g in naznach:
            if travels[i]['B'] == g:
                dnaznach[g] += int(travels[i]['kg'])
                drashod[g] += int(travels[i]['petrol'])/int(travels[i]['km'])

        pet = max(drashod, key=drashod.get)


    if max(fi,t,s) == fi:
        datee = '1октября'
    elif max(fi,t,s) == t:
        datee = '3октября'
    else:
        datee = '2октября'


    print(' ')
    print(' ')
    print('Суммарное расстояние, которое проехал грузовой транспорт за 1.10 ---', rast )
    print(' ')
    print ('Перевезено больше всего грузов --- ' , datee,', суммарным объемом ---',max(fi,t,s))
    print(' ')
    print ('Масса отправленных из Липки --- ' ,dpunkts['Липки'])
    print(' ')
    print('Количество ПО --- ',len(punkts),'. Пункты: \n ', dpunkts)
    print(' ')
    print('Количество ПН --- ',len(naznach),'. Пункты: \n ',dnaznach)
    print(' ')
    print('Пункт назначения с наибольшим расходом бензина --- ', pet)



