#dbConn.py
import pyodbc
import pandas as pd

def connect():
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=TEDSQL050;'
                      'Database=MDMStage;'
                      'Trusted_Connection=yes;')

    cursor = conn.cursor()
    cursor.execute('SELECT CREATION_DATE, CUST_ACCOUNT_ID, CUSTOMER_NAME, CUSTOMER_ACCOUNT_NAME, CUST_ACCT_NUM FROM dbo.Customers')

    for row in cursor:
        print(row)


sql_query = pd.read_sql_query('SELECT * FROM dbo.Customers',conn)
print(sql_query)
print(type(sql_query))

