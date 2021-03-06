import json
import re

from pprint import pprint
from pykakasi import kakasi as kks

import tweepy
from config import consumer_key, consumer_secret, access_token, access_secret
from models import find_or_add_tweet, find_or_add_word, session, Tweet, Word

from analysis import save_word_from_tweet


ACCOUNT = 'a_a_vanilove'
COUNT = 20

def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    results = api.user_timeline(screen_name=ACCOUNT, count=COUNT, tweet_mode="extended")

    for r in results:
        save_word_from_tweet(r.full_text, r.entities['hashtags'])

        tweet = Tweet()
        tweet.twitterId = r.id
        tweet.text = r.full_text
        find_or_add_tweet(session, tweet)





if __name__ == '__main__':
    main()
