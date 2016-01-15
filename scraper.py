# Matt Gring
# 7/10/2015
# experimenting with web scraping

# import modules
import requests
from bs4 import BeautifulSoup

# global variable declarations
url = "http://bigcharts.marketwatch.com/markets/screener.asp"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

# prints out the whole dom
print(soup.prettify())

# this is how you find stuff by finding the html tags
rows = soup.find_all("tr", {"class": "up"})

# not sure if this worked
for row in rows:
    #print(row)
    row_data = row.find_all("td")
    for data in row_data:
        print(data.contents[0])

# this worked
for row in rows:
	print(row.contents[1].text)

# declare array to hold the variables
symbol = []
companyName = []
price = []
priceChange = []
percentChange = []
volume = []
dollarsTraded = []

# loop to grab data and append it to the arrays 
for row in rows:
        symbol.append(row.contents[1].text)
        companyName.append(row.contents[3].text)
        price.append(row.contents[5].text)
        priceChange.append(row.contents[7].text)
        percentChange.append(row.contents[9].text)
        volume.append(row.contents[11].text)
        dollarsTraded.append(row.contents[13].text)
        
# print out one row    
print(symbol[1] + " " + companyName[1] + " " + price[1] + " " + priceChange[1] + " " + percentChange[1] + " " + volume[1] + " " + dollarsTraded[1])


# url for bulletin board and 50wk high X percent gain screener
# http://bigcharts.marketwatch.com/markets/screener.asp?market=BulletinBoard&report=High52WeekbyPercentGain&x=25&y=23
# market=BulletinBoard&report=High52WeekbyPercentGain
# market=Nasdaq&report=High52WeekbyPercentGain
# market=Amex&report=High52WeekbyPercentGain
# market=Nyse&report=High52WeekbyPercentGain


# market options:
#
# Nyse, Amex, Nasdaq, BulletinBoard

# report options:
#
# LargestPercentGainReport
# LargestPercentLossReport
# LargestNetPriceGain
# LargestNetPriceLoss
# High52WeekbyPercentGain
# Low52WeekbyPercentLoss
# MostActive
# MostActiveByDollarsTraded












