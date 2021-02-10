import os
import csv
import pyodbc

location = 'C:/Python39/TestFiles/'
substring = 'BrokerFeeVouch'

#Create database connection
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=TEDSQL050;'
                      'Database=MDMStage;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

#Loop through directory
for file in os.listdir(location):
    #look for only CSV files
    if file.endswith(".csv"):
        if substring in file:
        
            #Open the file
            with open(os.path.join(location, file)) as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    line_count = 0
                    
                    #BEGIN FOR
                    for row in csv_reader:
                        if line_count == 0:
                            #print(f'Column names are {", ".join(row)}')
                            line_count += 1
                        else:

                            #Write/Insert row info into database
                            sql_insert_query = "INSERT INTO stg_BrokerFeeVoucher (BookingNumber, NetWeight, SupplierSourceCustomerId, BsmSupplierProfileId, BuyerSourceCustomerId, BsmBuyerProfileId, InternalSalesContract, SaleContract, BsmOrderId, OBD, DestinationPortCode, DestinationPortName, Commodity, BrokerSourceCustomerId, BsmBrokerProfileId ,CostIndex ,BrokerTotalFee, Location, Source, SubSource) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                            val=[row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19]]
            
                            cursor.execute(sql_insert_query, val)                

                            conn.commit()
                            print('Record inserted')
                            line_count += 1
