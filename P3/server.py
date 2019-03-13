import socket
from P3.Seq_P3 import Seq


IP = "10.3.50.176"
PORT = 8082
MAX_OPEN_REQUEST = 5

# IT IS NOT FINISHED YET!!!


def client_request(cr):
    # Reading the message from the client
    msg = cr.recv(2048).decode('utf-8')

    if msg == '':
        cr.send(str.encode('ALIVE'))
        cr.close()

    else:
        msg = msg.split('\n')
        dnaseq = msg[0]
        seq = Seq(dnaseq)

        bases = ['A', 'C', 'T', 'G']

        for c in dnaseq:
            if c not in bases:
                cr.send(str.encode("ERROR"))
                cr.close()

        to_do = {"len": seq.len(), "complement": seq.complement(), "reverse": seq.reverse()}

        for i in msg[1:]:
            if "count" in i:
                msg_out = seq.count()
                base = i[-1]
                return msg_out[base]
            elif "perc" in i:
                base = i[-1]
                return seq.perc(base)
            elif i in to_do:
                msg_out = to_do[i]
                return msg_out
            else:
                pass


s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s_socket.bind((IP, PORT))

s_socket.listen(MAX_OPEN_REQUEST)

while True:
    (c_socket, address) = s_socket.accept()

    # -- Process the client request
    print("Attending client: {}".format(address))

    client_request(c_socket)

    c_socket.close()
