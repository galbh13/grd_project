import pyaudio
import threading

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

class VoiceCall(threading.Thread):
    def __init__(self, client, address):
        threading.Thread.__init__(self)
        self.sock = client
        self.address = address
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024
        self.recording()
        self.audio = pyaudio.PyAudio()

    def callback(self, in_data, frame_count, time_info, status):
        self.sock.send(in_data)
        return None, pyaudio.paContinue

    def recording(self):
        recording_stream = self.audio.open(format=FORMAT,
                                      channels=CHANNELS,
                                      rate=RATE,
                                      input=True,
                                      frames_per_buffer=CHUNK,
                                      stream_callback=self.callback,
                                      start=False)

        self.record = recording_stream.start_stream

        self.playing_stream = self.audio.open(format=FORMAT,
                                    channels=CHANNELS,
                                    rate=RATE,
                                    output=True,
                                    frames_per_buffer=CHUNK)

    def play(self):
        while True:
            self.playing_stream.write(self.sock.recv(CHUNK))

    def run(self):
        self.record()
        self.play()


