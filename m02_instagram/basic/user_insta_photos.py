'''
Created by Tomasz Kowalczyk
@tomkowalczyk
http://kownet.info
'''
# You will probably want to remove or comment below line
from _instagram_keys import *

from instagram.client import InstagramAPI

import csv
import urllib
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
			writer.writerow(["photo_id","photo_url","like_count"])
			writer.writerows(array)

def get_all_user_photos(user_to_track, filename, api, save_files, number):

	user = api.user_search(user_to_track)[0]

	all_photos = []

	new_photos = api.user_recent_media(user_id = user.id, count = number)

	all_photos.extend(new_photos[0])

	oldest_image = all_photos[-1]

	oldest_id = all_photos[-1].id

	print "Downloaded %s, where last id is: %s" % (len(all_photos), oldest_id)

	while oldest_id is not 'null':

		new_photos = api.user_recent_media(user_id = user.id, count = number, max_id = oldest_id)

		all_photos.extend(new_photos[0])

		try:
			oldest_id = new_photos[0][-1].id

			print "Downloaded %s, where last id is: %s" % (len(all_photos), oldest_id)

		except IndexError:
			oldest_id = 'null'
		
	outphotos = [[photo.id, photo.images['standard_resolution'].url, photo.like_count] for photo in all_photos]

	save_csv_file(filename, outphotos)

	if(save_files == 'yes'):
		count = 0
		for photo in all_photos:
			filename = "%s_%s_instagram.jpg" % (user_to_track, str(count))
			urllib.urlretrieve(photo.images['standard_resolution'].url, filename)
			count = count + 1

if __name__ == '__main__':

	ap = argparse.ArgumentParser()

	ap.add_argument("-u","--user",required=True,help="User to track")
	ap.add_argument("-s",'--save',required=True,help="Save files?")

	args = vars(ap.parse_args())

	user_to_track = args['user']
	save_files = args['save']

	user_photos_file_name = 'insta_photos_of_%s.csv' % user_to_track

	photos_to_download_once = 20

	get_all_user_photos(
		user_to_track=user_to_track,
		filename=user_photos_file_name,
		api=api, 
		save_files=save_files,
		number=photos_to_download_once)