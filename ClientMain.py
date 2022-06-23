from ConnectionWitheServer import *
from Gui import *
from main_final_client import *
from controlled_client import *

class MainClient:
    def __init__(self):
        """
                starting the client.
                :return:
                """
        self.sessionWithServer = SessionWithServer()
        self.sessionWithServer.start()
        self.gui = MyAppFIRST(self, self.sessionWithServer)

    def starting_client(self, address, email):
        print("got to starting_client")
        self.f = FinalMainClient(address, email)

    def starting_server(self):
        print("got to starting_server")
        self.sessionWithServer.closing()
        self.gui.ending()
        self.h = Host()


if __name__ == "__main__":
    MainClient()
