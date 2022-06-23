import wx
from streaming_server import *



class MyFrame(wx.Frame):
    def __init__(self, client_socket, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 500))

        # my var
        self.client_socket = client_socket

        # my panels
        self.center_page = CenterPage(self, self.client_socket)

        # creating sizer
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # adding
        self.sizer.Add(self.center_page, 1, wx.EXPAND)

        # set sizer
        self.SetSizer(self.sizer)


class CenterPage(wx.Panel):
    def __init__(self, parent, client):
        super(CenterPage, self).__init__(parent)

        # my var
        self.parent = parent
        self.client = client
        self.st = Streamer()
        font = wx.Font(25, family=wx.FONTFAMILY_MODERN, style=0, weight=90, underline=False, faceName="",
                       encoding=wx.FONTENCODING_DEFAULT)
        font2 = wx.Font(12, family=wx.FONTFAMILY_MODERN, style=0, weight=90, underline=False, faceName="",
                        encoding=wx.FONTENCODING_DEFAULT)

        # creating the boxes
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        # creating the labels
        self.topic = wx.StaticText(self, label="welcome to session with ", style=wx.ALIGN_CENTER)
        self.topic.SetFont(font)

        # creating the buttons
        self.sharing = wx.Button(self, label="share screen")
        self.sharing.SetFont(font2)

        self.stop_sharing = wx.Button(self, label="stop sharing")
        self.stop_sharing.SetFont(font2)

        # adding to the boxes
        hbox1.Add(self.topic, wx.EXPAND, 1)
        hbox2.Add(self.sharing, wx.EXPAND, 1)
        hbox2.Add(self.stop_sharing, wx.EXPAND, 1)

        # adding to the vbox
        vbox.Add(hbox1, 1, wx.ALIGN_CENTER)
        vbox.Add(hbox2, 1, wx.ALIGN_CENTER)
        self.SetSizer(vbox)

        # creating the button's bind
        self.sharing.Bind(wx.EVT_BUTTON, self.sharing_screen)
        self.stop_sharing.Bind(wx.EVT_BUTTON, self.stop_streaming)

    def sharing_screen(self, eve):
        self.client.send_mes("start stream")
        print("made till here")
        self.st.stream()

    def stop_streaming(self, eve):
        self.client.send_mes("stop stream")
        print("now we stop")
        self.st.stopping()



class MyAppServer(wx.App):
    def __init__(self, client_socket):
        wx.App.__init__(self)
        self.frame = MyFrame(client_socket, parent=None, title="my project")
        self.frame.Show()
        self.MainLoop()


