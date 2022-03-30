import wx
import socket
import random
import sys

# creating the main frame
class MyFrame(wx.Frame):
    def __init__(self, client, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 500))
        # my var
        self.flage = False
        # setting the panels
        self.panel = MyPanel(self, client)
        self.panel2 = MyPanel2(self, client)
        self.panel2.Hide()
        self.infoPanel = MyPanelInfo(self, client)
        self.infoPanel.Hide()
        self.helpPanel = MyHelpingPanel(self, client)
        self.helpPanel.Hide()
        self.needHelpPanel = MyNeedHelpPanel(self, client)
        self.needHelpPanel.Hide()

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel, 1, wx.EXPAND)
        self.sizer.Add(self.panel2, 1, wx.EXPAND)
        self.sizer.Add(self.infoPanel, 1, wx.EXPAND)
        self.sizer.Add(self.helpPanel, 1, wx.EXPAND)
        self.sizer.Add(self.needHelpPanel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

    def onSwitchPanels(self):
        """
        switch from the first panel to the second panel and opposite
        :return:
        """
        if self.panel.IsShown():
            self.panel.Hide()
            self.panel2.label2.SetLabelText("hey " + self.panel.name)
            self.panel2.Show()
        else:
            self.panel.Show()
            self.panel2.Hide()
        self.Layout()

    def infoSwitch(self):
        """
        switch from the second panel to the info panel and opposite
        :return:
        """
        if self.panel2.IsShown():
            self.panel2.Hide()
            self.infoPanel.Show()
        else:
            self.infoPanel.Hide()
            self.panel2.Show()
        self.Layout()

    def helpSwitch(self):
        """
        switch from the second panel to the helping panel and opposite
        :return:
        """
        if self.panel2.IsShown():
            self.panel2.Hide()
            self.helpPanel.Show()
        else:
            self.helpPanel.Hide()
            self.panel2.Show()
        self.Layout()

    def needSwitch(self):
        """
        switch from the second panel to the need help panel panel and opposite
        :return:
        """
        if self.panel2.IsShown():
            self.panel2.Hide()
            self.needHelpPanel.Show()
        else:
            self.needHelpPanel.Hide()
            self.panel2.Show()
        self.Layout()


class MyPanel(wx.Panel):
    def __init__(self, parent, client):
        super(MyPanel, self).__init__(parent)
        # my vars
        self.parent = parent
        self.name = ""
        font = wx.Font(20, family=wx.FONTFAMILY_MODERN, style=0, weight=90, underline=False, faceName="",
                       encoding=wx.FONTENCODING_DEFAULT)

        # creating the boxes
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        # creating the labels
        self.labelId = wx.StaticText(self, label="Id : " + client.Id, style=wx.ALIGN_CENTER)
        self.labelId.SetFont(font)
        self.label = wx.StaticText(self, label=":enter your name", style=wx.ALIGN_CENTER)
        self.label.SetFont(font)

        # creating the button
        self.button = wx.Button(self, label="ok")

        # binding the button
        self.button.Bind(wx.EVT_BUTTON, self.onButton)

        # creating the TextControl
        self.tc = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.tc.SetFocus()

        # adding the labels to the boxes
        vbox.Add(self.labelId, 0, wx.EXPAND)
        vbox.Add(self.label, 0, wx.EXPAND)
        hbox.Add(self.button)
        hbox.Add(self.tc, proportion=1)
        vbox.Add(hbox, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        self.SetSizer(vbox)

    def onButton(self, event):
        """
        when clicking the button we getting the user's name and switching to the second panel
        :param event:
        :return:
        """
        self.name = self.tc.GetValue()
        self.parent.onSwitchPanels()


class MyPanel2(wx.Panel):
    def __init__(self, parent, client):
        super(MyPanel2, self).__init__(parent)
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
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)

        # creating the labels
        self.label1 = wx.StaticText(self, label="what would you like to do", style=wx.ALIGN_CENTER)
        self.label1.SetFont(font)
        self.label2 = wx.StaticText(self, label="", style=wx.ALIGN_CENTER)
        self.label2.SetFont(font)
        self.labelId = wx.StaticText(self, label="Id : " + client.Id, style=wx.ALIGN_CENTER)
        self.labelId.SetFont(font)

        # creating the buttons
        self.info_bot = wx.Button(self, label="info")
        self.helping_bot = wx.Button(self, label="i want to help")
        self.need_help_bot = wx.Button(self, label="i need help !")

        # adding the labels to the boxes
        hbox1.Add(self.label2, 1, wx.EXPAND)
        hbox2.Add(self.label1, 1, wx.EXPAND)
        hbox3.Add(self.info_bot, 1, wx.RIGHT)
        hbox3.Add(self.helping_bot, 1, wx.LEFT)
        hbox3.Add(self.need_help_bot, 1, wx.RIGHT)
        hbox4.Add(self.labelId, 1, wx.EXPAND)

        # adding all the hboxes to the vbox
        vbox.Add(hbox1, 1, wx.EXPAND)
        vbox.Add(hbox2, 1, wx.EXPAND)
        vbox.Add(hbox3, 1, wx.EXPAND)
        vbox.Add(hbox4, 1, wx.EXPAND)
        self.SetSizer(vbox)

        # creating the button's bind
        self.info_bot.Bind(wx.EVT_BUTTON, self.information)
        self.helping_bot.Bind(wx.EVT_BUTTON, self.helping_mode)
        self.need_help_bot.Bind(wx.EVT_BUTTON, self.get_help)

    def information(self, event):
        """
        using the info switch function
        :param event:
        :return:
        """
        self.parent.infoSwitch()

    def helping_mode(self, event):
        """
        using the help switch function
        :param event:
        :return:
        """
        self.parent.helpSwitch()

    def get_help(self, event):
        """
        using the get help function and apply a request to get someone to help
        :param event:
        :return:
        """
        self.client.send("waiting")
        self.parent.needSwitch()


class MyPanelInfo(wx.Panel):
    def __init__(self, parent, client):
        super(MyPanelInfo, self).__init__(parent)
        # my var
        self.parent = parent
        # creating boxes
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        # creating labels
        self.info_art = wx.StaticText(self, label="INFORMATION", style=wx.ALIGN_CENTER)
        self.opening = wx.StaticText(self,
                                     label="in this program you will help other people or get help from other people",
                                     style=wx.ALIGN_LEFT)
        # creating buttons
        self.info_back = wx.Button(self, label="return")

        # adding the labels to the boxes
        hbox1.Add(self.info_art, 1, wx.EXPAND)
        hbox2.Add(self.opening, 1, wx.EXPAND)
        hbox3.Add(self.info_back, 1, wx.EXPAND)

        # adding all the hboxes to the vbox
        vbox.Add(hbox1, 1, wx.EXPAND)
        vbox.Add(hbox2, 1, wx.EXPAND)
        vbox.Add(hbox3, 1, wx.EXPAND)

        # creating the button's bind
        self.info_back.Bind(wx.EVT_BUTTON, self.back_home_from_info)

        # set sizer
        self.SetSizer(vbox)

    # functions
    def back_home_from_info(self, event):
        """
        using the info switch function
        :param event:
        :return:
        """
        self.parent.infoSwitch()



class MyHelpingPanel(wx.Panel):
    def __init__(self, parent, client):
        super(MyHelpingPanel, self).__init__(parent)
        # my var
        self.client = client
        self.typed_id = ""
        self.parent = parent

        # creating boxes
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)

        # creating labels
        self.help_art = wx.StaticText(self, label="HELPING MODE", style=wx.ALIGN_CENTER)
        self.opening = wx.StaticText(self, label="type your friend id and start the call", style=wx.ALIGN_CENTER)
        self.reply = wx.StaticText(self, label="")

        # creating buttons
        self.button = wx.Button(self, label="ok")
        self.help_back = wx.Button(self, label="return")

        # creating the TextControl
        self.tc = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.tc.SetFocus()

        # adding the labels to the boxes
        hbox1.Add(self.help_art, 1, wx.EXPAND)
        hbox2.Add(self.opening, 1, wx.EXPAND)
        hbox3.Add(self.button)
        hbox3.Add(self.tc, proportion=1)
        hbox4.Add(self.help_back, 1, wx.EXPAND)
        # adding all the hboxes to the vbox
        vbox.Add(hbox1, 1, wx.EXPAND)
        vbox.Add(hbox3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        vbox.Add(hbox2, 1, wx.EXPAND)
        vbox.Add(hbox4, 1, wx.EXPAND)
        # creating the button's bind
        self.button.Bind(wx.EVT_BUTTON, self.on_button_ok)
        self.help_back.Bind(wx.EVT_BUTTON, self.back_home_from_helping)

        # set sizer
        self.SetSizer(vbox)

    def on_button_ok(self, event):
        self.typed_id = self.tc.GetValue()
        print(self.typed_id)
        self.client.send(str(self.typed_id))
        data = self.client.receive()
        rep = self.answer_from_server(data)
        self.reply.SetLabelText(rep)

    def answer_from_server(self, ans):
        if ans == "wrong":
            return "there is no one with that id, please try again"
        elif ans == "exist":
            return "we found someone and we send the request to start the session"



    def back_home_from_helping(self, event):
        """
        using the help switch function
        :param event:
        :return:
        """
        self.parent.helpSwitch()


class MyNeedHelpPanel(wx.Panel):
    def __init__(self, parent, client):
        super(MyNeedHelpPanel, self).__init__(parent)
        # my var
        self.parent = parent
        self.client = client
        # creating the boxes
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)

        # creating labels
        self.needhelp_title = wx.StaticText(self, label="getting help", style=wx.ALIGN_CENTER)
        self.opening = wx.StaticText(self, label="wait here till someone enter your id and then we will connect you",
                                     style=wx.ALIGN_CENTER)
        # creating buttons
        self.need_back = wx.Button(self, label="return")

        # adding the labels to the boxes
        hbox1.Add(self.needhelp_title, 1, wx.EXPAND)
        hbox2.Add(self.opening, 1, wx.EXPAND)
        hbox3.Add(self.need_back, 1, wx.EXPAND)

        # adding all the hboxes to the vbox
        vbox.Add(hbox1, 1, wx.EXPAND)
        vbox.Add(hbox2, 1, wx.EXPAND)
        vbox.Add(hbox3, 1, wx.EXPAND)

        # creating the button's bind
        self.need_back.Bind(wx.EVT_BUTTON, self.back_home_from_need_help)

        # set sizer
        self.SetSizer(vbox)

    def back_home_from_need_help(self, event):
        """
        using the need help switch function and cancel the application for help
        :param event:
        :return:
        """
        self.client.send("cancel")
        self.parent.needSwitch()


class MyApp(wx.App):
    def __init__(self, sessionWithServer):
        wx.App.__init__(self)
        self.frame = MyFrame(sessionWithServer, parent=None, title="my project")
        self.frame.Show()
        self.MainLoop()

