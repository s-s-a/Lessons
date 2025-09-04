#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import (QWidget, QPushButton, QFrame, QColorDialog, QApplication)
from PySide6.QtGui import QColor

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0)
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog')
        self.show()


    def showDialog(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
<<<<<<< HEAD
    sys.exit(app.exec())
=======
    sys.exit(app.exec_())
>>>>>>> 5c39f649394f144af54e86d1663d6d480dab1841
