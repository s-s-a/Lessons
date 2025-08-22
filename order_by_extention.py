# ��� ��� �������������� ������ �� ����������� � ����������� �� �� ���������� �� Python
from pathlib import Path


# ������� ����� ��� ������� ���������� �����
def create_folders(folder_path):
    # �������� ������ ���� ������ � �����
    files = folder_path.iterdir()

    # ���������� �� ������� ����� � ������� ����� �� �����������
    for file in files:
        if file.is_file():
            file_extension = file.suffix
            folder_name = file_extension[1:]
            folder_path_new = folder_path / folder_name

            # ���������, ���������� �� ����� ��� ������� ����������
            if not folder_path_new.exists():
                folder_path_new.mkdir(parents=True)


# ���������� ����� � ��������������� �����
def move_files(folder_path):
    create_folders(folder_path)
    # �������� ������ ���� ������ � �����
    files = folder_path.iterdir()

    # ���������� �� ������� ����� � ���������� ��� � ��������������� �����
    for file in files:
        if file.is_file():
            file_extension = file.suffix
            folder_name = file_extension[1:]
            folder_path_new = folder_path / folder_name
            file_path_new = folder_path_new / file.name

            # ���������� ���� � ��������������� �����
            file.rename(file_path_new)


move_files(Path(r'C:\Users\admin\pythonProject\files'))
