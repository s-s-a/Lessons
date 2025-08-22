from PySide6 import QtCore, QtWidgets, QtWebEngineWidgets
import sys


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.Window)
        self.setWindowTitle("Класс QWebEngineView")
        vbox = QtWidgets.QVBoxLayout()
        hbox = QtWidgets.QHBoxLayout()
        self.btnBack = QtWidgets.QPushButton("&Назад")
        hbox.addWidget(self.btnBack)
        self.btnForward = QtWidgets.QPushButton("&Вперёд")
        hbox.addWidget(self.btnForward)
        self.btnStop = QtWidgets.QPushButton("&Стоп")
        hbox.addWidget(self.btnStop)
        self.btnReload = QtWidgets.QPushButton("&Обновить")
        hbox.addWidget(self.btnReload)
        self.txtUrl = QtWidgets.QLineEdit()
        hbox.addWidget(self.txtUrl)
        self.btnGo = QtWidgets.QPushButton("&Перейти")
        self.btnGo.setAutoDefault(True)
        self.btnGo.setDefault(True)
        hbox.addWidget(self.btnGo)
        vbox.addLayout(hbox)
        self.wvwMain = QtWebEngineWidgets.QWebEngineView()
        self.wvwMain.urlChanged.connect(self.setUrl)
        self.wvwMain.titleChanged.connect(self.setTitle)
        self.wvwMain.loadProgress.connect(self.showProgress)
        self.wvwMain.loadFinished.connect(self.showStatus)
        self.btnBack.clicked.connect(self.wvwMain.back)
        self.btnForward.clicked.connect(self.wvwMain.forward)
        self.btnStop.clicked.connect(self.wvwMain.stop)
        self.btnReload.clicked.connect(self.wvwMain.reload)
        self.btnGo.clicked.connect(self.loadPage)
        vbox.addWidget(self.wvwMain)
        self.stbMain = QtWidgets.QStatusBar()
        self.stbMain.setSizeGripEnabled(False)
        self.lblStatus = QtWidgets.QLabel("Готов")
        self.stbMain.addWidget(self.lblStatus)
        vbox.addWidget(self.stbMain)
        self.setLayout(vbox)
        self.resize(600, 400)

    def loadPage(self):
        self.wvwMain.load(QtCore.QUrl(self.txtUrl.text()))

    def setUrl(self, url):
        self.txtUrl.setText(url.url())

    def setTitle(self, text):
        self.setWindowTitle(text)

    def showProgress(self, percent):
        self.lblStatus.setText("Загружено " + str(percent) + "%")

    def showStatus(self, flag):
        if flag:
            self.lblStatus.setText("Готов")
        else:
            self.lblStatus.setText("Ошибка")


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
