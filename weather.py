# Код для получения прогноза погоды без API на Python

import requests


city = input("Введите название города: ")

url = f"https://wttr.in/{city}"


try:

    res = requests.get(url)

    print(res.text)

except:

    print("Произошла ошибка, пожалуйста, повторите попытку позже...")