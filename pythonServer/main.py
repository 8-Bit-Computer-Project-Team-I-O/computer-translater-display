
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 9999))
s.listen(1)
conn, addr = s.accept()
while True:
    print("Waiting for a message...")
    data = conn.recv(4096)
    print(data.decode('utf-8'))