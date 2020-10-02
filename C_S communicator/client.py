import zmq

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

while True:
    #Here the message depends on the question, even the length of the message will vary
    question = input()
    socket.send_string (question)

    #Here gets the reply and shows it
    message = socket.recv()
    print("...")

    if "stop" in question:
        #Server will halt when it receives the "stop" message
        socket.send_string ("stop")
        break