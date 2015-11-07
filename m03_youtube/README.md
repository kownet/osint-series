OSINT - M03 - Gathering data from YouTube
=========================================
##Scripts

###1.1 Search for video with keywords.

How to run this code:

`python movie_keywords.py --q test --max-results 10` 

Parameters:

`--q` - *Query to search*

`--max-results` - *Number of results to return*

Output:

`Output printed in console`

Comment:

The above script will let you search YouTube for a specific phrase and get the movie results.

###1.2 Search for video with keywords and geolocation.

How to run this code:

`python geolocation_keywords.py --q test --location "52.23,21.01" --location-radius 5km --max-results 10` 

Parameters:

`--q` - *Query to search*

`--location` - *Coordinates of the place*

`--location-radius` - *Radius*

`--max-results` - *Number of results to return*

Output:

`Output printed in console`

Comment:

The above script will let you search YouTube for specific content like: movies, playlists etc which was uploaded at the specified location.


##Author:

[Tomasz Kowalczyk](http://kownet.info)