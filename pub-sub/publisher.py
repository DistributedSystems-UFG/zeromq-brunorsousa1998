import zmq, time
from environments import *

context = zmq.Context()         
socket = context.socket(zmq.PUB)
socket.bind(f"tcp://*:{PUB_PORT}")

while True:
    time.sleep(5)
    t = "TIME " + time.asctime()
    socket.send(t.encode())
