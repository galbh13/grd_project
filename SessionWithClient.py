import threading
from server_setting import *
import sys


class Client(threading.Thread):
    def __init__(self, server, client_sock, address):
        threading.Thread.__init__(self)
        self.server = server
        self.client_sock = client_sock
        self.address = address
        print(self.address)
        self.Id = ""

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
        """
        this is the ...
        :return:
        """

        while True:
            try:
                size = self.massage_len_answer()
                data = self.client_sock.recv(size).decode("utf-8")
                print(data)
            except Exception as e:
                print(e)
                break
            print(self.server.active_clients.values())
            if data == "waiting":
                self.server.active_clients[self.Id] = self.address
                print(self.server.active_clients.keys())
            elif data == "cancel":
                print(self.server.active_clients[self.Id])
                del self.server.active_clients[self.Id]
            elif data[:3] == "try":
                print(data[4:0] + "hey day")
                if data[4:] in self.server.active_clients.keys():
                    self.send_mes("exist")
                    print(self.server.active_clients[data[4:]])
                    self.send_mes(self.server.active_clients[data[4:]])
            elif data[:3] == "sql":
                after = data.split("|")
                e = after[2]
                p = after[3]
                print(p + " space " + e)
                if after[1] == "create":
                    if self.server.create_account(e, p) == "created":
                        self.Id = e
                        self.send_mes("created")
                        self.server.online_clients.append(e)
                    else:
                        self.send_mes("wrong1")
                else:
                    if self.server.account_login(e, p) == "success":
                        self.Id = e
                        self.send_mes("success")
                        self.server.online_clients.append(e)
                    else:
                        self.send_mes("wrong2")
            else:
                print("he had mistake")
                self.send_mes("wrong")





