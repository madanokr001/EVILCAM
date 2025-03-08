import socket
import cv2
import numpy as np
import time

def connect():
    ip = "192.168.55.178"
    port = 4444
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    return client

def send(client):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        _, encoded = cv2.imencode('.jpg', frame)
        data = np.array(encoded).tobytes()
        size = len(data).to_bytes(4, byteorder='big')
        client.sendall(size + data)
        time.sleep(2)
    cap.release()
    client.close()

if __name__ == "__main__":
    client = connect()
    send(client)