import unittest
from analysis import save_word_from_tweet
from models import find_or_add_tweet, Word, Tweet, session

""" ImportErrorで、直接は実行できないのでインタープリタでドーンするしかNASA """


sample = [
        ("チョン↑パァ！(勝利)", [], "ちょんぱぁ", "チョン↑パァ！(勝利)", 10),
        ("ばにしぇだよ〜wwwww", [], "ばにしぇだよ",  "ばにしぇだよ〜wwwww", 20),
        ("任せてほ↑しい", [], "まかせてほしい", "任せてほ↑しい", 30)
        ]

for text, hashtags, yomi, kaki, n in sample:
    for i in range(1, 6):
        tweet = Tweet()
        tweet.text = text
        tweet.twitterId = 200 + n + i
        find_or_add_tweet(session, tweet)
    word = Word()
    word.yomi = yomi
    word.kaki = kaki
    tmp = save_word_from_tweet(text, hashtags)
    print("generated: ", word.yomi, " => ", word.kaki)
    print("expected:  ", tmp.yomi,  " => ", tmp.kaki)
    print(word.yomi == tmp.yomi and word.kaki == tmp.kaki)

