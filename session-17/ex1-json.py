import json
import termcolor

# -- Open the json file
f = open("ex1-person.json", 'r')

# Read the data from the file
# Now person is a dictionary with all the information
person = json.load(f)

print('Total people in the database: {}'.format(len(person['people'])))

# Print the information in the object
for individual in person['people']:
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(individual['Firstname'], individual['Lastname'])

    termcolor.cprint("Age: ", 'green', end="")
    print(individual['age'])

    # Get the phoneNumber list
    phoneNumbers = individual['phonenumber']

    # Print the number of elements int the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    # Print all the numbers
    for i, num in enumerate(phoneNumbers):
        termcolor.cprint("  Phone {}:".format(i), 'blue')

        # The element num contains 2 fields: number and type
        termcolor.cprint("    Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("    Number: ", 'red', end='')
        print(num['number'])