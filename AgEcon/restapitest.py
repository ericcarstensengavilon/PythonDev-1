import requests

API_KEY = '5E67F11C-DBE0-40CE-A72F-5F8F0EC566D7'

#payload = {
    #'api_key': API_KEY,
    #'format': 'json',
    #'commodity': '4244000',
    #'year' : '1990'
    #}
    
##r = requests.get('https://apps.fas.usda.gov/PSDOnlineDataServices/api/CommodityData/GetCommodityDataByYear', params=payload)
##r.json()
##r.status_code


#print(r.url)

#print(r)

url = 'https://apps.fas.usda.gov/PSDOnlineDataServices/api/CommodityData/GetCommodityDataByYear?api_key=5E67F11C-DBE0-40CE-A72F-5F8F0EC566D7&commodity=4244000&year=1990'
headers = {'api_key': API_KEY,
           'commodity': '4244000',
           'year' : '1990'
           }
r = requests.get(url, headers=headers, allow_redirects=False)

response = r.json()
print(r.json())

print(r.url)
print(r)

################

#url = "https://apps.fas.usda.gov/PSDOnlineDataServices/api/CommodityData/GetCommodityDataByYear"

#headers = {"Accept": "application/json", "API_KEY": "5E67F11C-DBE0-40CE-A72F-5F8F0EC566D7", 'CommodityCode': '4244000', 'MarketYear': '1990'}

#response = requests.get(url, headers=headers)

#print(url)
#print (response.json())
