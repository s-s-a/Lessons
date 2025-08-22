# Код для поиска строки по файлам

# Для работы с файлами в коде используется стандартный модуль os.

# Как работает скрипт:
# 🔵os.walk — рекурсивно обходит все папки и файлы.
# 🔵Открывает каждый файл в режиме чтения (utf-8, игнорируя ошибки кодировки).
# 🔵Проверяет каждую строку на наличие искомого текста.
# 🔵Выводит путь к файлу, номер строки и саму строку.

import os


def search_string_in_files(folder_path, search_string):
    # Проходимся по всем файлам и папкам, начиная с указанного пути
    for root, _, files in os.walk(folder_path):
        # Итерируемся по каждому файлу в текущей папке
        for file_name in files:
            file_path = os.path.join(root, file_name)

            try:
                # Открываем файл для чтения в режиме "r" с кодировкой "utf-8"
                with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
                    # Итерируемся по каждой строке в файле, начиная нумерацию с 1
                    for line_number, line in enumerate(file, start=1):
                        # Проверяем, содержится ли искомая строка в текущей строке файла
                        if search_string in line:
                            print(f"[Найдено] {file_path} (строка {line_number}): {line.strip()}")
            except (IOError, OSError):
                print(f"[Ошибка] Не удалось открыть файл: {file_path}")


if __name__ == "__main__":
    folder = input("Введите путь к папке: ")
    query = input("Введите строку для поиска: ")
    search_string_in_files(folder, query)
