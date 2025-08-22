# stdDialogDemo_pyside.py

from PySide import QtCore, QtGui

########################################################################
class DialogDemo(QtGui.QWidget):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        # super(DialogDemo, self).__init__()
        QtGui.QWidget.__init__(self)
        
        self.label = QtGui.QLabel("Python rules!")
        
        # create the buttons
        colorDialogBtn = QtGui.QPushButton("Open Color Dialog")
        fileDialogBtn =  QtGui.QPushButton("Open File Dialog")
        self.fontDialogBtn = QtGui.QPushButton("Open Font Dialog")
        inputDlgBtn = QtGui.QPushButton("Open Input Dialog")
        
        # connect the buttons to the functions (signals to slots)
        colorDialogBtn.clicked.connect(self.openColorDialog)
        fileDialogBtn.clicked.connect(self.openFileDialog)
        self.fontDialogBtn.clicked.connect(self.openFontDialog)
        self.connect(inputDlgBtn, QtCore.SIGNAL("clicked()"), self.openInputDialog)
        
        # layout widgets
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(colorDialogBtn)
        layout.addWidget(fileDialogBtn)
        layout.addWidget(self.fontDialogBtn)
        layout.addWidget(inputDlgBtn)
        self.setLayout(layout)
        
        # set the position and size of the window
        self.setGeometry(100, 100, 400, 100)
        
        self.setWindowTitle("Dialog Demo")
        
    #----------------------------------------------------------------------
    def openColorDialog(self):
        """
        Opens the color dialog
        """
        color = QtGui.QColorDialog.getColor()
        
        if color.isValid():
            print color.name()
            btn = self.sender()
            pal = btn.palette()
            pal.setColor(QtGui.QPalette.Button, color)
            btn.setPalette(pal)
            btn.setAutoFillBackground(True)
            
            #btn.setStyleSheet("QPushButton {background-color: %s}" % color)
            
    #----------------------------------------------------------------------
    def openFileDialog(self):
        """
        Opens a file dialog and sets the label to the chosen path
        """
        import os
        path, _ = QtGui.QFileDialog.getOpenFileName(self, "Open File", os.getcwd())
        self.label.setText(path)
        
        
    #----------------------------------------------------------------------
    def openDirectoryDialog(self):
        """
        Opens a dialog to allow user to choose a directory
        """
        flags = QtGui.QFileDialog.DontResolveSymlinks | QtGui.QFileDialog.ShowDirsOnly
        d = directory = QtGui.QFileDialog.getExistingDirectory(self,
                                                               "Open Directory",
                                                               os.getcwd(),
                                                               flags)
        self.label.setText(d)
        
    #----------------------------------------------------------------------
    def openFontDialog(self):
        """
        Open the QFontDialog and set the label's font
        """
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.label.setFont(font)
        
    #----------------------------------------------------------------------
    def openInputDialog(self):
        """
        Opens the text version of the input dialog
        """
        text, result = QtGui.QInputDialog.getText(self, "I'm a text Input Dialog!",
                                            "What is your favorite programming language?")
        if result:
            print "You love %s!" % text
            
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = QtGui.QApplication([])
    form = DialogDemo()
    form.show()
    app.exec_()