from SessionWithServer import *
from Gui import *


def main():
    """
        starting the client.
        :return:
        """
    sessionWithServer = SessionWithServer()
    sessionWithServer.start()
    gui = MyApp(sessionWithServer)

if __name__ == "__main__":
    main()
