import json
import requests

...
api_token = '5E67F11C-DBE0-40CE-A72F-5F8F0EC566D7'
api_url_base = 'https://apps.fas.usda.gov/PSDOnlineDataServices/api/CommodityData/GetCommodityDataByYear?'
#commoditycode=4244000&year=1990&API_KEY=5E67F11C-DBE0-40CE-A72F-5F8F0EC566D7'
...
headers = {'Content-Type': 'application/json',
           'API_KEY': '5E67F11C-DBE0-40CE-A72F-5F8F0EC566D7',
           'commoditycode': '4244000',
           'year': '1990'
           }
...
print(api_url_base)
#def get_account_info():

    #api_url = '{0}account'.format(api_url_base)
#print(api_url)
response = requests.request(api_url_base, headers=headers)
print(response)

##if response.status_code == 200:
##    return json.loads(response.content.decode('utf-8'))
##else:
##    print(response)
##    print(api_url)
##    return None
...
print(get_account_info())
account_info = get_account_info()
