# Задача 1: Найти все email-адреса в тексте
# Условие: Напишите регулярное выражение, которое извлечет все корректные email-адреса из данного текста. Email состоит из имени пользователя, символа @, домена и доменной зоны. Имя пользователя и домен могут содержать буквы, цифры, подчеркивание, дефис и точки.
#
# text = """
# Свяжитесь с нами по info@example.com или support@my-domain.co.uk.
# Невалидный адрес: user@.com. Также есть test.user@gmail.com.
# """
# # Ваш код здесь

import re

text = """
Свяжитесь с нами по info@example.com или support@my-domain.co.uk.
Невалидный адрес: user@.com. Также есть test.user@gmail.com.
"""

pattern = r'[\w.-]+@[\w.-]+\.[\w.-]+'
emails = re.findall(pattern, text)
print(emails)

# Решение:
#
# import re
#
# text = """
# Свяжитесь с нами по info@example.com или support@my-domain.co.uk.
# Невалидный адрес: user@.com. Также есть test.user@gmail.com.
# """
#
# pattern = r'[\w.-]+@[\w.-]+\.[\w.-]+'
# emails = re.findall(pattern, text)
# print(emails)
# # Ожидаемый вывод: ['info@example.com', 'support@my-domain.co.uk', 'test.user@gmail.com']
# [\w.-]+: Один или более символов (буква, цифра, _, ., -) для имени пользователя.
#
# @: Буквальный символ @.
#
# [\w.-]+: Один или более символов для домена.
#
# \.: Экранированная точка.
#
# [\w.-]+: Один или более символов для доменной зоны верхнего уровня.