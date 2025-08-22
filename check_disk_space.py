# Код для контроля свободного места на Python
# Для контроля свободного места на диске в коде используется модуль psutil.

import shutil

def check_disk_space(path='/'):
    try:
        total, used, free = shutil.disk_usage(path)
        return total, used, free
    except FileNotFoundError:
        print(f"Ошибка: Путь '{path}' не найден.")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def bytes_to_gb(bytes_value):
    """Конвертирует байты в гигабайты."""
    return bytes_value / (1024**3)

if __name__ == "__main__":
    # Можно указать путь, который необходимо проверить.
    # Для Windows используйте букву диска, например 'C:/'
    # Для Linux/macOS используйте '/' для корня или определенную точку монтирования, например '/home'
    path_to_check = 'C:/' # Измените, если хотите проверить другой путь

    disk_info = check_disk_space(path_to_check)

    if disk_info:
        total_bytes, used_bytes, free_bytes = disk_info

        total_gb = bytes_to_gb(total_bytes)
        used_gb = bytes_to_gb(used_bytes)
        free_gb = bytes_to_gb(free_bytes)

        print(f"--- Информация о дисковом пространстве для '{path_to_check}' ---")
        print(f"Общий объем: {total_gb:.2f} GB")
        print(f"Использовано: {used_gb:.2f} GB")
        print(f"Свободно: {free_gb:.2f} GB")

        # Здесь можно добавить проверку порогового значения
        free_percentage = (free_bytes / total_bytes) * 100
        print(f"Свободно: {free_percentage:.2f}%")

        if free_percentage < 10:
            print("ВНИМАНИЕ: Свободное место на диске ниже 10%! Рассмотрите возможность очистки.")
    else:
        print("Не удалось получить информацию о дисковом пространстве.")
