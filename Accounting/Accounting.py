import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3

connection = sqlite3.connect('finance.db')
cur = connection.cursor()

cur.execute("""
    Create table if not exists transactions (
        id integer primary key autoincrement,
        type text,
        amount real,
        comment text
        )
""")

connection.commit()


def add_transaction():
    if type_combobox.get() and amount_entry.get():
        try:
            transaction_type = type_combobox.get()
            amount = float(amount_entry.get())
            comment = comment_entry.get()

            cur.execute("""
            insert into transactions (type, amount, comment)
            values (?,?,?)
            """, (transaction_type, amount, comment))
            connection.commit()

            type_combobox.set('')
            amount_entry.delete(0, tkinter.END)
            comment_entry.delete(0, tkinter.END)
            messagebox.showinfo("Успех", "Транзакция успешно добавлена!")

        except ValueError:
            messagebox.showinfo("Ошибка", "Сумма введена некорректно!")

    else:
        messagebox.showinfo("Предупреждение", "Заполнены не все поля.")


def view_data():
    view_window = tkinter.Toplevel(root)
    view_window.title("Просмотр транзакций")

    treeview = ttk.Treeview(view_window)
    treeview.pack()

    treeview["columns"] = ("type", "amount", "comment")
    treeview.column("#0", width=0, stretch=tkinter.NO)
    treeview.column("type", width=100, anchor=tkinter.W)
    treeview.column("amount", anchor=tkinter.E, width=100)
    treeview.column("comment", anchor=tkinter.W, width=200)

    treeview.heading("#0", text="")
    treeview.heading("type", text="Тип")
    treeview.heading("amount", text="Сумма")
    treeview.heading("comment", text="Комментарий")
    cur.execute("Select * from transactions")
    rows = cur.fetchall()

    for row in rows:
        treeview.insert("", "end", text="", values=row[1:])


root = tkinter.Tk()
root.title("Домашняя бухгалтерия")
root.geometry('200x280')
root.resizable(True, False)
root.wm_minsize(200, 280)

type_label = tkinter.Label(root, text="Тип:")
type_label.pack(pady=10)

type_combobox = ttk.Combobox(root, values=["Доход", "Расход"])
type_combobox.pack()

amount_label = tkinter.Label(root, text="Сумма:")
amount_label.pack(pady=10)

amount_entry = tkinter.Entry(root)
amount_entry.pack()

comment_label = tkinter.Label(root, text="Комментарий:")
comment_label.pack(pady=10)

comment_entry = tkinter.Entry(root)
comment_entry.pack()

add_button = tkinter.Button(root, text="Добавить транзакцию", command=add_transaction)
add_button.pack(pady=10)

view_button = tkinter.Button(root, text="Посмотреть транзакции", command=view_data)
view_button.pack()

root.mainloop()

connection.close()
