import random
import threading
from server_setting import *


class Client(threading.Thread):
    def __init__(self, server, client_sock, address):
        threading.Thread.__init__(self)
        self.server = server
        self.client_sock = client_sock
        self.address = address
        self.Id = self.user_info()

    def user_info(self):
        """
        selecting the user's id
        :return: user's id
        """
        found = False
        while not found:
            num = random.randint(100000, 999999)
            if num not in self.server.clients.keys():
                return num

    def send_mes(self, mes):
        """
        sending a message to the client
        :param mes: the message
        :return:
        """
        try:
            self.client_sock.send(mes.encode(FORMAT))
        except Exception as e:
            print(e)

    def send_tuple(self, tup):
        """
        here we are sending tuples
        :param tup: the tuple
        :return: NONE
        """
        print(tup)
        a = tup[0]
        b = tup[1]
        print(str(a))
        print(str(b))
        try:
            self.client_sock.send(str(a).encode(FORMAT))
            self.client_sock.send(str(b).encode(FORMAT))
        except Exception as e:
            print(e)

    def run(self):
        data = ""
        """
        this is the ...
        :return:
        """

        try:
            self.send_mes(str(self.Id))
        except Exception as e:
            print(e)
        while True:
            try:
                data = self.client_sock.recv(SIZE).decode("utf-8")
                print(data)
                print(self.server.active_clients.keys())
            except Exception as e:
                print(e)
                break

            if data == "waiting":
                print(self.server.clients[self.Id])
                self.server.active_clients[self.Id] = self.server.clients[self.Id]
                print(self.server.active_clients.keys())
            elif data == "cancel":
                print(self.server.active_clients[self.Id])
                del self.server.active_clients[self.Id]
            elif int(data) in self.server.active_clients.keys():
                self.send_mes("exist")
                self.server.active_clients[int(data)].client_sock.send("start".encode("utf-8"))
                self.send_tuple(self.server.active_clients[int(data)].address)
            else:
                print("he had mistake")
                self.send_mes("wrong")





