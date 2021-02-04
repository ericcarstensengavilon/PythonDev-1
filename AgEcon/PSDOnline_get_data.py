import requests
import json

headers = {
    'API_KEY': 'C8A31F5C-ABE3-4466-B46F-6A970A34298D',
    'Accept': 'application/json'
}

#years = ["1990", "1991", "1992", "1993", "1994", "1995","1996", "1997", "1998", "1999"]

#years = 1990

for y in range(1990, 2021):
    query = {'commodityCode': 4244000, 'marketYear': y}

    url = requests.get('https://apps.fas.usda.gov/PSDOnlineDataServices/api/CommodityData/GetCommodityDataByYear', headers=headers, params=query)

    data = (url.json())

    with open('data.' + str(y) + '.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

