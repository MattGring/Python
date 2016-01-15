import pyodbc


# create the connection
print("Attempting to connect to SQL Server...\n")
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=PC763\SQL;DATABASE=Stocks;UID=sa;PWD=perry')
print("Successfully connected to SQL Server!\n")

#create the cursor
cursor = cnxn.cursor()

cursor.execute("select distinct * from tbl_rawData where tbl_rawData.DollarsTraded >= 10000 and tbl_rawData.Price >= 0.01 and tbl_rawData.Exchange = 'BulletinBoard'")
#row = cursor.fetchone()
#if row:
#    print(row)

while 1:
    row = cursor.fetchone()
    if not row:
        break
    print(row.Date, row[1])
