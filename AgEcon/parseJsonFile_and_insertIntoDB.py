import json
import pyodbc
import datetime as dt
import os
import csv
from datetime import datetime

def insert_data():

    t1 = datetime.now()

    #set location of directory to look for files.
    location = 'C:/Python39/DEVFiles/PythonDev/AgEcon/'

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=TEDSQL050;'
                          'Database=AgEcon;'
                          'Trusted_Connection=yes;'
                          'Driver={ODBC Driver 17 for SQL Server};')
    cursor = conn.cursor()
    print("Data connection made.")
        
    #Loop through directory
    for file in os.listdir(location):
        #look for only json files
        if file.endswith(".json"):

            print(file)
            # read file
            with open(os.path.join(location, file)) as json_file:
                data = json.load(json_file)

        #set record counter
            r = 1

            print("Starting file parsing.")
            # parse file
            for p in data:

                #Get todays' date for DATE_INSERTED field below
                now = dt.date.today()
                    
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

                print(sql_insert_query, vals)

                cursor.execute(sql_insert_query, vals)                

                conn.commit()

                r += 1
                print('Record inserted: ' + str(r))

    t2 = datetime.now()
    delta = t2 - t1
    print(delta.seconds)


