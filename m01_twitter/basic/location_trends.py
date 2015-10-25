'''
@author Tomasz Kowalczyk
@tomkowalczyk
http://kownet.info
'''
# You will probably want to remove or comment below line
from _twitter_keys import *

from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor

import argparse

# You will probably want to uncomment below lines
# CONSUMER_KEY = 
# CONSUMER_SECRET = 
# ACCESS_TOKEN_KEY = 
# ACCESS_TOKEN_SECRET = 

def get_location_trends(locations, auth):

	api = API(auth)

	trends = api.trends_place(locations)
	data = trends[0]
	trends_data = data['trends']
	names = [trend['name'] for trend in trends_data]

	print names

if __name__ == '__main__':

	auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

	ap = argparse.ArgumentParser()

	ap.add_argument("-w","--woeid",required=True,help="WOEID code")

	args = vars(ap.parse_args())

	woeid = args['woeid']
	
	get_location_trends(woeid, auth)