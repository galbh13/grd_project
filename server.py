import socket
from session_with_client import *
from server_setting import *

class Server:
    def __init__(self):
        self.clients = {}
        self.active_clients = {}
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((IP, PORT))
        server_socket.listen()
        print("we ready to go !!!")

        while True:
            connection, address = server_socket.accept()
            client = Client(self, connection, address)
            client.start()
            self.clients[client.Id] = client


if __name__ == '__main__':
    Server()


