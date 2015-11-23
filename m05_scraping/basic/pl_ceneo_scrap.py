'''
@author Tomasz Kowalczyk 
@tomkowalczyk

To use this script we should pass a product name as argument.
For example: -p nokia+130
'''

from bs4 import BeautifulSoup
from ipify import get_ip
from geoip import geolite2
from time import gmtime, strftime

import requests
import re
import csv
import argparse

# Getting additional information
REQ_IP = get_ip()
REQ_IP_MATCH = geolite2.lookup(REQ_IP)
REQ_COUNTRY = REQ_IP_MATCH.country
REQ_TIME = strftime("%Y-%m-%d %H:%M:%S", gmtime())
REQ_PRICE_COMP = "http://www.ceneo.pl"

def save_csv_file(filename, array):
	with open(filename, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["item_name","item_price","item_category","req_ip","req_country","req_time","req_price_comp"])
		writer.writerows(array)

def process_data(name, price, category):

	item_name = name.text if name else 'NA'
	item_price = price.text if price else 'NA'
	item_category = category.text if category else 'NA'

	item_name = item_name.replace(" ", "").replace("\r\n", "").replace("\n", "").encode("utf-8")
	item_price = item_price.replace(" ", "").replace("\r\n", "").replace("\n", "").encode("utf-8")
	item_category = item_category.replace(" ", "").replace("\r\n", "").replace("\n", "").encode("utf-8")

	return (item_name, item_price, item_category, REQ_IP, REQ_COUNTRY, REQ_TIME, REQ_PRICE_COMP)

def ceneo_scrap(filename, url, payload, headers):

	# Request the URL with parameters and headers
	r = requests.post(url, payload, headers = headers)

	if(r.status_code == 200):

		# Save response content in html variable
		html = r.content

		# Parsed html variable into HTML file with bs4
		parsed_html = BeautifulSoup(html, "html.parser")

		# Print document title
		print parsed_html.head.find('title').text

		# Find all of the HTML elements which are describing hotels
		tables = parsed_html.find_all("div", {"class" : "cat-prod-row-body"})

		# Print the numbers of the hotels
		print "Found %s records." % len(tables)

		# Empty helpers
		items = []
		count = 0

		# Looping the HTML elements and print properties for each hotel
		for table in tables:
		    name = table.find("strong", {"class" : "cat-prod-row-name"})
		    price = table.find("strong", {"class" : re.compile(r".*\bprice\b.*")})
		    category = table.find("p", {"class" : "cat-prod-row-category"})

		    items.append(process_data(name, price, category))
		    count += 1

		if count > 0:
			# Save array with data to csv file
			save_csv_file(filename = filename, array = items)

			# Print end of job info
			print "\n%s records downloaded and saved to %s." % (count, filename)

	else:
		print "Code error: %s" % r.status_code
		
if __name__ == '__main__':

	payload = {
		'':''
	}

	headers = {
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Encoding':'gzip, deflate, sdch',
		'Accept-Language':'pl-PL,pl;q=0.8,en-US;q=0.6,en;q=0.4',
		'Upgrade-Insecure-Requests':'1',
		'Host':'www.ceneo.pl'
	}

	ap = argparse.ArgumentParser()

	ap.add_argument("-p","--product",required=True,help="Product name")
	ap.add_argument("-c","--category",default="",help="Product category")

	args = vars(ap.parse_args())

	product = args['product']
	category = args['category']

	url = "http://www.ceneo.pl/%s;szukaj-%s" % (category, product)

	filename = "%s_pl_ceneo_data.csv" % product

	ceneo_scrap(
		filename=filename,
		url=url,
		payload=payload,
		headers=headers)