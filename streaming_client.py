from vidstream import ScreenShareClient
from session_settings import *
import threading

class Streamer:
    def __init__(self, add):
        self.sender = ScreenShareClient(add, SHARE_SCREEN_PORT)
        self.t = threading.Thread(target=self.sender.start_stream)

    def stream(self):
        self.t.start()

    def stopping(self):
        self.sender.stop_stream()



