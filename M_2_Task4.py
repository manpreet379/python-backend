import yfinance as yf
import csv 
import os
import requests
import re

ticker='AAPL'

stock=yf.Ticker(ticker)


data=stock.history(period='1mo')

with open('stock.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['Date','Open','High','Low','Close','Volume'])

    for time_stamp,row in data.iterrows():
        writer.writerow([time_stamp,row['Open'],row['High'],row['Low'],row['Close'],row['Volume']])


with open ('stock.csv','r') as file:
    reader=csv.reader(file)
    for row in reader:
        date, open_price, high, low, close, volume = row
        print(f"Date: {date} | Open: {open_price} | Close: {close} | Volume: {volume}")
    

print("Current directory is:",os.getcwd())
print("All the files in current directory are :",os.listdir(os.getcwd()))
print(os.path.isdir('.'))

source="stock.csv"
destination="/Quokkalabsintern"
dest=os.path.join(destination,source)

# os.rename(source,dest)

# req=requests.get("https://www.quokkalabs.com/")
# print(req.status_code)
# # print(req.text) 
# # print(req.headers)
# print(req.headers['content-type'])
# print(req.encoding)
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



