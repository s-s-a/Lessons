"""Текстовый редактор на Qt"""

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QFileDialog, QMessageBox

class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.btnOpen.clicked.connect(self.open_file)
        self.btnSaveAs.clicked.connect(self.save_file_as)

    def open_file(self):
        """
        Диалоговое окно открытия файла:
        1. После self, выберите файл - заголовок окна открытия файла.
        2. Устанавливает по умолчанию имя файла которое требуется открыть
        3. Устанавливает только выбранные расширения при открытии файлов
        4. [0] - Инедкс считывания, говорит о том, с какого символа нужно начать считывание файла
        """
        file_path = QFileDialog.getOpenFileName(self, 'Выберите файл', '', 'Только текстовые файлы (*.txt)')[0]
        # Если файл не выбран то программа не закроется с ошибкой
        if not file_path:
            return
        # Открытие файла с ключом 'r' для чтения, as f открывает его в переменной f, encoding='utf-8' - выбор кодировки.
        with open(file_path, "r", encoding='utf-8') as f:
            # Читает файл в переменную text
            text = f.read()
            # заполняет textEdit из переменной text
            self.textEdit.setText(text)

    def save_file_as(self):
        """
        Диалоговое окно сохранения файла:
        1. После self, Куда сохранить - заголовок окна сохранения файла.
        2. Устанавливает по умолчанию имя файла для сохранения.
        3. Устанавливает только выбранные расширения при сохранении файлов
        4. [0] - Инедкс считывания, говорит о том с какого символа нужно начать считывание файла
        """
        file_path = QFileDialog.getSaveFileName(self, 'Куда сохранить', '', 'Только (*.txt)')[0]
        # Если файл не выбран то программа не закроется с ошибкой
        if not file_path:
            return
        # Открытие файла с ключом 'w' для записи, as f открывает его в переменной f, encoding='utf-8' - выбор кодировки.
        with open(file_path, "w", encoding='utf-8') as f:
            # Считывает текст из textEdit в переменную text
            text = self.textEdit.toPlainText()
            # Записывает файл из переменной text
            f.write(text)
            """
            Системное сообещние:
            information - иконка с восклицательным знаком, при желании можно заменить.
            "Сообщение" - это название окна.
            "Файл сохранен" - это текст сообщения.
            """
            QMessageBox.information(self, "Сообщение", "Файл сохранен")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(646, 454)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnOpen = QtWidgets.QPushButton(self.frame)
        self.btnOpen.setObjectName("btnOpen")
        self.horizontalLayout.addWidget(self.btnOpen)
        self.btnSaveAs = QtWidgets.QPushButton(self.frame)
        self.btnSaveAs.setObjectName("btnSaveAs")
        self.horizontalLayout.addWidget(self.btnSaveAs)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Текстовый редактор"))
        self.btnOpen.setText(_translate("MainWindow", "Открыть"))
        self.btnSaveAs.setText(_translate("MainWindow", "Сохранить как..."))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
