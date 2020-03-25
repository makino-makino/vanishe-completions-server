import json
from pprint import pprint

import tweepy
from config import consumer_key, consumer_secret, access_token, access_secret

from models import find_or_add_tweet, session, Tweet

ACCOUNT = 'a_a_vanilove'
COUNT = 20
THRESHOLD = 4

def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    results = api.user_timeline(screen_name=ACCOUNT, count=COUNT)
    for r in results:
        tweet = Tweet()
        tweet.twitterId = r.id
        tweet.text = r.text

        lines = r.text.splitlines()
        for l in lines:
            find_word(l)

        find_or_add_tweet(session, tweet)

        
    
    session.commit()

def find_word(line):
    res = session.query(Tweet).filter(Tweet.text.like("%" + line + "%"))
    if res.count() > THRESHOLD:
        print("fonud")
        find_or_add_word(line)


if __name__ == '__main__':
    main()
