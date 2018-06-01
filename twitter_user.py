# A small script for showing info about a user, using the Twitter API

import os
import tweepy
from tweepy import OAuthHandler

# Set up authentication vars (see README.md)
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
OAUTH_TOKEN = os.getenv('OAUTH_TOKEN')
OAUTH_TOKEN_SECRET = os.getenv('OAUTH_TOKEN_SECRET')

# Authenticate
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

# Get the user object
user = api.get_user('@realDonaldTrump')

# Print out their screen name and follower count
print('User {} has {} followers.\n'.format(user.screen_name, user.followers_count))

# Get follower count for the user's friends
for friend in user.friends():
    print('Donald\'s friend {} has {} followers.'.format(friend.screen_name, friend.followers_count))

# Print the 10 most recent tweets from your own timeline
for status in tweepy.Cursor(api.home_timeline).items(10):
    print(status.text)