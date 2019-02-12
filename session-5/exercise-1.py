def count_bases(seq):
    #counts the number each base appears
    num_a = 0
    num_c = 0
    num_t = 0
    num_g = 0

    bases = ["A", "C", "T", "G"]


    for i in seq:
        if i == "A":
            num_a += 1
        elif i == "C":
            num_c += 1
        elif i == "T":
            num_t += 1
        elif i == "G":
            num_g += 1

    list_count = [num_a, num_c, num_t, num_g]

    #dictionary of the base and the number of times it appears
    dict_bases = dict(zip(bases, list_count))
    return dict_bases


# Main program

s = str(input("Please enter a valid sequence: "))
num_bases = count_bases(s)

for i in s:
    if i not in ["A", "G", "C", "T"]:
        # DNA sequences can only contain A,C, T, and G
        print("This is no a valid DNA sequence")
        exit(0)

# Calculate the total length
tl = len(s)

print("This sequence is {} bases in length".format(tl))

if tl > 0:
    perc_a = round(100.0 * num_bases["A"]/tl, 1)
    perc_c = round(100.0 * num_bases["C"]/tl, 1)
    perc_t = round(100.0 * num_bases["T"]/tl, 1)
    perc_g = round(100.0 * num_bases["G"]/tl, 1)
    # A
    print("Base A: \n  Counter:", num_bases["A"], "\n  Percentage:", perc_a)
    print("Base C: \n  Counter:", num_bases["C"], "\n  Percentage:", perc_c)
    print("Base T: \n  Counter:", num_bases["T"], "\n  Percentage:", perc_t)
    print("Base G: \n  Counter:", num_bases["G"], "\n  Percentage:", perc_g)
else:
    perc = 0
    print("Base A: \n  Counter:", num_bases["A"], "\n  Percentage:", perc)
    print("Base C: \n  Counter:", num_bases["C"], "\n  Percentage:", perc)
    print("Base T: \n  Counter:", num_bases["T"], "\n  Percentage:", perc)
    print("Base G: \n  Counter:", num_bases["G"], "\n  Percentage:", perc)


