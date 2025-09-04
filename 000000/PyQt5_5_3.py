#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)
        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
<<<<<<< HEAD
    sys.exit(app.exec())
=======
    sys.exit(app.exec_())
>>>>>>> 5c39f649394f144af54e86d1663d6d480dab1841
