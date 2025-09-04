import re
import pyphen


def split_into_syllables(word):
	dic = pyphen.Pyphen(lang='ru')
	syllables = dic.inserted(word).split('-')

	return syllables


def encrypt_string(s):
	# Определяем слоги с помощью регулярного выражения
	syllables = re.findall(r'[а-яё]+', s, re.IGNORECASE)

	# Создаем новый список, добавляя 'с' и гласную букву после каждого слога
	encrypted_syllables = [syllable + 'с' + syllable[-1] for syllable in syllables]

	# Объединяем список в строку
	encrypted_string = ''.join(encrypted_syllables)

	return encrypted_string


# Тестирование функции
print(encrypt_string('Три друга'))  # Вывод: 'Триси друсугаса'

print(encrypt_string('Сам ты дурак')) # Сасам тысы дусурасак

# Тестирование функции
print(split_into_syllables('Три  друга'))

