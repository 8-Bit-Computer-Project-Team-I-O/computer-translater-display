
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 9999))
s.listen(1)
sock=socket.create_connection(("",9999))
conn, addr = s.accept()
while True:
    sock.send(b"test")
    data = conn.recv(4096)
    print(data.decode('utf-8'))
    print("Waiting for a message...")