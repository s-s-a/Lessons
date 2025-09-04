# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QWidget, QPushButton
from PySide6.QtGui import QIcon
<<<<<<< HEAD
from PySide6 import QtCore, QtGui
import sys

=======
from PyQt5 import QtCore, QtGui
import sys
>>>>>>> 5c39f649394f144af54e86d1663d6d480dab1841
app = QApplication(sys.argv)
window = QWidget(flags=QtCore.Qt.Dialog)
window.setWindowTitle("Bcплывaюшиe подсказки")
window.resize(300, 70)
button = QPushButton("&Закрыть окно", window)
button.setFixedSize(150, 30)
button.move(75, 20)
button.setToolTip("Это всплывающая подсказка для <b>кнопки</b>")
window.setToolTip("Этo всплывающая подсказка для <b>окна</b>")
button.setWhatsThis("Этo справка для <b>кнопки</b>")
window.setWhatsThis("Этo справка для <b>окна</b>")
button.clicked.connect(app.instance().quit)
window.show()
<<<<<<< HEAD
sys.exit(app.exec_())
=======
sys.exit(app.exec_())
>>>>>>> 5c39f649394f144af54e86d1663d6d480dab1841
