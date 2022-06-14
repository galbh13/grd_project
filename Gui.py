import wx
from main_final_client import *
# import controlled_client
import hashlib


# creating the main frame
class MyFrame(wx.Frame):
    def __init__(self, client, main, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 500))
        # my var
        self.flage = False
        self.my_email = ""
        # setting the panels
        self.choice = Choice(self, client)
        self.panel2 = MyPanel2(self, client)
        self.panel2.Hide()
        self.infoPanel = MyPanelInfo(self, client)
        self.infoPanel.Hide()
        self.helpPanel = MyHelpingPanel(self, client, main)
        self.helpPanel.Hide()
        self.needHelpPanel = MyNeedHelpPanel(self, client, main)
        self.needHelpPanel.Hide()
        self.registration = Registration(self, client)
        self.registration.Hide()
        self.login = LogingIn(self, client)
        self.login.Hide()


        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.choice, 1, wx.EXPAND)
        self.sizer.Add(self.panel2, 1, wx.EXPAND)
        self.sizer.Add(self.infoPanel, 1, wx.EXPAND)
        self.sizer.Add(self.helpPanel, 1, wx.EXPAND)
        self.sizer.Add(self.needHelpPanel, 1, wx.EXPAND)
        self.sizer.Add(self.registration, 1, wx.EXPAND)
        self.sizer.Add(self.login, 1, wx.EXPAND)

        self.SetSizer(self.sizer)

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

    def regi(self):
        if self.choice.IsShown():
            self.choice.Hide()
            self.registration.Show()
        else:
            self.registration.Hide()
            self.choice.Show()
        self.Layout()

    def logi(self):
        if self.choice.IsShown():
            self.choice.Hide()
            self.login.Show()
        else:
            self.login.Hide()
            self.choice.Show()
        self.Layout()

    def log_to_pan(self):
        if self.panel2.IsShown():
            self.panel2.Hide()
            self.login.Show()
        else:
            self.login.Hide()
            self.panel2.Show()
        self.Layout()

    def sign_to_pan(self):
        if self.panel2.IsShown():
            self.panel2.Hide()
            self.registration.Show()
        else:
            self.registration.Hide()
            self.panel2.Show()
        self.Layout()

    def move_forward(self):
        self.Destroy()


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
        self.opening = wx.StaticText(self, label="welcome to my app, please log in or register and lets start !",
                                     style=wx.ALIGN_CENTER)

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
        self.parent.regi()

    def loging_in(self, eve):
        self.parent.logi()


