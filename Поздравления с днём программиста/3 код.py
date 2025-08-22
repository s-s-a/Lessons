import tkinter as tk
import random
import time

# Функция для создания падающих строк кода
def create_rain(canvas, width, height):
    letters = "0123456789ABCDEF"  # Строки кода
    font_size = 14
    speed = 50

    # Позиции для строк
    positions = [random.randint(0, width // font_size) for _ in range(50)]

    # Бесконечная анимация "дождя"
    while True:
        canvas.delete("all")  # Очищаем экран

        for i in range(len(positions)):
            x = positions[i] * font_size
            y = (i * font_size + time.time() * speed) % height

            # Рисуем символы
            canvas.create_text(x, y, text=random.choice(letters), font=("Courier", font_size), fill="green")

        canvas.update()
        time.sleep(0.05)

# Создаем основное окно
root = tk.Tk()
root.title("С Днём программиста")
root.geometry("500x500")
root.config(bg="black")

# Надпись с поздравлением
label = tk.Label(root, text="Поздравляю с Днём программиста!", font=("Helvetica", 16), fg="lime", bg="black")
label.pack(pady=20)

# Холст для отображения анимации
canvas = tk.Canvas(root, width=500, height=400, bg="black")
canvas.pack()

# Запускаем анимацию дождя из кода в отдельном потоке
root.after(0, create_rain, canvas, 500, 400)

# Запуск основного цикла
root.mainloop()
