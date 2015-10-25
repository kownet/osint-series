OSINT - M01 - Gathering data from Twitter
=========================================

##Scripts

###1.1 [Get user tweets and save them](https://github.com/kownet/osint-series/blob/master/m01_twitter/basic/all_tweets_from_user.py).

How to run this code:

`python all_tweets_from_user.py -u tomkowalczyk` 

Parameters:

`-u` - *Twitter user name*

Output:

`tomkowalczyk_tweets.csv`

File Header:

`"id","created_at","text"`

Comment:

When having these kind of data about user we then will be able to find out more information using other technics, For example:

- what is interesting for this user?
- about what he tweets?

###1.2 [Discover friends for Twitter user](https://github.com/kownet/osint-series/blob/master/m01_twitter/basic/user_friends.py).

How to run this code:

`python user_friends.py -u tomkowalczyk` 

Parameters:

`-u` - *Twitter user name*

Output:

`friends_of_tomkowalczyk.csv`

File Header:

`"friend_id","name"`

Comment:

When having these kind of data about user we then will be able to find out more information about specific user, For example:

- who are users friends?
- what kind of people they are?
- do they might have any others mutual connections?

###1.3 [Discover followers for Twitter user](https://github.com/kownet/osint-series/blob/master/m01_twitter/basic/user_followers.py).

How to run this code:

`python user_followers.py -u tomkowalczyk` 

Parameters:

`-u` - *Twitter user name*

Output:

`followers_of_tomkowalczyk.csv`

File Header:

`"follower_id","name"`

Comment:

When having these kind of data about user we then will be able to find out more information about specific user, For example:

- who are users whom user is following?
- what kind of people they are?
- do they might have any others mutual connections?

###1.4 [Determine about what people are tweeting at the current moment](https://github.com/kownet/osint-series/blob/master/m01_twitter/basic/location_trends.py).

How to run this code:

`python location_trends.py -w 523920` 

Parameters:

`-w` - *WOEID code of location*

Output:

`Output printed in console`

Comment:

When having these kind of data about user we then will be able to find out more information about specific region, For example:

- what is happening there?
- what interests people out there?

##Additional information

For all of the above code it is sometimes better to uncomment lines such as this `time.sleep(1)` to not call Twitter API so often and avoid API limitations.

##Author:

[Tomasz Kowalczyk](http://kownet.info)