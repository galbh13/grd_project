from vidstream import ScreenShareClient
import client_setting
import threading



class Streamer:
    def __init__(self, add, port):
        self.sender = ScreenShareClient(add, port)
        t = threading.Thread(target=self.sender.start_stream)
        t.start()

    def stopping(self):
        self.sender.stop_stream()

