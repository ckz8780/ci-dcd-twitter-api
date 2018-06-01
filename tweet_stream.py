# A simple stream listener for outputting tweets to a json file, limited to 250 tweets

import os
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

# Set up authentication vars (see README.md)
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
OAUTH_TOKEN = os.getenv('OAUTH_TOKEN')
OAUTH_TOKEN_SECRET = os.getenv('OAUTH_TOKEN_SECRET')

# Set of hashtags we'll filter for
keyword_list = ['python', 'javascript', 'php', 'C#']
limit = 250

# Extend the base StreamListener class
class MyStreamListener(StreamListener):
    
    def __init__(self):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
    
    # On data is executed whenever data comes into the stream
    def on_data(self, data):
        if self.num_tweets < limit:
            self.num_tweets += 1
            try:
                with open('tweet_mining.json', 'a') as tweet_file:
                    tweet_file.write(data)
                    return True
            except BaseException as e:
                print('Failed on_data: {}'.format(e))
            return True
        else:
            return False
        
    def on_error(self, status):
        print(status)
        return True
        
# Authenticate
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Now dump all tweets containing a hashtag in our keyword list into a json file
twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list)
    