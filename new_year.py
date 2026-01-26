import tkinter as tk
from datetime import datetime

BACK1 = "#0a2e36" # цвет окна
BACK2 = "#1a4a5a" # цвет фона под цыфрами
DIGITS = "#4afc9f" # цвет цыфр

font_large = ("Courier", 48, "bold")
font_small = ("Arial", 14)

headers = ["ДНЕЙ", "ЧАСОВ", "МИНУТ", "СЕКУНД"]

class DigitLabel(tk.Label):
    """Виджет для отображения цыфр"""
    def __init__(self):
        tk.Label.__init__(self, frame, text="00", bg=BACK2, fg=DIGITS, font=font_large, width=3)


class HeaderLabel(tk.Label):
    """Виджет для отображения заголовков над цыфрами"""
    def __init__(self, header):
        tk.Label.__init__(self, frame, text=header, font=font_small, bg=BACK1, fg="white")


def update_countdown():
    """
    Обновляет отсчёт времени до Нового года каждую секунду.

    Функция вычисляет разницу между текущим моментом и ближайшим Новым годом
    (следующим или текущим, если он ещё не наступил), затем извлекает количество
    дней, часов, минут и секунд из этой разницы и обновляет соответствующие
    виджеты интерфейса. После обновления планирует свой повторный вызов
    через 1000 миллисекунд (1 секунду).

    Использует глобальные объекты:
        - datetime: для работы с датой и временем.
        - now: текущая дата и время.
        - new_year: дата и время ближайшего Нового года.
        - label_days, label_hours, label_minutes, label_seconds: виджеты Label,
          отображающие соответствующие части отсчёта.
        - root: главное окно Tkinter, используемое для метода after().

    Методы:
        root.after(1000, update_countdown) — запускает функцию повторно
        через 1000 мс, обеспечивая непрерывное обновление.

    Примечание:
        Функция предполагает, что переменные root, label_days, label_hours,
        label_minutes, label_seconds определены в глобальной области видимости
        и являются корректными виджетами Tkinter.
    """
    now = datetime.now()
    new_year = datetime(now.year + 1, 1, 1, 0, 0, 0)

    if now > new_year:
        new_year = datetime(now.year, 1, 1, 0, 0, 0)

    time_left = new_year - now

    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    label_days.config(text=f"{days:02d}")
    label_hours.config(text=f"{hours:02d}")
    label_minutes.config(text=f"{minutes:02d}")
    label_seconds.config(text=f"{seconds:02d}")
    root.after(1000, update_countdown)


root = tk.Tk()
root.title("🎄 До Нового Года осталось:")
root.configure(bg=BACK1)

frame = tk.Frame(root, bg=BACK1)
frame.pack(expand=True)

for header in headers:
    HeaderLabel(header).grid(row=0, column=headers.index(header), pady=10)

label_days = DigitLabel()
label_hours = DigitLabel()
label_minutes = DigitLabel()
label_seconds = DigitLabel()

label_days.grid(row=1, column=0, padx=10, pady=10)
label_hours.grid(row=1, column=1, padx=10, pady=10)
label_minutes.grid(row=1, column=2, padx=10, pady=10)
label_seconds.grid(row=1, column=3, padx=10, pady=10)

update_countdown()
root.mainloop()
