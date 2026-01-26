import requests
# import niquests as requests

city = input("Введите название города: ")
url = f"https://wttr.in/{city}"

try:
    res = requests.get(url)
    print(res.text)
except:
    print("Произошла ошибка, пожалуйста, повторите попытку позже...")
