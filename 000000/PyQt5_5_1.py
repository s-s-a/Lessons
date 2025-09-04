#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication)

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)
        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)
        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
<<<<<<< HEAD
    sys.exit(app.exec())
=======
    sys.exit(app.exec_())
>>>>>>> 5c39f649394f144af54e86d1663d6d480dab1841
