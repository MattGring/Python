import requests
from bs4 import BeautifulSoup


audioPAs = ['NOS-2A3', 'NOS-5AQ5', 'NOS-5CZ5', 'NOS-5V6GT', 'NOS-6AQ5A', 'NOS-6AS5', 'NOS-6BQ5', 'NOS-6CA5', 'NOS-6CM6',
        'NOS-6CU5', 'NOS-6CZ5', 'NOS-6DG6GT', 'NOS-6DS5', 'NOS-6EM5', 'NOS-6GC5', 'NOS-6FE5', 'NOS-6L6',
        'NOS-6L6GB', 'NOS-6L6GC', 'NOS-6V6', 'NOS-6V6GTA', 'NOS-6W6GT', 'NOS-6Y6G', 'NOS-8BQ5', 'NOS-8EM5', 'NOS-12AB5',
        'NOS-12AQ5', 'NOS-12CA5', 'NOS-12CU5', 'NOS-12L6GT', 'NOS-12V6GT', 'NOS-12W6GT', 'NOS-25C5',
        'NOS-25F5A', 'NOS-34GD5', 'NOS-34GD5A', 'NOS-35B5', 'NOS-35C5', 'NOS-35L6GT', 'NOS-50B5',
        'NOS-50C5', 'NOS-50FE5', 'NOS-50L6GT', 'NOS-6973', 'NOS-7027A', 'NOS-7408', 'NOS-6BQ5',
        'NOS-6EH5', 'NOS-6F6', 'NOS-6CK6', 'NOS-6K6GT', 'NOS-8BQ5', 'NOS-12EH5', 'NOS-25EH5',
        'NOS-35EH5', 'NOS-50EH5', 'NOS-50FK5', 'NOS-60FX5', 'NOS-7189', 'NOS-7868']

print('Audio Power Tubes: \n\n')

for audioPA in audioPAs:

    url = 'https://www.tubedepot.com/products?utf8=%E2%9C%93&keywords=' + audioPA 
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    rows = soup.find_all("div", {"class": "price selling"})
    for row in rows:
        price = row.contents[0]
        print(audioPA + '  ' + price)
        
print('\n\nHorizontal Deflection Tubes:\n\n')

horizs = ['NOS-6AG7', 'NOS-6AU5GT', 'NOS-6AV5GA', 'NOS-6BG6A', 'NOS-6BL7GTA', 'NOS-6BQ6GTB', 'NOS-6CB5A', 'NOS-6CD6GA', 'NOS-6CL6', 'NOS-6DN6',
        'NOS-6DQ5', 'NOS-6DQ6B', 'NOS-6EX6', 'NOS-6GJ5', 'NOS-6GK6', 'NOS-6GT5', 'NOS-6GW6', 'NOS-6JB6',
        'NOS-6JE6', 'NOS-12AV5GA', 'NOS-12BQ6GTB', 'NOS-12DQ6A', 'NOS-12DQ6B', 'NOS-12GJ5', 'NOS-12GT5',
        'NOS-12GW6', 'NOS-12JB6', 'NOS-17BQ6GTB', 'NOS-17DQ6B', 'NOS-17GJ5', 'NOS-17GT5', 'NOS-17GW6',
        'NOS-17JB6', 'NOS-22JG6', 'NOS-25AV5GA', 'NOS-25BK5', 'NOS-25BQ6', 'NOS-25CD6GB', 'NOS-25DN6']

for horiz in horizs:

    url = 'https://www.tubedepot.com/products?utf8=%E2%9C%93&keywords=' + horiz 
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    rows = soup.find_all("div", {"class": "price selling"})
    for row in rows:
        price = row.contents[0]
        print(horiz + '  ' + price)      
