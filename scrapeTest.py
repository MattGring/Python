import requests
from bs4 import BeautifulSoup

url = 'http://bigcharts.marketwatch.com/markets/screener.asp?market=Nyse&report=LargestPercentLossReport&x=18&y=22'

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
rowsDown = soup.find_all("tr", {"class": "down"})
rowsUp = soup.find_all("tr", {"class": "up"})

rows = rowsDown + rowsUp
print(rows)


