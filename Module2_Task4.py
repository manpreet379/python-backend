import csv 
import os
import requests
import re

req=requests.get("https://finance.yahoo.com/quote/SBIN.NS/")


url = "https://finance.yahoo.com/quote/SBIN.NS/"
headers = {'User-Agent': 'Mozilla/5.0'}  
response = requests.get(url, headers=headers)


match = re.search(r'"regularMarketPrice":{"raw":([\d.]+)', response.text)

if match:
    price = match.group(1)
    print(f"Current SBIN Stock Price: ₹{price}")
else:
    print("Stock price not found.")
    
with open('newstock.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['Stock','Price'])
    writer.writerow(['SBIN',price])

print("Current directory is:",os.getcwd())
print("All the files in current directory are :",os.listdir(os.getcwd()))
print(os.path.isdir('.'))