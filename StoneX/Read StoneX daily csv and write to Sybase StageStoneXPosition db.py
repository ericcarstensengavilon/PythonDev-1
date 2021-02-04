#import os
#import csv
from datetime import date
import pypyodbc

location = '\\\\tedfil01\\InformaticaDEV\\Process\\StoneX\\'
substring = 'GAVPOS_20201215_221233.csv'

# Get today's date 
today = date.today()
print(today)
#Create database connection


import urllib
from sqlalchemy import create_engine
connection_string = (
    'SERVER=tedappsyb01;'
    'PORT=5000;'
    'UID=zec0009;PWD=Thursday04;'
    'DATABASE=INST01;'
    'charset=utf8;'
)
connection_uri = f"sybase+pyodbc:///?odbc_connect={urllib.parse.quote_plus(connection_string)}"
engine = create_engine(connection_uri)

engine.execute("select * from StageStoneXPosition")





# Close the connection



# =============================================================================
# conn = sqlanydb.connect(dsn='SybaseIQDemo')
# curs = conn.cursor()
# curs.execute("select 'Hello, world!'")
# print( "SQL Anywhere says: %s" % curs.fetchone())
# curs.execute("select * from StageStoneXPosition")
# curs.close()
# conn.close()
# =============================================================================



# =============================================================================
# #Loop through directory
# for file in os.listdir(location):
#     #look for only CSV files
#     if file.endswith(".csv"):
#         if substring in file:
#         
#             #Open the file
#             with open(os.path.join(location, file)) as csv_file:
#                     csv_reader = csv.reader(csv_file, delimiter=',')
#                     line_count = 0
#                     
#                     #BEGIN FOR
#                     for row in csv_reader:
#                         if line_count == 0:
#                             #print(f'Column names are {", ".join(row)}')
#                             line_count += 1
#                         else:
# 
#                             #Write/Insert row info into database
#                             sql_insert_query = "INSERT INTO StageStoneXPosition \
#                             ([RECID],[Firm],[OfficeCode],[FimatAcctCode],[AccountType], \
#                              [ContractMonth],[StrikePrice],[TradeDate],[BuySellCode],[IntTracerNum],\
#                              [SpreadCode],[AccountClass],[NetPosition],[MarketValue],[LastTradingDate], \
#                              [GMIExchangeCode],[GMIFuturesCode],[GMIExchangeTradedCode],[ClosePriceDecimal],[OpenCloseCode],\
#                              [CardNumber],[GiveINGiveOUTCode],[GiveINFirmNum],[OrderType],\
#                              [DeleteCode],[RoutingCode],[GMIOperatorID],[TradePriceDecimal],[CustomerName],\
#                              [Instrument],[TradePriceFractional],[ClosePriceFractional],[Value],[Buys],\
#                              [Sells],[CUSIP],[Fee1],[Fee2],[Fee3],\
#                              [Fee4],[Fee5],[Fee6],[Fee7],[Fee8],\
#                              [Fee9],[PGICHG],[PBKCHG],[POTHER],[PFUFE1],\
#                              [PFUFE2],[PFUFE3],[PFUFE4],[PFUFE5],[PFUFE6],\
#                              [PFUFE7],[PFUFE8],[PFUFE9],[PFUGIV],[PFUBKG],\
#                              [PFUOTH],[Delta],[Commission],[DealID],[SettleDate],[UnderlyingPrice],\
#                              [CommentCode],[RecordLoaded]) \
#                             VALUES \
#                             (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,\
#                              ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
#                             #,,,Instrument,TradePriceFractional,ClosePriceFractional,Value,Buys,Sells,PositionType,Unused3,CUSIP,UCUSIP,SUNDCN,Fee1,Fee2,Fee3,Fee4,Fee5,Fee6,Fee7,Fee8,Fee9,PGICHG,PBKCHG,POTHER,PFUFE1,PFUFE2,PFUFE3,PFUFE4,PFUFE5,PFUFE6,PFUFE7,PFUFE8,PFUFE9,PFUGIV,PFUBKG,PFUOTH,Delta,Commission,DealID,SettleDate,UnderlyingPrice,COLUMNBS,COLUMNBT,COLUMNBU,COLUMNBV,CommentCode,DummyX,ExceptionKey,Source,Control_M_Date,) VALUES ,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?))"
#                             val=[row[0],row[1],row[2],row[3],row[4],\
#                                  row[5],row[6],row[7],row[8],row[9],\
#                                  row[10],row[11],row[12],row[13],row[14],\
#                                  row[15],row[16],row[17],row[18],row[19],\
#                                  row[20],row[21],row[22],row[23],\
#                                  row[24],row[25],row[26], row[27], row[28],\
#                                  row[29],row[30],row[31],row[32],row[33],\
#                                  row[34],row[35],row[36],row[37],row[38],
#                                  row[39],row[40],row[41],row[42],row[43],\
#                                  row[44],row[45],row[46],row[47],row[48],\
#                                  row[49],row[50],row[51],row[52],row[53],\
#                                  row[54],row[55],row[56],row[57],row[58],\
#                                  row[59],row[60],row[61],row[62],row[63],row[64],\
#                                  row[65],today]#,],,,row[65],row[66],row[67],row[68],row[69],row[70],row[71],row[72],row[73],row[74],row[75],row[76],row[77],row[78],row[79],today]
# 
#                             print(sql_insert_query, val)
#                             cursor.execute(sql_insert_query, val)                
# 
# =============================================================================
print('Record inserted')

