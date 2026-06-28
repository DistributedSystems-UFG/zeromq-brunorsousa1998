import sys

import zmq

from environments import *


def handle_request(request):
  parts = request.strip().split(maxsplit=1)
  command = parts[0].upper() if parts else ""
  value = parts[1] if len(parts) > 1 else ""

  if command == "UPPER":
    return value.upper()
  if command == "LOWER":
    return value.lower()
  if command == "REVERSE":
    return value[::-1]
  if command == "COUNT":
    return f"chars={len(value)} words={len(value.split())}"
  if command == "HELP":
    return "Commands: UPPER, LOWER, REVERSE, COUNT, HELP, STOP"
  return "Unknown command. Use HELP to list commands."


port = sys.argv[1] if len(sys.argv) > 1 else SERVER_PORT

context = zmq.Context()
socket  = context.socket(zmq.REP)       # create reply socket
socket.bind(f"tcp://*:{port}")          # bind socket to all network interfaces

print(f"Server listening on tcp://*:{port}")

while True:
  message = socket.recv()               # wait for incoming message
  request = message.decode()

  if request.strip().upper() == "STOP":
    socket.send(b"Server stopped")
    break

  socket.send(handle_request(request).encode())

