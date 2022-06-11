import socket
from SessionWithClient import *
from server_setting import *
import grd_db


class Server:
    def __init__(self):
        self.db = grd_db.Users()
        #self.db.select_user_by_id()
        self.online_clients = []
        self.active_clients = {}
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((IP, PORT))
        server_socket.listen()
        print("we ready to go !!!")

        while True:
            connection, address = server_socket.accept()
            client = Client(self, connection, address)
            client.start()

    def create_account(self, email, password):
        if email in self.online_clients:
            return "try again"
        if self.db.account_exist(email):
            return "try again"
        else:
            self.db.insert_user(password, email)
            return "created"

    def account_login(self, email, password):
        if email in self.online_clients:
            return "fail"
        if self.db.is_account(email, password):
            return "success"
        return "fail"


if __name__ == '__main__':
    Server()
