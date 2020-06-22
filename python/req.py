import requests

responce = requests.get("https://www.engineerspock.com/")
print(responce.status_code)
