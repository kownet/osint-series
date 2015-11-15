'''
Created by Tomasz Kowalczyk
@tomkowalczyk
http://kownet.info
'''
# You will probably want to remove or comment below line
from _facebook_keys import *

import facebook
import argparse

# You will probably want to uncomment below line
#ACCESS_TOKEN = ''

def get_search_result(term, type_to_s, limit):

	graph = facebook.GraphAPI(access_token=ACCESS_TOKEN)
	search_result = graph.request("search", {'q' : term, 'type' : type_to_s, 'limit' : limit})

	print search_result

if __name__ == '__main__':

	ap = argparse.ArgumentParser()
	ap.add_argument("-q","--query",required=True,help="Search phrase")
	ap.add_argument("-t","--type", default="page",help="Type to search")
	ap.add_argument("-l","--limit",default="5",help="Number of results")

	args = vars(ap.parse_args())

	search_term = args['query']
	search_type = args['type']
	search_limit = args['limit']

	get_search_result(
		term = search_term, 
		type_to_s = search_type , 
		limit = search_limit)