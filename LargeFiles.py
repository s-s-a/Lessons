from pathlib import Path


def find_large_files(folder_path, size_threshold_mb):
    # Преобразуем порог размера в байты
    size_threshold_bytes: int = size_threshold_mb * 1024 * 1024

    # Создаём объект Path для указанной папки
    folder = Path(folder_path)

    # Рекурсивно проходим по всем файлам в папке и подкаталогах
    for file_path in folder.rglob('*'):
        # Проверяем, является ли найденный объект файлом
        if file_path.is_file():
            try:
                # Получаем размер файла в байтах
                file_size = file_path.stat().st_size

                # Если размер файла превышает указанный порог, выводим его путь и размер в МБ
                if file_size > size_threshold_bytes:
                    print(f"{file_path} - {file_size / (1024 ** 2):.2f} MB")
            except FileNotFoundError:
                # Если файл был удалён до обработки, игнорируем ошибку
                pass


# Пример: найти файлы больше 1024 МБ в папке "C:/"
find_large_files("D:/", 1024)