class Registration(wx.Panel):
    def __init__(self, parent, client):
        super(Registration, self).__init__(parent)
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
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        hbox6 = wx.BoxSizer(wx.HORIZONTAL)

        # creating the labels
        self.topic = wx.StaticText(self, label="Signing in", style=wx.ALIGN_CENTER)
        self.topic.SetFont(font)
        self.password_text = wx.StaticText(self, label="  :enter your password ", style=wx.ALIGN_CENTER)
        self.email_text = wx.StaticText(self, label="  :enter your email ", style=wx.ALIGN_CENTER)
        self.reply = wx.StaticText(self, label="give your shot", style=wx.ALIGN_CENTER)
        self.confirm = wx.StaticText(self, label="    :confirm password  ", style=wx.ALIGN_CENTER)

        # creating the TextControl
        self.tc1 = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.tc1.SetFocus()
        self.tc2 = wx.TextCtrl(self, style=wx.TE_PASSWORD)
        self.tc2.SetFocus()
        self.tc3 = wx.TextCtrl(self, style=wx.TE_PASSWORD)
        self.tc3.SetFocus()

        # creating the buttons
        self.submit = wx.Button(self, label="register")
        self.back = wx.Button(self, label="back")

        # adding to the boxes
        hbox1.Add(self.topic, 1, wx.EXPAND)
        hbox2.Add(self.tc1, 1, wx.LEFT)
        hbox2.Add(self.email_text, 1, wx.RIGHT)
        hbox3.Add(self.tc2, 1, wx.LEFT)
        hbox3.Add(self.password_text, 1, wx.RIGHT)
        hbox4.Add(self.tc3, 1, wx.LEFT)
        hbox4.Add(self.confirm, 1, wx.RIGHT)
        hbox5.Add(self.reply, 1, wx.EXPAND)
        hbox6.Add(self.submit, 1, wx.RIGHT)
        hbox6.Add(self.back, 1, wx.LEFT)

        # adding all the hboxes to the vbox
        vbox.Add(hbox1, 1, wx.ALIGN_CENTER)
        vbox.Add(hbox2, 1, wx.ALIGN_CENTER)
        vbox.Add(hbox3, 1, wx.ALIGN_CENTER)
        vbox.Add(hbox4, 1, wx.ALIGN_CENTER)
        vbox.Add(hbox5, 1, wx.ALIGN_CENTER)
        vbox.Add(hbox6, 1, wx.ALIGN_CENTER)
        self.SetSizer(vbox)

        # creating the button's bind
        self.submit.Bind(wx.EVT_BUTTON, self.creating)
        self.back.Bind(wx.EVT_BUTTON, self.backing)

    def is_a(self, e):
        count_a = 0
        count_d = 0
        count_p = 0

        # checking the symbol
        for a in e:
            if "@" == a:
                count_a += 1
        if count_a != 1:
            return False
        groups = e.split("@")

        # checking the Recipient name
        if len(groups[0]) > 64:
            return False
        for s in groups[0]:
            if s not in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890.!#$%&'*+-/=?^_`{|":
                return False
            if s == ".":
                count_d += 1
        if count_d > 1:
            return False

        for k in groups[1]:
            if k == ".":
                count_p += 1
        if count_p != 1:
            return False
        domains = groups[1].split(".")
        # checking domain
        d = domains[0]
        if len(d) > 253:
            return False
        for j in d:
            if j not in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890-.":
                return False

        # checking top level domain
        t = domains[1]
        if t == "com" or t == "net" or t == "org":
            return True
        return False

    def is_pass(self, p):
        count = 0
        for c in p:
            if c in "1234567890":
                count += 1
        if len(p) > 8 and count != 0:
            return True
        return False



    def is_valid(self):
        e = self.tc1.GetValue()
        p1 = self.tc2.GetValue()
        p2 = self.tc3.GetValue()
        if self.is_a(e) and self.is_pass(p1) and p1 == p2:
            print("valid")
            return True
        print("not valid")
        return False

    def creating(self, eve):
        """
        here we are sending a request to create the account
        :return:
        """
        if self.is_valid():
            print("we here")
            str1 = "sql|create|"
            e = self.tc1.GetValue()
            p = self.tc2.GetValue()
            password = p.encode()
            hash_password = hashlib.sha3_512(password).hexdigest()
            str1 += str(e) + "|"
            str1 += str(hash_password)
            self.client.send(str1)
            x = self.client.receive()
            if x == "created":
                self.parent.my_email = e
                self.parent.sign_to_pan()
            elif x == "logged":
                self.reply.SetLabelText("try again, this email already online")
            else:
                self.reply.SetLabelText("try again, this gmail is already taken")
        else:
            self.reply.SetLabelText("try again, you need to have valid gmail and at least 9 character at your password with at least one number")

    def backing(self, eve):
        """
        here we are going back to choice page
        :return:
        """
        self.parent.regi()


