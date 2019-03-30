
import http.client
import json

# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINT1 = "/jokes/count"
ENDPOINT2 = "/categories"
ENDPOINT3 = "/jokes/random"
allendpoints = [ENDPOINT1, ENDPOINT2, ENDPOINT3]
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standard one
# -- will be used
conn = http.client.HTTPConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers

for endpoint in allendpoints:
    conn.request(METHOD, endpoint, None, headers)

    # -- Wait for the server's response
    r1 = conn.getresponse()

    # -- Print the status
    print()
    print("Response received: ", end='')
    print(r1.status, r1.reason)

    # -- Read the response's body and close
    # -- the connection
    text_json = r1.read().decode("utf-8")
    conn.close()

    # -- Optionally you can print the
    # -- received json file for testing
    # print(text_json)

    # -- Generate the object from the json file
    jokes = json.loads(text_json)
    rec_url = jokes['value']

    if type(rec_url) is int:
        print("The number of jokes is", rec_url)
    elif type(rec_url) is list:
        print("The jokes categories are", rec_url[0], "and", rec_url[1])
    else:
        print("A Chuck Norris joke: {}".format(rec_url['joke']))

