import json

with open('0111000.1990.json') as json_file:
    data = json.load(json_file)
    for p in data:
        #print('CommodityCode: ' + p['CommodityCode'])
        #print('CommodityDescription: ' + p['CommodityDescription'])
        #print('CountryCode: ' + p['CountryCode'])
        #print('CountryName: ' + p['CountryName'])
        #print('MarketYear: ' + p['MarketYear'])
        #print('CalendarYear: ' + p['CalendarYear'])
        print('Month: ' + str(p['Month']))
        #print('AttributeId: ' + str(p['AttributeId']))
        #print('AttributeDescription: ' + p['AttributeDescription'])
        #print('UnitId: ' + str(p['UnitId']))
        #print('UnitDescription: ' + p['UnitDescription'])
        #print('Value: ' + str(p['Value']))
        print('')
