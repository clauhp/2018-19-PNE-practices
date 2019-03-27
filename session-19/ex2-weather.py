import http.client
import json

# -- API information


def retrievewoeid(place):
    HOSTNAME = "www.metaweather.com"

    ENDPOINT = "/api/location/search/?query="
    ENDPOINT += place
    METHOD = "GET"

    # -- Here we can define special headers if needed
    headers = {'User-Agent': 'http-client'}

    # -- Connect to the server
    # -- NOTICE it is an HTTPS connection!
    conn = http.client.HTTPSConnection(HOSTNAME)

    # -- Send the request. No body (None)
    # -- Use the defined headers
    conn.request(METHOD, ENDPOINT, None, headers)

    # -- Wait for the server's response
    r1 = conn.getresponse()

    text_json = r1.read().decode("utf-8")
    conn.close()

    # -- Generate the object from the json file
    locationid = json.loads(text_json)

    return locationid


HOSTNAME = "www.metaweather.com"
citydata = retrievewoeid(input('Please introduce a capital of the world: '))
woeid = citydata[0]['woeid']
ENDPOINT = "/api/location/" + str(woeid) +'/'
METHOD = 'GET'

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT, None, headers)

r1 = conn.getresponse()

text_json = r1.read().decode("utf-8")
conn.close()

weather = json.loads(text_json)


time = weather['time']
temp0 = weather['consolidated_weather'][0]
temp = temp0['the_temp']

print()
print("Time: {}".format(time))
print("Current temp: {} degrees".format(temp))





# -- Read the response's body and close
# -- the connection
