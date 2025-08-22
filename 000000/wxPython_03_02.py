import wx
import apply_ico


class MyForm(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='Python Image Title')
        self.panel = wx.Panel(self, wx.ID_ANY)

#        ico = apply_ico.python.GetIcon()
        ico = apply_ico.apply
        self.SetIcon(ico)


# Запустите программу
if __name__ == '__main__':
    app = wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()