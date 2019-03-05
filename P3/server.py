import socket

IP = "192.168.1.39"
PORT = 8080
MAX_OPEN_REQUEST = 5

# IT IS NOT FINISHED YET!!!

def client_request(cr):
    # Reading the message from the client
    msg = cr.recv(2048).decode("utf-8")

    if msg == '':
        answer = 'ALIVE'
        cr.send(str.encode(answer))
    else:
        pass



s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s_socket.bind((IP, PORT))

s_socket.listen(MAX_OPEN_REQUEST)

while True:
    c_socket, address = s_socket.accept()

    #-- Process the client request
    print("Attending client: {}".format(address))

    client_request(s_socket)

    #FGHJKLLIU