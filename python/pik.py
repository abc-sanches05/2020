import requests
import re

r = requests.get("https://www.mr-group.ru/catalog/apartments/?project=42&min_price=&max_price=")
#print(responce.headers)

r_e = r.content
r_e = bytes.decode(r_e, encoding= 'Windows-1251', errors= 'ignore' )


with open("C:\\Users\\Александр\\Desktop\\python\\log\\varshavskay_new3.html", "w") as output_file:
  output_file.write(r_e)





result = re.findall(r'a href="/catalog/apartments/mtr.*catalog-item__col _favorite-wrap', r_e, flags=re.DOTALL)
print(type(result))
#for x in result: print(x)
result2 = ''.join(result)
resultsplit = re.split(r'</a>', result2)

#for x in resultsplit: print(x)

print(type(resultsplit))
print(resultsplit[1])

with open("C:\\Users\\Александр\\Desktop\\python\\log\\varshavskay_new3_log.txt", "w") as output_file:
  output_file.write(*result)

with open("C:\\Users\\Александр\\Desktop\\python\\log\\varshavskay_new3_split_log.txt", "w") as output_file2:
  output_file2.write(str(resultsplit))
  #output_file2.write(resultsplit[0])