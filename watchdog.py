# Код для отслеживания изменений в папке на Python

# Для отслеживания изменений в директории в коде используется библиотека watchdog (https://t.me/programmersGuide_1/1435).

# ➡️Установка библиотеки: pip install watchdog

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

class MyEventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        """Логирует любое событие файловой системы."""
        if event.is_directory:
            event_type = "Каталог"
        else:
            event_type = "Файл"

        if event.event_type == 'created':
            print(f"СОЗДАН: {event_type} {event.src_path}")
        elif event.event_type == 'deleted':
            print(f"УДАЛЕН: {event_type} {event.src_path}")
        elif event.event_type == 'modified':
            print(f"ИЗМЕНЕН: {event_type} {event.src_path}")
        elif event.event_type == 'moved':
            print(f"ПЕРЕМЕЩЕН: {event_type} из {event.src_path} в {event.dest_path}")

def start_watching(path):
    event_handler = MyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print(f"Мониторинг папки: {path}. Нажмите Ctrl+C для остановки.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    print("Мониторинг остановлен.")


if __name__ == "__main__":
    # Замените 'путь_к_папке' на фактический путь к папке, которую вы хотите отслеживать
    folder_to_watch = 'путь_к_папке'

    # Создаем папку, если она не существует (необязательно, для демонстрации)
    if not os.path.exists(folder_to_watch):
        os.makedirs(folder_to_watch)
        print(f"Создана папка для демонстрации: {folder_to_watch}")

    start_watching(folder_to_watch)
