import zmq, time, pickle, sys
from environments import *

context = zmq.Context()
me = str(sys.argv[1]) if len(sys.argv) > 1 else "0"
r = context.socket(zmq.PULL)
p1 = f"tcp://{PRODUCER_HOST}:{PRODUCER_PORT}"
p2 = f"tcp://{PRODUCER_HOST}:{CONSUMER_PORT}"
r.connect(p1)
r.connect(p2)

print(f"{me} started")

while True:
    work = pickle.loads(r.recv())
    print(f"{me} received {work}")
    time.sleep(work[1]*0.01 if isinstance(work, tuple) else work * 0.01)
