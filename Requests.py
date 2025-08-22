# %% [markdown]
# Библиотека requests

# %% [markdown]
# В современном веб-программировании взаимодействие между клиентом и сервером на основе протокола HTTP является одной из ключевых задач. Для разработчиков на языке Python библиотека requests стала стандартом де-факто для выполнения HTTP-запросов благодаря своей простоте и удобству. В этой статье мы рассмотрим, что такое библиотека requests, а также охватим основы работы с HTTP/S.
#
# Что такое библиотека requests?
#
# requests — это мощная и популярная библиотека для языка Python, разработанная для удобного выполнения HTTP-запросов. Она позволяет вам взаимодействовать с веб-ресурсами, отправлять запросы и обрабатывать ответы, используя простые и лаконичные методы. Библиотека была создана, чтобы сделать процесс работы с HTTP более интуитивно понятным, чем традиционные методы, такие как стандартный модуль urllib.
#
# Некоторые ключевые особенности библиотеки requests включают:
#
# Легкость в использовании: библиотека имеет простой и понятный интерфейс.
# Поддержка HTTP-методов: GET, POST, PUT, DELETE, и многие другие.
# Работа с JSON: простое преобразование данных между Python-объектами и JSON.
# Обработка сессий: поддержка управления сессиями и куки через объект Session.
# Управление заголовками и параметрами запроса: возможность легко добавлять параметры и заголовки к запросам.
# Работа с сертификатами: поддержка HTTPS и безопасных соединений.Основы работы с HTTP
#

# %% [markdown]
# Что такое HTTP?
# HTTP (HyperText Transfer Protocol) — это протокол, который используется при обмене данными в интернете. Он основан на модели клиент-сервер, где клиент (обычно веб-браузер) отправляет запросы к серверу, а сервер отвечает на эти запросы. ПротоколHTTP имеет множество методов, среди которых наибольшее распространение получили:
#
# GET: используется для получения данных с сервера. Например, запрос на получение веб-страницы.
# POST: применяется для отправки данных на сервер, например, при отправке формы на веб-сайте.
# PUT: предназначен для обновления существующих ресурсов на сервере.
# DELETE: используется для удаления ресурсов с сервера.
# Когда клиент выполняет HTTP-запрос, он отправляет запрос, который может содержать заголовки, параметры и тело (особенно для методов POST и PUT). Сервер обрабатывает запрос и отправляет обратно ответ, который включает статусный код, заголовки и, возможно, тело ответа (например, HTML-код страницы или данные в формате JSON).
#
# Выполнение запросов с библиотекой requests
# Теперь давайте рассмотрим, как использовать библиотеку requests для выполнения различных типов запросов.
#
# Установка библиотеки
# Чтобы установить библиотеку requests, вы можете использовать pip:

# %%
# pip install requests

# %% [markdown]
# Простой GET-запрос
# Выполнение GET-запроса очень просто. Например, чтобы получить данные с определенного URL, вы можете сделать следующее:

# %%
import niquests as requests
# import requests

response = requests.get("https://yandex.ru")
print(f"Status code: {response.status_code}")  # Выводит статусный код ответа
print()
print(f"Text: {response.text}")  # Выводит текст ответа

# %% [markdown]
# POST-запрос

# %%

data = {"key": "value"}
response = requests.post("https://api.example.com/submit", json=data)
print(response.status_code)
print(response.json())  # Если ответ в формате JSON

# %% [markdown]
# Обработка ошибок
# При работе с HTTP-запросами важно обрабатывать возможные ошибки. Библиотека requests предоставляет удобные методы для этого:

# %%
# import requests

try:
    response = requests.get("https://api.example.com/data")
    response.raise_for_status()  # Вызывает исключение для ошибок НТТР
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")  # 06pa60TKa own60K
except Exception as err:
    print(f"An error occurred: {err}")

# %% [markdown]
# 1. Отправка GET-запросов

