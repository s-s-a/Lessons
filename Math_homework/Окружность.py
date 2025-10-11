import math

radius = float(input('Введите радиус окружности: '))
if radius > 0:
    print('Площадь окружности: ', math.pi * radius ** 2)
    print('Длина окружности: ', 2 * math.pi * radius)