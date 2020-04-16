import requests
from work1.L2 import Location,WeatherElement
url='https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization=rdec-key-123-45678-011121314'
html_content = requests.get(url)
json_content=html_content.json()
print(json_content)
records=json_content.get('records')
location=records.get('location')
print(location)
# for i in range(len(location)):
#     print(location[i])
# for item in location:
#     print(item)
locations=[]
for l in location:
    location_site=Location()
    location_site.from_json(l)
    locations.append(location_site)
#怎麼import 另一個.py的變數