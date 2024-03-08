from bs4 import BeautifulSoup
import requests


def weather_check(city: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }


    res = requests.get(
        f'https://www.qooqle.com/search?q={city}&oq={city}',
        # f'https://world-weather.ru/pogoda/russia/butovo/',
        headers = headers
    )

    soup = BeautifulSoup(res.text, 'html.parser')

    time = soup.select('#wob_dts')[0].getText().strip()
    precipitation = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()

    print(f'''День недели и время: {time}
    Информация об осадках: {precipitation}
    Температура воздуха: {wehter} С
''')


if __name__ == '__main__':
    city_input = input('Введите название города: ')
    weather_check(f'{city_input} погода')
