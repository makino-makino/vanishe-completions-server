import json
import re

from pprint import pprint
from pykakasi import kakasi as kks

import tweepy
from config import consumer_key, consumer_secret, access_token, access_secret
from models import find_or_add_tweet, session, Tweet, Word

ACCOUNT = 'a_a_vanilove'
COUNT = 20
THRESHOLD = 4
PEINGS_TAGS = ['Peing', 'peing', '質問箱']

def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    kakasi = kks()
    kakasi.setMode('K', 'H')
    kakasi.setMode('J', 'H')
    conv = kakasi.getConverter()

    results = api.user_timeline(screen_name=ACCOUNT, count=COUNT)

    for r in results:

        hashtag_tags = r.entities['hashtags']
        hashtag = ""
        if hashtag_tags:
            hashtag = hashtag_tags[0]['text']
        text = r.text

        text = filter_text(text, hashtag)

        if not text:
            pass

        lines = text.splitlines()
        for l in lines:
            if find_word(l):
                word = Word()
                word.kaki = l
                word.yomi = conv.do(l)
                print(word.kaki, conv.do(l))
                # find_or_add_word(session, word)

        tweet = Tweet()
        tweet.twitterId = r.id
        tweet.text = text
        find_or_add_tweet(session, tweet)

    session.commit()

def find_word(line):
    print()
    if not line:
        return
    print("==== search: ```" + line + "''' ====")
    res = session.query(Tweet).filter(Tweet.text.like("%" + line + "%"))

    """ しきい値より多かったら """
    if res.count() > THRESHOLD:
        print("~~~~ fonud ~~~~")
        for i in res:
            print(i.text)
        return True
    return False


def filter_text(text, hashtag):
  '''文字列とハッシュタグからフィルタリングを行う'''
  if len(text) > 2 and text[:2] == 'RT':
    return ''
  
  if len(text) > 11 and text[:11] == 'ばにしぇ🥤の質問箱です':
    return ''

  if hashtag in PEINGS_TAGS:
    return ''

  text = re.sub(r'@[0-9a-zA-Z_]{1,15} ', '', text)
  text = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', '', text)

  text = re.sub(r'\A\n+', '', text)
  text = re.sub(r'\A +', '', text)


  return text


if __name__ == '__main__':
    main()
