# Код для генерации лиц людей на Python

# Для отправки HTTP-запроса на получение сгенерированного лица в коде используется библиотека requests.

import requests

# Отправляем GET-запрос для получения изображения
img = requests.get(
    "https://thispersondoesnotexist.com/"
).content

# Открываем файл с именем "person.jpg" в режиме записи бинарных данных ("wb")
with open("person.jpg", "wb") as f:
    # Записываем байты полученного изображения в файл
    f.write(img)
