import requests
import json

API_KEY = '5E67F11C-DBE0-40CE-A72F-5F8F0EC566D7'

payload = {
    'api_key': API_KEY,
    'method': 'commodityCode',
    'format': 'json',
    'commodity': '4244000'
}

#Just pull the data in
response = requests.get('https://apps.fas.usda.gov/PSDOnlineDataServices/api/CommodityData/GetCommodityDataByYear?commodityCode=424000&marketYear=1990',params=payload)

#Get the status code - 200 is a good request
print('Status code is:')
print(response.status_code)

#Get the raw string data
print('Raw String Returned with default params is:')
print(response.json())

#Format it pretty
#print('Now formtat it pretty')
#def jprint(obj):
#    # create a formatted string of the Python JSON object
#    text = json.dumps(obj, sort_keys=True, indent=4)
#    print(text)

#jprint(response.json())

#Adding the parameters with coordinates of New York for each ISS passover
print('Adding the parameters lat/long for New York here for each ISS passover')

parameters = {
    "lat": 40.71,
    "lon": -74
}

#Now you don't have to type the line below
#http://api.open-notify.org/iss-pass.json?lat=40.71&lon;=-74

response = requests.get("https://apps.fas.usda.gov/PSDOnlineDataServices/api/CommodityData/GetWorldCommodityDataByYear?commodityCode=", params=parameters)

jprint(response.json())

#extract the pass times from our JSON object: 
pass_times = response.json()['response']
jprint(pass_times)
risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print(risetimes)


#extract the pass times from our JSON object and format the timestamp 
from datetime import datetime

times = []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)
    
