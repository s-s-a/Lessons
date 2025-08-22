from tkinter.constants import NW, LEFT

import customtkinter as ctk
from PIL import ImageTk


def add(task):
    f = ctk.CTkFrame(App)

    ctk.CTkCheckBox(f, text=task).pack(anchor=NW, side=LEFT)
    ctk.CTkButton(f, image=img_del,text='',width=30,command=lambda: f.pack_forget()).pack(anchor=NW,side=LEFT,padx=10)
    f.pack(anchor=NW,padx=5,pady=5)



class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        # self.label = customtkinter.CTkLabel(self, text="ToplevelWindow")
        # self.label.pack(padx=20, pady=20)
        self.task_text = ctk.CTkEntry(self)
        self.task_text.pack(pady=5)

        ctk.CTkButton(self, text='Добавить',font=ctk.CTkFont('Arial',13,'bold'),command=lambda: add(self.task_text.get())).pack()


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")

        self.button_1 = ctk.CTkButton(self, text="'Добавить задачу'", command=self.open_toplevel)
        self.button_1.pack(side="top", padx=20, pady=20)

        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

if __name__ == "__main__":

    app = App()
    img_del = ImageTk.PhotoImage(file='delete.bmp')
    app.mainloop()
