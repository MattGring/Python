import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=PC763\SQL;DATABASE=Stocks;UID=sa;PWD=perry')

cursor = cnxn.cursor()

cursor.execute("insert into tbl_rawData(Date, Ticker, Price, PriceChange, PercentChange, Volume, DollarsTraded, UniqueNumber, Exchange, ReportType, AfterHoursTrading) values (getdate(), 'test', 10.00, 1.00, 10.0, 200000, 2000000, NULL, 'Nyse', '52weekhigh', NULL)")

cnxn.commit()
