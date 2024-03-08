"""
Упражнения с исключениями
"""

a: int = int(input('Введите первое число:'))
b: int = int(input('Введите второе число:'))

result: int = 0

try:
    result = int(a / b)
except ZeroDivisionError:
    print('На ноль делить нельзя')
print(f'Результат = {result}')

# ZeroDivisionError