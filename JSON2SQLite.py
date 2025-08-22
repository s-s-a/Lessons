# Конвертация JSON в SQLite на Python
# https://dzen.ru/subscriptions-manager?channel=615c3ace71bd4944acea8a67
# Пример JSON-данных
# Допустим, что у нас есть файл users.json со следующим содержимым:

[
{
"id": 1,
"name": "Anna",
"email": "anna@example.com"
},
{
"id": 2,
"name": "Ivan",
"email": "ivan@example.com"
}
]

# Скрипт для конвертации
# Перед написанием скрипта, первым делом мы импортируем модуль sqlite3 для работы с БД, а также модуль json для работы с нашим json-файлом:

import json
import sqlite3

# Загрузим данные из json-файла, используя контекстный менеджер with … as:

import json
import sqlite3

# Загружаем JSON-данные
with open('users.json', 'r', encoding='utf-8') as f:
data = json.load(f)

# Подключимся к базе данных SQLite под названием users.db (будет создана, если её не существует):

import json
import sqlite3

with open('users.json', 'r', encoding='utf-8') as f:
data = json.load(f)

# Подключаемся к SQLite (создаст файл, если его нет)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Создадим таблицу, предварительно удалив её, чтобы избежать ошибок в случае, если она уже существовала:

import json
import sqlite3

with open('users.json', 'r', encoding='utf-8') as f:
data = json.load(f)

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Создаём таблицу (если нужно, удаляем перед этим)
cursor.execute('DROP TABLE IF EXISTS users')
cursor.execute('''
CREATE TABLE users (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
email TEXT NOT NULL
)
''')

# Используя цикл вставим данные из json-файла в таблицу базы данных:

import json
import sqlite3

with open('users.json', 'r', encoding='utf-8') as f:
data = json.load(f)

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS users')
cursor.execute('''
CREATE TABLE users (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
email TEXT NOT NULL
)
''')

# Вставляем данные
for user in data:
cursor.execute('''
INSERT INTO users (id, name, email)
VALUES (:id, :name, :email)
''', user)

# Сохраним изменения и закрываем соединение:

import json
import sqlite3

with open('users.json', 'r', encoding='utf-8') as f:
data = json.load(f)

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS users')
cursor.execute('''
CREATE TABLE users (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
email TEXT NOT NULL
)
''')

for user in data:
cursor.execute('''
INSERT INTO users (id, name, email)
VALUES (:id, :name, :email)
''', user)

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()
