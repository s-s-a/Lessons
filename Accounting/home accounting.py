import sqlite3
from tkinter import END, W, E, Toplevel, NO, Tk, Label, Entry, Button
from tkinter import messagebox
from tkinter import ttk

connection = sqlite3.connect('finance.db')
cur = connection.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        amount REAL,
        comment TEXT
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
                INSERT INTO transactions (type, amount, comment)
                VALUES (?, ?, ?)
                """, (transaction_type, amount, comment))
            connection.commit()

            type_combobox.set('')
            amount_entry.delete(0, END)
            comment_entry.delete(0, END)
            messagebox.showinfo("Успех", "Транзакция успешно добавлена!")
        except ValueError:
            messagebox.showerror('Ошибка', 'Сумма введена некорректно!')
    else:
        messagebox.showinfo('Предупреждение', 'Заполнены не все поля!')


def view_data():
    view_window = Toplevel(root)
    view_window.title("Просмотр транзакций")

    treeview = ttk.Treeview(view_window)
    treeview.pack()

    treeview["columns"] = ("type", "amount", "comment")
    treeview.column("#0", width=0, stretch=NO)
    treeview.column("type", anchor=W, width=100)
    treeview.column("amount", anchor=E, width=100)
    treeview.column("comment", anchor=W, width=200)

    treeview.heading("#0", text="")
    treeview.heading("type", text="Тип")
    treeview.heading("amount", text="Сумма")
    treeview.heading("comment", text="Комментарий")

    cur.execute("SELECT * FROM transactions")
    rows = cur.fetchall()

    for row in rows:
        treeview.insert("", END, text="", values=row[1:])


root = Tk()
root.title("Домашняя Бухгалтерия")
root.geometry('200x280')

type_label = Label(root, text="Тип:")
type_label.pack(pady=10)
type_combobox = ttk.Combobox(root, values=["Доход", "Расход"])
type_combobox.pack()

amount_label = Label(root, text="Сумма:")
amount_label.pack(pady=10)
amount_entry = Entry(root)
amount_entry.pack()

comment_label = Label(root, text="Комментарий:")
comment_label.pack(pady=10)
comment_entry = Entry(root)
comment_entry.pack()

add_button = Button(root, text="Добавить транзакцию", command=add_transaction)
add_button.pack(pady=10)

view_button = Button(root, text="Просмотреть транзакции", command=view_data)
view_button.pack()

root.mainloop()

connection.close()