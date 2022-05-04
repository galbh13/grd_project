import socket, pickle, struct, cv2
import imutils




class Controlled:
    def __init__(self):
        self. my_server = socket.socket()
        self.my_server.bind(('0.0.0.0', 50000))
        self.my_server.listen()
        client_socket, client_adress = self.my_server.accept()
        print('GOT CONNECTION FROM:', client_adress)
        while True:
            if client_socket:
                vid = cv2.VideoCapture(0)
                while (vid.isOpened()):
                    img, frame = vid.read()
                    frame = imutils.resize(frame, width=320)
                    a = pickle.dumps(frame)  # serialize frame to bytes
                    message = struct.pack("Q", len(a)) + a
                    try:
                        client_socket.sendall(message)
                    except Exception as e:
                        print(e)
                        raise Exception(e)
                    cv2.imshow('TRANSMITTING VIDEO', frame)  # will show video frame on server side.
                    key = cv2.waitKey(1) & 0xFF
                    if key == ord('q'):
                        client_socket.close()

    def start_call(self, client):
        pass


c = Controlled()



