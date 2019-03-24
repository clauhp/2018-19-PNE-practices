import socket
from P3.Seq_P3 import Seq


IP = "192.168.1.37"
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

        msg_out = ""

        for i in msg[1:]:
            if "count" in i:
                base = i[-1]
                count_base = seq.count()
                msg_out += count_base[base] + '\n'
            elif "perc" in i:
                base = i[-1]
                msg_out += seq.perc(base)
            elif i in to_do:
                msg_out += str(to_do[i]) + '\n'
            else:
                pass

            return msg_out


s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s_socket.bind((IP, PORT))

s_socket.listen(MAX_OPEN_REQUEST)

while True:
    (c_socket, address) = s_socket.accept()

    # -- Process the client request
    print("Attending client: {}".format(address))

    infosend = client_request(c_socket)
    c_socket.send(str.encode(infosend))

    c_socket.close()
