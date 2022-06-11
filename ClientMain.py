from ConnectionWitheServer import *
from Gui import *

class MainClient:
    def __init__(self):
        """
                starting the client.
                :return:
                """
        sessionWithServer = SessionWithServer()
        sessionWithServer.start()
        gui = MyApp(sessionWithServer)

    def starting(self):
        pass



if __name__ == "__main__":
    MainClient()
