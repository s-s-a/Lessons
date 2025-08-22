# -*- coding: utf-8 -*-

import wx
import random


class MyPanel(wx.Panel):

    def __init__(self, parent):
        """Constructor"""
        # создадим панель в которую помести окно вывода и кнопку для генерации событий
        wx.Panel.__init__(self, parent)

        self.logText = wx.TextCtrl(
            self,
            style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL | wx.TE_RICH)

        btn = wx.Button(self, label="Press Me")
        btn.Bind(wx.EVT_BUTTON, self.onPress)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.logText, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(btn, 0, wx.ALL, 5)
        self.SetSizer(sizer)

    def onPress(self, event):
        """
        Ивент который генерит сообщение по нажатию на кнопку
        """
        random_list = ['ERROR: this is error\n',
                       'INFO: start program\n', 'DEBUG: debug info for developer\n']
        self.outputPrint(random.choice(random_list))

    def outputPrint(self, message):
        self.logText.AppendText(message)


class MyFrame(wx.Frame):
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Logging test")
        #panel = MyPanel(self)
        MyPanel(self)
        self.Show()


if __name__ == '__main__':
    app = wx.App(False)
    frm = MyFrame()
    frm.Show()
    app.MainLoop()
