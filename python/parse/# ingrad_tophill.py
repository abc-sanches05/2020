# не работает не отобращаются данные по квартирам

import requests
import re
import psycopg2


def pgsql_insert(lstapart):
    conn = psycopg2.connect(dbname='test', user='postgres',
                            password='110167', host='localhost')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO mr_pavel ( apart, price, price_m, date, hull, floor, size, finish) VALUES (%s, %s, %s, CURRENT_DATE,%s, %s, %s, %s)',
                   (lstapart[0], lstapart[1], lstapart[2], lstapart[3], lstapart[4], lstapart[5], lstapart[6],))
    conn.commit()
    cursor.close()
    conn.close()


def parse(site):
    r = requests.get(site)
    r_e = r.content
    r_e = bytes.decode(r_e, encoding='utf-8', errors='ignore')
    print(r_e)

    result = re.findall(
        r'search_result_row active.*textScroll__track', r_e, flags=re.DOTALL)
    print(type(result))
    result2 = ''.join(result)
    resultsplit = re.split(r'</div>', result2)
    print(resultsplit)

#     for oneapart in resultsplit:
#         apart_n = re.findall(r'alt="(Квартира.+)"', oneapart)
#         apart_data = re.findall(
#             r'<div class="catalog-item__title _hover">(.+)</div>', oneapart)
#         apart_price = re.findall(
#             r'<div class="catalog-item__title _price _hover ">(.+) <span class="rub">q</span></div>', oneapart)
#         apart_price_m = re.findall(
#             r'<div class="catalog-item__subtitle _area">(.+) <span class="rub">q</span>/м²</div>', oneapart)
#         apart_price = ''.join(apart_price).replace('&nbsp;', ' ')
#         apart_price_m = ''.join(apart_price_m).replace('&nbsp;', ' ')
#         apart_n = ''.join(apart_n)

#         lstapart = []
#         lstapart.append(apart_n)
#         lstapart.append(apart_price)
#         lstapart.append(apart_price_m)
#         lstapart.append(''.join(apart_data[0]))
#         lstapart.append(''.join(apart_data[1]))
#         lstapart.append(''.join(apart_data[2]))
#         lstapart.append(''.join(apart_data[3]))
#         print(lstapart)
#         pgsql_insert(lstapart)


# # считаем сколько страниц
# all_apart = pages(
#     'https://www.mr-group.ru/catalog/apartments/?project=41666&type=12&min_price=&max_price=')
# студии павелецкая
parse('https://www.ingrad.ru/find-apartment?pn=1&sort=price&projectId%5B0%5D=28&priceFrom=7198532&priceTo=25734229&totalAreaFrom=27&totalAreaTo=90&floorFrom=2&floorTo=22&buildingType=1&layout=list&isProjectSelector=1')
# #  1 комнатные
# parse('https://www.mr-group.ru/catalog/apartments/?project=41666&view_mode=list&scheme_building=&building=all&rooms%5B%5D=1&min_area=&max_area=&min_price=&max_price=&floor=all&renovation=all&sort=PRICE_ASC&page=1')
# #  2 комнатные
# parse('https://www.mr-group.ru/catalog/apartments/?project=41666&view_mode=list&scheme_building=&building=all&rooms%5B%5D=2&min_area=&max_area=&min_price=&max_price=&floor=all&renovation=all&sort=PRICE_ASC&page=1')
# # # 3 комнатные
# parse('https://www.mr-group.ru/catalog/apartments/?project=41666&view_mode=list&scheme_building=&building=all&rooms%5B%5D=3&min_area=&max_area=&min_price=&max_price=&floor=all&renovation=all&sort=PRICE_ASC&page=1')
