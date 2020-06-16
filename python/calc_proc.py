# считает на сколько поднимется акция после падения
def opros(f):
    while True:
        try:
            st = int(input(f))
        except:
            print('Вы ввели неправильное значение, введите заново')
            continue
        else:
            # print(f'Начальная стоимость: {st}')
            break
    return st


def calc(s, p):
    d = 100/s*(s-p)
    print(f'Акция упала на {int(d)} %')
    u = s/p * 100 - 100
    print(f'Акции {int(u)} % до прежнего уровня')


calc(opros('Введите начальную стоимость акции: '), opros('Введите какая цена на данный момент: '))

