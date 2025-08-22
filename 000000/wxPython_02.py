import sys
import wx
#import snapshotPrinter


class MyForm(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Screenshot Tutorial")

        panel = wx.Panel(self)
        screenshotBtn = wx.Button(panel, label="Take Screenshot")
        screenshotBtn.Bind(wx.EVT_BUTTON, self.onTakeScreenShot)
        printBtn = wx.Button(panel, label="Print Screenshot")
        printBtn.Bind(wx.EVT_BUTTON, self.onPrint)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(screenshotBtn, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(printBtn, 0, wx.ALL|wx.CENTER, 5)
        panel.SetSizer(sizer)

    def onTakeScreenShot(self, event):
        """
        Делает скриншот выбранного фрагмента экрана
        Основано на методе, предложенном Андреа Гавана
        """
        print('Taking screenshot...')
        rect = self.GetRect()

        # Настройка ширины для Linux обнаружено Джоном Торресом
        # http://article.gmane.org/gmane.comp.python.wxpython/67327
        if sys.platform == 'linux2':
            client_x, client_y = self.ClientToScreen((0, 0))
            border_width = client_x - rect.x
            title_bar_height = client_y - rect.y
            rect.width += (border_width * 2)
            rect.height += title_bar_height + border_width

        # Сделать скриншот всей зоны DC (контекста устройства)
        dcScreen = wx.ScreenDC()

        # Создать битмап, в котором сохранится скриншот
        # Учтите, что битмап должен быть достаточно большим, чтобы в него поместился скриншот
        # -1 значит использование текущей стандартной глубины цвета
        bmp = wx.EmptyBitmap(rect.width, rect.height)

        # Создать в памяти DC, который будет использован непосредственно для скриншота
        memDC = wx.MemoryDC()

        # Прикажите DC использовать наш битмап
        # Все изображения из DC теперь переместится в битмап
        memDC.SelectObject(bmp)

        # Blit в данном случае скопируйте сам экран в кэш памяти
        # и, таким образом, он попадёт в битмап
        memDC.Blit( 0, # Скопируйте сюда координат Х
            0, # Скопируйте сюда координат Y
            rect.width, # Скопируйте эту ширину
            rect.height, # Скопируйте эту высоту
            dcScreen, # Место, откуда нужно скопировать
            rect.x, # Какой офсет у Х в оригинальном DC (контексте устройства)?
            rect.y # Какой офсет у Y в оригинальном DC?
        )

        # Select the Bitmap out of the memory DC by selecting a new
        # uninitialized Bitmap
        memDC.SelectObject(wx.NullBitmap)

        img = bmp.ConvertToImage()
        fileName = "myImage.png"
        img.SaveFile(fileName, wx.BITMAP_TYPE_PNG)
        print('...saving as png!')


    def onPrint(self, event):
        """
        Отправляем скриншот на печать.
        """
        printer = snapshotPrinter.SnapshotPrinter()
        printer.sendToPrinter()


# Запустите программу
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()