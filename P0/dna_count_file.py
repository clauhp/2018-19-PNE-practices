print('Counting the total number of bases in a DNA sequence and the number of each different base from a text file')

f = open('dna_count_file.txt', 'r')
seq = f.read()
print('the length of the sequence is ', len(seq))

T = seq.count('T')
A = seq.count('A')
G = seq.count('G')
C = seq.count('C')

print('A:', A)
print('C:', C)
print('T:', T)
print('G:', G)
f.close()