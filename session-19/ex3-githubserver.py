import http.client
import json

GITHUB_ID = input("Please introduce a github user: ")
hostname = "api.github.com"
METHOD = "GET"

def getrepos(name):

    endpoint = "/users/" + str(GITHUB_ID) + '/repos'

    # -- Here we can define special headers if needed
    headers = {'User-Agent': 'http-client'}

    conn = http.client.HTTPSConnection(hostname)

    # -- Use the defined headers
    conn.request(METHOD, endpoint, None, headers)

    # -- Wait for the server's response
    r1 = conn.getresponse()

    text_json = r1.read().decode("utf-8")
    conn.close()

    allrepos = json.loads(text_json)
    rep_names = []

    for element in allrepos:
        rep_names.append(element['name'])

    return rep_names


ENDPOINT = "/users/" + str(GITHUB_ID)

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(hostname)

conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

text_json2 = r1.read().decode("utf-8")
conn.close()

user = json.loads(text_json2)

name = user['name']

print()
print("Name: {}".format(name))
print('Repos list: {}'.format(getrepos(GITHUB_ID)))