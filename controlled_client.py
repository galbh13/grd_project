import socket
from controlled_client_assisted import *
from get_help_gui import *


class Host:
    def __init__(self):
        sc = ServerCall()
        sc.start()
        g = MyAppServer(sc)