# %% [markdown]
# GET — это основной HTTP-метод, который используется для запроса данных с сервера. Обычно запросы GET используются для получения информации без изменения состояния ресурса на сервере.
#
# Для отправки GET-запроса в библиотеке requests достаточно вызвать функцию requests.get(). Например:

# %%
import os
# import requests

response = requests.get("https: //jsonplaceholder.typicode.com/posts")
print(response.status_code)  # Выводим код состояния ответа
print(response.text)  # Выводим текст ответа
print(response.json())  # Выводим ответ в формате JSON

# %% [markdown]
# Параметры запроса:

# %%
# import requests

params = {"userId": 1}
response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)
print(response.json())

# %% [markdown]
# 2. Отправка POST-запросов

# %% [markdown]
# POST-запросы часто используются для отправки данных на сервер, например, для создания новых записей в базе данных. В библиотеке requests для отправки POST-запроса используется метод requests.post().

# %% [markdown]
# Пример отправки POST-запроса:

# %%
data = {"title": "foo", "body": "bar", "userId": 1}

response = requests.post("https://jsonplaceholder.typicode.com/posts", data=data)

# Выводим код состояния ответа
print(response.status_code)

# Выводим данные, отправленные сервером в ответ
print(response.json())

# %% [markdown]
# Параметры запроса:

# %% [markdown]
# Для отправки данных, например, в формате JSON, можно использовать параметр json:

# %%
# import requests

data = {"title": "foo", "body": "bar", "userId": 1}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)

print(response.json())

# %% [markdown]
# 3. Другие HTTP-методы: PUT, PATCH, DELETE

# %% [markdown]
# В библиотеке requests также поддерживаются другие HTTP-методы, такие как PUT, PATCH и DELETE.

# %% [markdown]
# PUT-запросы

# %% [markdown]
# PUT используется для обновления существующего ресурса на сервере. Он заменяет весь ресурс новыми данными.

# %% [markdown]
# Пример отправки PUT-запроса:

# %%
# import requests

data = {"id": 1, "title": "Updated Title", "body": "Updated Body", "userId": 1}

response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=data)

print(response.status_code)
print(response.json())

# %% [markdown]
# PATCH-запросы

# %% [markdown]
# PATCH — это метод, который используется для частичного обновления ресурса. В отличие от PUT, который заменяет весь ресурс, PATCH позволяет обновить только некоторые поля.

# %% [markdown]
# Пример отправки PATCH-запроса:

# %%
# import requests

data = {"title": "Updated Title"}

response = requests.patch("https://jsonplaceholder.typicode.com/posts/1", json=data)

print(response.status_code)
print(response.json())

# %% [markdown]
# DELETE-запросы

# %% [markdown]
# DELETE используется для удаления ресурса на сервере. Этот метод может быть использован, чтобы удалить данные по определённому URL.
#
# Пример отправки DELETE-запроса:

# %%
import requests

response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

print(
    response.status_code
)  # Ожидаемый код состояния: 200 (ОК), если удаление прошло успешно

# %% [markdown]
# Работа с ответами в библиотеке requests в Python

# %% [markdown]
# Работа с ответами является важной частью взаимодействия с веб-сервисами, и библиотека requests предоставляет удобные средства для обработки ответов от серверов. В этой статье мы рассмотрим, как обрабатывать ответы, проверять успешность запросов и обрабатывать возможные ошибки.

# %% [markdown]
# 1. Обработка ответов

# %% [markdown]
# После отправки HTTP-запроса с помощью библиотеки requests, сервер отправляет ответ, который доступен через объект Response. Этот объект содержит информацию о статусе запроса, теле ответа и другие полезные данные.
#
# Пример отправки запроса и получения ответа:

# %%
# import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

# Получение кода состояния ответа
print("Status Code:", response.status_code)

# Получение текста ответа
print("Response Text:", response.text)

# Получение данных в формате JSON (если они есть)
print("Response JSON:", response.json())

