# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QWidget, QPushButton, QApplication
from PySide6 import QtCore
# from PyQt5.QtCore import QTranslator, QLocale
from MessageBox import messagebox
from MessageBoxConstants import YES_NO, SECONDBUTTON, RETURN_YES


def left(__s, __amount):
    return __s[:__amount]


def right(_s, amount):
    return _s[-amount:]


def substring(_s, offset, amount):
    return _s[offset:offset+amount]


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()

    def closeEvent(self, event):
        if messagebox(
                "Are you sure to quit?", YES_NO+SECONDBUTTON) == RETURN_YES:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # попытка включить автоперевод текста стандартных кнопок
    translator = QtCore.QTranslator(app)
    locale = QtCore.QLocale.system().name()
    path = QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath)
    if translator.load('qtbase_%s' % left(locale, 2), path):
        # print('Translator loaded')
        app.installTranslator(translator)

    ex = Example()
    sys.exit(app.exec())
