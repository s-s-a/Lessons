# https://www.youtube.com/watch?v=HIWfeIHocUc
import check_time

"""
Не используем циклы для выполнения встроенных задач.
Если их можно заменить оптимизированным действием,
лучше это сделать.
"""


@check_time
def cycle_example():
    result = 0
    numbers = [num for num in range(1_000_000)]

    for num in numbers:
        result += num
    print(result)


@check_time
def sum_example():
    numbers = [num for num in range(1_000_000)]
    print(sum(numbers))


@check_time
def summary():
    print(sum(range(1_000_000)))

if __name__ == "__main__":
    cycle_example()
    sum_example()
