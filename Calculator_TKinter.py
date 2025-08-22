'''Калькулятор на TKinter'''

from tkinter import END, Frame, NSEW, Tk, Button, Entry,BOTH

expression = ''


def btn_click(item):
    global expression
    try:
        input_field['state'] = 'normal'
        expression += item
        input_field.insert(END, item)

        if item == '=':
            result = str(eval(expression[:-1]))
            input_field.insert(END, result)
            expression = ''
        input_field['state'] = 'readonly'

    except ZeroDivisionError:
        input_field.delete(0, END)
        input_field.insert(0, 'Ошибка (деление на 0)')
    except SyntaxError:
        input_field.delete(0, END)
        input_field.insert(0, 'Ошибка')


def btn_clear():
    global expression
    expression = ''
    input_field['state'] = 'normal'
    input_field.delete(0, END)
    input_field['state'] = 'readonly'


root = Tk()
root.geometry('268x316')
root.title("Калькулятор")

frame_input = Frame(root)
frame_input.grid(row=0, column=0, columnspan=4, sticky=NSEW)

input_field = Entry(frame_input, font='Arial 15 bold', width=24, state='readonly')
input_field.pack(fill=BOTH)

buttons = (('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4'),
           )

expression = ''

button = Button(root, text='C', font='Arial 20 bold', command=lambda: btn_clear())
button.grid(row=1, column=3, sticky=NSEW)
for row in range(4):
    for col in range(4):
        Button(root, width=2, height=1, text=buttons[row][col], font='Arial 20 bold',
               command=lambda row=row, col=col: btn_click(buttons[row][col])).grid \
            (row=row + 2, column=col, sticky=NSEW, padx=1, pady=1)

root.mainloop()