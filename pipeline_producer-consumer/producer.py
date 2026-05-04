import zmq, time, pickle, sys, random
from environments import *

context = zmq.Context()              
socket  = context.socket(zmq.PUSH)
socket.bind(f"tcp://{PRODUCER_HOST}:{PRODUCER_PORT}")
    
for i in range(100):
    workload = random.randint(1, 100)
    print(f"Producer sending workload item of size {workload}")
    socket.send(pickle.dumps(workload))
