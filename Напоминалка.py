""" Программа напоминалка v 1.0"""

import time

def msg(timer, text):
    for i in range(timer, -1, -1):
        if int(i) == 0:
            print(text)
        time.sleep(1)

text = input("Введите то что нужно напомнить: ")
timer = int(input("Через сколько секунд напомнить?: "))
msg(timer, text)
