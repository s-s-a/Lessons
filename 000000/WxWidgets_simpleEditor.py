# a minimal text editor to demo wxPython

# GNU All-Permissive License
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved.  This file is offered as-is,
# without any warranty.

import wx
import os


class TextEdit(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, wx.ID_ANY, title, size=(520, 340))
        menuBar = wx.MenuBar()
        menuFile = wx.Menu()
        menuBar.Append(menuFile, "&File")
        menuFile.Append(1, "&Open")
        menuFile.Append(2, "&Save")
        menuFile.Append(3, "&Quit")
        self.SetMenuBar(menuBar)
        wx.EVT_MENU(self, 1, self.openAction)
        wx.EVT_MENU(self, 2, self.saveAction)
        wx.EVT_MENU(self, 3, self.quitAction)
        self.p1 = wx.Panel(self)
        self.initUI()

    def initUI(self):
        self.text = wx.TextCtrl(self.p1, style=wx.TE_MULTILINE)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.p1, 1, wx.EXPAND | wx.ALIGN_CENTER)
        self.SetSizer(vbox)
        self.Bind(wx.EVT_SIZE, self._onSize)
        self.Show()

    def _onSize(self, e):
        e.Skip()
        self.text.SetSize(self.GetClientSizeTuple())

    def quitAction(self, e):
        if self.text.IsModified():
            dlg = wx.MessageDialog(
                self, "Quit? All changes will be lost.", "", wx.YES_NO)
            if dlg.ShowModal() == wx.ID_YES:
                self.Close(True)
            else:
                self.saveAction(self)
        else:
            exit()

    def openAction(self, e):
        dlg = wx.FileDialog(self, "File chooser",
                            os.path.expanduser('~'), "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetFilename()
            dir = dlg.GetDirectory()
            f = open(os.path.join(dir, filename), 'r')
            self.text.SetValue(f.read())
            f.close()
        dlg.Destroy()

    def saveAction(self, e):
        dlg = wx.FileDialog(self, "Save as", os.path.expanduser(
            '~'), "", "*.*", wx.SAVE | wx.OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            filedata = self.text.GetValue()
            filename = dlg.GetFilename()
            dir = dlg.GetDirectory()
            f = open(os.path.join(dir, filename), 'w')
            f.write(filedata)
            f.close()
        dlg.Destroy()


def main():
    app = wx.App(False)
    view = TextEdit(None, "TextEdit")
    app.MainLoop()


if __name__ == '__main__':
    main()
