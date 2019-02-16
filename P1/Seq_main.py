from Seq import Seq



s1 = Seq(input("Please introduce a first sequence: ").upper())
s2 = Seq(input("Please, introduce a second sequence: ").upper())
s3 = Seq(s1.complement())
s4 = Seq(s3.reverse())



sequences = s1, s2, s3, s4
n = 1
bases = ["A","C","G","T"]


for s in sequences:
    print("\nSequence {}: {}".format(n,s.strbases), "\n   Length: {}".format(s.len()), "\n   Bases count: ", end='')
    d_count = s.count()
    print('A:{},'.format(d_count['A']), 'C:{},'.format(d_count['C']), 'G:{},'.format(d_count['G']), 'T:{}'.format(d_count['T']), '\n   Bases percentage: ', end='')
    print('A:{}%,'.format(s.perc('A')), 'C:{}%,'.format(s.perc('C')), 'G:{}%,'.format(s.perc('G')), 'T:{}%'.format(s.perc('T')))
    n += 1