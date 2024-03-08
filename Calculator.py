from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from math import sqrt

from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout

'''
Calculator (sample)
'''

CHECK_YOUR_SAMPLE: str = "Check your sample"
RESULT: str = 'Result'

app = QApplication()
main = QWidget()
main.setGeometry(400, 300, 400, 300)
main.setWindowTitle('Calculator')
app.setWindowIcon(QIcon('calc.png'))

line: QLabel = QLabel(RESULT)
delete_last: QPushButton = QPushButton('<=')
delete_left: QPushButton = QPushButton('=>')
delete_all: QPushButton = QPushButton('C')
sqrtes: QPushButton = QPushButton('?')
num_seven: QPushButton = QPushButton('7')
num_eight: QPushButton = QPushButton('8')
num_nine: QPushButton = QPushButton('9')
divide: QPushButton = QPushButton('?')
num_four: QPushButton = QPushButton('4')
num_five: QPushButton = QPushButton('5')
num_six: QPushButton = QPushButton('6')
multiplate: QPushButton = QPushButton('?')
num_one: QPushButton = QPushButton('1')
num_two: QPushButton = QPushButton('2')
num_three: QPushButton = QPushButton('3')
minus: QPushButton = QPushButton('?')
num_zero: QPushButton = QPushButton('0')
points: QPushButton = QPushButton('.')
summa: QPushButton = QPushButton('=')
plus: QPushButton = QPushButton('+')

row: QVBoxLayout = QVBoxLayout()
row1: QVBoxLayout = QHBoxLayout()
row2: QVBoxLayout = QHBoxLayout()
row3: QVBoxLayout = QHBoxLayout()
row4: QVBoxLayout = QHBoxLayout()
row5: QVBoxLayout = QHBoxLayout()
row6: QVBoxLayout = QHBoxLayout()


def check():
    '''
    Check the line is empty
    '''
    if line.text() == RESULT:
        line.setText('')


def click_digit_or_operator(digit:str) -> None:
    """
    :param digit: clicked digit
    """
    check()
    line.setText(line.text() + digit)


def delete():
    line.setText(RESULT)


def delete_right():
    line.setText(RESULT if len(line.text()) == 1 or line.text() == RESULT else line.text()[:-1])


def delete_lef():
    line.setText(RESULT if len(line.text()) == 1 or line.text() == RESULT else line.text()[1::])


def total():
    try:
        line.setText(str(eval(line.text())))
    except:
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText(CHECK_YOUR_SAMPLE)
        msg.exec_()


def koren():
    try:
        line.setText(str(sqrt(float(line.text()))))
    except:
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText(CHECK_YOUR_SAMPLE)
        msg.exec_()


def point():
    line.setText(line.text() + '.')


row1.addWidget(line)
row2.addWidget(sqrtes)
row2.addWidget(delete_all)
row2.addWidget(delete_left)
row2.addWidget(delete_last)
row3.addWidget(num_seven)
row3.addWidget(num_eight)
row3.addWidget(num_nine)
row3.addWidget(divide)
row4.addWidget(num_four)
row4.addWidget(num_five)
row4.addWidget(num_six)
row4.addWidget(multiplate)
row5.addWidget(num_one)
row5.addWidget(num_two)
row5.addWidget(num_three)
row5.addWidget(minus)
row6.addWidget(points)
row6.addWidget(num_zero)
row6.addWidget(summa)
row6.addWidget(plus)

num_one.clicked.connect(click_digit_or_operator('1'))
num_two.clicked.connect(click_digit_or_operator('2'))
num_three.clicked.connect(click_digit_or_operator('3'))
num_four.clicked.connect(click_digit_or_operator('4'))
num_five.clicked.connect(click_digit_or_operator('5'))
num_six.clicked.connect(click_digit_or_operator('6'))
num_seven.clicked.connect(click_digit_or_operator('7'))
num_eight.clicked.connect(click_digit_or_operator('8'))
num_nine.clicked.connect(click_digit_or_operator('9'))
num_zero.clicked.connect(click_digit_or_operator('0'))

multiplate.clicked.connect(clck_multiplate)
divide.clicked.connect(clck_divide)
plus.clicked.connect(clck_plus)
minus.clicked.connect(clck_minus)

summa.clicked.connect(total)
delete_all.clicked.connect(delete)
delete_last.clicked.connect(delete_right)
delete_left.clicked.connect(delete_lef)
sqrtes.clicked.connect(koren)
points.clicked.connect(point)

row.addLayout(row1)
row.addLayout(row2)
row.addLayout(row3)
row.addLayout(row4)
row.addLayout(row5)
row.addLayout(row6)
main.setLayout(row)

main.show()
app.exec()
