import time
import requests as rq
from bs4 import BeautifulSoup
import json

def pushbullet_noti(title, body):

		    TOKEN = 'o.xYE1qAvnRxm9SN4Ioh0SBWxDL0E62cOy'  # Pass your Access Token here
		    # Make a dictionary that includes, title and body
		    msg = {"type": "note", "title": title, "body": body}
		    # Sent a posts request
		    resp = rq.post('https://api.pushbullet.com/v2/pushes',
		                         data=json.dumps(msg),
		                         headers={'Authorization': 'Bearer ' + TOKEN,
		                                  'Content-Type': 'application/json'})



header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

site = "https://www.amazon.co.uk/GeoBook-12-5-inch-Laptop-Windows-Celeron/dp/B093CKF956/ref=sr_1_1?keywords=linux+laptop&qid=1670177694&refinements=p_36%3A5000-11100&rnid=9708204031&sprefix=linux+lap%2Caps%2C94&sr=8-1"

seperator = '/'
product = site.replace('/','',1)
product = product.replace('/','',1)
product = product.replace('/','',1)
product = product.split(seperator, 1)[0]
product = product.replace('https:www.amazon.co.uk','')
print(product)

while True:
	html = rq.get(site, headers=header).text
	soup = BeautifulSoup(html, 'html.parser')
	price_pounds = [i.get_text() for i in
		soup.find('span', {'class': 'a-price-whole'})]
	price_pence = [i.get_text() for i in
		soup.find('span', {'class': 'a-price-fraction'})]
	price_pounds = ''.join(price_pounds)
	price_pence = ''.join(price_pence)
	price_pounds_real= float(price_pounds)
	price_pence_real = float(price_pence)
	final_price_real = price_pounds_real + price_pence_real
	final_price = '£'+price_pounds+price_pence
	print(final_price)
	
	time.sleep(10)
	
	html2 = rq.get(site, headers=header).text
	soup2 = BeautifulSoup(html, 'html.parser')
	price_pounds2 = [i.get_text() for i in
		soup.find('span', {'class': 'a-price-whole'})]
	price_pence2 = [i.get_text() for i in
		soup.find('span', {'class': 'a-price-fraction'})]
	price_pounds2 = ''.join(price_pounds2)
	price_pence2 = ''.join(price_pence2)
	price_pounds2_real= float(price_pounds2)
	price_pence2_real = float(price_pence2)
	final_price2_real = price_pounds2_real + price_pence2_real
	final_price2= '£'+price_pounds2 + price_pence2
	print(final_price2)
	
	if final_price2_real < final_price_real:
		pushbullet_noti("Price drop for ",product)
		time.sleep(10)
	
	else:
		pushbullet_noti(product,' Has not dropped in price')
		time.sleep(10)
		
		