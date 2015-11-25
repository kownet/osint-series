'''
Created by Tomasz Kowalczyk
@tomkowalczyk
http://kownet.info
'''
# You will probably want to remove or comment below line
from _wikimapia_keys import *

from wikimapia_api import API

import csv
import argparse

# You will probably want to uncomment below line
# ACCESS_TOKEN = ''

places_data_filename = 'places_data.csv'

def save_csv_file(filename, array):
	with open(filename, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["place_id","title","urlhtml","lon","lat"])
		writer.writerows(array)

def process_place(place):
	place_id = 'NA' if 'id' not in place.keys() else place['id']
	title = 'NA' if 'title' not in place.keys() else place['title'].encode('utf-8')
	urlhtml = 'NA' if 'title' not in place.keys() else place['urlhtml'].encode('utf-8')
	lon = 'NA' if 'title' not in place.keys() else place['location']['lon']
	lat = 'NA' if 'title' not in place.keys() else place['location']['lat']

	return (place_id,title,urlhtml,lon,lat)

def get_places_from_bb(apitoken, lon_min, lat_min, lon_max, lat_max):

	API.config.key = apitoken
	API.config.language = 'en'
	API.config.compression = False

	places = API.places.inside(lon_min, lat_min, lon_max, lat_max)

	places_data = []
	count = 0

	for place in places:
		places_data.append(process_place(place))

		count += 1
		
		if count % 25 == 0:
			print "%s places downloaded" % count 

	save_csv_file(filename = places_data_filename, array = places_data)

	print "\nAll of the %s places downloaded and saved to %s." % (count, places_data_filename)

if __name__ == '__main__':

	ap = argparse.ArgumentParser()
	ap.add_argument("-lon_min","--longitude_minimal",default=20.9977,help="Place minimal longitude")
	ap.add_argument("-lat_min","--latitude_minimal",default=52.2283,help="Place minimal latitude")
	ap.add_argument("-lon_max","--longitude_maximum",default=21.0132,help="Place maximum longitude")
	ap.add_argument("-lat_max","--latitude_maximum",default=52.2334,help="Place maximum latitude")

	args = vars(ap.parse_args())

	longitude_minimal = args['longitude_minimal']
	latitude_minimal = args['latitude_minimal']
	longitude_maximum = args['longitude_maximum']
	latitude_maximum = args['latitude_maximum']
	
	get_places_from_bb(ACCESS_TOKEN, 
		lon_min = float(longitude_minimal), 
		lat_min = float(latitude_minimal), 
		lon_max = float(longitude_maximum), 
		lat_max = float(latitude_maximum))