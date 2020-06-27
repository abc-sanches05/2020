import requests
import re
import psycopg2


def pgsql_insert(lstapart):
    conn = psycopg2.connect(dbname='test', user='postgres', password='110167', host='localhost')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO mr_d1 ( apart, price, price_m, date, hull, floor, size, finish) VALUES (%s, %s, %s, CURRENT_DATE,%s, %s, %s, %s)', (lstapart[0], lstapart[1], lstapart[2],lstapart[3], lstapart[4], lstapart[5],lstapart[6],))
    conn.commit()
    cursor.close()
    conn.close()

def parse(site):

    r = requests.get(site)
    # print(responce.headers)

    r_e = r.content
    r_e = bytes.decode(r_e, encoding='utf-8', errors='ignore')


    # with open(r"C:\Users\Александр\Desktop\python\log\varshavskay_new3.html", "w", encoding='utf8') as output_file:
    #     output_file.write(r_e)


    result = re.findall(r'a href="/catalog/apartments/dmi.*catalog-item__col _favorite-wrap', r_e, flags=re.DOTALL)
    print(type(result))
    # print(result)
    result2 = ''.join(result)
    resultsplit = re.split(r'</a>', result2)

    # for x in resultsplit: print(x)
    # print(type(resultsplit))
    # print(type(resultsplit[0]))
    # print(resultsplit[0])

    # with open(r"C:\Users\Александр\Desktop\python\log\varshavskay_new3_log.txt", "w", encoding='utf8') as output_file:
    #     output_file.write(*result)

    # with open(r"C:\Users\Александр\Desktop\python\log\varshavskay_new3_split_log.txt", "w", encoding='utf8') as output_file2:
    #     output_file2.write(str(resultsplit))
    #     # output_file2.write(resultsplit[0])

    for oneapart in resultsplit:
        apart_n = re.findall(r'alt="(Квартира.+)"', oneapart)
        apart_data = re.findall(r'<div class="catalog-item__title _hover">(.+)</div>', oneapart)
        apart_price = re.findall(r'<div class="catalog-item__title _price _hover ">(.+) <span class="rub">q</span></div>', oneapart)
        apart_price_m = re.findall(r'<div class="catalog-item__subtitle _area">(.+) <span class="rub">q</span>/м²</div>', oneapart)
        apart_price = ''.join(apart_price).replace('&nbsp;', ' ')
        apart_price_m = ''.join(apart_price_m).replace('&nbsp;', ' ')
        apart_n = ''.join(apart_n)

        # print (apart_n)
        # print (apart_data)
        # print (apart_price)
        # print (apart_price_m)
        lstapart = []
        lstapart.append(apart_n)
        lstapart.append(apart_price)
        lstapart.append(apart_price_m)
        lstapart.append(''.join(apart_data[0]))
        lstapart.append(''.join(apart_data[1]))
        lstapart.append(''.join(apart_data[2]))
        lstapart.append(''.join(apart_data[3]))
        print(lstapart)
        pgsql_insert(lstapart)

# студии павелецкая
parse('https://www.mr-group.ru/catalog/apartments/?project=19&view_mode=list&scheme_building=&building=all&rooms%5B%5D=%D0%A1%D1%82%D1%83%D0%B4%D0%B8%D1%8F&min_area=&max_area=&min_price=&max_price=&floor=all&renovation=all&sort=PRICE_ASC&page=1')
#  1 комнатные
parse('https://www.mr-group.ru/catalog/apartments/?project=19&view_mode=list&scheme_building=&building=all&rooms%5B%5D=1&min_area=&max_area=&min_price=&max_price=&floor=all&renovation=all&sort=PRICE_ASC&page=1')
#  2 комнатные
parse('https://www.mr-group.ru/catalog/apartments/?project=19&view_mode=list&scheme_building=&building=all&rooms%5B%5D=2&min_area=&max_area=&min_price=&max_price=&floor=all&renovation=all&sort=PRICE_ASC&page=1')
# # 3 комнатные
parse('https://www.mr-group.ru/catalog/apartments/?project=19&view_mode=list&scheme_building=&building=all&rooms%5B%5D=3&min_area=&max_area=&min_price=&max_price=&floor=all&renovation=all&sort=PRICE_ASC&page=1')
