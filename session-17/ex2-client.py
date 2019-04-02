# -- Example of a client that uses the HTTP.client library
# -- for requesting a JSON object and printing their
# -- contents
import http.client
import json
import termcolor

PORT = 8001
SERVER = 'localhost'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
conn.request("GET", "/listusers")

r1 = conn.getresponse()

print("Response received!: {} {}\n".format(r1.status, r1.reason))

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
person = json.loads(data1)

print("CONTENT: ")

print("Total people in the database: {}".format(len(person['people'])))

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