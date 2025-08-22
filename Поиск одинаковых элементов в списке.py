'''Поиск одинаковых элементов в списке с помощью словаря'''

unordered_list = [6, 6, 8, 7, 5, 1, 4, 5, 4, 7]
duplicate_elements = {}

for item in unordered_list:
    if item in duplicate_elements:
        duplicate_elements[item] += 1
    else:
        duplicate_elements[item] = 1

print(duplicate_elements)

# Вывод: {6: 2, 8: 1, 7: 2, 5: 2, 1: 1, 4: 2}

'''Поиск одинаковых элементов в списке с помощью модуля collections'''

import collections

unordered_list = [6, 6, 8, 7, 5, 1, 4, 5, 4, 7]
count_frequency = collections.Counter(unordered_list)
print(dict(count_frequency))

# Вывод: {6: 2, 8: 1, 7: 2, 5: 2, 1: 1, 4: 2}


'''Поиск одинаковых элементов в списке с помощью функции filter()'''

unordered_list = [6, 6, 8, 7, 5, 1, 4, 5, 4, 7]

count_frequency = filter(lambda x: unordered_list.count(x) > 1, unordered_list)
count_frequency = list(set(count_frequency))

print(count_frequency)

# Вывод: [4, 5, 6, 7]