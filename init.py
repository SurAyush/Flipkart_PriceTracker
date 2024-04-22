from bs4 import BeautifulSoup
import requests
import time
import datetime
import pandas as pd
import csv
from spaceremover import clean

URL = "https://www.flipkart.com/realme-12-pro-5g-navigator-beige-128-gb/p/itmcc78f150eeabd?pid=MOBGWH8S46ZD2ZGH&lid=LSTMOBGWH8S46ZD2ZGHOFJ8VN&marketplace=FLIPKART&q=realme+12+pro&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&fm=organic&iid=95abe56f-880e-4b06-81e1-427720edbc27.MOBGWH8S46ZD2ZGH.SEARCH&ppt=hp&ppn=homepage&ssid=pyvwyerfe80000001713798405728&qH=fd53babedc54877e"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

d = datetime.datetime.now()

import csv

header = ['Title', 'Price', 'Date']
title = soup2.find(class_="VU-ZEz").get_text()
price = soup2.find(class_="Nx9bqj CxhGGd").get_text()
title = title.strip()
title = clean(title)
p = price.strip()
p=p[1:]
p = p.replace(",","")


data = [title, p, d]

with open('FlipkartWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


