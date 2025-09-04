<<<<<<< HEAD
# ��� ��� �������������� ������ �� ����������� � ����������� �� �� ���������� �� Python
from pathlib import Path


# ������� ����� ��� ������� ���������� �����
def create_folders(folder_path):
    # �������� ������ ���� ������ � �����
    files = folder_path.iterdir()

    # ���������� �� ������� ����� � ������� ����� �� �����������
=======
# Код для упорядочивания файлов по директориям в зависимости от их расширения на Python
from pathlib import Path


# Создаем папки для каждого расширения файла
def create_folders(folder_path):
    # Получаем список всех файлов в папке
    files = folder_path.iterdir()

    # Проходимся по каждому файлу и создаем папки по расширениям
>>>>>>> 5c39f649394f144af54e86d1663d6d480dab1841
    for file in files:
        if file.is_file():
            file_extension = file.suffix
            folder_name = file_extension[1:]
            folder_path_new = folder_path / folder_name

<<<<<<< HEAD
            # ���������, ���������� �� ����� ��� ������� ����������
=======
            # Проверяем, существует ли папка для данного расширения
>>>>>>> 5c39f649394f144af54e86d1663d6d480dab1841
            if not folder_path_new.exists():
                folder_path_new.mkdir(parents=True)


<<<<<<< HEAD
# ���������� ����� � ��������������� �����
def move_files(folder_path):
    create_folders(folder_path)
    # �������� ������ ���� ������ � �����
    files = folder_path.iterdir()

    # ���������� �� ������� ����� � ���������� ��� � ��������������� �����
=======
# Перемещаем файлы в соответствующие папки
def move_files(folder_path):
    create_folders(folder_path)
    # Получаем список всех файлов в папке
    files = folder_path.iterdir()

    # Проходимся по каждому файлу и перемещаем его в соответствующую папку
>>>>>>> 5c39f649394f144af54e86d1663d6d480dab1841
    for file in files:
        if file.is_file():
            file_extension = file.suffix
            folder_name = file_extension[1:]
            folder_path_new = folder_path / folder_name
            file_path_new = folder_path_new / file.name

<<<<<<< HEAD
            # ���������� ���� � ��������������� �����
=======
            # Перемещаем файл в соответствующую папку
>>>>>>> 5c39f649394f144af54e86d1663d6d480dab1841
            file.rename(file_path_new)


move_files(Path(r'C:\Users\admin\pythonProject\files'))
