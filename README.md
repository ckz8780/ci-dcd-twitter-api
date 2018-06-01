# Welcome!

This is a simple app to play with the Twitter API. It is part of the Data Centric Development module for CodeInstitute.

It has been lightly extended to eliminate maintaining Twitter app key information in source control for those who are building a test app using a real Twitter account that they actually care about. Follow the instructions in this README to make sure your credentials and account stay safe!

#### Requirements:

- Python3
- Tweepy (`sudo pip3 install tweepy`)
- PrettyTable (`sudo pip3 install PrettyTable`)
- A Twitter account
- A Twitter app you've created at app.twitter.com
- Authentication tokens/keys for your app

#### Setup (Linux/OSX):

To set up authentication, just export environment variables for your app's auth info. If you want them to be persistent, add them to your .profile and/or .bash_profile and/or .bashrc, or environment.plist (for certain OS X versions), depending on your preferences.

    export CONSUMER_KEY=[your app's consumer key]
    export CONSUMER_SECRET=[your app's consumer secret key]
    export OAUTH_TOKEN=[your app's oauth token]
    export OAUTH_TOKEN_SECRET=[your app's oauth token secret]

##### For Windows, use `set` in place of `export` above.

#### Usage:

    python3 twitter_intro.py
    python3 tweet_access.py