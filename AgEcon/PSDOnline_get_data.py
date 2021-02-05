# Python 3 Created:2/4/21 By: EJC

import requests
import json

headers = {
    'API_KEY': 'C8A31F5C-ABE3-4466-B46F-6A970A34298D',
    'Accept': 'application/json'
}

commodities = ["0111000", "0113000", "0114200", "0114300", "0224200", "0230000", "0240000", "0410000", "0422110", "0430000", "0440000", "0451000", "0452000", "0459100", "0459200", "0459900", "0612000", "0813100", "0813101", "0813200", "0813300", "0813500", "0813600", "0813700", "0813800", "0814200", "2221000", "2222000", "2222001", "2223000", "2224000", "2226000", "2231000", "2232000", "4232000", "4232001", "4233000", "4234000", "4235000", "4236000", "4239100", "4242000", "4243000", "4244000"]

for c in commodities:
    for y in range(1990, 2021):
        try:
            query = {'commodityCode': c, 'marketYear': y}

            url = requests.get('https://apps.fas.usda.gov/PSDOnlineDataServices/api/CommodityData/GetCommodityDataByYear', headers=headers, params=query)

            data = (url.json())

            with open(str(c) + '.' + str(y) + '.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

