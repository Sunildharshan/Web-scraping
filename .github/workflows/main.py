import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

browser = webdriver.Chrome()
browser.get('https://www.flipkart.com/search?q=phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')

url = "https://www.flipkart.com/search?q=phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

products = []
ratings = []
prices = []

page = requests.get("https://www.flipkart.com/search?q=phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soup = BeautifulSoup(page.content, 'html.parser')

name = soup.find_all('a', {"class": "_4rR01T"})
rate = soup.find_all("div", {"class": "_3LWZ1K"})
price = soup.find_all('div', {"class": "_3tbKJL _25b18c"})

for i in name:
    products.append(i.text)
for i in range(len(products)):
    ratings.append(rate[i].text)
for i in range(len(products)):
    prices.append(price[i].text)

df = pd.DataFrame(dict(Product_Name=products, Price=prices, Rating=ratings))
df.to_csv('Web-s.csv', index=False, encoding='utf-8')
print(df)
