'''
Created by Tomasz Kowalczyk
@tomkowalczyk
http://kownet.info
'''
# You will probably want to remove or comment below line
from _facebook_keys import *

from urlparse import urlparse, parse_qs

import facebook
import json
import time
import datetime
import csv
import argparse

# You will probably want to uncomment below line
#ACCESS_TOKEN = ''

FIELDS = 'id,message,link,type,created_time,shares,likes.limit(1).summary(True),comments.limit(1).summary(True)'

graph = facebook.GraphAPI(access_token=ACCESS_TOKEN)

def save_csv_file(filename, array):
	with open(filename, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["item_id","item_message","item_link_name","item_type","status_link","created_time","num_likes","num_comments","num_shares"])
		writer.writerows(array)

def process_funpage_feed_data(fb_record):

	item_id = fb_record['id']
	item_message = '' if 'message' not in fb_record.keys() else fb_record['message'].encode('utf-8')
	item_link_name = '' if 'name' not in fb_record.keys() else fb_record['name'].encode('utf-8')
	item_type = fb_record['type']
	status_link = '' if 'link' not in fb_record.keys() else fb_record['link']

	item_published = datetime.datetime.strptime(fb_record['created_time'],'%Y-%m-%dT%H:%M:%S+0000')
	item_published = item_published + datetime.timedelta(hours=-5) # EST
	item_published = item_published.strftime('%Y-%m-%d %H:%M:%S')

	num_likes = 0 if 'likes' not in fb_record.keys() else fb_record['likes']['summary']['total_count']
	num_comments = 0 if 'comments' not in fb_record.keys() else fb_record['comments']['summary']['total_count']
	num_shares = 0 if 'shares' not in fb_record.keys() else fb_record['shares']['count']

	return (item_id, item_message, item_link_name, item_type, status_link, item_published, num_likes, num_comments, num_shares)

def get_funpage_info(fb_request, filename, objects_limit):

	has_more = True
	count = 0
	feed_data = []

	fb_records = graph.get_object(fb_request, fields = FIELDS, limit = objects_limit)

	while has_more:
		for fb_record in fb_records['data']:

			feed_data.append(process_funpage_feed_data(fb_record))

			count += 1
			if count % 25 == 0:
				print "%s records downloaded" % count

		if 'paging' in fb_records.keys():

			next_page_url = fb_records['paging']['next']

			parsed_url = parse_qs(urlparse(next_page_url).query, keep_blank_values=True)

			until = parsed_url['until']

			until_time = time.strftime('%Y-%m-%d', time.localtime(float(until[0])))

			paging_token = parsed_url['__paging_token']

			time.sleep(2)
			
			fb_records = graph.get_object(fb_request, fields = FIELDS, limit = objects_limit, until = until_time, paging_token = paging_token)
		else:
			has_more = False

	save_csv_file(filename = filename, array = feed_data)

	print "\nAll of the %s records downloaded and saved to %s." % (count, filename)

if __name__ == '__main__':

	ap = argparse.ArgumentParser()
	ap.add_argument("-f","--fanpage",required=True,help="Fanpage name")
	ap.add_argument("-l","--limit",default="25",help="Number of gathered likes each API call")

	args = vars(ap.parse_args())

	fanpage = args['fanpage']
	limit = args['limit']

	feed_data_filename = '%s_feed_data.csv' % fanpage

	request = '%s/feed' % fanpage

	get_funpage_info(
		fb_request=request,
		filename=feed_data_filename,
		objects_limit=limit)