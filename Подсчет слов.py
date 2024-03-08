from PySide2 import QtCore, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.btnCount.clicked.connect(self.symbol_count)
        self.btnCount.clicked.connect(self.word_count)
        self.btnCount.clicked.connect(self.number_count)

    def symbol_count(self):
        text = self.textEdit.toPlainText()
        res = []
        for i in text:
            if i.isalpha():
                res.append(i)
        count = str(len(res))
        self.labelSymbol.setText(f"Букв в тексте: {count}")

    def word_count(self):
        text = self.textEdit.toPlainText()
        clean = ''.join(x for x in text if x.isalpha() or x == " ")
        clean = clean.split(" ")
        res = list(filter(None, clean))
        count = str(len(res))
        self.labelWord.setText(str(f"Слов в тексте: {count}"))

    def number_count(self):
        number = self.textEdit.toPlainText()
        res = []
        for i in number:
            if i.isdigit():
                res.append(i)
        count = str(len(res))
        self.labelNumber.setText(f"Цифр в тексте: {count}")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(635, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelSymbol = QtWidgets.QLabel(self.frame)
        self.labelSymbol.setObjectName("labelSymbol")
        self.verticalLayout.addWidget(self.labelSymbol)
        self.labelWord = QtWidgets.QLabel(self.frame)
        self.labelWord.setStyleSheet("")
        self.labelWord.setObjectName("labelWord")
        self.verticalLayout.addWidget(self.labelWord)
        self.labelNumber = QtWidgets.QLabel(self.frame)
        self.labelNumber.setObjectName("labelNumber")
        self.verticalLayout.addWidget(self.labelNumber)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setEnabled(True)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnCount = QtWidgets.QPushButton(self.frame_2)
        self.btnCount.setObjectName("btnCount")
        self.verticalLayout_2.addWidget(self.btnCount)
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout_3.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Подсчет слов"))
        self.labelSymbol.setText(_translate("MainWindow", "Букв в тексте:"))
        self.labelWord.setText(_translate("MainWindow", "Слов в тексте:"))
        self.labelNumber.setText(_translate("MainWindow", "Цифр в тексте:"))
        self.btnCount.setText(_translate("MainWindow", "Подсчет"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
