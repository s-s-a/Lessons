# Сжатие файлов в ZIP-архив с помощью Python
# Сжатие данных в ZIP-архивы — один из самых удобных способов уменьшить размер файлов
# и объединить их для передачи или хранения. Встроенный модуль zipfile в Python позволяет
# работать с ZIP-архивами без установки дополнительных библиотек.

# Для начала импортируем модуль zipfile и класс Path из pathlib:

import zipfile
from pathlib import Path

# Создадим функцию create_zip(), которая будет создавать ZIP-архив с указанными файлами.
# У функции будет присутствовать три параметра, а именно:
# folder_path — путь к папке, которую нужно заархивировать
# archive_name — имя создаваемого ZIP-архива.
import zipfile
from pathlib import Path


def zip_folder(folder_path: str, archive_name: str) -> None:
	# Внутри неё, первым делом произведём проверку на существование папки:
	folder = Path(folder_path)

	# Проверяем, существует ли указанная папка
	if not folder.is_dir():
		print(f"Папка '{folder_path}' не найдена.")
		return

	# Далее воспользуемся контекстным менеджером и откроем/создадим ZIP-архив в режиме записи.
	# Циклом рекурсивно пройдёмся по всем файлам в директории и добавим их в итоговый архив:

	# Открываем или создаём ZIP-архив в режиме записи
	with zipfile.ZipFile(archive_name, mode="w", compression=zipfile.ZIP_DEFLATED) as archive:
		# Рекурсивно обходим все файлы и папки внутри заданной директории
		for file_path in folder.rglob("*"):
			if file_path.is_file():
			# Добавляем файл в архив, сохраняя структуру директорий
			archive.write(file_path, arcname=file_path.relative_to(folder))
			print(f"Добавлен файл: {file_path}")

	print(f"Архив '{archive_name}' успешно создан.")


# Осталось добавить точку входа:
if __name__ == "__main__":
	# Пример использования
	# Пользователь вводит путь к папке
	folder_path = input("Введите путь к папке для сжатия: ").strip()

	# Автоматически формируем имя архива из имени папки
	archive_name = Path(folder_path).name + ".zip"

	# Вызываем функцию архивации
	zip_folder(folder_path, archive_name)
