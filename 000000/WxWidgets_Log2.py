# -*- coding: utf-8 -*-

import wx
import random


class MyPanel(wx.Panel):

    def __init__(self, parent):
        """Constructor"""
        # создадим панель в которую помести окно вывода, чебокс инвертировать и кнопку для генерации событий
        wx.Panel.__init__(self, parent)
        # десь мы будем хранить все сообщения
        self.cache_msg = list()

        self.logText = wx.TextCtrl(
            self,
            style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL | wx.TE_RICH)

        btn = wx.Button(self, label="Press Me")
        btn.Bind(wx.EVT_BUTTON, self.onPress)
        # чебокс
        self.check_box_invert = wx.CheckBox(
            self, wx.ID_ANY, 'Invert log', wx.DefaultPosition, wx.DefaultSize, 0)

        sizer = wx.BoxSizer(wx.VERTICAL)
        # горизонтальный сайзер в который мы поместим кнопку и чекбокс, что бы они были рядом
        hor_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.logText, 1, wx.EXPAND | wx.ALL, 5)
        hor_sizer.Add(btn, 0, wx.ALL, 5)
        hor_sizer.Add(self.check_box_invert, 0, wx.ALL, 5)
        sizer.Add(hor_sizer, 0, wx.ALL, 5)
        self.SetSizer(sizer)

    def onPress(self, event):
        """
        Ивент который генерит сообщение по нажатию на кнопку
        """
        random_list = ['ERROR: this is error\n',
                       'INFO: start program\n', 'DEBUG: debug info for developer\n']
        self.outputPrint(random.choice(random_list))

    def outputPrint(self, message):
        # сохраним наше сообщение в списке
        self.cache_msg.append(message)
        # очистим окно от старых сообщений
        self.logText.Clear()
        # в зависимости от состояния флажка обном сообщения в окне
        # если флажок устновлен, то инвертируме лог (последнее сообщение будет вверху)
        if self.check_box_invert.IsChecked():
            for msg in reversed(self.cache_msg):
                # определим цвет сообщения
                color = self.outputColored(str(msg))
                # добавим его в окно
                self.logText.AppendText(msg)
                # окрасим вывод
                self.logText.SetForegroundColour(color)
            # перемещаем курсор в верхнее положение, иначе пользователь будет видеть нижнее сообщение
            # используем только если инвертировать лог включено
            self.logText.SetInsertionPoint(0)
        else:
            for msg in self.cache_msg:
                color = self.outputColored(str(msg))
                self.logText.AppendText(msg)
                self.logText.SetForegroundColour(color)

    @staticmethod
    # метод определяет цвет вывода
    def outputColored(message):
            return wx.RED if message.split()[0] == 'ERROR:' else wx.BLACK


class MyFrame(wx.Frame):
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Logging test")
        panel = MyPanel(self)
        self.Show()


def main():
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()


if __name__ == "__main__":
    main()
