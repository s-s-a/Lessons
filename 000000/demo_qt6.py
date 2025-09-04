import sys
<<<<<<< HEAD
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
from PySide6 import QtQuickWidgets, QtCore, QtWidgets #, QtLineEdit, QtPushButton, QtTextEdit, QtVBoxlayout
=======
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from PySide6 import QtWidgets
>>>>>>> 5c39f649394f144af54e86d1663d6d480dab1841


class MyApp(QtWidgets.QWidget):
  def __init__(self, parent=None):
    QtWidgets.QWidget.__init__(self, parent)
    self.setWindowTitle('hello app')
    self.setWindowIcon(QIcon('apply.ico'))
    self.resize(300, 200)  # width, height

    layout = QtWidgets.QVBoxLayout()
    self.setLayout(layout)

    # widgets
    self.inputField = QtWidgets.QLineEdit()
    button = QtWidgets.QPushButton('&Say Hello, ', clicked = self.sayHello)
    self.output = QtWidgets.QTextEdit()

    layout.addWidget(self.inputField)
    layout.addWidget(button)
    layout.addWidget(self.output)

  def sayHello(self):
    inputText = self.inputField.text()
    self.output.setText('Hello {0}'.format(inputText))


app = QApplication(sys.argv)
app.setStyleSheet('''
    Qwidget {
      font-size^ 25px;
    }

    QPushButton {
      font-size: 20px;
    }
''')

window = MyApp()
window.show()

app.exec()