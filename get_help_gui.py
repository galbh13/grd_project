import wx
from streaming_server import *



class MyFrame(wx.Frame):
    def __init__(self, client_socket, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 500))

        # my var
        self.conn = ""
        self.client_socket = client_socket

        # my panels
        self.wait = Waiting(self, self.client_socket)
        self.center_page = CenterPage(self, self.client_socket)
        self.center_page.Hide()

        # creating sizer
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # adding
        self.sizer.Add(self.wait, 1, wx.EXPAND)
        self.sizer.Add(self.center_page, 1, wx.EXPAND)

        # set sizer
        self.SetSizer(self.sizer)

    def change(self, adding):
        if self.wait.IsShown():
            self.center_page.topic.SetLabelText("welcome to session with " + adding)
            self.wait.Hide()
            self.center_page.Show()
        else:
            self.center_page.Hide()
            self.wait.Show()
        self.Layout()


class Waiting(wx.Panel):
    def __init__(self, parent, client):
        super(Waiting, self).__init__(parent)

        # my var
        self.parent = parent
        self.client = client

        # creating the boxes
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)

        # creating the labels
        self.message = wx.StaticText(self, label="...waiting", style=wx.ALIGN_CENTER)

        # adding to the boxes
        hbox1.Add(self.message, wx.EXPAND, 1)

        # adding to the vbox
        vbox.Add(hbox1, 1, wx.ALIGN_CENTER)
        self.SetSizer(vbox)

        # session
        x = self.parent.client_socket.receive()
        if x[:4] == "start":
            self.parent.change(x[6:])


class CenterPage(wx.Panel):
    def __init__(self, parent, client):
        super(CenterPage, self).__init__(parent)

        # my var
        self.parent = parent
        self.client = client

        # creating the boxes
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        # creating the labels
        self.topic = wx.StaticText(self, label="welcome to session with ", style=wx.ALIGN_CENTER)

        # creating the buttons
        self.sharing = wx.Button(self, label="share screen")
        self.chatting = wx.Button(self, label="chat")

        # adding to the boxes
        hbox1.Add(self.topic, wx.EXPAND, 1)
        hbox2.Add(self.sharing, wx.EXPAND, 1)
        hbox2.Add(self.chatting, wx.EXPAND, 1)

        # adding to the vbox
        vbox.Add(hbox1, 1, wx.ALIGN_CENTER)
        vbox.Add(hbox2, 1, wx.ALIGN_CENTER)
        self.SetSizer(vbox)

        # creating the button's bind
        self.sharing.Bind(wx.EVT_BUTTON, self.sharing_screen)
        self.chatting.Bind(wx.EVT_BUTTON, self.chatting_with)

    def sharing_screen(self, eve):
        st = Streamer()
        # changing the buttons

    def chatting_with(self, eve):
        pass



class MyApp(wx.App):
    def __init__(self, client_socket):
        wx.App.__init__(self)
        self.frame = MyFrame(client_socket, parent=None, title="my project")
        self.frame.Show()
        self.MainLoop()


app = MyApp("why")
