import random
import sys
import time

import zmq

from environments import *

port = sys.argv[1] if len(sys.argv) > 1 else PUB_PORT

context = zmq.Context()         
socket = context.socket(zmq.PUB)
socket.bind(f"tcp://*:{port}")

print(f"Publisher listening on tcp://*:{port}")

while True:
    messages = [
        f"TIME {time.asctime()}",
        f"TEMP {random.randint(20, 35)}C",
        f"HUMIDITY {random.randint(40, 90)}%",
        f"NEWS sample-news-{random.randint(1, 5)}",
    ]

    for message in messages:
        socket.send(message.encode())
        print(f"Published {message}")

    time.sleep(2)
