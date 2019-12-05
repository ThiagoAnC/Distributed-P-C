import random
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    mess = socket.recv()

    if "start" in mess:
        socket.send_string("OK")
        
    if "produce" in mess:
        socket.send_string("prod")
        
    if "sleep" in mess:
        time.sleep(Random.random())

    socket.send_string("prod")
