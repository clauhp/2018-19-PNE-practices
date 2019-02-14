class Seq:
    def __init__(self, strbases):
        self.strbases = strbases

    def len(self):
        return len(self.strbases)

    def complement(self):
        comp = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
        base_list = list(self.strbases)
        comp_list = []
        for i in base_list:
            comp_list.append(comp[i])
        comp_str = ''.join(comp_list)
        return comp_str
    def reverse(self):
        rev_seq= self.strbases[::-1]
        return rev_seq
    def count(self):
        num_a = 0
        num_c = 0
        num_t = 0
        num_g = 0

        tup_bases = ("A", "C", "G", "T")

        for i in self.strbases:
            if i == "A":
                num_a += 1
            elif i == "C":
                num_c += 1
            elif i == "T":
                num_t += 1
            elif i == "G":
                num_g += 1
        tup_num = (num_a, num_c, num_g, num_t)
        numcount = dict(zip(tup_bases, tup_num))

        return numcount

    def perc(self, base):
        length = len(self.strbases)
        numcount = self.count()
        if length > 0:
            perc = round(100.0 * numcount[base] / length, 1)
        else:
            perc = 0

        return perc




s1 = Seq(input("Please write a valid sequence: ").upper())

c1 = s1.complement()
l1 = s1.len()
r1 = s1.reverse()
n1 = s1.count()
p1 = s1.perc('C')

print (c1)
print (l1)
print (r1)
print (n1)
print (p1)
