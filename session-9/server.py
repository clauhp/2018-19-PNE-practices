import socket

PORT = 8080
IP = "212.128.253.80"
MAX_OPEN_REQUEST = 5

def process_client(cs):

    #Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")

    print("Message from te client: {}".format(msg))

    cs.send (str.encode(msg))
    # -- Close the socket
    cs.close()


# create a socket for connecting to the clients
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))


while True:
    print("Waiting for connections at: {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    #-- Process the client request
    print("Attending client: {}".format(address))

    process_client(clientsocket)