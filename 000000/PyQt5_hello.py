#!c:\Users\Sizov\AppData\Local\Programs\Python\Python37\python
# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Hello!')
    w.show()

    sys.exit(app.exec())