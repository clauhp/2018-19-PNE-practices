import socket

# SERVER IP, PORT
PORT = 8080
IP = "10.3.53.94"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

msg = """GATTACA
complement
reverse
countT"""

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send the request message to the server
s.send(str.encode(msg))

# Receive the servers response
response = s.recv(2048).decode()

# Print the server's response
print("Response: {}".format(response))
s.close()