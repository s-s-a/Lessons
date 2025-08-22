import tkinter as tk
import time

# Функция для эффекта печати текста
def type_text(label, text, delay=100):
    label.config(text="")  # Очищаем текст в метке перед печатью
    for i in range(len(text) + 1):
        label.config(text=text[:i])
        label.update()
        time.sleep(delay / 1000)

# Функция для старта анимации
def start_animation():
    type_text(label, "Поздравляю с Днём программиста!", delay=150)

# Создаем основное окно
root = tk.Tk()
root.title("Поздравление с Днём программиста")
root.geometry("500x400")

# Надпись для отображения текста с анимацией
label = tk.Label(root, text="", font=("Helvetica", 16), fg="green")
label.pack(pady=50)

# Кнопка для запуска анимации
button = tk.Button(root, text="Показать поздравление", command=start_animation, font=("Helvetica", 12))
button.pack(pady=20)

# Рисование простого элемента графики
canvas = tk.Canvas(root, width=200, height=100)
canvas.pack()

# Рисуем простую фигуру (например, сердце)
canvas.create_polygon(100, 40, 120, 60, 140, 40, 160, 60, 140, 80, 100, 80, 80, 60, fill="red", outline="black")

# Запуск основного цикла
root.mainloop()
