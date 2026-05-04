import zmq, time
from environments import *

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect(f"tcp://{PUB_HOST}:{PUB_PORT}")
socket.setsockopt(zmq.SUBSCRIBE, b"TIME")

for i in range(5):
    msg = socket.recv()
    print(msg.decode())
