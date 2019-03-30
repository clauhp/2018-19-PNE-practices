import http.client
import json

# -- API information


def retrievewoeid(place):

    HOSTNAME1 = "www.metaweather.com"

    ENDPOINT1 = "/api/location/search/?query="
    ENDPOINT1 += place
    METHOD1 = "GET"

    # -- Here we can define special headers if needed
    headers = {'User-Agent': 'http-client'}

    # -- Connect to the server
    # -- NOTICE it is an HTTPS connection!
    conn = http.client.HTTPSConnection(HOSTNAME1)

    # -- Send the request. No body (None)
    # -- Use the defined headers
    conn.request(METHOD1, ENDPOINT1, None, headers)

    # -- Wait for the server's response
    r1 = conn.getresponse()

    text_json = r1.read().decode("utf-8")
    conn.close()

    # -- Generate the object from the json file
    locationid = json.loads(text_json)

    return locationid


HOSTNAME = "www.metaweather.com"
citydata = retrievewoeid(input('Please introduce a capital of the world: '))


try:

    woeid = citydata[0]['woeid']
    ENDPOINT = "/api/location/" + str(woeid) + '/'
    METHOD = 'GET'

    headers = {'User-Agent': 'http-client'}

    conn = http.client.HTTPSConnection(HOSTNAME)

    conn.request(METHOD, ENDPOINT, None, headers)

    r1 = conn.getresponse()

    text_json = r1.read().decode("utf-8")
    conn.close()

    weather = json.loads(text_json)

    time = weather['time'].split('T')[1].split('.')
    temp0 = weather['consolidated_weather'][0]
    temp = temp0['the_temp']
    sunset = weather['sun_set'].split('T')[1].split('.')

    print()
    print("Time: {}".format(time[0]))
    print("Temperature: {} ºC".format(temp))
    print('Sun set time: {}'.format(sunset[0]))

except IndexError:
    print("Sorry, there's no info about that city")
