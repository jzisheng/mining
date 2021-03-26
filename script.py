import os
import json
import pprint as pp
import requests

with open('/home/zisheng/Documents/keys/et.json') as json_file:
    authd = json.load(json_file)
    pass

print(authd)

try:
    print("data loaded")
    data
    pass
except NameError:
    url = "https://api.f2pool.com/ethereum/zisheng"
    x = requests.get(url)
    data = x.json()
    pass

ss = []




      
for idx, d in enumerate(data['workers']):
    print(d[0],d[4]*1e-11)
    s = '{{ "fields": {{ "name":"{}", "mh/s":{} }} }}\n'.format(d[0], d[4]*1e-11)
    ss.append(s)

fields_str = (", ".join(ss))

    

jdata = ''' '{{ 
  "records": [ 
       {fields_str}
  ] 
}}' '''.format(fields_str=fields_str)

request = '''curl -v -X POST https://api.airtable.com/v0/appyiT4yESTgRhwvE/Table%201 \
  -H "Authorization: Bearer {}" \
  -H "Content-Type: application/json" \
  --data {}'''.format(authd['auth'], jdata)

# print(request)


#stream = os.popen(request)
#output = stream.read()
#print(output)
