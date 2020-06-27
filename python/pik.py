import requests
import re

r = requests.get(
    "https://www.mr-group.ru/catalog/apartments/?project=42&min_price=&max_price=")
# print(responce.headers)

r_e = r.content
r_e = bytes.decode(r_e, encoding='utf-8', errors='ignore')


with open(r"C:\Users\Александр\Desktop\python\log\varshavskay_new3.html", "w", encoding='utf8') as output_file:
    output_file.write(r_e)


result = re.findall(
    r'a href="/catalog/apartments/mtr.*catalog-item__col _favorite-wrap', r_e, flags=re.DOTALL)
print(type(result))
# for x in result: print(x)
result2 = ''.join(result)
resultsplit = re.split(r'</a>', result2)

# for x in resultsplit: print(x)

# print(type(resultsplit))
# print(type(resultsplit[0]))
# print(resultsplit[0])

with open(r"C:\Users\Александр\Desktop\python\log\varshavskay_new3_log.txt", "w", encoding='utf8') as output_file:
    output_file.write(*result)

with open(r"C:\Users\Александр\Desktop\python\log\varshavskay_new3_split_log.txt", "w", encoding='utf8') as output_file2:
    output_file2.write(str(resultsplit))
    # output_file2.write(resultsplit[0])

i = 0
for oneapart in resultsplit:
    apart_n = re.findall(r'alt="(Квартира.+)"', oneapart)
    apart_data = re.findall(r'<div class="catalog-item__title _hover">(.+)</div>', oneapart)
    apart_price = re.findall(r'<div class="catalog-item__title _price _hover ">(.+) <span class="rub">q</span></div>', oneapart)
    apart_price_m = re.findall(r'<div class="catalog-item__subtitle _area">(.+) <span class="rub">q</span>/м²</div>', oneapart)
    print(apart_n)
    print(apart_data)
    print(apart_price)
    print(apart_price_m)
    # lstapart =[]
    # lstapart.append(apart_n)
    # lstapart.append(apart_data)
    # lstapart.append(apart_price)
    # print(lstapart)