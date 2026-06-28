import sys

import zmq

from environments import *

host = sys.argv[1] if len(sys.argv) > 1 else SERVER_HOST
port = sys.argv[2] if len(sys.argv) > 2 else SERVER_PORT

context = zmq.Context()
socket  = context.socket(zmq.REQ)       # create request socket

socket.connect(f"tcp://{host}:{port}") # block until connected

print("Connected. Type HELP for commands or STOP to stop the server.")

while True:
  request = input("> ").strip()
  if not request:
    continue

  socket.send(request.encode())
  message = socket.recv()
  print(message.decode())

  if request.upper() == "STOP":
    break

