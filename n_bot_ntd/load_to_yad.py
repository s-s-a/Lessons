# Дабы не закидывать в ЯД файлы вручную, набросал скрипт. Использует он тот же файл с токенами, что и бот cfg_token.
# Возле скрипта кладу файлы, внутри в нем отмечаю папку куда надо закинуть (правлю или как вариант заготовить на
# каждую отдельно) и запускаю его. После загрузки он удаляет обработанные файлы.
#
# Код скрипта наполнения папки на ЯД
import os
from datetime import datetime
import yadisk
import cfg_token

# токен яндекс диска
y = yadisk.YaDisk(token=cfg_token.ya_dsk_token)

# загружаемый файл должен иметь расширение
format_move_files = (
    ".pdf",
    ".doc",
    ".docx",
    ".djvu",
    ".rar",
)  # , '.rtf') '.zip', - зипы плохо обраб. ЯД
up_dir = "Serii"  # папка для хранения


## 'GOST'  'SP'  'VSN' 'STO'


def up_to_dir(file_name):
    """
    Загрузка файла в папку на ЯД
    :param file_name:
    """
    try:
        # путь к загружаемым в облако файлам от пользователей
        src = f"/{up_dir}"
        dst = f"{src}/{file_name}"
        if not y.is_dir(src):  # если папки нет, то создать
            y.mkdir(src)
        # грузим в облако файл
        if os.path.exists(file_name):
            if y.is_file(dst):  # если такой файл есть то яндя даст ошибку, поэтому: вот
                dst = f'{src}/Double-{datetime.now().strftime("%d.%m.%Y-%H.%M.%S")}-{file_name}'
            y.upload(file_name, dst)
            print(f"Загружен файл: {file_name} в облако {dst}")
            os.remove(file_name)
            print(f"Удален файл: {file_name}")
    except Exception as e:
        print(f"Ошибка: {e}")


k_file = 0
file_in_dir = os.listdir(os.getcwd())
for file in file_in_dir:
    if file.endswith(
        format_move_files, 0, len(file)
    ):  # '.pdf'  if file.endswith('.pdf'):tuple(
        print(f"Обрабатываю файл: {file}")
        up_to_dir(file)
        k_file = k_file + 1
        print("-----------------------------------------------")
    else:
        continue
print(f"Обработано файлов: {k_file:d}")
input("Работа завершена. Тисни ентер.")
