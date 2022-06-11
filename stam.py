import wx


class Choice(wx.Panel):
    def __init__(self, parent, client):
        super(Choice, self).__init__(parent)
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
        self.topic = wx.StaticText(self, label="Remote Desktop - overcome physics", style=wx.ALIGN_CENTER)
        self.topic.SetFont(font)
        self.opening = wx.StaticText(self, label="welcome to my app, please log in or register and lets start !", style=wx.ALIGN_CENTER)

        # creating the buttons
        self.sign_in = wx.Button(self, label="sign in")
        self.login = wx.Button(self, label="login")

        # adding to the boxes
        hbox1.Add(self.topic, wx.EXPAND, 1)
        hbox2.Add(self.opening, wx.EXPAND, 1)
        hbox3.Add(self.sign_in, wx.EXPAND, 1)
        hbox3.Add(self.login, wx.EXPAND, 1)

        # adding to the vbox
        vbox.Add(hbox1, 1, wx.ALIGN_CENTER)
        vbox.Add(hbox2, 1, wx.ALIGN_CENTER)
        vbox.Add(hbox3, 1, wx.ALIGN_CENTER)
        self.SetSizer(vbox)

        # creating the button's bind
        self.sign_in.Bind(wx.EVT_BUTTON, self.signing_in)
        self.login.Bind(wx.EVT_BUTTON, self.loging_in)

    def signing_in(self, eve):
        pass
    def loging_in(self, eve):
        pass

class MyFrame(wx.Frame):
    def __init__(self, client, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 500))
        reg = Choice(self, client)

class MyApp(wx.App):
    def __init__(self, sessionWithServer):
        wx.App.__init__(self)
        self.frame = MyFrame(sessionWithServer, parent=None, title="my project")
        self.frame.Show()
        self.MainLoop()

test = MyApp("why")


