import time
from tkinter import *
import pygame

def stop()->None:
    btn_start.pack()
    btn_stop.pack_forget()
    pygame.mixer.music.pause()


def sound()->None:
    btn_start.pack_forget()
    btn_stop.pack()
    pygame.mixer.music.play()

def start()->None:
    duration:int = int(seconds.get())
    while duration:
        m, s = divmod(int(duration), 60)
        min_sec_format:str = '{:02d}:{:02d}'.format(m, s)
        count_digit['text'] = min_sec_format
        count_digit.update()
        time.sleep(1)
        duration -= 1

    sound()


file:str = '1.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)

root:object = Tk()
root.title('Таймер')
root.geometry('150x150')
root.resizable(False, False)

count_digit:object = Label(root, text='0', font='Arial 15 bold')
count_digit.pack()

seconds:object = Entry(root, font='Arial 15 bold', width=7)
seconds.pack()

btn_start:object = Button(root, text='Старт', font='Arial 15 bold', command=start)
btn_start.pack()

btn_stop:object = Button(root, text='Выключить', font='Arial 15 bold', command=stop)

root.mainloop()
