import pyperclip
import time

buffer_pause = ''

while True:
    buffer = pyperclip.paste()

    if buffer != buffer_pause:
        print(buffer)
        with open('text.txt', 'a', encoding='utf-8') as file:
            file.write(buffer)

        buffer_pause = buffer
    time.sleep(0.01)

