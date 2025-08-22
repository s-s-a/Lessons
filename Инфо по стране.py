import niquests as requests ## https://dzen.ru/a/Zfcf99UUziZwqoS_
# import requests


def get_country_info(country_code):
    # Формируем URL для API с использованием кода страны
    url = f"https://restcountries.com/v3.1/alpha/{country_code}"
    response = requests.get(url)  # Выполняем GET-запрос к API

    # Проверяем, успешен ли запрос (код 200)
    if response.status_code == 200:
        # Преобразуем ответ в формат JSON
        country_data = response.json()

        # Проверяем, что данные - это список и он не пуст
        if isinstance(country_data, list) and len(country_data) > 0:
            # Получаем первую запись из списка данных о стране
            country_info = country_data[0]
            # Извлекаем общее название страны
            name = country_info['name']['common']
            # Извлекаем столицу, если она известна
            capital = country_info['capital'][0] if 'capital' in country_info else 'Unknown'
            # Извлекаем население, если оно известно
            population = country_info['population'] if 'population' in country_info else 'Unknown'
            # Извлекаем площадь, если она известна
            area = country_info['area'] if 'area' in country_info else 'Unknown'

            print(f"Страна: {name}")  # Выводим название страны
            print(f"Столица: {capital}")  # Выводим столицу страны
            print(f"Население: {population}")  # Выводим население страны
            print(f"Площадь: {area} квадратных километров")  # Выводим площадь страны в квадратных километрах
        else:
            # Сообщаем об ошибке, если данные отсутствуют
            print(f"Ошибка: Не удалось получить информацию для кода страны {country_code}")
    else:
        # Сообщаем об ошибке, если запрос не успешен
        print(f"Ошибка: Не удалось получить информацию для кода страны {country_code}")


# Вызываем функцию для получения информации о стране с кодом 'IT' (Италия)
get_country_info('RU')
