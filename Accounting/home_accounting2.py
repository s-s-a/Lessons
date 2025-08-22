from tkcalendar import DateEntry
import sqlite3
from tkinter import END, W, E, Toplevel, NO, Tk, Label, Entry, Button, Frame, SUNKEN, LEFT, TOP, BOTH, Scrollbar, \
    VERTICAL, RIGHT, Y, N, YES
from tkinter import messagebox
from tkinter import ttk

connection = sqlite3.connect('finance.db')
cur = connection.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE NOT NULL,
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
            date = date_entry.get_date()

            cur.execute("""
                INSERT INTO transactions (type, amount, comment)
                VALUES (?, ?, ?)
                """, (transaction_type, amount, comment))

            transaction_id = cur.lastrowid
            treeview.insert("", END, values=(transaction_id, date, transaction_type, amount, comment))

            connection.commit()

            type_combobox.set('')
            amount_entry.delete(0, END)
            comment_entry.delete(0, END)
            messagebox.showinfo("Успех", "Transaction added!")
        except ValueError:
            messagebox.showerror('Ошибка', 'Сумма введена некорректно!')
    else:
        messagebox.showinfo('Предупреждение', 'Заполнены не все поля!')


def delete_transaction():
    selected_item = treeview.selection()
    if selected_item:
        item_values = treeview.item(selected_item, "values")
        transaction_id = item_values[0]
        cur.execute("DELETE FROM transactions WHERE id =?", (transaction_id,))
        connection.commit()
        treeview.delete(selected_item)
        messagebox.showinfo("Успех", "Транзакция успешно удалена!")
    else:
        messagebox.showinfo('Предупреждение', 'Выберите транзакцию для удаления!')


def delete_all_transactions():
    confirm = messagebox.askyesno("Предупреждение", "Вы уверены, что хотите удалить все транзакции?") == YES
    if confirm:
        cur.execute("DELETE FROM transactions")
        connection.commit()
        treeview.delete(*treeview.get_children())
        messagebox.showinfo("Успех", "Все транзакции успешно удалены!")


def edit_transaction():
    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showinfo('Транзакция не выбрана!',
                            'Выберите транзакцию для редактирования!')
        return

    transaction_id = treeview.set(selected_item, "#1")
    date = date_entry.get_date()
    transaction_type = type_combobox.get()
    amount = float(amount_entry.get())
    comment = comment_entry.get()
    cur.execute("UPDATE transactions SET date =?, type =?, amount =?, comment =? WHERE id =?",
                (date, transaction_type, amount, comment, transaction_id))
    connection.commit()

    treeview.item(selected_item, values=(transaction_id, date, transaction_type, amount, comment))


def on_row_click(event):
    item = treeview.selection()
    values = treeview.item(item, 'values')

    date_entry.delete(0, END)
    date_entry.insert(0, values[1])
    type_combobox.set(values[2])
    amount_entry.delete(0, END)
    amount_entry.insert(0, values[3])
    comment_entry.delete(0, END)
    comment_entry.insert(0, values[4])


root = Tk()
root.title("Домашняя Бухгалтерия")
root.geometry('700x350')
root.resizable(False, False)  # не разрешаем растягивать окно

left_frame = Frame(root, bd=2, relief=SUNKEN)
left_frame.pack(side=LEFT, anchor=N, pady=10)

date_label = Label(left_frame, text="Дата:")
date_label.pack(pady=10, padx=10, anchor=W)

date_entry = DateEntry(left_frame, width=20, foreground="white", borderwidth=2, date_pattern="dd.mm.y", locale="ru")
date_entry.pack(pady=10, padx=10, anchor=W)

type_label = Label(left_frame, text="Тип:")
type_label.pack(pady=10, anchor=W)
type_combobox = ttk.Combobox(left_frame, values=["Доход", "Расход"], state="readonly")
type_combobox.pack(pady=10, anchor=W)

amount_label = Label(left_frame, text="Сумма:")
amount_label.pack(pady=10, padx=10, anchor=W)
amount_entry = Entry(left_frame)
amount_entry.pack(pady=10, padx=10, anchor=W)

comment_label = Label(left_frame, text="Комментарий:")
comment_label.pack(pady=10, padx=10, anchor=W)
comment_entry = Entry(left_frame)
comment_entry.pack(pady=10, padx=10, anchor=W)

add_button = Button(left_frame, text="Добавить транзакцию", command=add_transaction)
add_button.pack(pady=10, padx=10, anchor=W)

button_frame = Frame(root, bd=2, relief=SUNKEN)
button_frame.pack(side=TOP, pady=10, padx=10, fill=BOTH)

delete_button = Button(button_frame, text="Удалить транзакцию", command=delete_transaction)
delete_button.pack(pady=10, padx=10, side=LEFT)

delete_all_button = Button(button_frame, text="Удалить все транзакции", command=delete_all_transactions)
delete_all_button.pack(pady=10, padx=10, side=LEFT)

edit_button = Button(button_frame, text="Редактировать транзакцию", command=edit_transaction)
edit_button.pack(pady=10, padx=10, side=LEFT)

right_frame = Frame(root, bd=2, relief=SUNKEN)
right_frame.pack(side=LEFT, pady=10)

data_frame = Frame(root, bd=2, relief=SUNKEN)
data_frame.pack(side=LEFT, fill=BOTH, expand=True)

treeview = ttk.Treeview(data_frame)
treeview.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(data_frame, orient=VERTICAL, command=treeview.yview)
scrollbar.pack(side=RIGHT, fill=Y)
treeview.configure(yscrollcommand=scrollbar.set)

treeview['columns'] = ('id', 'date', 'type', 'amount', 'comment')
treeview.column('#0', width=0, stretch=NO)
treeview.column('id', anchor=W, width=100)
treeview.column('date', anchor=W, width=100)
treeview.column('type', anchor=W, width=100)
treeview.column('amount', anchor=E, width=100)
treeview.column('comment', anchor=W, width=200)

treeview.heading('#0', text='')
treeview.heading('id', text='ID')
treeview.heading('date', text='Дата')
treeview.heading('type', text='Тип')
treeview.heading('amount', text='Сумма')
treeview.heading('comment', text='Комментарий')

cur.execute("SELECT * FROM transactions")
rows = cur.fetchall()

for row in rows:
    treeview.insert('', END, values=row)

treeview.bind('<ButtonRelease-1>', on_row_click) # выбор транзакции


root.mainloop()

connection.close()
