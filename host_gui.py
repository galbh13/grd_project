import wx


class MyFrame(wx.Frame):
    def __init__(self, client, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 500))
        # my var

        # setting the panels



class MainPage(wx.Panel):
    def __init__(self, parent, client):
        super(MainPage, self).__init__(parent)
        # my var
        self.client = client
        self.parent = parent
        font = wx.Font(20, family=wx.FONTFAMILY_MODERN, style=0, weight=90, underline=False, faceName="",
                       encoding=wx.FONTENCODING_DEFAULT)

        # creating the boxes
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)

        # creating the labels
        self.topic = wx.StaticText(self, label="welcome host", style=wx.ALIGN_CENTER)
        self.topic.SetFont(font)
        self.opening = wx.StaticText(self, label="now you will wait for a person to join the session.",
                                     style=wx.ALIGN_CENTER)

        # adding to the boxes
        hbox1.Add(self.topic, wx.EXPAND, 1)
        hbox2.Add(self.opening, wx.EXPAND, 1)

        # adding to the vbox
        vbox.Add(hbox1, 1, wx.ALIGN_CENTER)
        vbox.Add(hbox2, 1, wx.ALIGN_CENTER)
        self.SetSizer(vbox)



class MyApp(wx.App):
    def __init__(self, sessionWithServer):
        wx.App.__init__(self)
        self.frame = MyFrame(sessionWithServer, parent=None, title="my project")
        self.frame.Show()
        self.MainLoop()