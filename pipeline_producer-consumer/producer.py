import pickle
import random
import sys
import time

import zmq

from environments import *

port = sys.argv[1] if len(sys.argv) > 1 else PRODUCER_PORT
task_count = int(sys.argv[2]) if len(sys.argv) > 2 else TASK_COUNT

context = zmq.Context()              
socket  = context.socket(zmq.PUSH)
socket.bind(f"tcp://*:{port}")

print(f"Producer listening on tcp://*:{port}")
time.sleep(1)

for task_id in range(1, task_count + 1):
    number = random.randint(1, 100)
    task = {
        "id": task_id,
        "operation": "square",
        "value": number,
    }
    print(f"Producer sending task {task_id}: square({number})")
    socket.send(pickle.dumps(task))
    time.sleep(0.2)

socket.send(pickle.dumps({"type": "STOP"}))
print("Producer finished")
