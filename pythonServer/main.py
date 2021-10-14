import json
import socket
import interpreter

def set_up_connection(source):
    # establish the base variables
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 9999))
    s.listen(1)
    # if BE architecture, we're going to get stuff from the GPIO pins, then do the interpretation in a forever loop. Add some sort of exception later
    if (source=="True"):
        sock = socket.create_connection(("", 9999))
        conn, addr = s.accept()
        while True:
            sock.send(b"test")
            data = conn.recv(4096)
            allValues = data.decode('utf-8').split('#')
            print(allValues)
    # same as BE architecture except we're getting the connection from a Java program
    else:
        conn, addr = s.accept()
        while True:
            data = conn.recv(4096)
            allValues = data.decode('utf-8').split('#')
            interpreter.interpret(allValues)


# make a file reader
f = open('data.json', )
# load the json values into a variable
json_vals = json.load(f)
set_up_connection(json_vals["BE Architecture"])
