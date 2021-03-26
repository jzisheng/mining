from datetime import datetime
import os
import json
import pprint as pp
import requests

with open('/home/zisheng/Documents/keys/et.json') as json_file:
    authd = json.load(json_file)
    pass

try:
    print("[data loaded]")
    data
    pass
except NameError:
    url = "https://api.f2pool.com/ethereum/zisheng"
    x = requests.get(url)
    data = x.json()
    pass

ss = []  
for idx, d in enumerate(data['workers']):
    s = '"{}":{}'.format(d[0],d[4]*1e-11)
    ss.append(s)
now = datetime.now()
fields_str = (",".join(ss))
fields_str = '{{"fields":{{ "datetime":"{}",{} }} }}'.format(now.strftime("%d/%m/%Y %H:%M:%S"),fields_str)

jdata = ''' '{{ 
  "records": [ 
       {fields_str}
  ] 
}}' '''.format(fields_str=fields_str)
request = '''curl -v -X POST https://api.airtable.com/v0/appyiT4yESTgRhwvE/Table%201 \
  -H "Authorization: Bearer {}" \
  -H "Content-Type: application/json" \
  --data {}'''.format(authd['auth'], jdata)

print(request)


stream = os.popen(request)
output = stream.read()
print(output)
