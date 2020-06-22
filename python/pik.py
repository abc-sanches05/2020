import requests
import re

responce = requests.get("https://www.pik.ru/sles/search/list?sortBy=price")
#print(responce.headers)

with open("C:\\Users\\Александр\\Desktop\\python\\log\\varshavskay.txt", "w") as file:
    print(responce.content, file=file, sep="\n")

""" не работает
res = responce.content
print(type(res))

search_price = re.search('FlatsResultTable-rowPriceTitle', res)
print(search_price)

"""


