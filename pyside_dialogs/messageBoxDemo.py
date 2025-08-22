
from PySide import QtCore, QtGui

########################################################################
class MessageBoxDemo(QtGui.QWidget):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        # super(DialogDemo, self).__init__()
        QtGui.QWidget.__init__(self)
        self.setWindowTitle("MessageBox Demo")
        
        # create buttons
        criticalMsgBtn = QtGui.QPushButton("Show Critical Message")
        criticalMsgBtn.clicked.connect(self.onShowCriticalMessage)
                
        infoMsgBtn = QtGui.QPushButton("Show Informational Message")
        infoMsgBtn.clicked.connect(self.onShowInformation)
        
        questionMsgBtn = QtGui.QPushButton("Show Question Message")
        questionMsgBtn.clicked.connect(self.onShowQuestion)
        
        warningMsgBtn = QtGui.QPushButton("Show Warning Message")
        warningMsgBtn.clicked.connect(self.onShowWarning)
        
        # layout widgets
        layout = QtGui.QVBoxLayout()
        layout.addWidget(criticalMsgBtn)
        layout.addWidget(infoMsgBtn)
        layout.addWidget(questionMsgBtn)
        layout.addWidget(warningMsgBtn)
        self.setLayout(layout)
        
        self.setGeometry(100,100,300,100)
        
    #----------------------------------------------------------------------
    def onShowCriticalMessage(self):
        """
        Show the critical message
        """
        flags = QtGui.QMessageBox.Abort
        flags |= QtGui.QMessageBox.StandardButton.Retry
        flags |= QtGui.QMessageBox.StandardButton.Ignore
            
        result = QtGui.QMessageBox.critical(self, "CRITICAL ERROR",
                                            "You're trying Perl aren't you?",
                                            flags)
        if result == QtGui.QMessageBox.Abort:
            print "Aborted!"
        elif result == QtGui.QMessageBox.Retry:
            print "Retrying!"
        elif result == QtGui.QMessageBox.Ignore:
            print "Ignoring!"
               
    #----------------------------------------------------------------------
    def onShowInformation(self):
        """
        Show the information message
        """
        QtGui.QMessageBox.information(self, "Information", "Python rocks!")
        
    #----------------------------------------------------------------------
    def onShowQuestion(self):
        """
        Show the question message
        """
        flags = QtGui.QMessageBox.StandardButton.Yes 
        flags |= QtGui.QMessageBox.StandardButton.No
        question = "Do you really want to work right now?"
        response = QtGui.QMessageBox.question(self, "Question",
                                              question,
                                              flags)
        if response == QtGui.QMessageBox.Yes:
            print "You're very dedicated!"
        elif QtGui.QMessageBox.No:
            print "You're fired!"
        else:
            print "You chose wisely!"
            
    #----------------------------------------------------------------------
    def onShowWarning(self):
        """
        Show a warning message
        """
        flags = QtGui.QMessageBox.StandardButton.Ok
        flags |= QtGui.QMessageBox.StandardButton.Discard
        msg = "This message will self-destruct in 30 seconds!"
        response = QtGui.QMessageBox.warning(self, "Warning!",
                                             msg, flags)
        if response == 0:
            print "BOOM!"
        else:
            print "MessageBox disarmed!"
        
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = QtGui.QApplication([])
    form = MessageBoxDemo()
    form.show()
    app.exec_()