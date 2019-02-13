from Bases import count_bases


# Main program

s1 = str(input("Please enter sequence 1: "))
s2 = str(input("Please enter sequence 2: "))
sequences = [s1,s2]
seq_number = 0

for s in sequences:
    for i in s:
        if i not in ["A", "G", "C", "T"]:
            # DNA sequences can only contain A,C, T, and G
            print("This is no a valid DNA sequence")
            exit(0)
    num_bases = count_bases(s)
    seq_number += 1
    # Calculate the total length
    tl = len(s)

    print("\nSequence {} is {} bases in length".format(seq_number,tl))

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