class LogingIn(wx.Panel):
    def __init__(self, parent, client):
        super(LogingIn, self).__init__(parent)
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
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)

        # creating the labels
        self.topic = wx.StaticText(self, label="loging in", style=wx.ALIGN_CENTER)
        self.topic.SetFont(font)
        self.password_text = wx.StaticText(self, label="  :enter your password ", style=wx.ALIGN_CENTER)
        self.email_text = wx.StaticText(self, label="  :enter your email ", style=wx.ALIGN_CENTER)
        self.reply = wx.StaticText(self, label="give your best shot", style=wx.ALIGN_CENTER)

        # creating the TextControl
        self.tc1 = wx.TextCtrl(self, style=wx.TE_PASSWORD)
        self.tc1.SetFocus()
        self.tc2 = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.tc2.SetFocus()

        # creating the buttons
        self.submit = wx.Button(self, label="submit")
        self.back = wx.Button(self, label="back")

        # adding to the boxes
        hbox1.Add(self.topic, 1, wx.EXPAND)
        hbox2.Add(self.tc2, 1, wx.LEFT)
        hbox2.Add(self.email_text, 1, wx.RIGHT)
        hbox3.Add(self.tc1, 1, wx.LEFT)
        hbox3.Add(self.password_text, 1, wx.RIGHT)
        hbox4.Add(self.reply, 1, wx.EXPAND)
        hbox5.Add(self.submit, 1, wx.EXPAND)
        hbox5.Add(self.back, 1, wx.EXPAND)

        # adding all the hboxes to the vbox
        vbox.Add(hbox1, 1, wx.ALIGN_CENTER)
        vbox.Add(hbox2, 1, wx.ALIGN_CENTER)
        vbox.Add(hbox3, 1, wx.ALIGN_CENTER)
        vbox.Add(hbox4, 1, wx.EXPAND)
        vbox.Add(hbox5, 1, wx.EXPAND)
        self.SetSizer(vbox)

        # creating the button's bind
        self.submit.Bind(wx.EVT_BUTTON, self.submiting)
        self.back.Bind(wx.EVT_BUTTON, self.backing)


    def submiting(self, eve):
        """
        here we sending a request for the server to see if the client is existed
        :param eve:
        :return:
        """
        str1 = "sql|submit|"
        e = self.tc2.GetValue()
        p = self.tc1.GetValue()
        print(p)
        password = p.encode()
        hash_password = hashlib.sha3_512(password).hexdigest()
        print(hash_password)
        str1 += str(e) + "|"
        str1 += str(hash_password)
        self.client.send(str1)
        x = self.client.receive()
        print("received")
        if x == "success":
            self.parent.my_email = e
            self.parent.log_to_pan()
        elif x == "logged":
            self.reply.SetLabelText("try again, the email is already online")
        else:
            print("reply")
            self.reply.SetLabelText("try again, the gmail or the password is wrong")

    def backing(self, eve):
        """
        here we are going back to choice page
        :return:
        """
        self.parent.logi()


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

        # creating the labels
        self.label1 = wx.StaticText(self, label="what would you like to do", style=wx.ALIGN_CENTER)
        self.label1.SetFont(font)
        self.label2 = wx.StaticText(self, label="", style=wx.ALIGN_CENTER)
        self.label2.SetFont(font)

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

        # adding all the hboxes to the vbox
        vbox.Add(hbox1, 1, wx.EXPAND)
        vbox.Add(hbox2, 1, wx.EXPAND)
        vbox.Add(hbox3, 1, wx.EXPAND)
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
    def __init__(self, parent, client, main):
        super(MyHelpingPanel, self).__init__(parent)
        # my var
        self.client = client
        self.typed_id = ""
        self.parent = parent
        self.main = main

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
        hbox2.Add(self.reply, 1, wx.EXPAND)
        hbox3.Add(self.button)
        hbox3.Add(self.tc, proportion=1)
        hbox4.Add(self.help_back, 1, wx.EXPAND)
        # adding all the hboxes to the vbox
        vbox.Add(hbox1, 1, wx.EXPAND)
        vbox.Add(hbox3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        vbox.Add(hbox2, 1, wx.EXPAND)
        vbox.Add(hbox4, 1, wx.CENTER)

        # creating the button's bind
        self.button.Bind(wx.EVT_BUTTON, self.on_button_ok)
        self.help_back.Bind(wx.EVT_BUTTON, self.back_home_from_helping)

        # set sizer
        self.SetSizer(vbox)

    def on_button_ok(self, event):
        self.typed_id = self.tc.GetValue()
        str1 = "try."
        print(self.typed_id + "typed")
        str1 += self.typed_id
        self.client.send(str1)
        data = self.client.receive()
        print("data is " + data)
        rep = self.answer_from_server(data)
        self.reply.SetLabelText(rep)
        if data == "exist":
            tup = self.client.receive()
            print(tup)
            x = tup.split("|")
            print("x - " + str(x))
            address = x[0]
            print("add - " + address)
            self.client.closing()
            self.parent.move_forward()
            self.main.starting_client(address, self.parent.my_email)



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
    def __init__(self, parent, client, main):
        super(MyNeedHelpPanel, self).__init__(parent)
        # my var
        self.parent = parent
        self.client = client
        self.main = main

        # creating the boxes
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)

        # creating labels
        self.needhelp_title = wx.StaticText(self, label="Are You Sure?", style=wx.ALIGN_CENTER)

        # creating buttons
        self.need_back = wx.Button(self, label="return")
        self.begin = wx.Button(self, label="continue")

        # adding the labels to the boxes
        hbox1.Add(self.needhelp_title, 1, wx.EXPAND)
        hbox2.Add(self.need_back, 1, wx.EXPAND)
        hbox2.Add(self.begin, 1, wx.EXPAND)

        # adding all the hboxes to the vbox
        vbox.Add(hbox1, 1, wx.EXPAND)
        vbox.Add(hbox2, 1, wx.EXPAND)
        vbox.Add(hbox3, 1, wx.EXPAND)
        vbox.Add(hbox4, 1, wx.EXPAND)

        # creating the button's bind
        self.need_back.Bind(wx.EVT_BUTTON, self.back_home_from_need_help)
        self.begin.Bind(wx.EVT_BUTTON, self.lets_begin)

        # set sizer
        self.SetSizer(vbox)

    def back_home_from_need_help(self, event):
        """
        using the need help switch function and cancel the application for help
        :param event:
        :return:
        """
        self.parent.needSwitch()

    def lets_begin(self, event):
        # here we start the session
        self.client.send("waiting")
        self.client.closing()
        self.parent.move_forward()
        self.main.starting_server()


class MyApp(wx.App):
    def __init__(self, main, sessionWithServer):
        wx.App.__init__(self)
        self.frame = MyFrame(sessionWithServer, main, parent=None, title="my project")
        self.frame.Show()
        self.MainLoop()

