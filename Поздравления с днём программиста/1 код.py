import tkinter as tk
from tkinter import messagebox

# Функция для отображения поздравления
def show_congratulation():
    messagebox.showinfo("Поздравление", "Поздравляю с Днём программиста!\nПусть код всегда работает!")

# Создаем основное окно
root = tk.Tk()
root.title("Поздравление с Днём программиста")
root.geometry("400x300")

# Надпись с поздравлением
label = tk.Label(root, text="С Днём программиста!", font=("Helvetica", 18), fg="blue")
label.pack(pady=50)

# Кнопка для отображения всплывающего сообщения
button = tk.Button(root, text="Показать поздравление", command=show_congratulation, font=("Helvetica", 12))
button.pack(pady=20)

# Рисование простого элемента графики
canvas = tk.Canvas(root, width=200, height=100)
canvas.pack()

# Рисуем простую фигуру (например, смайлик)
canvas.create_oval(50, 20, 150, 100, fill="yellow", outline="black")
canvas.create_oval(70, 40, 90, 60, fill="black")  # Левый глаз
canvas.create_oval(110, 40, 130, 60, fill="black")  # Правый глаз
canvas.create_arc(70, 60, 130, 90, start=0, extent=-180, style=tk.ARC, outline="black")  # Улыбка

# Запуск цикла обработки событий
root.mainloop()
