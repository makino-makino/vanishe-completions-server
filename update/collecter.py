import json
from pprint import pprint

import tweepy
from config import consumer_key, consumer_secret, access_token, access_secret

ACCOUNT = 'a_a_vanilove'

def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    data = []

    tweets = api.user_timeline(screen_name=ACCOUNT, count=10)
    for tweet in tweets:
        data.append({'id': tweet.id, 'text': tweet.text})

    pprint(data)

    # with open('data.json', 'w') as f:
        # json.dump(data, f, ensure_ascii=False)


if __name__ == '__main__':
    main()