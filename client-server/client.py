import multiprocessing #-
import zmq
from time import sleep #-
from environments import *
                       
context = zmq.Context()
socket  = context.socket(zmq.REQ)       # create request socket

socket.connect(f"tcp://{SERVER_HOST}:{SERVER_PORT}") # block until connected
socket.send(b"Hello world")             # send message
message = socket.recv()                 # block until response
socket.send(b"STOP")                    # tell server to stop
print(message.decode())                 # print result

