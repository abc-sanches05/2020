import datetime
today = datetime.datetime.today().strftime("%Y-%m-%d-%H.%M")


# передаем соддержимое файла в список
def lst(file):
    lst_set = []
    with open(file) as f:
        lst_set = f.read().splitlines()
    return lst_set


l_old = set(lst('C:\\Users\\Александр\\Desktop\\test_itoo'))
l_new = set(lst('C:\\Users\\Александр\\Desktop\\test_itoo_2'))
add_old = 0
add_new = 0
add_old_param = 0
lst_finish = list()

for ln2_new in l_new:
    if ln2_new in l_old:
        add_old += 1
        lst_finish.append(ln2_new + ' ' + today)
        print(f'Cовпадение {ln2_new} {today}')  # заменяем на текущую дату
    else:
        add_new += 1
        lst_finish.append(ln2_new + ' ' + today)
        print(f'Не совпало {ln2_new} {today}')  # новые значения, добавляем дату

for ln_old in l_old:
    if ln_old not in l_new:
        add_old_param += 1
        lst_finish.append(ln_old + ' ' + today)
        print(f'Cовпадение 2 {ln_old} {today}')  # старое значения, оставляем старую дату
for ls in lst_finish:
    print(ls)
print(f'\nВсего:{add_old+add_new+add_old_param}, старые активные регистрации:{add_old}, добавлены новые:{add_new}, старые не активные регистрации:{add_old_param}')


with open("C:\\Users\\Александр\\Desktop\\test_itoo_finish.txt", "w") as file:
    print(*lst_finish, file=file, sep="\n")


"""
def read2list(file):
    # открываем файл в режиме чтения utf-8
    file = open(file, 'r', encoding='utf-8')

    # читаем все строки и удаляем переводы строк
    lines = file.readlines()
    lines = [line.rstrip('\n') for line in lines]

    file.close()

    return lines

lines = read2list('C:\\Users\\Александр\\Desktop\\test_itoo')
print(lines)


# print(lines[0].split(' ', 1)[1])
"""


"""
for ln_old in l_old:
    ln_old = ln_old.split(' ', 2)
    # print (type(ln_old))
    print (ln_old[1])

"""
"""

print(len(l_old))
print(len(l_new))

# совпадение
result=list(set(l_old) & set(l_new))
print(len(result))


# разность симетричная (в данной программе не используется)
result2=list(set(l_old) ^ set(l_new))
print(result2)

# разность страрый - новый(остаются значения старого списка)
result3=list(set(l_old) - set(l_new))
print('(Нет значений в новом списке)')
print(result3)

# разность страрый - новый(остаются новые значения)
result4=list(set(l_new) - set(l_old))
print('(новые значения)')
print(result4)

"""
