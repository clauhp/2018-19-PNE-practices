FILENAME = "mynotes.txt"

# -- Open the file for reading
f = open(FILENAME, 'r')

# -- Read the content
contents = f.read()

print("File: {}".format(f.name))
print("{}".format(contents))

# -- Closing the file
f.close()

# -- Open again for adding
f = open(FILENAME, "a")

# -- write some information to the file
f.write("Helllo!!!! just writing into the file!\n Have a nice day\n")

f.close()

print("End")