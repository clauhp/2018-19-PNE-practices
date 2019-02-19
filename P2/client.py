import socket

IP = "192.168.1.39"
PORT = 8080

class Seq:
    def __init__(self, strbases):
        self.strbases = strbases

    def complement(self):
        comp = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
        base_list = list(self.strbases)
        comp_list = []                      #empty list to store the complementary bases
        for i in base_list:
            comp_list.append(comp[i])
        comp_str = ''.join(comp_list)       #transforms the list onto a string
        return comp_str

    def reverse(self):
        rev_seq = self.strbases[::-1]
        return rev_seq



# Loop to forever go on asking for a sequence
conection = True
while conection:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    s1 = Seq(input("Please, introduce a valid DNA sequence: ").upper())
    rs1 = Seq(s1.reverse())
    c_rs1 = rs1.complement()

    # We send the reverse complement sequence
    s.send(str.encode(c_rs1))

    s.close()
