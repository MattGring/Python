# StockPicker_03.py
# Matt Gring
# 7/28/2015
#
# This program scrapes data from bigcharts.com stock screener and saves
# it to SQL Server.


# ------------- IMPORT MODULES ------------->
import requests
from bs4 import BeautifulSoup
import pyodbc
import getpass


# ------------ VARIABLE DECLARATIONS ----------->
url = "http://bigcharts.marketwatch.com/markets/screener.asp?"
exchanges = ["Nyse", "Amex", "Nasdaq", "BulletinBoard"]
reportTypes = ["LargestPercentGainReport", "LargestPercentLossReport", "LargestNetPriceGain", "LargestNetPriceLoss", "High52WeekbyPercentGain", "Low52WeekbyPercentLoss", "MostActive", "MostActiveByDollarsTraded"]
DbRowsCreated = 0
testMode = False

# ------------ FUNCTION DEFINITIONS ------------>

# gather data function definition
# usage: gatherData(url, exchange, reportType)
def gatherData(url, exchange, reportType, cursor):
    url += "market=" + exchange + "&report=" + reportType
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    rowsUp = soup.find_all("tr", {"class": "up"})
    rowsDown = soup.find_all("tr", {"class": "down"})
    rows = rowsUp + rowsDown

    # loop through the data
    for row in rows:
        
        # extract data and convert to usable format
        
        #TICKER SYMBOL
        ticker = row.contents[1].text
        #SHARE PRICE
        price = (row.contents[5].text).replace(",","")
        #CHANGE IN SHARE PRICE
        priceChange = (row.contents[7].text).replace(",","")
        #PERCENTAGE CHANGE
        percentChange = (row.contents[9].text).replace(",","")
        percentChange = percentChange.replace("%","")
        #VOLUME
        volume = (row.contents[11].text).replace(",","")
        #DOLLARS TRADED
        dollarsTraded = row.contents[13].text     
        if ("M" in dollarsTraded):
            dollarsTraded = str(int(float(dollarsTraded.replace("M","")) * 1000000))
        elif ("B" in dollarsTraded):
            dollarsTraded = str(int(float(dollarsTraded.replace("B","")) * 1000000000))                 
        else:
            dollarsTraded = str(int(dollarsTraded.replace(",","")))        

        # for testing
        if (testMode):
            print(exchange + "\t" + reportType + "\t" + ticker + "\t" + price + "\t" + priceChange + "\t" + percentChange + "\t" + volume + "\t" + dollarsTraded)
            print(str(type(exchange)) + "\t" + str(type(reportType)) + "\t" + str(type(ticker)) + "\t" + str(type(price)) + "\t" + str(type(priceChange)) + "\t" + str(type(percentChange)) + "\t" + str(type(volume)) + "\t" + str(type(dollarsTraded)))

        # create the SQL insert statement and execute it
        cursor.execute("insert into tbl_rawData(Date, Ticker, Price, PriceChange, PercentChange, Volume, DollarsTraded, UniqueNumber, Exchange, ReportType, AfterHoursTrading) values (GETDATE(),?,?,?,?,?,?,NULL,?,?,NULL)", ticker, price, priceChange, percentChange, volume, dollarsTraded, exchange, reportType)

        # commit the changes to the table
        cnxn.commit()

        # create a variable to hold the number of rows created
        global DbRowsCreated
        # increment the rows created variable
        DbRowsCreated = DbRowsCreated + 1

            
# ------------ MAIN STARTS HERE --------------->

# ask for the username and pw
user = input("User: ")
pw = getpass.getpass("Password for \'" + user + "\': ")

# create the connection
print("Attempting to connect to SQL Server...\n")
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=PC763\SQL;DATABASE=Stocks;UID=' + user + ';PWD=' + pw)
print("Successfully connected to SQL Server!\n")

#create the cursor
cursor = cnxn.cursor()

print("Writing Data... Please Wait...\n")
DbRowsCreated = 0
# outer loop
for exchange in exchanges:

    # inner loop
    for reportType in reportTypes:

        # get data from url's and export to Dbase
        # usage: gatherData(url, exchange, reportType)
        gatherData(url, exchange, reportType, cursor)

# print success message        
print("Success! " + str(DbRowsCreated) + " rows have been written to the DB.")

# same as system pause
input("Press ENTER to continue...")










