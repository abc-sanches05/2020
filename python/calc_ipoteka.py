def proc():
   
    while True:
        try:
            pr = int(input('Введите процентную ставку: '))     
        except:
            print('Вы ввели неправильное значение, введите заново')
            continue
        else:
            print(f'процентная ставка: {pr}')
            break
    return(pr)
    

def dolg():
    
    while True:
        try:
            do = int(input('Введите сумму инвестирования: '))
        except:
            print('Вы ввели неправильное значение, введите заново')
            continue
        else:
            print(f'Сумма долга: {do}')
            break
    return(do)


def srok():
    
    while True:
        try:
            sr= int(input('Введите на сколько лет: '))
            
        except:
            print('Вы ввели неправильное значение, введите заново')
            continue
        else:
            print(f'на {sr} лет')
            break
    return(sr)


def inv(): 
    while True:
        try:
            i = int(input('Введите на сколько вы готовы пополниять вклад: '))           
        except:
            print('Вы ввели неправильное значение, введите заново')
            continue
        else:
            print(f'По {i} рублей вы готовы пополниять каждый месяц')
            break
    return(i) 


def doh_list(s,d,p,i):
    dlist = []
    p = p * 0.01
    ig = 0
    for y in range(2020,2020+s):
        dlist.append(y)
        if ig > 400000:
            ig = 400000
        ig = ig * 0.13  # 13 процентов
        ig = int(ig)
        dlist.append(f'Доход за год по ИИС {ig}')
        d = d + ig  # + доход по иис
        ig = 0
        for m in range(1, 13):
            ig = ig+i
            dg = d * (p/12) + i
            d = d + dg
            # print(f'{m}.{y} доход по вкладу {int(dg)} общая сумма {int(d)}')
            dlist.append(f'{m}.{y} доход по вкладу: {int(dg)} общая сумма: {int(d)}')       
    return(dlist)


p = proc()
d = dolg()
s = srok()
i = inv()


"""

p = 11
d = 10000
s = 15
i = 1500

"""


# doch_god(s,d,p,i)



for x in doh_list(s,d,p,i):
    print (x)

print(f'Вклад на общую сумму {d} с процентной ставкой {p} на срок {s} с пополнением по {i}' )
