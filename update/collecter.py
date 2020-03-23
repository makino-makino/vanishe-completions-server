import json
from pprint import pprint

import tweepy
from config import consumer_key, consumer_secret, access_token, access_secret

from models import find_or_add_tweet, session, Tweet

ACCOUNT = 'a_a_vanilove'
COUNT = 20

def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    results = api.user_timeline(screen_name=ACCOUNT, count=COUNT)
    for r in results:
        tweet = Tweet()
        tweet.twitterId = r.id
        tweet.text = r.text

        find_or_add_tweet(session, tweet)
        
    
    session.commit()



if __name__ == '__main__':
    main()