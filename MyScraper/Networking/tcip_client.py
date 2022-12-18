import socket


s = socket.socket()

s.connect(('localhost', 4000))

file_name = input("Enter file name:")
# msg = s.recv(1024)

# print("mesg is ", msg.decode())

s.send(file_name.encode())
content = s.recv(1024)

print(content.decode())
s.close()