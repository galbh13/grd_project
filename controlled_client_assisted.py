import socket
import threading
from client_setting import *
from session_settings import *


class ServerCall(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.my_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_server.bind((IP_SERVER, SERVER_PORT))
        self.my_server.listen()
        print("we ready to go !!!")
        self.client_socket, self.client_address = self.my_server.accept()
        self.data = ""

    def send(self, mes):
        """
        sending a message to the client
        :param mes: the message
        :return:
        """
        try:
            self.client_socket.send(mes.encode(FORMAT))
        except socket.error as e:
            print(e)

    def receive(self):
        try:
            return self.client_socket.recv(1024).decode("utf-8")
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


