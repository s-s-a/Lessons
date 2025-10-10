"""
Замена обоев на рабочем столе
"""
# https://it-start.online/articles/smena-oboev-rabochego-stola-windows-na-python

# Импортируем необходимые библиотеки
import ctypes
import os


def change_wallpaper_windows(path_to_image) -> bool:
    """
    Заменяет обои на рабочем столе используя функцию SystemParametersInfoW
    :param path_to_image:
    :return:
    """
    if not os.path.isfile(path_to_image):
        print(f"Ошибка: Файл '{path_to_image}' не найден.")
        return False

    user32 = ctypes.WinDLL('user32.dll')

    result = user32.SystemParametersInfoW(0x0014, 0, path_to_image, 0x01 | 0x02)
    message = f"Обои успешно изменены! Использовано изображение: {path_to_image}" if result \
        else "Не удалось изменить обои. Возможно, проблема с изображением или пути."
    print()
    return result


if __name__ == "__main__":
    # Указываем абсолютный путь к изображению
    path_to_your_image = r"C:\Users\ВашеИмя\Pictures\my_awesome_wallpaper.jpg"

    # Вызываем функцию
    change_wallpaper_windows(path_to_your_image)
