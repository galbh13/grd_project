import socket
import threading
from client_setting import *


class ServerCall(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.data = ""
        self.client_sock = conn

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
        print("we ready")
        while True:
            pass


