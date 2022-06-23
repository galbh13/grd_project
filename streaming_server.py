from vidstream import StreamingServer
import threading
from session_settings import *



class Streamer:
    def __init__(self):
        self.reciever = StreamingServer("0.0.0.0", SHARE_SCREEN_PORT)
        self.t = threading.Thread(target=self.reciever.start_server)

    def stream(self):
        self.t.start()

    def stopping(self):
        self.reciever.stop_server()

