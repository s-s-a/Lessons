# Код для упорядочивания файлов по директориям в зависимости от их расширения на Python
from pathlib import Path


# Создаем папки для каждого расширения файла
def create_folders(folder_path):
    # Получаем список всех файлов в папке
    files = folder_path.iterdir()

    # Проходимся по каждому файлу и создаем папки по расширениям
    for file in files:
        if file.is_file():
            file_extension = file.suffix
            folder_name = file_extension[1:]
            folder_path_new = folder_path / folder_name

            # Проверяем, существует ли папка для данного расширения
            if not folder_path_new.exists():
                folder_path_new.mkdir(parents=True)


# Перемещаем файлы в соответствующие папки
def move_files(folder_path):
    create_folders(folder_path)
    # Получаем список всех файлов в папке
    files = folder_path.iterdir()

    # Проходимся по каждому файлу и перемещаем его в соответствующую папку
    for file in files:
        if file.is_file():
            file_extension = file.suffix
            folder_name = file_extension[1:]
            folder_path_new = folder_path / folder_name
            file_path_new = folder_path_new / file.name

            # Перемещаем файл в соответствующую папку
            file.rename(file_path_new)


move_files(Path(r'C:\Users\admin\pythonProject\files'))
