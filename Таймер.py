""" Таймер со сзвуком """

import time
from tkinter import *
from playsound import *


def sound():
    btn_start.pack_forget()
    btn_stop.pack()
    playsound(file, False)

def start():
    duration = int(seconds.get())
    while duration:
        m, s = divmod(int(duration), 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        count_digit['text'] = min_sec_format
        count_digit.update()
        tim.sleep(1)
        duration -= 1
    sound()

def stop():
    btn_stop.pack_forget()
    btn_start.pack()
    playsound(file, True)


file = '1.mp3'

root = Tk()
root.title('Таймер')
root.geometry('150x150')
root.resizeble(False, False)

count_digit = Label(root, text='0', font='Arial 15 bold')
count_digit.pack()

seconds = Entry(root, font='Arial 15 bold', width=7)
seconds.pack(pady=10)

btn_start = Button(root, text='Старт', font='Arial 15 bold', command=start)
btn_start.pack()

btn_stop = Button(root, text='Выключить', font='Arial 15 bold', command=stop)
btn_stop.pack()

root.mainloop()
