from vidstream import StreamingServer
import threading
import server_setting



class Streamer:
    def __init__(self):
        self.reciever = StreamingServer("0.0.0.0", 6123)
        t = threading.Thread(target=self.reciever.start_server)
        t.start()

    def stopping(self):
        self.reciever.stop_server()
