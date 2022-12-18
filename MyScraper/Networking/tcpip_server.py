import socket

host = 'localhost'
port = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
s.listen(1)

print("Server listening at port "+ str(port))

c, addr = s.accept()

print("connection from: ", str(addr))

c.send(b"Hello")
c.close()