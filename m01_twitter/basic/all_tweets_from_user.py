'''
Code below is inspired by this gist https://gist.github.com/yanofsky/5436496

Modification by Tomasz Kowalczyk
@tomkowalczyk
http://kownet.info
'''
# You will probably want to remove or comment below line
from _twitter_keys import *

from tweepy import OAuthHandler
from tweepy import API

import csv
import argparse

# You will probably want to uncomment below lines
# CONSUMER_KEY = 
# CONSUMER_SECRET = 
# ACCESS_TOKEN_KEY = 
# ACCESS_TOKEN_SECRET = 

def all_tweets_from_user(screen_name, auth):

	api = API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets downloaded so far" % (len(alltweets))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)

if __name__ == '__main__':

	auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

	ap = argparse.ArgumentParser()

	ap.add_argument("-u","--user",required=True,help="User to track")

	args = vars(ap.parse_args())

	user_to_track = args['user']
	
	all_tweets_from_user(user_to_track, auth)