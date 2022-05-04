import socket, pickle, struct
import cv2

class Controlling:
    def __init__(self):
        try:
            self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.my_socket.connect(('127.0.0.1', 50000))
        except Exception as e:
            print("we couldn't connect")
            print(e)
        data = b""
        payload_size = struct.calcsize("Q")
        while True:
            while len(data) < payload_size:
                packet = self.my_socket.recv(4 * 1024)
                if not packet:
                    break
                data += packet
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("Q", packed_msg_size)[0]
            print(msg_size)
            while len(data) < msg_size:
                data += self.my_socket.recv(4 * 1024)
            frame_data = data[:msg_size]
            data = data[msg_size:]
            frame = pickle.loads(frame_data)
            cv2.imshow("RECEIVING VIDEO", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break


h = Controlling()
