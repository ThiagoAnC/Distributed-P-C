import zmq

queue = []
condition = 0

context = zmq.Context()

prod = context.socket(zmq.REQ)
prod.connect("tcp://localhost:5555")

cons = context.socket(zmq.REQ)
cons.connect("tcp://localhost:5556")


prod.send_string ("start")
mess = prod.recv()
if "OK" in mess:
    queue.append(1)

while True:
    message = prod.recv()
    message1 = cons.recv()

    if "prod" in message:
        if (condition == 0) and (not len(queue) == 10):
            condition = 1
            queue.append(1)
            print ("Produced")
            condition = 0
        else:
            prod.send_string("sleep")
            cons.send_string("consume")
        
    elif "con" in message1:
        if (condition == 0) and (queue):
            condition = 1
            queue.pop(0)
            print ("Consumed")
            condition = 0
        else:
            cons.send_string("sleep")
            prod.send_string("produce")            
            
