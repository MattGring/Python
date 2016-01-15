# New scrape to find data for each stock


# --------------------------- IMPORT STATEMENTS -------------------------------->
import requests
from bs4 import BeautifulSoup
import pyodbc
from datetime import date, timedelta

# --------------------------- VARIABLES ---------------------------------------->
exchanges = ["Nyse", "Amex", "Nasdaq", "BulletinBoard"]
reportTypes = ["LargestPercentGainReport", "LargestPercentLossReport", "LargestNetPriceGain", "LargestNetPriceLoss", "High52WeekbyPercentGain", "Low52WeekbyPercentLoss", "MostActive", "MostActiveByDollarsTraded"]
tickers = []
yesterdaysDate = str(date.today() - timedelta(1))
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=PC763\SQL;DATABASE=Stocks;UID=sa;PWD=perry')
cursor = cnxn.cursor()


# --------------------------- FUNCTION DEFINITIONS ----------------------------->
def getVolumeAndPercentChange(ticker):
    url = "http://bigcharts.marketwatch.com/quickchart/quickchart.asp?symb=" + ticker + "&insttype=&freq=&show="
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    rows = soup.find_all("td", {"class": "change"})

    percentChange = (rows[1].contents[3].text).replace(",","")
    percentChange = percentChange.replace("%","")
    if (percentChange == 'n/a'):
        percentChange = 0
    else:
        percentChange = float(percentChange)

    rows = soup.find_all("div")
    volume = (rows[42].text).replace(",","")
    if (volume == 'n/a'):
        volume = 0
    else:
        volume = int(volume)

    print(ticker)
    print(percentChange)
    print(volume)

    volumeAndPercentChange = [volume, percentChange]
    return volumeAndPercentChange
     

def getSentiment():
    url = 'http://bigcharts.marketwatch.com/quickchart/quickchart.asp?symb=XX%3AW5000&insttype=Index'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    rows = soup.find_all("td", {"class": "change"})

    
    sentiment = (rows[1].contents[3].text).replace(",","")
    sentiment = sentiment.replace("%","")

    return sentiment


def getTickers(cursor, exchange, reportType, date):
    cursor.execute("select tbl_rawData.Ticker from tbl_rawData where tbl_rawData.Exchange = ? and tbl_rawData.ReportType = ? and tbl_rawData.date = ?", exchange, reportType, date)
    rows = cursor.fetchall()
    tickers = []
    for row in rows:
        tickers.append(row[0])
    return tickers
                      


def getNumRows(cursor, exchange, reportType, date):
    cursor.execute("select count(*) from tbl_rawData where tbl_rawData.Exchange = ? and tbl_rawData.ReportType = ? and tbl_rawData.date = ?", exchange, reportType, date)
    row = cursor.fetchone()
    if not row:
        rows = 0
    else:
        rows = row[0]
    return rows


    

# -------------------------------- MAIN ---------------------------------->

sentiment = getSentiment()

for exchange in exchanges:
    print(exchange)
    
    for reportType in reportTypes:
        
        print(reportType)
        # get the number of rows
        numRows = getNumRows(cursor, exchange, reportType, yesterdaysDate)
        # get the list of tickers
        tickers = getTickers(cursor, exchange, reportType, yesterdaysDate)
        
        for ticker in tickers:
            try:
                volumeAndChnge = getVolumeAndPercentChange(ticker)               
            except Exception:
                pass
            volume = volumeAndChange[0]
            percentChange = volumeAndChange[1]
            
            totalPercentChange = totalPercentChange + percentChange

            if (volume >= 25000):
                if (percentChange >= 0.01):
                    above_01 = above_01 + 1
                if (percentChange >= 1):
                    above_1 = above_1 + 1
                if (percentChange >= 5):
                    above_5 = above_5 + 1
                if (percentChange >= 10):
                    above_10 = above_10 + 1
                if (percentChange >= 20):
                    above_20 = above_20 + 1
                if (percentChange <= 0.01):
                    below_01 = below_01 + 1
                if (percentChange <= 1):
                    below_1 = below_1 + 1
                if (percentChange <= 5):
                    below_5 = below_5 + 1
                if (percentChange <= 10):
                    below_10 = below_10 + 1
                if (percentChange <= 20):
                    below_20 = below_20 + 1
        # check for divide by 0
        if (numRows == 0):
            hitPercentage = 0
        # calculate the percentage of tickers that met requirements
        else:
            hitPercentage = (hits / numRows) * 100
        # write the results to the HitCount table
        cursor.execute("insert into tbl_HitCount(Exchange, ReportType, TotalRows, HitCount, HitPercentage, Date, Sentiment) values (?,?,?,?,?,GETDATE(),?)", exchange, reportType, numRows, hits, hitPercentage, sentiment)
        cnxn.commit()






# --------------------------------- NOTES -------------------------------->

# 1.) show the date the report was run and the date that the stocks closed at
#
# 2.) add hits and percentages for 0.01% 1%, 5%, 10%, 20% etc...  OR averge %gain






    
