"""Разные способы создания переменной с именем из строки """

test_str = 'ITStart'

exec('%s = %d' % (test_str, 10)) # формируется и выполняется строка

print(f'Итог: {ITStart}')

locals()[test_str] = 20 # добавление в список локальных переменных
print(ITStart)

globals()[test_str] = 30 # добавление в список глобальных переменных
print(ITStart)