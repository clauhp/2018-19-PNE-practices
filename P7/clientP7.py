import http.client
import json
from P7.Seq_analyze import Seq

HOSTNAME = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/ENSG00000165879?content-type=application/json'
METHOD = "GET"

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT, None, headers)

r1 = conn.getresponse()

print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

msg = json.loads(text_json)
dna = msg['seq']
seq = Seq(dna)


print("Number of bases in the FRAT1 gene: ", seq.len())
print("In the FRAT1 gene there is a total number of {} T bases".format(seq.count('T')))

d_perc = {}

for base in ['A', 'C', 'T', 'G']:
    d_perc.update({base: seq.perc(base)})
    percentages = list(d_perc.values())
    dnabase = list(d_perc.keys())
    most_repeated = dnabase[percentages.index(max(percentages))]

print("The most repeated base is {}, with a percentage of {} %\n".format(most_repeated, d_perc[most_repeated]))
for base in d_perc:
    print(' The percentage of the {} base is {} %'.format(base, d_perc[base]))
