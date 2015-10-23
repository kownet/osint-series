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

import time
import csv
import argparse

# You will probably want to uncomment below lines
# CONSUMER_KEY = 
# CONSUMER_SECRET = 
# ACCESS_TOKEN_KEY = 
# ACCESS_TOKEN_SECRET = 

def init_csv_file(filename):
	with open(filename, 'wb') as f:
			writer = csv.writer(f)
			writer.writerow(["friend_id","name"])

def write_to_csv(filename, array):
	with open(filename, 'a') as f:
			writer = csv.writer(f)
			writer.writerow(array)

def get_all_user_friends(name, auth):

	api = API(auth)

	# get ids for all of the user followers
	ids = []
	for friend in Cursor(api.friends, screen_name=name).items():
	    ids.append(friend.id_str)
	    # time.sleep(1)

	# get information about each user
	for key in range(len(ids)):
		user = api.get_user(ids[key])
		temp_array = [user.id_str, user.screen_name]
		write_to_csv(user_friends_file_name, temp_array)
		# time.sleep(1)

	print "Exported: " + str(len(ids)) + " users."

if __name__ == '__main__':

	auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

	ap = argparse.ArgumentParser()

	ap.add_argument("-u","--user",required=True,help="User to track")

	args = vars(ap.parse_args())

	user_to_track = args['user']

	user_friends_file_name = 'friends_of_%s.csv' % user_to_track

	init_csv_file(user_friends_file_name)

	get_all_user_friends(user_to_track, auth)