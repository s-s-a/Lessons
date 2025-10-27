"""
Часы по статье https://habr.com/ru/companies/pixel_study/articles/840970/
с некоторыми переделками
"""

import locale
import tkinter
import time

def get_info()-> tuple[str, str]:
    # current_time = time.localtime()
    # hour = current_time.tm_hour if current_time.tm_hour >= 10 else f"0{current_time.tm_hour}"
    # minute = current_time.tm_min if current_time.tm_min >= 10 else f"0{current_time.tm_min}"
    # days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    # monthes = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    # На Windows используйте кодировку CP1251 или UTF-8
    locale.setlocale(locale.LC_TIME, 'Russian_Russia.1251')  # Или 'ru_RU.UTF-8' если установлено

    # date_str: str = f'{current_time.tm_mday} {monthes[current_time.tm_mon - 1]}, {days[current_time.tm_wday]}'
    date_str:str = time.strftime("%d %B, %A").lower().replace('ь,', 'я,').replace('т,', 'та,').replace('й,', 'я,') 
    time_str: str = time.strftime("%H:%M")
    return (date_str, time_str)


window = tkinter.Tk()

window.geometry("430x250")
window.title("Часы")
window.resizable(False, False)

date_label = tkinter.Label(window, text="27 октября, Понедельник", font=("Arial Bold", 20))
date_label.pack(anchor=tkinter.CENTER)

time_label = tkinter.Label(window, text="19:16", font=("Arial Bold", 125))
time_label.pack(anchor=tkinter.CENTER)

# window.mainloop()

while True:
    date_str, time_str = get_info()
    date_label.config(text=date_str)
    time_label.config(text=time_str)
    date_label.update()
    time_label.update()
    time.sleep(0.25)