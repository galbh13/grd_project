import wx
from session_settings import *
from streaming_client import *

class MyFrame(wx.Frame):
    def __init__(self, client, add, email, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 500))

        # my panels
        self.center_page = CenterPage(self, client, add, email)
        # creating sizer
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # adding
        self.sizer.Add(self.center_page, 1, wx.EXPAND)

        # set sizer
        self.SetSizer(self.sizer)


class CenterPage(wx.Panel):
    def __init__(self, parent, client, add, email):
        super(CenterPage, self).__init__(parent)

        # my var
        self.parent = parent
        self.client = client
        self.add = add
        self.email = email
        self.s = Streamer(self.add)

        # creating the boxes
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)

        # creating the labels
        self.topic = wx.StaticText(self, label="welcome to session with ", style=wx.ALIGN_CENTER)
        self.rules = wx.StaticText(self, label="you have 2 tools you can activated so this call be more effective", style=wx.ALIGN_CENTER)
        self.features = wx.StaticText(self, label="ask the owner if he can share his screen or activate audio", style=wx.ALIGN_CENTER)

        # adding to the boxes
        hbox1.Add(self.topic, wx.EXPAND, 1)
        hbox2.Add(self.rules, wx.EXPAND, 1)
        hbox3.Add(self.features, wx.EXPAND, 1)

        # adding to the vbox
        vbox.Add(hbox1, 1, wx.ALIGN_CENTER)
        vbox.Add(hbox2, 1, wx.ALIGN_CENTER)
        vbox.Add(hbox3, 1, wx.ALIGN_CENTER)

        self.SetSizer(vbox)
        str1 = "start." + str(email)
        self.client.send_mes(str1)
        while True:
            action = self.client.receive()
            if action == "start stream":
                self.streaming()
            elif action == "start talking":
                self.talking()
            elif action == "stop stream":
                self.stop_stream()

    def streaming(self):
        self.s.stream()

    def stop_stream(self):
        self.s.stopping()

    def talking(self):
        pass


class MyApp(wx.App):
    def __init__(self, client, add, email):
        wx.App.__init__(self)
        self.frame = MyFrame(client, add, email, parent=None, title="my project")
        self.frame.Show()
        self.MainLoop()



