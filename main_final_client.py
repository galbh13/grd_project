from assisted_final_client import *

class FinalMainClient:
    def __init__(self, address, email):
        """
                starting the client.
                :return:
                """
        call = Call(address="127.0.0.1", email="gal@gmail.com")
        call.start()


