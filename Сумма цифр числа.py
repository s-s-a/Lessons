# MARK: Использование цикла for

number: int = 11223344
sum_digits: int = 0
for i in str(number):
    sum_digits += int(i)

print(f"Сумма цифр числа: {sum_digits}")
# Вывод: 20


# MARK: Использование цикла while

number = 11223344
sum_digits = 0

while number > 0:
    sum_digits += number % 10
    number //= 10

print(f"Сумма цифр числа: {sum_digits}")

# Вывод: Сумма цифр числа: 20

# MARK: Использование рекурсии
'''Использование рекурсии'''


def f_sum_digits(n):
    return 0 if n == 0 else int(n % 10) + f_sum_digits(int(n / 10))

number = 11223344
print(f"Сумма цифр числа: {f_sum_digits(number)}")

# Вывод: Сумма цифр числа: 20

# MARK: Использование map
'''Использование map'''

number = 11223344
a = str(number)
print(f"Сумма цифр числа: {sum(map(int, a))}")