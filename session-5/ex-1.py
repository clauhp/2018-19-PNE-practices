def count_a(seq):
    """Counting the number of As in a sequence
    """
    # Counter for As

    result = 0

    for b in seq:
        if b == 'A':
            result += 1

    #Return the results
    return result

# Main program
s = input("Please enter the sequence: ")
na = count_a(s)
print("The number of As is: {}".format(na))

# Claculate the total sequence lenght
tl = len(s)

# Calculate the percentage of As in the sequence

if tl>0:
    perc = round(100.0*na / tl, 1)
else:
    perc = 0

print("The total length is: {}".format(tl))
print ("The total percentage of A's is {}%".format(perc))
