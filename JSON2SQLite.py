# ����������� JSON � SQLite �� Python
# https://dzen.ru/subscriptions-manager?channel=615c3ace71bd4944acea8a67
# ������ JSON-������
# ��������, ��� � ��� ���� ���� users.json �� ��������� ����������:

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

# ������ ��� �����������
# ����� ���������� �������, ������ ����� �� ����������� ������ sqlite3 ��� ������ � ��, � ����� ������ json ��� ������ � ����� json-������:

import json
import sqlite3

# �������� ������ �� json-�����, ��������� ����������� �������� with � as:

import json
import sqlite3

# ��������� JSON-������
with open('users.json', 'r', encoding='utf-8') as f:
data = json.load(f)

# ����������� � ���� ������ SQLite ��� ��������� users.db (����� �������, ���� � �� ����������):

import json
import sqlite3

with open('users.json', 'r', encoding='utf-8') as f:
data = json.load(f)

# ������������ � SQLite (������� ����, ���� ��� ���)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# �������� �������, �������������� ������ �, ����� �������� ������ � ������, ���� ��� ��� ������������:

import json
import sqlite3

with open('users.json', 'r', encoding='utf-8') as f:
data = json.load(f)

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# ������ ������� (���� �����, ������� ����� ����)
cursor.execute('DROP TABLE IF EXISTS users')
cursor.execute('''
CREATE TABLE users (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
email TEXT NOT NULL
)
''')

# ��������� ���� ������� ������ �� json-����� � ������� ���� ������:

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

# ��������� ������
for user in data:
cursor.execute('''
INSERT INTO users (id, name, email)
VALUES (:id, :name, :email)
''', user)

# �������� ��������� � ��������� ����������:

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

# ��������� ��������� � ��������� ����������
conn.commit()
conn.close()
