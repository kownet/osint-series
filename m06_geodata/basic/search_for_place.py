'''
Created by Tomasz Kowalczyk
@tomkowalczyk
http://kownet.info
'''
# You will probably want to remove or comment below line
from _wikimapia_keys import *

from wikimapia_api import API
import argparse

# You will probably want to uncomment below line
# ACCESS_TOKEN = ''

def search_for_place(apitoken, phrase, lon, lat):

	API.config.key = apitoken
	API.config.language = 'en'
	API.config.compression = False

	places = API.places.search(phrase, lon, lat)
	
	print(places[0])

if __name__ == '__main__':

	ap = argparse.ArgumentParser()
	ap.add_argument("-n","--name",required=True,help="Name of the place")
	ap.add_argument("-long","--longitude",default="21.00",help="Place longitude")
	ap.add_argument("-lat","--latitude",default="52.22",help="Place latitude")

	args = vars(ap.parse_args())

	name = args['name']
	longitude = args['longitude']
	latitude = args['latitude']

	search_for_place(ACCESS_TOKEN,
		name,
		longitude,
		latitude)