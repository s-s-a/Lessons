# printDlgDemo.py

from PySide import QtGui, QtCore

########################################################################
class PrinterWindow(QtGui.QWidget):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        QtGui.QWidget.__init__(self)
        self.setWindowTitle("Printing Demo")
        self.text_editor = QtGui.QTextEdit(self)
        
        printButton = QtGui.QPushButton('Print')
        printButton.clicked.connect(self.onPrint)
        printPreviewButton = QtGui.QPushButton('Print Preview')
        printPreviewButton.clicked.connect(self.onPrintPreview)
        
        btnLayout = QtGui.QHBoxLayout()
        mainLayout = QtGui.QVBoxLayout()
    
        btnLayout.addWidget(printButton)
        btnLayout.addWidget(printPreviewButton)
        mainLayout.addWidget(self.text_editor)
        mainLayout.addLayout(btnLayout)
        
        self.setLayout(mainLayout)
        
    #----------------------------------------------------------------------
    def onPrint(self):
        """
        Create and show the print dialog
        """
        dialog = QtGui.QPrintDialog()
        if dialog.exec_() == QtGui.QDialog.Accepted:
            doc = self.text_editor.document()
            doc.print_(dialog.printer())
            
    #----------------------------------------------------------------------
    def onPrintPreview(self):
        """
        Create and show a print preview window
        """
        dialog = QtGui.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.text_editor.print_)
        dialog.exec_()
    
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = QtGui.QApplication([])
    form = PrinterWindow()
    form.show()
    app.exec_()