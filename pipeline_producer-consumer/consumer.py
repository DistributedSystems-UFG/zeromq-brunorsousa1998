import pickle
import sys

import zmq

from environments import *

context = zmq.Context()
worker_host = sys.argv[1] if len(sys.argv) > 1 else WORKER_HOST
worker_port = sys.argv[2] if len(sys.argv) > 2 else WORKER_PORT

receiver = context.socket(zmq.PULL)
receiver.connect(f"tcp://{worker_host}:{worker_port}")

print(f"Consumer connected to tcp://{worker_host}:{worker_port}")

while True:
    message = pickle.loads(receiver.recv())

    if message.get("type") == "STOP":
        print("Consumer stopped")
        break

    print(
        f"Task {message['id']} processed by {message['worker']}: "
        f"{message['operation']}({message['value']}) = {message['result']}"
    )
