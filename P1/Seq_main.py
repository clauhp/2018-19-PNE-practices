from Seq import Seq



s1 = Seq(input("Please introduce a first sequence: ").upper())
s2 = Seq(input("Please, introduce a second sequence: ").upper())
s3 = s1.complement()
s4 = s3.reverse()

sequences = s1, s2, s3, s4
n = 1

for s in sequences:
    print("Sequence {}: {}".format(n,s1), "\n   Length: {}".format(s.len()))






