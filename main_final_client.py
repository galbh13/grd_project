from assisted_final_client import *
from helping_gui import *

class FinalMainClient:
    def __init__(self, address):
        """
                starting the client.
                :return:
                """
        call = Call(address)
        call.start()
        gui = MyApp(call)


