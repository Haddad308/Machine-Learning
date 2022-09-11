import time
from bs4 import BeautifulSoup 
from itertools import zip_longest  
import csv 
import requests 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from requests_html import HTMLSession
import numpy as np 

# Information of drivers 
Path = "C:\\Program Files (x86)\\chromedriver.exe"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,ar;q=0.7"} 
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(Path,options=options)

# Data information 
car_names = ['Maruti Swift Dzire ZDI','Hyundai Grand i10 Sportz','Mahindra Scorpio VLX']
prices = []

# Loop over all car names to find the new price 
for car in car_names :
    driver.get("https://www.cardekho.com/")
    time.sleep(1)
    search = driver.find_element(By.XPATH,'//*[@id="cardekhosearchtext"]')
    search.send_keys(" ".join(car.split()[:3]))
    time.sleep(2)
    search.send_keys(Keys.RETURN)
    time.sleep(1)
    response = requests.get(driver.current_url, headers=headers)
    soup = BeautifulSoup(response.content,'lxml')
    try : 
        price = soup.find("div",{"class":"price"}).text.split("*")[0]
        prices.append(price)
    except : 
        prices.append(np.nan)

    time.sleep(3)

print(prices)
time.sleep(2)
driver.close()