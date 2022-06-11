import socket
import threading
from client_setting import *


class Call(threading.Thread):
    def __init__(self, address):
        threading.Thread.__init__(self)
        self.data = ""
        self.address = address
        self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        """
        trying consistency to connect the server
        :return:
        """
        while True:
            try:
                self.client_sock.connect((self.address, PORT))
                print("client connected")
                break
            except socket.error as e:
                continue

    def send(self, mes):
        """
        sending a message to the client
        :param mes: the message
        :return:
        """
        try:
            self.client_sock.send(mes.encode(FORMAT))
        except socket.error as e:
            print(e)

    def receive(self):
        try:
            return self.client_sock.recv(1024).decode("utf-8")
        except Exception as e:
            print(e)

    def run(self):
        """
        here is the ...
        :return:
        """
        print("Wait to server...")
        self.connect()
        while True:
            pass


