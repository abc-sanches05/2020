import datetime
today = datetime.datetime.today().strftime("%Y-%m-%d-%H.%M")


def lst(file):
    lst_set = []
    with open(file) as f:
        lst_set = f.read().replace('\t', ' ').splitlines()
    return lst_set


l_old = set(lst('C:\\Users\\Александр\\Desktop\\test_itoo_2'))
l_new = set(lst('C:\\Users\\Александр\\Desktop\\itoolabs.txt'))


lst_old2 = list()
lst_old3 = list()

# print(l_new)

for l in l_old:
    lc = l.rsplit(' ', 1)
    lst_old2.append(lc)
    lst_old3.append(lc[0])


add_old = 0
add_new = 0
add_old_param = 0
lst_finish = list()

for l_old2 in lst_old2:
    if l_old2[0] in l_new:
        add_old += 1
        lst_finish.append(l_old2[0] + ' ' + today)
        # print(f'обновили дату {l_old2[0]} {today}')  # заменяем на текущую дату
    else:
        add_old_param += 1
        lst_finish.append(l_old2[0] + ' ' + l_old2[1])
        # print(f'Оставили старое значение {l_old2}')  # старое значения, оставляем старую дату

for ln_new in l_new:
    if ln_new not in lst_old3:
        add_new += 1
        lst_finish.append(ln_new + ' ' + today)
        # print(f'добавили новое значение {ln_new}')  # новое значение


print(f'\nВсего:{add_old+add_old_param+add_new}, старые активные регистрации:{add_old}, добавлены новые:{add_new}, старые не активные регистрации:{add_old_param}')


with open("C:\\Users\\Александр\\Desktop\\test_itoo_finish.txt", "w") as file:
    print(*lst_finish, file=file, sep="\n")
