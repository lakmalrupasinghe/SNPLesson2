import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect

# connect to the server on local computer
target = 'www.google.com'
port = 80

s.connect((target, port))

req = "GET / HTTP/1.1\r\nHost: " + target + "\r\n\r\n"

response = s.send(req.encode())

print(s.recv(4096).decode())








