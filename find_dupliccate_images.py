# Код для поиска повторяющихся изображений на Python
#   pip install Pillow imagehash

from PIL import Image
import imagehash
import os


def find_duplicate_images(folder):
    hashes = {}  # Словарь для хранения хэшей изображений и соответствующих им имен файлов
    for filename in os.listdir(folder):
        # Проверяем, что файл имеет расширение изображения
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            path = os.path.join(folder, filename)
            hash_val = imagehash.average_hash(Image.open(path))  # Создаем хэш изображения
            if hash_val in hashes:  # Если такой хэш уже встречался
                print(f"Дубликат: {filename} и {hashes[hash_val]}")  # Выводим найденный дубликат
            else:
                hashes[hash_val] = filename  # Сохраняем хэш и имя файла в словарь


if __name__ == '__main__':
    folder = input("Введите путь к папке с изображениями: ")
    find_duplicate_images(folder)
