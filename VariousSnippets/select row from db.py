# Python SQL Select Statement Example
import pyodbc

#Create database connection
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=tepdagagr01;'
                      'Database=AgrisExtension;'
                      'Trusted_Connection=yes;')
#try:
cursor = conn.cursor()

cursor.execute('SELECT top 100 * FROM [AgrisExtension].[Agris].[B01_TRANS]')

#sql_select_Query = "SELECT * FROM [AgrisExtension].[Agris].[B01_TRANS]"
##for row in cursor:
##    print('row = %r' % (row,))
##    print()
#cursor.execute(sql_select_Query)

records = cursor.fetchall()
print("Total number of rows is: ", cursor.rowcount)

print("\nPrinting each record")
for row in records:
    print("===========NEW RECORD===========")
    print("BookingNumber = ", row[0], )
    print("NetWeight = ", row[1])
    print("SupplierSourceCustomerId  = ", row[2])
    print("BsmSupplierProfileId  = ", row[3])
    print("BuyerSourceCustomerId  = ", row[4])
    print("BsmBuyerProfileId  = ", row[5])
    print("InternalSalesContract  = ", row[6])
    print("SaleContract  = ", row[7])
    print("BsmOrderId  = ", row[8])
    print("OBD  = ", row[9])
    print("DestinationPortCode  = ", row[10])
    print("DestinationPortName  = ", row[11])
    print("Commodity  = ", row[12])
    print("BrokerSourceCustomerId  = ", row[13])
    print("BsmBrokerProfileId  = ", row[14])
    print("CostIndex  = ", row[15])
    print("BrokerTotalFee  = ", row[16])
    print("Location  = ", row[17])
    print("Source  = ", row[18])
    print("SubSource  = ", row[19])
    print("FileDate  = ", row[20], "\n")

##    sql_delete_query = """Delete from PackingList where BookingNumber = ?""" 
##    val = row[0]
##    print(sql_delete_query, val)
##    cursor.execute(sql_delete_query, val)
##    conn.commit()
##    print('Records deleted')
##    
##    sql_insert_query = "INSERT INTO PackingList (BookingNumber ,SupplierSourceCustomerId ,BsmSupplierProfileId ,BuyerSourceCustomerId, BsmBuyerProfileId, SaleContract, BsmOrderId, OBD, DestinationPortCode, DestinationPortName, Commodity, Location, Source, Subsource) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
##    val=[row[0],row[2],row[3],row[4],row[5],row[7],row[8],row[9],row[10],row[11],row[12],row[17],row[18], row[19]]
##    print(sql_insert_query, val)        
##    cursor.execute(sql_insert_query, val)
##    conn.commit()
##    print('Record inserted')
         
##except Error as e:
##    print("Error reading data from SQL table", e)
##finally:
##    if (conn.is_connected()):

cursor.close()
conn.close()

print("SQL connection is closed")
