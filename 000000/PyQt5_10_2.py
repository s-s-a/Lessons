#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, random
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):
        qp.setPen(Qt.red)
        size = self.size()

        for i in range(1000):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            qp.drawPoint(x, y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
<<<<<<< HEAD
    sys.exit(app.exec())
=======
    sys.exit(app.exec_())
>>>>>>> 5c39f649394f144af54e86d1663d6d480dab1841
