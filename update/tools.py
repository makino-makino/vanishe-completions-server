import json
import argparse

from models import find_or_add_tweet, session, Tweet



def load(filename):
    with open(filename) as f:
        data = json.load(f)
    
    for word_dict in data:
        tweet = Tweet()
        tweet.twitterId = word_dict['twitterId']
        tweet.text = word_dict['text']

        find_or_add_tweet(session, tweet)

    session.commit()


parser = argparse.ArgumentParser()
parser.add_argument("command")
parser.add_argument("--file")
args = parser.parse_args()


if args.command == 'load':
    load(args.file)
    
