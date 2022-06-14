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
        sessionWithServer = SessionWithServer()
        sessionWithServer.start()
        gui = MyApp(self, sessionWithServer)

    def starting_client(self, address, email):
        f = FinalMainClient(address, email)

    def starting_server(self):
        s = Host()



if __name__ == "__main__":
    MainClient()
