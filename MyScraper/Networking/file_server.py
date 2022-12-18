import socket

print("running file server")
host = 'localhost'
port = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
s.listen(1)

print("Server listening at port "+ str(port))

c, addr = s.accept()

print("connection from: ", str(addr))

#c.send(b"Hello choose file")
file_name = c.recv(1024)

with open(file_name, 'rb') as f:
    content = f.read()
    c.send(content)

c.close()