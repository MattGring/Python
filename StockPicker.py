# StockPicker.py
# By: M Gring
# 7/12/2015
# The aim of this script is to automate stock picking process using
# web scraping the bigcharts.com website.
#
# This will create a file, add stock pics to it and then email the file


# import modules
import sys
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# global variable declarations
url = "http://bigcharts.marketwatch.com/markets/screener.asp?"
emailAddress = "gring.matt@gmail.com"
path = "C:\\Users\\mattg\\Desktop\\"
fileName = path + str(datetime.now().date()) + ".txt"

# gather data
# usage: gatherData(url, exchange, reportType)
def gatherData(url, exchange, reportType):
    url += "market=" + exchange + "&report=" + reportType
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    rows = soup.find_all("tr", {"class": "up"})
    file.write(url + "\n")
    # loop through the data and print it to the file
    for row in rows:
        # more logic here to sift through the records
        # criteria for comparing variables: price >= 0.001; dollarsTraded >= 10,000; etc..
        # if variables meet criteria then print the line, else skip it
        # print the data to the file
        file.write(row.contents[1].text +"\t"+ row.contents[3].text +"\t"+ row.contents[5].text +"\t"+ row.contents[7].text +"\t"+ row.contents[9].text +"\t"+ row.contents[11].text +"\t"+ row.contents[13].text + "\n")

# main
# create file
file = open(fileName, 'a')

# get data from url's and write to file
# usage: gatherData(url, exchange, reportType)

# possible exchange values:
# Nyse, Amex, Nasdaq, BulletinBoard

# possible report types:
# LargestPercentGainReport
# LargestPercentLossReport
# LargestNetPriceGain
# LargestNetPriceLoss
# High52WeekbyPercentGain
# Low52WeekbyPercentLoss
# MostActive
# MostActiveByDollarsTraded
gatherData(url, "Nyse", "LargestPercentGainReport")
gatherData(url, "Amex", "LargestPercentGainReport")
gatherData(url, "Nasdaq", "LargestPercentGainReport")
gatherData(url, "BulletinBoard", "LargestPercentGainReport")

# close file
file.close()



