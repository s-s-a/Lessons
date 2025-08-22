from pathlib import Path
import shutil
from datetime import datetime


def sort_photos_by_date(photo_folder):
    # Преобразуем строку пути к папке в объект Path
    folder_path = Path(photo_folder)
    # Проходимся по всем элементам в указанной папке
    for file_path in folder_path.iterdir():
        # Проверяем, является ли элемент файлом и имеет ли он нужное расширение
        if file_path.is_file() and file_path.suffix.lower() in {'.png', '.jpg', '.jpeg'}:
            # Получаем время последнего изменения файла
            creation_time = file_path.stat().st_mtime
            # Преобразуем время в формат даты 'ГГГГ-ММ-ДД'
            date_folder = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d')
            # Создаем путь к папке с датой
            target_folder = folder_path / date_folder

            # Создаем папку с датой, если она не существует
            target_folder.mkdir(exist_ok=True)

            # Перемещаем файл в соответствующую папку
            shutil.move(str(file_path), str(target_folder / file_path.name))
            # Выводим сообщение о перемещении файла
            print(f"Изображение {file_path.name} перенесено в {target_folder}")


# Указываем папку с изображениями
photo_folder = 'images2'
# Вызываем функцию для сортировки фотографий по дате
sort_photos_by_date(photo_folder)
