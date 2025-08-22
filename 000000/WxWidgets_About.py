# -*- coding: utf-8 -*-

import wx
import wx.adv
import wx.html
from wx.lib.wordwrap import wordwrap
import webbrowser


class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, title='The About Box')

        # Add a panel so it looks correct on all platforms
        self.panel = wx.Panel(self, wx.ID_ANY)

        # Создаём кнопки
        aboutBtn = wx.Button(self.panel, wx.ID_ANY, "Open wx.AboutBox")
        self.Bind(wx.EVT_BUTTON, self.onAboutDlg, aboutBtn)
        aboutHtmlBtn = wx.Button(self.panel, wx.ID_ANY, "Open HtmlAboutBox")
        self.Bind(wx.EVT_BUTTON, self.onAboutHtmlDlg, aboutHtmlBtn)

        closeBtn = wx.Button(self.panel, wx.ID_ANY, "Close")
        self.Bind(wx.EVT_BUTTON, self.onClose, closeBtn)

        # Создаём сайзеры
        topSizer = wx.BoxSizer(wx.VERTICAL)

        # Добавляем виджеты в сайзеры
        topSizer.Add(aboutBtn, 0, wx.ALL|wx.CENTER, 5)
        topSizer.Add(aboutHtmlBtn, 0, wx.ALL|wx.CENTER, 5)
        topSizer.Add(closeBtn, 0, wx.ALL|wx.CENTER, 5)

        # Создаём меню
        self.createMenu()
        self.statusBar = self.CreateStatusBar()

        self.panel.SetSizer(topSizer)
        self.SetSizeHints(250,300,500,400)
        self.Fit()
        self.Refresh()

    def createMenu(self):
        """ Создаём меню приложения """
        menubar = wx.MenuBar()

        # Создаём файловое меню
        fileMenu = wx.Menu()

        # Добавляем итем «Закрыть»
        # Выделение включает id, текстовый ярлык и стринг,
        # Чтобы отображать в строке статуса, когда итем выбран (выделен)
        close_menu_item = fileMenu.Append(wx.NewIdRef(count=1),
                                          "&Close",
                                          "Closes the application")
        # Создаём событие для итема меню
        self.Bind(wx.EVT_MENU, self.onClose, close_menu_item)
        # Добавляем fileMenu в полосу меню
        menubar.Append(fileMenu, "&File")

        # Создаём меню помощи
        helpMenu = wx.Menu()
        about_menu_item = helpMenu.Append(wx.NewIdRef(count=1),
                                          "&About",
                                          "Opens the About Box")
        self.Bind(wx.EVT_MENU, self.onAboutDlg, about_menu_item)
        menubar.Append(helpMenu, "&Help")

        # Добавляем полосу меню в рамку (фрейм)
        self.SetMenuBar(menubar)

    def onAboutHtmlDlg(self, event):
        aboutDlg = AboutDlg(None)
        aboutDlg.Show()

    def onAboutDlg(self, event):
        info = wx.adv.AboutDialogInfo()
        info.Name = "My About Box"
        info.Version = "0.0.1 Beta"
        info.Copyright = "(C) 2008 Python Geeks Everywhere"
        info.Description = wordwrap(
            "This is an example application that shows how to create "
            "different kinds of About Boxes using wxPython!",
            350, wx.ClientDC(self.panel))
        info.WebSite = ("http://www.pythonlibrary.org", "My Home Page")
        info.Developers = ["Mike Driscoll"]
        info.License = wordwrap("Completely and totally open source!", 500,
                                wx.ClientDC(self.panel))
        # Отображаем wx.AboutBox
        wx.adv.AboutBox(info)

    def onClose(self, event):
        self.Close()


class AboutDlg(wx.Frame):

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, wx.ID_ANY, title="About", size=(400,400))

        html = wxHTML(self)

        html.SetPage(
            ''

            "<h2>About the About Tutorial</h2>"

            "<p>This about box is for demo purposes only. It was created in June 2006"

            "by Mike Driscoll.</p>"

            "<p><b>Software used in making this demo:</h3></p>"

            '<p><b><a href="http://www.python.org">Python 2.4</a></b></p>'

            '<p><b><a href="http://www.wxpython.org">wxPython 2.8</a></b></p>'
        )

class wxHTML(wx.html.HtmlWindow):

    def OnLinkClicked(self, link):
        webbrowser.open(link.GetHref())


# Запускаем программу
if __name__ == '__main__':
    app = wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()