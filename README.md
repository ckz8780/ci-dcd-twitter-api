# Welcome!

This is a simple app to play with the Twitter API. It is part of the Data Centric Development module for CodeInstitute.

It has been lightly extended to eliminate maintaining Twitter app key information in source control for those who are building a test app using a real Twitter account that they actually care about. Follow the instructions in this README to make sure your credentials and account stay safe! This is a bit different from the module which uses a separate file added to the .gitignore file, but works the same way, except that by doing it this way you will not have plaintext keys in your commit history from the beginning of the module.

#### Requirements:

- Python3
- Tweepy (`sudo pip3 install tweepy`)
- PrettyTable (`sudo pip3 install PrettyTable`)
- A Twitter account
- A Twitter app you've created at app.twitter.com
- Authentication tokens/keys for your app

#### Setup (Linux/OSX):

To set up authentication, just export environment variables for your app's auth info. If you want them to be persistent, add them to your .profile, .bash_profile and/or .bashrc, or environment.plist (for certain OS X versions), depending on your preferences.

    export CONSUMER_KEY=[your app's consumer key]
    export CONSUMER_SECRET=[your app's consumer secret key]
    export OAUTH_TOKEN=[your app's oauth token]
    export OAUTH_TOKEN_SECRET=[your app's oauth token secret]

##### For Windows, use `set` in place of `export` above.

#### Usage:

    # Use WhereOnEarth IDs to find trends in various areas
    python3 twitter_intro.py
    
    # Find, organize and analyze various tweet data
    python3 tweet_access.py
    
    # Get user info like followers, friends, and timeline info
    python3 twitter_user.py
    
    # Learn about tweet popularity based on number of retweets
    python3 tweet_popularity.py
    
    # Stream some tweets into a json file using the Twitter Stream API
    python3 twitter_stream.py