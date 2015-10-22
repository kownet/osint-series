OSINT - M01 - Gathering data from Twitter
=========================================

##Scripts

###1.1 Get user tweets and save them.

How to run this code:

`python all_tweets_from_user.py -u tomkowalczyk` 

Parameters:

`-u` - *Twitter user name*

Output:

`tomkowalczyk_tweets.csv`

File Header:

`"id","created_at","text"`

###1.2 Discover friends for Twitter user.

How to run this code:

`python user_friends.py -u tomkowalczyk` 

Parameters:

`-u` - *Twitter user name*

Output:

`friends_of_tomkowalczyk.csv`

File Header:

`"friend_id","name"`

###1.3 Discover followers for Twitter user.

How to run this code:

`python user_followers.py -u tomkowalczyk` 

Parameters:

`-u` - *Twitter user name*

Output:

`followers_of_tomkowalczyk.csv`

File Header:

`"follower_id","name"`

###1.4 Determine about what people are tweeting at the current moment.

How to run this code:

`python location_trends.py -w 523920` 

Parameters:

`-w` - *WOEID code of location*

Output:

`Output printed in console`

##Additional information

For all of the above code it is sometimes better to uncomment lines such as this `time.sleep(1)` to not call Twitter API so often and avoid API limitations.

##Author:

[Tomasz Kowalczyk](http://kownet.info)