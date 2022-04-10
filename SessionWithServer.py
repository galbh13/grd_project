import socket
import threading
from Settings import *


class SessionWithServer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.data = ""
        self.Id = ""
        self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        """
        trying consistency to connect the server
        :return:
        """
        while True:
            try:
                self.client_sock.connect((IP, PORT))
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
            return self.client_sock.recv(SIZE).decode("utf-8")
        except Exception as e:
            print(e)




    def run(self):
        """
        here is the ...
        :return:
        """
        print("Wait to server...")
        self.connect()
        try:
            self.Id = self.client_sock.recv(SIZE).decode("utf-8")
        except socket.error as e:
            print(e)
        while True:
            pass


