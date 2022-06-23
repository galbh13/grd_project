import socket
import threading
from session_settings import *
from helping_gui import *
import sys
from streaming_client import *


class Call(threading.Thread):
    def __init__(self, address, email):
        threading.Thread.__init__(self)
        self.data = ""
        self.address = address
        self.port = CLIENT_PORT
        self.email = email
        self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s = Streamer(self.address)


    def massage_len_give(self, replay):
        """
        this function have 2 parts, we use it when we want to send something
        and we need to do with getting the exact amount of letters
        :param replay: the word we want to send her length
        :return: nothing but sending the server the word's length
        """
        x = len(replay)
        count = 10
        zover = 1
        while True:
            if x < count:
                try:
                    self.client_sock.send(str(x).encode("utf-8"))
                except Exception as e:
                    print("something went wrong")
                    print(e)
                    sys.exit()
                break
            else:
                length = "0" * zover
                try:
                    self.client_sock.send(length.encode("utf-8"))
                except Exception as e:
                    print("something went wrong")
                    print(e)
                    sys.exit()
                zover = zover + 1
            count = count * 10

    # this function is one of 2 parts function, this is the receiving one

    def massage_len_answer(self):
        """
        this is the second function of the 2 part function.
        it get massages from the server, the server sending him the length of
        the word / sentence he want to give
        :return: it return the length of the word / sentence the server want
        to send
        """
        i = 1
        while True:
            try:
                is_fit = self.client_sock.recv(i).decode()
            except Exception as e:
                print("something went wrong")
                print(e)
                sys.exit()
            if "0" * i in is_fit:
                i = i + 1
            else:
                return int(is_fit)

    def connect(self):
        """
        trying consistency to connect the server
        :return:
        """
        while True:
            try:
                self.client_sock.connect((self.address, self.port))
                print("client connected")
                break
            except socket.error as e:
                continue

    def send_mes(self, mes):
        """
        sending a message to the client
        :param mes: the message
        :return:
        """
        self.massage_len_give(mes)
        try:
            print(mes + " ----------------------------------")
            self.client_sock.send(mes.encode(FORMAT))
        except Exception as e:
            print(e)

    def receive(self):
        try:
            size = self.massage_len_answer()
            data = self.client_sock.recv(size).decode("utf-8")
            print(data)
        except Exception as e:
            print(e)

    def run(self):
        """
        here is the ...
        :return:
        """
        print("Wait to server...")
        self.connect()
        self.gui = MyAppClient(self.address)
        str1 = "start." + str(self.email)
        #self.send_mes(str1)
        while True:
            action = self.receive()
            print(action)
            if action == "start stream":
                self.s.stream()
            elif action == "start talking":
                pass
            elif action == "stop stream":
                self.s.stopping()


