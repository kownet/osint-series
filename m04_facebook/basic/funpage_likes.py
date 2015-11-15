'''
Created by Tomasz Kowalczyk
@tomkowalczyk
http://kownet.info
'''
# You will probably want to remove or comment below line
from _facebook_keys import *

from urlparse import urlparse, parse_qs

import facebook
import csv
import time
import argparse

# You will probably want to uncomment below line
#ACCESS_TOKEN = ''

graph = facebook.GraphAPI(access_token=ACCESS_TOKEN)

def save_csv_file(filename, array):
	with open(filename, 'wb') as f:
			writer = csv.writer(f)
			writer.writerow(["fan_id","fan_category","fan_name"])
			writer.writerows(array)

def process_fan_data(fan_record):

	fan_id = fan_record['id']
	fan_category = fan_record['category']
	fan_name = fan_record['name'].encode('utf-8')

	return (fan_id, fan_category, fan_name)

def get_funpage_fans(fanpage, filename, limit):

	has_more = True
	count = 0
	fans_data = []

	fans_records = graph.get_connections(id = fanpage, connection_name = "likes", limit = limit)
	
	while has_more:
		for fan_record in fans_records['data']:

			fans_data.append(process_fan_data(fan_record))
			
			count += 1
			if count % 5 == 0:
				print "%s likes recognized" % count

		if 'next' in fans_records['paging']:

			next_page_url = fans_records['paging']['next']

			parsed_url = parse_qs(urlparse(next_page_url).query, keep_blank_values=True)

			after = parsed_url['after']

			time.sleep(1)
			
			fans_records = graph.get_connections(id = fanpage, connection_name = "likes", limit = limit, after = after[0])
		else:
			has_more = False

	save_csv_file(filename = filename, array = fans_data)

	print "\nAll of the %s likes downloaded and saved to %s." % (count, filename)

if __name__ == '__main__':

	ap = argparse.ArgumentParser()
	ap.add_argument("-f","--fanpage",required=True,help="Fanpage name")
	ap.add_argument("-l","--limit",default="1",help="Number of gathered likes each API call")

	args = vars(ap.parse_args())

	fanpage = args['fanpage']
	limit = args['limit']

	fans_data_filename = '%s_likes.csv' % fanpage

	get_funpage_fans(
		fanpage = fanpage,
		filename = fans_data_filename,
		limit = limit)