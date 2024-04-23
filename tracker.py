from bs4 import BeautifulSoup
import requests
import datetime
from spaceremover import clean
import csv
import uuid
import pandas as pd

from send_email import send_email_func
from graph import save_graph

#function compares the present price of the product and the threshold price set for the product
#if price is lesser than or equal to the threshold send_mail_func is called that send the mail to the customer using smtplib
def pricethreshold(threshold,p,URL,title,receiver):
    if p <= int(threshold):
        x=uuid.uuid4()
        save_graph(x,title,threshold)
        try:
            send_email_func(title,p,URL,threshold,x,receiver)
        except:
            print("Sorry! Mail cannot be sent")


#this function takes a list of url and threshold as input
#it runs a loop to iterate over all url and threshold price
#it sends a request to the url to retreive the data in text form
#the data is parsed to html first and then to a tree (prettify()) for easier access and navigation
#product name and price data is then scraped using Beautiful soup
#this then calls pricethreshold() for comaparsion
def get_price(URLs,thresholds,receivers):

    print("Get_price function called")

    #common header file to pass request
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    #traversing list
    for index,URL in enumerate(URLs):
        try:
            #sending request to URL
            page = requests.get(URL, headers=headers)

            #parsing
            soup1 = BeautifulSoup(page.content, "html.parser")

            soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

            #getting present time stamp
            d = datetime.datetime.now()

            #scraping product name and price
            title = soup2.find(class_="VU-ZEz").get_text()
            price = soup2.find(class_="Nx9bqj CxhGGd").get_text()

            #removing unnecessary parts from scraped title and price
            title = title.strip()
            title = clean(title)
            p = price.strip()
            p = p[1:]
            p = p.replace(",", "")

            data = [title, p, d]

            #exception handling
            try:
                #writing the content into the csv file
                with open('FlipkartWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
                    writer = csv.writer(f)
                    writer.writerow(data)
            except:
                print("CSV file cannot be handled")

            print("Request accepted")
            #calling pricethreshold() function for comparison
            pricethreshold(thresholds[index], int(p), URL, title, receivers[index])
        except:
            print("Request cannot be processed")


#creating list of url and threshold prices
#can be modified by taking input from a user and a GUI interface


URLs = ["https://www.flipkart.com/realme-12-pro-5g-navigator-beige-128-gb/p/itmcc78f150eeabd?pid=MOBGWH8S46ZD2ZGH&lid=LSTMOBGWH8S46ZD2ZGHOFJ8VN&marketplace=FLIPKART&q=realme+12+pro&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&fm=organic&iid=95abe56f-880e-4b06-81e1-427720edbc27.MOBGWH8S46ZD2ZGH.SEARCH&ppt=hp&ppn=homepage&ssid=pyvwyerfe80000001713798405728&qH=fd53babedc54877e","https://www.flipkart.com/sandisk-cruzer-blade-usb-2-0-32-gb-flash-pen-drive/p/itmf3qy9ykf8zjbs?pid=ACCD9XW3YU6VYCYS&lid=LSTACCD9XW3YU6VYCYSJR4ACL&marketplace=FLIPKART&q=sandisk+pendrive&store=6bo%2Fjdy%2Fuar&spotlightTagId=BestsellerId_6bo%2Fjdy%2Fuar&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&fm=search-autosuggest&iid=0e0a848c-5e51-435e-af83-8130b115e338.ACCD9XW3YU6VYCYS.SEARCH&ppt=sp&ppn=sp&ssid=k299v3ahzk0000001713806817220&qH=f6ba78bd04e69b9b","https://www.flipkart.com/samsung-22-inch-full-hd-ips-panel-monitor-ls22c310eawxxl/p/itmac31067559ef1?pid=MONGAQTQKCEZGVSC&lid=LSTMONGAQTQKCEZGVSCG4LB7V&marketplace=FLIPKART&q=monitor+samsung+ips&store=6bo%2Fg0i%2F9no&srno=s_1_2&otracker=search&otracker1=search&fm=Search&iid=04391792-0701-4f78-b8eb-1ba0be45d13b.MONGAQTQKCEZGVSC.SEARCH&ppt=sp&ppn=sp&ssid=a38rpyd8wg0000001713806864085&qH=75aa57e5d26a81d7"]
thresholds = [24000,400,6000]
receiver = ["ayushsur26@gmail.com","ayushsur26@gmail.com","ayushsur26@gmail.com"]
def get_price_caller():
    df = pd.read_csv('data.csv')
    url_ext=df['url']
    email_ext=df['email']
    threshold_ext = df['threshold']
    URLs.extend(url_ext)
    receiver.extend(email_ext)
    thresholds.extend(threshold_ext)
    get_price(URLs, thresholds,receiver)



