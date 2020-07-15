import tweepy
from twitter_config import API_KEY, API_SECRET, ACCESS_SECRET, ACCESS_TOKEN

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='#python').items(3):
    try:
        api.retweet(tweet.id)
    except:
        print('Failed to RT tweet ID', tweet.id)
    pass

for tweet in tweepy.Cursor(api.search, q='#programming').items(3):
    try:
        api.retweet(tweet.id)
    except:
        print('Failed to RT tweet ID', tweet.id)
    pass

for tweet in tweepy.Cursor(api.search, q='#angular').items(3):
    try:
        api.retweet(tweet.id)
    except:
        print('Failed to RT tweet ID', tweet.id)
    pass

