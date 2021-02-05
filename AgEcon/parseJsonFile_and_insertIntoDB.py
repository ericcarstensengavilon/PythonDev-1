import json
import pyodbc
import datetime

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=TEDSQL050;'
                      'Database=AgEcon;'
                      'Trusted_Connection=yes;'
                      'Driver={ODBC Driver 17 for SQL Server};')


# read file
with open('0111000.1990.json') as json_file:
    data = json.load(json_file)

    #set record counter
    r = 1
    
    # parse file
    for p in data:

        # show values
        #print('CommodityCode: ' + p['CommodityCode'])
        #print('CommodityDescription: ' + p['CommodityDescription'])
        #print('CountryCode: ' + p['CountryCode'])
        #print('CountryName: ' + p['CountryName'])
        #print('MarketYear: ' + p['MarketYear'])
        #print('CalendarYear: ' + p['CalendarYear'])
        #print('Month: ' + str(p['Month']))
        #print('AttributeId: ' + str(p['AttributeId']))
        #print('AttributeDescription: ' + p['AttributeDescription'])
        #print('UnitId: ' + str(p['UnitId']))
        #print('UnitDescription: ' + p['UnitDescription'])
        #print('Value: ' + str(p['Value']))
        #print('')
        

        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=TEDSQL050;'
                      'Database=AgEcon;'
                      'Trusted_Connection=yes;'
                      'Driver={ODBC Driver 17 for SQL Server};')
        cursor = conn.cursor()

        now = datetime.date.today()
        
        sql_insert_query = "INSERT INTO AgEcon_PSD_All_Data_Staging_Python \
                            ([Date_Entered], [Commodity_Code], \
                            [Commodity_Description], [Country_Code], \
                            [Country_Name], 	[Market_Year], [Calendar_Year], \
                            [Month], [Attribute_ID], [Attribute_Description], \
                            [Unit_ID], [Unit_Description], [Value]) \
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        vals = (now, p['CommodityCode'], p['CommodityDescription'], \
                p['CountryCode'], p['CountryName'], p['MarketYear'], \
                p['CalendarYear'], str(p['Month']), str(p['AttributeId']), \
                p['AttributeDescription'], str(p['UnitId']), p['UnitDescription'],
                str(p['Value']))

        #print(sql_insert_query, vals)

        cursor.execute(sql_insert_query, vals)                

        conn.commit()
        r += 1
        print('Record inserted' + str(r))

