import requests
import re
import psycopg2


def pgsql_insert(lstapart):
    conn = psycopg2.connect(dbname='test', user='postgres', password='110167', host='localhost')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO mr_metropolia ( apart, price, price_m, date, hull, floor, size, finish) VALUES (%s, %s, %s, CURRENT_DATE,%s, %s, %s, %s)', (lstapart[0], lstapart[1], lstapart[2],lstapart[3], lstapart[4], lstapart[5],lstapart[6],))
    conn.commit()
    cursor.close()
    conn.close()

def parse(site):

    r = requests.get(site)
    # print(responce.headers)

    r_e = r.content
    r_e = bytes.decode(r_e, encoding='utf-8', errors='ignore')

    pages = re.findall(r'Pagination.*End of Pagination', r_e, flags=re.DOTALL)
    pages2 = ''.join(pages)
    pages3 = re.findall(r'data-val="([0-9]+)', pages2)
    pages4 = [int(item) for item in pages3]
    max1 = max(pages4)
    print (max1)
    

    # with open(r"C:\Users\Александр\Desktop\python\log\metr.html", "w", encoding='utf8') as output_file:
    #     output_file.write(r_e)

    # pages = re.findall(r'a href="/catalog/apartments/mtr.*catalog-item__col _favorite-wrap', r_e, flags=re.DOTALL)
    # print(type(pages))
    # pages2 = ''.join(pages)
    # pagessplit = re.split(r'</a>', pages2)
    
    # # for x in pagessplit: print(x)
    # # print(type(pagessplit))
    # # print(type(pagessplit[0]))
    # # print(pagessplit[0])

    # # with open(r"C:\Users\Александр\Desktop\python\log\varshavskay_new3_log.txt", "w", encoding='utf8') as output_file:
    # #     output_file.write(*pages)

    # # with open(r"C:\Users\Александр\Desktop\python\log\varshavskay_new3_split_log.txt", "w", encoding='utf8') as output_file2:
    # #     output_file2.write(str(pagessplit))
    # #     # output_file2.write(pagessplit[0])

    # for oneapart in pagessplit:
    #     apart_n = re.findall(r'alt="(Квартира.+)"', oneapart)
    #     apart_data = re.findall(r'<div class="catalog-item__title _hover">(.+)</div>', oneapart)
    #     apart_price = re.findall(r'<div class="catalog-item__title _price _hover ">(.+) <span class="rub">q</span></div>', oneapart)
    #     apart_price_m = re.findall(r'<div class="catalog-item__subtitle _area">(.+) <span class="rub">q</span>/м²</div>', oneapart)
        
        
    #     apart_price = ''.join(apart_price).replace('&nbsp;', ' ')
    #     apart_price_m = ''.join(apart_price_m).replace('&nbsp;', ' ')
    #     apart_n = ''.join(apart_n)

    #     lstapart = []
    #     lstapart.append(apart_n)
    #     lstapart.append(apart_price)
    #     lstapart.append(apart_price_m)
    #     lstapart.append(''.join(apart_data[0]))
    #     lstapart.append(''.join(apart_data[1]))
    #     lstapart.append(''.join(apart_data[2]))
    #     lstapart.append(''.join(apart_data[3]))
    #     print(lstapart)
    #     # pgsql_insert(lstapart)

# 1 комнатные метрополия
parse('https://www.mr-group.ru/catalog/apartments/?project=42&view_mode=list&scheme_building=&building=all&rooms%5B%5D=1&min_area=&max_area=&min_price=&max_price=&floor=all&renovation=all&sort=PRICE_ASC&page=1')
