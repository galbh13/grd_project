import wx
from streaming_server import *


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 500))

        # my panels
        self.wait = Waiting(self)

        # creating sizer
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # adding
        self.sizer.Add(self.wait, 1, wx.EXPAND)

        # set sizer
        self.SetSizer(self.sizer)

    def closing(self):
        self.Close()


class Waiting(wx.Panel):
    def __init__(self, parent):
        super(Waiting, self).__init__(parent)

        # my var
        self.parent = parent

        # creating the boxes
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)

        # creating the labels
        self.message = wx.StaticText(self, label="...waiting", style=wx.ALIGN_CENTER)

        # adding to the boxes
        hbox1.Add(self.message, wx.EXPAND, 1)

        # adding to the vbox
        vbox.Add(hbox1, 1, wx.ALIGN_CENTER)

        # set sizer
        self.SetSizer(vbox)





class MyWaitingAPP(wx.App):
    def __init__(self):
        wx.App.__init__(self)
        self.frame = MyFrame(parent=None, title="my project")
        self.frame.Show()
        self.MainLoop()

    def finish(self):
        wx.Exit()

