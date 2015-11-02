OSINT - M02 - Gathering data from Instagram
===========================================
##Scripts

###1.1 Discover followers for Instagram user.

How to run this code:

`python user_insta_followers.py -u INSTA_USER_NAME` 

Parameters:

`-u` - *Instagram user name*

Output:

`insta_followers_of_INSTA_USER_NAME.csv`

File Header:

`"follower_id","name"`

Comment:

When having these kind of data about user we then will be able to find out more information about him, For example:

- who are users friends?
- what kind of people they are?
- do they might have any others mutual connections?

###1.2 Discover friends for Instagram user.

How to run this code:

`python user_insta_friends.py -u INSTA_USER_NAME` 

Parameters:

`-u` - *Instagram user name*

Output:

`insta_friends_of_INSTA_USER_NAME.csv`

File Header:

`"friend_id","name"`

Comment:

When having these kind of data about user we then will be able to find out more information about him, For example:

- who are users friends?
- what kind of people they are?
- do they might have any others mutual connections?

###1.3 Get photos of Instagram user.

How to run this code:

`python user_insta_photos.py -u INSTA_USER_NAME -s yes` 

Parameters:

`-u` - *Instagram user name*

`-s` - *yes/no if we want to download all user photos*

Output:

`insta_followers_of_INSTA_USER_NAME.csv`

`user photos as *.jpg files`

File Header:

`"photo_id","photo_url","like_count"`

Comment:

Having such big amount of photos we can of course use those for:

- finding faces on photos,
- trying to recognize concrete places,
- analyze photos and search for some kind of metadata (exif)

##Author:

[Tomasz Kowalczyk](http://kownet.info)