import tweepy
import time
from config import API_KEY, API_SECRET, ACCESS_SECRET, ACCESS_TOKEN


class TwitterService:
    def __init__(self):
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
        try:
            auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
            self.api = tweepy.API(auth)
        except:
            print('Failed to set up Tweepy API')

    def retweet_by_query(self, query, num_tweets=3):
        for tweet in tweepy.Cursor(self.api.search, q=query).items(num_tweets):
            time.sleep(1)
            try:
                self.api.retweet(tweet.id)
                print('Retweeted ID', tweet.id)
            except:
                print('Failed to RT tweet ID', tweet.id)
            pass
