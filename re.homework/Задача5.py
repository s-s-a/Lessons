# Задача 5: Валидация сложного пароля
# Условие: Напишите одно регулярное выражение для проверки пароля на соответствие следующим правилам:
#
# Длина от 8 до 32 символов.
# Должен содержать хотя бы одну строчную букву.
# Должен содержать хотя бы одну заглавную букву.
# Должен содержать хотя бы одну цифру.
#
# Ваш код здесь

import re

def validate_password(password):
    pattern = r'' # Ваше выражение
    return bool(re.match(pattern, password))

print(validate_password("Short7")) # False
print(validate_password("nouppercase7")) # False
print(validate_password("NOLOWERCASE7")) # False
print(validate_password("NoDigits")) # False
print(validate_password("ValidPass123")) # True

# Решение:
#
# import re
#
# def validate_password(password):
#     pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,32}$'
#     return bool(re.match(pattern, password))
#
# print(f'Short7 -> {validate_password("Short7")}')
# print(f'nouppercase7 -> {validate_password("nouppercase7")}')
# print(f'NOLOWERCASE7 -> {validate_password("NOLOWERCASE7")}')
# print(f'NoDigits -> {validate_password("NoDigits")}')
# print(f'ValidPass123 -> {validate_password("ValidPass123")}')
# # Ожидаемый вывод: False, False, False, False, True
# ^: Начало строки.
#
# (?=.*[a-z]): Просмотр вперед, который проверяет наличие хотя бы одной строчной буквы в любом месте строки.
#
# (?=.*[A-Z]): Просмотр вперед для проверки наличия заглавной буквы.
#
# (?=.*\d): Просмотр вперед для проверки наличия цифры.
#
# .{8,32}: Проверяет, что общая длина строки от 8 до 32 любых символов.
#
# $: Конец строки.
#
# Все просмотры вперед не "потребляют" символы, а просто проверяют условия из одной и той же начальной позиции,
# что позволяет нам проверить все правила одновременно.