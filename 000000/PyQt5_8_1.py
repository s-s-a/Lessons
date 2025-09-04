#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PySide6.QtGui import QPixmap

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("italika_logo_800.jpg")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
<<<<<<< HEAD
    sys.exit(app.exec())
=======
    sys.exit(app.exec_())
>>>>>>> 5c39f649394f144af54e86d1663d6d480dab1841
