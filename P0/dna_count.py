dnaseq = input("Introduce a sequence: ").upper()
print("\nTotal length:", len(dnaseq))

if not all(letter in "ACTG" for letter in dnaseq):
    print("Sorry, one of the letters you typed is not a DNA base")

else:
    for base in "ACTG":
        count = dnaseq.count(base)
        print(base, ":", count)
