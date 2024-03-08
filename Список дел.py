import customtkinter as ctk
from tkinter import *
from PIL import ImageTk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')


def add(task):
    f = ctk.CTkFrame(root)

    ctk.CTkCheckBox(f, text=task).pack(anchor=NW, side=LEFT)
    ctk.CTkButton(f, image=img_del,text='',width=30,command=lambda: f.pack_forget()).pack(anchor=NW,side=LEFT,padx=10)
    f.pack(anchor=NW,padx=5,pady=5)


class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("300x80")
        self.title('Добаить задачу')
        self.task_text = ctk.CTkEntry(self)
        self.task_text.pack(pady=5)

        ctk.CTkButton(wnd, text='Добавить',font=ctk.CTkFont('Arial',13,'bold'),command=lambda: add(task_text.get())).pack()


def add_task():
    wnd = ToplevelWindow()



root = ctk.CTk()
root.title = 'Планировщик задач'
root.geometry('700x300')

img_del = ImageTk.PhotoImage(file='delete.bmp')

btn_add_task = ctk.CTkButton(root, text='Добавить задачу', font=ctk.CTkFont('Arial', 13, 'bold'), command=add_task)
btn_add_task.pack(anchor='s', side='bottom', pady=5)

root.mainloop()
