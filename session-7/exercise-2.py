import socket

# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes
condition = True
while condition:
    IP = "212.128.253.64"
    PORT = 8086
    # First, create the socket
    # We will always use this parameters: AF_INET y SOCK_STREAM
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))


    s.send(str.encode(input("Please enter a string: ")))


s.close()