import http.client
import json

PORT = 8000
HOSTNAME = "rest.ensembl.org"
METHOD = "GET"
endpoint = '/sequence/id/ENSG00000165879'
content_type = 'text/html'

conn = http.client.HTTPConnection(HOSTNAME)


headers = {"Content-Type": content_type}

conn.request(METHOD, endpoint, None, headers)

r1 = conn.getresponse()

print()
print("Response received: ", end='')
print(r1.status, r1.reason)


answer = r1.read().decode("utf-8")
conn.close()


print(dna)
