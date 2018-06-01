# A small script for showing tweet popularity using the Twitter API

import os
import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter

# Set up authentication vars (see README.md)
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
OAUTH_TOKEN = os.getenv('OAUTH_TOKEN')
OAUTH_TOKEN_SECRET = os.getenv('OAUTH_TOKEN_SECRET')

# Authenticate
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

# Get all tweets for the search query
count = 150
query = 'Bacon'
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

# Minimum amount of times a status is retweeted to gain entry to our list (change to whatever your preferences)
min_retweets = 10

# Now we add tweets to our list if the number of retweets is greater than our minimum above
pop_tweets = [status for status in results if status._json['retweet_count'] > min_retweets]

# And generate a list of tuples associating each tweet's text w/ its retweet count
tweet_tups = [(tweet._json['text'].encode('utf-8'), tweet._json['retweet_count']) for tweet in pop_tweets]

# Finally, sort using itemgetter in descending order
most_popular = sorted(tweet_tups, key=itemgetter(1), reverse=True)[:5]

# And put them into a nice pretty table
table = PrettyTable(field_names=['Text', 'Retweet Count'])
for k, v in most_popular:
    table.add_row([k, v])
    
# Set max width and align columns 
table.max_width['Text'] = 50
table.align['Text'], table.align['Retweet Count'] = 'l', 'r'

print(table)