# %% [markdown]
# Что можно извлечь из объекта response?
#
# status_code: Код состояния HTTP-ответа, например, 200 для успешного запроса.
# text: Тело ответа в виде строки (может быть HTML, JSON и т.д.).
# json(): Преобразует тело ответа в формат JSON (если это возможно).
# headers: Заголовки ответа.
# cookies: Куки, если они присутствуют в ответе.
# url: URL-адрес, по которому был отправлен запрос.
# Пример вывода:

# %%
# Status Code: 200
# Response Text: [{"userId": 1, "id": 1, "title": "Post 1", ... }]
# Response JSON: [{"userId": 1, "id": 1, "title": "Post 1", ... }]


# %% [markdown]
# 2. Проверка успешности запроса

# %% [markdown]
# Для проверки, был ли запрос успешным, можно использовать код состояния ответа, который возвращается сервером. Обычно, если код состояния начинается с 2xx, запрос прошел успешно.
#
# 200 OK — успешный запрос.
# 201 Created — ресурс был успешно создан.
# 400 Bad Request — ошибка запроса на сервере.
# 404 Not Found — ресурс не найден.
# В библиотеке requests есть несколько удобных методов, чтобы проверить успешность запроса:
#
# Проверка через status_code:

# %%
# import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

if response.status_code == 200:
    print("Request was successful!")
else:
    print(f"Request failed with status code {response.status_code}")

# %% [markdown]
# Использование response.ok:

# %% [markdown]
# Библиотека requests предоставляет атрибут ok, который возвращает True, если код состояния ответа указывает на успешный запрос (коды от 200 до 299):

# %%
# import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

if response.ok:
    print("Request was successful!")
else:
    print(f"Request failed with status code {response.status_code}")

# %% [markdown]
# 3. Обработка ошибок

# %% [markdown]
# Когда запрос не может быть выполнен (например, сервер не доступен), будет выброшено исключение. Для обработки этих исключений можно использовать блоки try/except.
#
# Пример обработки ошибок:

# %%
# import requests
# from requests.exceptions import HTTPError, Timeout, RequestException
from niquests.exceptions import HTTPError, Timeout, RequestException

try:
    response.raise_for_status()  # Проверка на успешный код ответа (напри
except HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Timeout:
    print("The request timed out")
except RequestException as err:
    print(f"Other error occurred: {err}")
else:
    print("Request was successful!")
    print(response.json())


# %% [markdown]
# HTTPError: Ошибка, связанная с кодом ответа сервера (например, 404 или 500).
# Timeout: Ошибка, если запрос занял слишком много времени.
# RequestException: Общая ошибка, которая возникает при проблемах с сетевым соединением, например, если сервер недоступен.

# %% [markdown]
# 4. Проверка наличия данных в ответе

# %% [markdown]
# Иногда вам нужно убедиться, что сервер вернул данные в ответе, и корректно обработать отсутствие этих данных. Например, если сервер возвращает пустой список или ошибку, вы можете обработать это соответствующим образом.

# %%
# import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

if response.ok:
    data = response.json()
    if not data:
        print("No data found")
    else:
        print("Data received:", data)
else:
    print(f"Request failed with status code {response.status_code}")


# %% [markdown]
# Заголовки и куки

# %% [markdown]
# Заголовки и куки — это важные части HTTP-запросов, которые часто используются для передачи метаинформации, таких как тип содержимого, информация о браузере, авторизация и сессии.
#
# Работа с заголовками
#
# Заголовки позволяют клиенту сообщать серверу важную информацию. Например, мы можем указать, что отправляем JSON, или передать информацию о пользовательском агенте.
#
# Пример передачи заголовков в запросе:

# %%
# import requests

# Определение заголовков
headers = {
    "User-Agent": "my-app/1.0",
    "Accept": "application/json",
    "Authorization": "Bearer your_token",
}

response = requests.get("https://jsonplaceholder.typicode.com/posts", headers=headers)

print(response.status_code)
print(response.text)

