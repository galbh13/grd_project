import socket


class Controlled:
    def __init__(self, path):
        my_server = socket.socket()
        my_server.bind(path)
        my_server.listen()
        client_socket, client_adress = my_server.accept()


