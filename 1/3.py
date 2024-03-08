# https://www.youtube.com/watch?v=HIWfeIHocUc
import check_time


"""
Сравнение zip и обычного подхода с циклами
"""


# FIXME: Есть риск выйти за пределы списка
@check_time
def stupid_example():
    res = 0
    a = [num for num in range(1_000_000)]
    b = [num for num in range(1_000_000)]

    for index in range(len(a)):
        res = a[index] + b[index]
    print(res)


@check_time
def zip_example():
    res = 0
    a = [num for num in range(1_000_000)]
    b = [num for num in range(1_000_000)]

    for a_val, b_val in zip(a, b):
        res = a_val + b_val
    print(res)


if __name__ == "__main__":
    stupid_example()

    zip_example()