# %% [markdown]
# В этом примере мы передаем заголовки, которые указывают серверу, что клиент — это приложение с именем my-app/1.0, и что мы ожидаем ответ в формате JSON. Также передаем токен авторизации через заголовок Authorization.
#
# Работа с куками
#
# Куки используются для хранения информации о состоянии между запросами, например, для сохранения сессии пользователя.
#
# Пример работы с куками:

# %%
# import requests

# Создание куки
cookies = {"session_id": "123456789"}

# Отправка запроса с куками
response = requests.get("https://jsonplaceholder.typicode.com/posts", cookies=cookies)

print(response.status_code)
print(response.cookies)

# %% [markdown]
# В этом примере мы отправляем запрос с кукой session_id, которая может быть использована сервером для отслеживания состояния сессии пользователя.

# %% [markdown]
# 2. Передача параметров и заголовков в запросах

# %% [markdown]
# Параметры часто используются в URL-адресах для уточнения запроса (например, фильтры или лимиты). Библиотека requests позволяет легко передавать параметры и заголовки в запросах.
#
# Передача параметров в запросах
# Для передачи параметров в запросах GET, POST и других, библиотека requests позволяет использовать параметр params. Этот параметр принимает словарь, который автоматически преобразуется в строку запроса.
#
# Пример:

# %%
# import requests

# Параметры запроса
params = {"userId": 1, "limit": 5}

response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)

print(response.status_code)
print(response.json())

# %% [markdown]
# Здесь мы передаем параметры userId и limit, которые будут автоматически добавлены к URL как часть строки запроса: ?userId=1&limit=5.

# %% [markdown]
# Передача параметров в запросе POST
# В случае с методом POST, параметры передаются в теле запроса:
#

# %%
# import requests

# Данные для отправки
data = {"title": "New Post", "body": "This is the body of the post", "userId": 1}

response = requests.post("https://jsonplaceholder.typicode.com/posts", data=data)

print(response.status_code)
print(response.json())

# %% [markdown]
# Здесь мы отправляем данные в теле запроса, и сервер обрабатывает их как форму.

# %% [markdown]
# 3. Сессии и авторизация
# Сессии и авторизация необходимы для работы с веб-сервисами, которые требуют подтверждения личности пользователя или сохранения состояния между запросами.
#
# Использование сессий
# Сессия позволяет сохранять параметры, такие как куки, авторизационные данные и заголовки, между несколькими запросами. Это полезно, когда нужно работать с одним и тем же сервером в рамках одного сеанса.
#
# Пример:

# %%
# import requests

# Создание сессии
session = requests.Session()

# Добавление заголовков в сессию
session.headers.update({"User-Agent": "my-app/1.0"})

# Отправка первого запроса
response = session.get("https: //jsonplaceholder.typicode. com/posts")
print(response.status_code)

# Отправка второго запроса с той же сессией
response = session.get("https: //jsonplaceholder. typicode. com/posts/1")
print(response.status_code)

# %% [markdown]
# В этом примере мы создаем сессию, добавляем заголовки и отправляем несколько запросов в рамках одной сессии. Это позволяет эффективно управлять состоянием.
#
# Авторизация
# Авторизация необходима для получения доступа к защищенным ресурсам. Библиотека requests позволяет использовать базовую авторизацию и токены.
#
# Базовая авторизация
#

# %%
# import requests
# from requests.auth import HTTPBasicAuth
from niquests.auth import HTTPBasicAuth

response = requests.get(
    "https: //jsonplaceholder.typicode.com/posts",
    auth=HTTPBasicAuth("username", "password"),
)

print(response.status_code)
print(response.text)

# %% [markdown]
# Авторизация с использованием токена

# %%
# import requests

headers = {"Authorization": "Bearer your_token"}

response = requests.get("https://jsonplaceholder.typicode.com/posts", headers=headers)

print(response.status_code)
print(response.text)

# %% [markdown]
# В этом примере используется авторизация с помощью токена Bearer, который добавляется в заголовок запроса.
