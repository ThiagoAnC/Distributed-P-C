import time
import random
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

while True:
    mess = socket.recv()
    
    if "consume" in mess:
        socket.send_string("con")
        
    if "sleep" in mess:
        time.sleep(Random.random())

    socket.send_string("con")
