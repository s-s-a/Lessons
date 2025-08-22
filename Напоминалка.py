# """Программа напоминалка v 1.0"""

# import time
#
# def msg(timer, text):
#     for i in range(timer, -1, -1):
#         if int(i) == 0:
#             print(text)
#         time.sleep(1)
#
# text = input("Введите то что нужно напомнить: ")
# timer = int(input("Через сколько секунд напомнить?: "))
# msg(timer, text)

"""Программа напоминалка v 2.0"""

import schedule
import time
from plyer import notification


def show_notification(message) -> None:
    notification.notify(title="Напоминание", message=message, timeout=10)  # type: ignore


def add_reminder(text, reminder_time):
    schedule.every().day.at(reminder_time).do(show_notification, message=text)
    print(f"Напоминание добавлено на {reminder_time}: {text}")


if __name__ == "__main__":
    while True:
        text: str = input("Введите текст напоминания: ")
        reminder_time: str = input("Введите время (формат ЧЧ:ММ): ")
        add_reminder(text, reminder_time)
        print("Ожидание напоминания...")

        while True:
            schedule.run_pending()
            time.sleep(1)
