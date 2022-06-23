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
                    self.server.online_clients.remove(self.Id)
                    print("something went wrong")
                    print(e)
                    sys.exit()
                break
            else:
                length = "0" * zover
                try:
                    self.client_sock.send(length.encode("utf-8"))
                except Exception as e:
                    self.server.online_clients.remove(self.Id)
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
                self.server.online_clients.remove(self.Id)
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
            try:
                self.server.online_clients.remove(self.Id)
            except Exception as exc:
                print(exc)
            print(e)

    def send_tuple(self, tup):
        """
        here we are sending tuples
        :param tup: the tuple
        :return: NONE
        """
        x = ""
        print(tup)
        a = tup[0]
        b = tup[1]
        print(str(a))
        print(str(b))
        x += str(a) + "|"
        x += str(b)
        print(str(x))
        self.send_mes(str(x))

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
                print("something happend during recv")
                print(e)
                try:
                    self.server.online_clients.remove(self.Id)
                except Exception as e:
                    print(e)
                break
            print(self.server.active_clients.values())
            if data == "waiting":
                self.server.active_clients[self.Id] = self.address
                print(self.server.active_clients.keys())

            elif data[:3] == "try":
                print(data[4:0] + "hey day")
                key = data[4:]
                if key in self.server.active_clients.keys():
                    self.send_mes("exist")
                    print(self.server.active_clients[key])
                    self.send_tuple(self.server.active_clients[key])
                    del self.server.active_clients[key]
                    try:
                        self.server.online_clients.remove(key)
                    except Exception as e:
                        print(e)
                    try:
                        self.server.online_clients.remove(self.Id)
                    except Exception as e:
                        print(e)
                else:
                    self.send_mes("fail")


            elif data[:3] == "sql":
                after = data.split("|")
                e = after[2]
                p = after[3]
                print(p + " space " + e)
                if after[1] == "create":
                    rep = self.server.create_account(e, p)
                    if rep == "created":
                        self.Id = e
                        self.send_mes("created")
                        self.server.online_clients.append(e)
                        print(self.server.online_clients)
                    elif rep == "logged":
                        self.send_mes("logged")
                    else:
                        self.send_mes("wrong")
                else:
                    result = self.server.account_login(e, p)
                    print(result)
                    if result == "success":
                        self.Id = e
                        self.send_mes("success")
                        self.server.online_clients.append(e)
                    elif result == "logged":
                        self.send_mes("logged")
                    else:
                        self.send_mes("wrong")
            else:
                print("he had mistake")
                self.send_mes("wrong")





