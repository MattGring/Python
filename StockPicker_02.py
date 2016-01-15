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
path = "C:\\My Stuff\\StockPicks\\"
fileName = path + str(datetime.now().date()) + ".txt"

# gather data
# usage: gatherData(url, exchange, reportType)
def gatherData(url, exchange, reportType):
    url += "market=" + exchange + "&report=" + reportType
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    rows = soup.find_all("tr", {"class": "up"})
    file.write(url + "\n")
    priceCutoff = 0.001
    dollarsTradedCutoff = 10000
    # loop through the data and print it to the file
    for row in rows:
        # more logic here to sift through the records
        # criteria for comparing variables: price >= 0.001; dollarsTraded >= 10,000; etc..
        # if variables meet criteria then print the line, else skip it
        # print the data to the file
        price = float((row.contents[5].text).replace(",",""))
        dollarsTraded = row.contents[13].text
        if ("M" in dollarsTraded) or ("B" in dollarsTraded):
            dollarsTraded = 100000
        else:
            dollarsTraded = int((row.contents[13].text).replace(",",""))
        if((price >= priceCutoff) and (dollarsTraded >= dollarsTradedCutoff)): 
            file.write(row.contents[1].text +"\t"+ row.contents[3].text +"\t"+ row.contents[5].text +"\t"+ row.contents[7].text +"\t"+ row.contents[9].text +"\t"+ row.contents[11].text +"\t"+ row.contents[13].text + "\n")
        else:
            file.write(row.contents[1].text + " did not meet requirements. \n")

# send email
def sendMail(fileName):
    # import statements
    import yagmail

    # instantiate an email object
    # tried to use the keyring but the path to '.yagmail' could not be found
    yag = yagmail.SMTP('gring.matt@gmail.com', '6shadow1')

    # add some contents
    # for more info: https://github.com/kootenpv/yagmail
    contents = ['Text file is attached.', fileName]

    # send the message
    yag.send('gring.matt@gmail.com', 'Stock Picks for Today', contents)


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
gatherData(url, "Nyse", "High52WeekbyPercentGain")
gatherData(url, "Amex", "High52WeekbyPercentGain")
gatherData(url, "Nasdaq", "High52WeekbyPercentGain")
gatherData(url, "BulletinBoard", "High52WeekbyPercentGain")

# close file
file.close()

# send the email with file attached
sendMail(fileName)



