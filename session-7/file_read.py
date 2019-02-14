# -- Filename to read
NAME = "mynotes.txt"

# -- Open the file
myfile = open(NAME, 'r')

# -- myfile is an object!!! Let's see what it has inside

print("Print: file opened: {}".format(myfile.name))

# -- Read the whole file into a string
contents = myfile.read()

print("The file contents are: {}".format(contents))

# -- Close the file
myfile.close()