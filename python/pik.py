import requests
import re

r = requests.get("https://www.mr-group.ru/catalog/apartments/?project=42&min_price=&max_price=")
#print(responce.headers)

"""
with open("C:\\Users\\Александр\\Desktop\\python\\log\\varshavskay.txt", "w") as file:
    print(responce.content, file=file, sep="\n")
"""
r_e = r.content
r_e = bytes.decode(r_e, encoding= 'Windows-1251', errors= 'ignore' )


with open("C:\\Users\\Александр\\Desktop\\python\\log\\varshavskay_new3.html", "w") as output_file:
  output_file.write(r_e)





result = re.findall(r'a href="/catalog/apartments/mtr.*a>', r_e, re.S)

for x in result: print(x)

with open("C:\\Users\\Александр\\Desktop\\python\\log\\varshavskay_new3_log.txt", "w") as output_file:
  output_file.write(*result)
