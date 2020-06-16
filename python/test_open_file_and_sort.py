
# при r не надо экранировать
file = r'C:\Users\Александр\Desktop\python\файлы\sort_file.txt'
f = open(file, 'r', encoding='utf-8')
x = f.read().splitlines()
f.close


def two_line():
    s = 0
    f = 1
    for xl in range(len(x)):
        if f < len(x):
            print(f'{x[s]} {x[f]}')
            s += 2
            f += 2


def three_line():
    s = 0
    p = 1
    f = 2
    for xl in range(len(x)):
        if f < len(x):
            print(f'{x[s]} {x[p]} {x[f]}')
            s += 3
            p += 3
            f += 3


two_line()
# three_line()
