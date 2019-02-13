class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        print("New sequence created!")

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases

    def len(self):
        return len(self.strbases)


# Main program
# Create an object of the class Seq
s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")

# Access the attribute strbases for printing the sequence
str1 = s1.strbases
str2 = s2.strbases

# Invoking the len methods for calculating the sequence length
# Notice the parenthesis: methods always have parenthesis
# but not the attributes!!

l1 = s1.len()
l2 = s2.len()

print("Sequence 1: {}".format(str1))
print("  Length: {}".format(l1))
print("Sequence 2: {}".format(str2))
print("  Length: {}".format(l2))
