from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QTime, QTimer
from PySide6.QtGui import QFont

class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        # Изменение шрифта
        self.label.setFont(QFont("Arial", 20))
        # Создание переменной timer в которую помещается вызов функции таймер (QTimer)
        self.timer = QTimer()
        # Привязка метода перезагрузки к функции self.tm
        self.timer.timeout.connect(self.tm)
        # Старт функции QTimer() с интервалом 1000 мс
        self.timer.start(1000)
        # Сразу показывается текущее время в метке label, без этого метода бует показываться textLabel
        self.label.setText(QTime.currentTime().toString("hh:mm:ss"))

    def tm(self):
        # Показ текущего времени в метке label, функция будет перезагружаться каждые 1000 мс
        self.label.setText(QTime.currentTime().toString("hh:mm:ss"))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(320, 110)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Часы"))
        self.label.setText(_translate("MainWindow", "TextLabel"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec())
