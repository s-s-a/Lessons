# Код для очистки папки от старых файлов на Python

# Для работы с файлами в коде используется модуль os, а для работы со временем - time.


import os
import time


def clean_old_files(folder_path: str, days: int = 7):
    """
    Удаляет файлы старше указанного количества дней из папки.

    :param folder_path: путь к папке
    :param days: количество дней, старше которых файлы будут удалены
    """
    # Время "среза"
    cutoff_time = time.time() - days * 86400

    # Проходим по всем файлам в папке
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            file_mtime = os.path.getmtime(file_path)  # Время изменения файла

            if file_mtime < cutoff_time:
                try:
                    os.remove(file_path)
                    print(f"Удалён файл: {file_path}")
                except Exception as e:
                    print(f"Ошибка при удалении {file_path}: {e}")


if __name__ == "__main__":
    # Указываем путь к папке
    folder = r"C:\Users\YourName\Downloads"
    clean_old_files(folder, days=7)
