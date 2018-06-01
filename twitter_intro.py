import os
import json
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

# We use WOE (Where on Earth) IDs to find trends in specific areas
NY_WOE_ID = 2459115 # New York, USA
LON_WOE_ID = 44418 # London, UK
DUB_WOE_ID = 560743 # Dublin, Ireland

# Now let's call the API and get trend data for each place
ny_trends = api.trends_place(NY_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)
dub_trends = api.trends_place(DUB_WOE_ID)

# Organize them into sets of unique values
ny_trends_set = set([trend['name'] for trend in ny_trends[0]['trends']])
lon_trends_set = set([trend['name'] for trend in lon_trends[0]['trends']])
dub_trends_set = set([trend['name'] for trend in dub_trends[0]['trends']])

# And now we can find common trends among multiple places
ny_lon = set.intersection(ny_trends_set, lon_trends_set)
ny_dub = set.intersection(ny_trends_set, dub_trends_set)
lon_dub = set.intersection(lon_trends_set, dub_trends_set)

print('Common trends between NY and London: {}'.format(ny_lon))
print('Common trends between NY and Dublin: {}'.format(ny_dub if len(ny_dub) > 0 else 'None right now.'))
print('Common trends between London and Dublin: {}'.format(lon_dub))