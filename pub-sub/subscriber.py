import sys

import zmq

from environments import *

host = sys.argv[1] if len(sys.argv) > 1 else PUB_HOST
topic = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_TOPIC
port = sys.argv[3] if len(sys.argv) > 3 else PUB_PORT

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect(f"tcp://{host}:{port}")
socket.setsockopt(zmq.SUBSCRIBE, topic.encode())

print(f"Subscribed to {topic} at tcp://{host}:{port}")

for i in range(5):
    msg = socket.recv()
    print(msg.decode())
