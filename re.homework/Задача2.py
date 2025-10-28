# Задача 2: Разобрать лог-файл с именованными группами
# Условие: У вас есть строка лога. Используя именованные группы, извлеките из нее дату (date), время (time), уровень лога (level) и сообщение (message).
#
# log_entry = "2025-10-13 15:05:21 ERROR: Connection to database failed."
# # Ваш код здесь

import re

log_entry = "2025-10-13 15:05:21 ERROR: Connection to database failed."

pattern = r'^(?P<date>\d{4}-\d{2}-\d{2})\s(?P<time>\d{2}:\d{2}:\d{2})\s(?P<level>\w+):\s(?P<message>.*)$'
match = re.search(pattern, log_entry)

if match:
    print(match.groupdict())


# Решение:
#
# import re
#
# log_entry = "2025-10-13 15:05:21 ERROR: Connection to database failed."
#
# pattern = r'^(?P<date>\d{4}-\d{2}-\d{2})\s(?P<time>\d{2}:\d{2}:\d{2})\s(?P<level>\w+):\s(?P<message>.*)$'
# match = re.search(pattern, log_entry)
#
# if match:
#     print(match.groupdict())
# # Ожидаемый вывод: {'date': '2025-10-13', 'time': '15:05:21', 'level': 'ERROR', 'message': 'Connection to database failed.'}
# (?P<name>...): Создает именованную группу.
#
# \s: Соответствует пробельному символу.
#
# .*: Захватывает оставшуюся часть строки как сообщение.