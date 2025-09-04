<<<<<<< HEAD
import sys
from PySide6.QtWidgets import QWidget, QMessageBox, QApplication
import PySide6.QtWidgets as QtGui
from MessageBoxConstants import *
=======
import PySide6.QtWidgets as QtGui
from PySide6.QtWidgets import QMessageBox
import PySide6.QtCore as QtCore
from MessageBoxConstants import OK, CANCEL, ABORT, RETRY, IGNORE, YES, NO, RETURN_OK, RETURN_CANCEL, RETURN_ABORT, RETURN_RETRY, RETURN_IGNORE, RETURN_YES, RETURN_NO
>>>>>>> 5c39f649394f144af54e86d1663d6d480dab1841

def messagebox(msg, arg1=None, arg2=None, timeout=None, details=''):

    def center_widget(widget):
        '''center the widget on the screen'''
        widget_pos = widget.frameGeometry()
<<<<<<< HEAD
        screen_center = QtGui.QDesktopWidget().screenGeometry().center()
=======
        screen_center = QtGui.QDesktopWidget.screenGeometry().center()
>>>>>>> 5c39f649394f144af54e86d1663d6d480dab1841
        widget_pos.moveCenter(screen_center)
        widget.move(widget_pos.topLeft())

    flags = 0
    title = 'vfp2py'
    if arg1 is not None:
        if isinstance(arg1, str):
            title = arg1
            if arg2 is not None:
                flags = arg2
        else:
            flags = arg1
            if arg2 is not None:
                title = arg2
    flags = int(flags) & 1023

    buttons = {
        OK_ONLY: ((OK,), OK),
        OK_CANCEL: ((OK, CANCEL), CANCEL),
        ABORT_RETRY_IGNORE: ((ABORT, RETRY, IGNORE), IGNORE),
        YES_NO_CANCEL: ((YES, NO, CANCEL), CANCEL),
        YES_NO: ((YES, NO), NO),
        RETRY_CANCEL: ((RETRY, CANCEL), CANCEL)
    }[flags & 15]

    buttonobj = buttons[0][0]
    for button in buttons[0][1:]:
        buttonobj |= button

    icon = {
<<<<<<< HEAD
        NOICON: QtGui.QMessageBox.NoIcon,
        STOPSIGN: QtGui.QMessageBox.Critical,
        QUESTION: QtGui.QMessageBox.Question,
        EXCLAMATION: QtGui.QMessageBox.Warning,
        INFORMATION: QtGui.QMessageBox.Information
=======
        NOICON: QMessageBox.NoIcon,
        STOPSIGN: QMessageBox.Critical,
        QUESTION: QMessageBox.Question,
        EXCLAMATION: QMessageBox.Warning,
        INFORMATION: QMessageBox.Information
>>>>>>> 5c39f649394f144af54e86d1663d6d480dab1841
    }[flags & (15 << 4)]

    default_button = min(len(buttons[0])-1, (flags >> 8))

    msg_box = QtGui.QMessageBox(icon, title, msg, buttons=buttonobj)
    msg_box.setDefaultButton(buttons[0][default_button])
    msg_box.setEscapeButton(buttons[1])
    if details:
        msg_box.setDetailedText(details)

    msg_box.show()

    retval = [0]

    def closebox():
        t = retval
        t[0] = -1
        msg_box.close()

    if timeout:
        timer = QtCore.QTimer()
        timer.setSingleShot(True)
        timer.timeout.connect(closebox)
<<<<<<< HEAD
        timer.start(float(timeout)*1000)
        timeout = timer
    button = msg_box.exec_()
=======
        timer.start(int(float(timeout)*1000))
        timeout = timer
    button = msg_box.exec()
>>>>>>> 5c39f649394f144af54e86d1663d6d480dab1841
    if timeout and timeout.isActive():
        timeout.stop()
    retval = retval[0]
    center_widget(msg_box)
    return {
        OK: RETURN_OK,
        CANCEL: RETURN_CANCEL,
        ABORT: RETURN_ABORT,
        RETRY: RETURN_RETRY,
        IGNORE: RETURN_IGNORE,
        YES: RETURN_YES,
        NO: RETURN_NO
    }[button] if retval != -1 else -1


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     messagebox('Are yiu sure?', 4+256)
#     sys.exit(app.exec_())
