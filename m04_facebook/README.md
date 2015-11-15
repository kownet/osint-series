OSINT - M04 - Gathering data from Facebook
==========================================
##Scripts

###1.1 Download all feed from selected funpage.

How to run this code:

`python funpage_feed.py -f FANPAGE_NAME -l 25` 

Parameters:

`-f` - *Fanpage name*

`-l` - *Number of gathered elements each API call*

Output:

`FANPAGE_NAME_feed_data.csv`

File Header:

`"item_id","item_message","item_link_name","item_type","status_link","created_time","num_likes","num_comments","num_shares"`

Comment:

This script could be very valuable in many situations. We want to know what posts were the most popular. We can also scrape feed from few similar fanpage and compare them.

###1.2 Find out what fanpages are liked by another fanpage.

How to run this code:

`python funpage_likes.py -f FANPAGE_NAME -l 1` 

Parameters:

`-f` - *Fanpage name*

`-l` - *Number of gathered likes each API call*

Output:

`FANPAGE_NAME_likes.csv`

File Header:

`"fan_id","fan_category","fan_name"`

Comment:

This script will allow us easily find out what fanpages are liked by particular fanpage and going further this way find out the relations between fanpages.

###1.3 Search Facebook for specific phrase.

How to run this code:

`python search_fb.py -q dev -t page -l 5` 

Parameters:

`-q` - *Query to search*

`-t` - *Type of the results, default "page"*

`-l` - *Number of returned results*

Output:

`Output printed in console`

##Author:

[Tomasz Kowalczyk](http://kownet.info)