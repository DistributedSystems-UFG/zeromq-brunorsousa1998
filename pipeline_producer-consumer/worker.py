import pickle
import sys
import time

import zmq

from environments import *


producer_host = sys.argv[1] if len(sys.argv) > 1 else PRODUCER_HOST
producer_port = sys.argv[2] if len(sys.argv) > 2 else PRODUCER_PORT
worker_port = sys.argv[3] if len(sys.argv) > 3 else WORKER_PORT
worker_id = sys.argv[4] if len(sys.argv) > 4 else "worker-1"

context = zmq.Context()

receiver = context.socket(zmq.PULL)
receiver.connect(f"tcp://{producer_host}:{producer_port}")

sender = context.socket(zmq.PUSH)
sender.bind(f"tcp://*:{worker_port}")

print(f"{worker_id} receiving from tcp://{producer_host}:{producer_port}")
print(f"{worker_id} publishing results on tcp://*:{worker_port}")

while True:
    task = pickle.loads(receiver.recv())

    if task.get("type") == "STOP":
        sender.send(pickle.dumps(task))
        print(f"{worker_id} stopped")
        break

    value = task["value"]
    result = value * value
    processed = {
        **task,
        "result": result,
        "worker": worker_id,
    }

    print(f"{worker_id} processed task {task['id']}: {value} -> {result}")
    time.sleep(value * 0.01)
    sender.send(pickle.dumps(processed))
