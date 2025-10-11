from plyer import notification
import time
from datetime import datetime

def smart_timer(minutes, message="Время вышло!"):
    seconds = minutes * 60
    print(f"Таймер запущен на {minutes} минут(ы)")

    time.sleep(seconds)

    current_time = datetime.now().strftime('%H:%M')
    title = f"Таймер сработал! ({current_time})"

    notification.notify(
        title=title,
        message=message,
        app_name="Python Smart Timer",
        timeout=10
    ) # pyright: ignore[reportOptionalCall]

if __name__ == "__main__":
# Запускаем таймер на 1 минуту с кастомным сообщением
    smart_timer(1, "Пора размяться! Прошла уже целая минута!")
    print("Таймер завершил работу")

# Возможные доработки и улучшения
# После того как базовый таймер работает, можно добавить дополнительные функции:

# 1. Обработка ошибок — добавить try/except блоки
# 2. Аргументы командной строки — использовать библиотеку argparse для гибкости
# 3. Звуковые сигналы — добавить воспроизведение звука вместе с уведомлением
# 4. Графический интерфейс — создать окно с кнопками используя tkinter