OSINT - M06 - Gathering geographic data with WikiMapia
======================================================
##Scripts

###1.1 [Get places from Wikimapia based on provided BoundingBox](https://github.com/kownet/osint-series/blob/master/m06_geodata/basic/get_places.py).

How to run this code:

`python get_places.py -lon_min 20.99 -lat_min 52.22 -lon_max 21.01 -lat_max 52.23` 

Parameters:

`-lon_min` - *Place minimal longitude*

`-lat_min` - *Place minimal latitude*

`-lon_max` - *Place maximum longitude*

`-lat_max` - *Place maximum latitude*

Output:

`places_data.csv`

File Header:

`"place_id","title","urlhtml","lon","lat"`

###1.2 [Search for place nearest to the provided geo location](https://github.com/kownet/osint-series/blob/master/m06_geodata/basic/search_for_place.py).
How to run this code:

`python search_for_place.py -n tarasy -long 21.01 -lat 52.22` 

Parameters:

`-n` - *Name of the place*

`-long` - *Place longitude*

`-lat` - *Place latitude*

Output:

`Output printed in console`


##Author:

[Tomasz Kowalczyk](http://kownet.info)