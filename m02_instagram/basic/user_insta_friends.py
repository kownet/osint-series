'''
Created by Tomasz Kowalczyk
@tomkowalczyk
http://kownet.info
'''
# You will probably want to remove or comment below line
from _instagram_keys import *

from instagram.client import InstagramAPI

import csv
import argparse

# You will probably want to uncomment below lines
# CLIENT_ID = 
# CLIENT_SECRET = 
# ACCESS_TOKEN = 

api = InstagramAPI(access_token=ACCESS_TOKEN,  
                    client_ips=CLIENT_ID,
                    client_secret=CLIENT_SECRET)

def save_csv_file(filename, array):
	with open(filename, 'wb') as f:
			writer = csv.writer(f)
			writer.writerow(["friend_id","name"])
			writer.writerows(array)

def get_all_user_friends(user_to_track, filename, api):

	user = api.user_search(user_to_track)[0]

	user_follows, next = api.user_followed_by(user.id)

	users = []

	for user in user_follows:
	    users.append([user.id,user.username])

	while next:
	    user_follows, next = api.user_follows(with_next_url=next)
	    for user in user_follows:
	        users.append([user.ids,user.username])

	friends = []
	for user in users:
		friends.append([user[0], user[1]])

	save_csv_file(filename, friends)

if __name__ == '__main__':

	ap = argparse.ArgumentParser()

	ap.add_argument("-u","--user",required=True,help="User to track")

	args = vars(ap.parse_args())

	user_to_track = args['user']

	user_friends_file_name = 'insta_friends_of_%s.csv' % user_to_track

	get_all_user_friends(
		user_to_track=user_to_track,
		filename=user_friends_file_name,
		api=api)