def count_bases(seq):
    #counts the number each base appears
    num_a = 0
    num_c = 0
    num_t = 0
    num_g = 0

    for i in seq:
        if i == "A":
            num_a += 1
        elif i == "C":
            num_c += 1
        elif i == "T":
            num_t += 1
        elif i == "G":
            num_g += 1

    bases = ["A", "C", "T", "G"]
    list_count = [num_a, num_c, num_t, num_g]

    #dictionary of the base and the number of times it appears
    dict_bases = dict(zip(bases, list_count))
    return dict_bases