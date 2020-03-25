from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, Text, Float, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker


ENGINE = create_engine('sqlite:///db.sqlite3', echo=True)
Base = declarative_base()

session = scoped_session(
    sessionmaker(
        bind = ENGINE,
        autocommit=False,
    )
)

class Tweet(Base):
    '''ツイートのデータ'''
    __tablename__ = 'tweets'

    _id = Column('id', Integer, primary_key = True)
    twitterId = Column('twitterId', Integer)
    text = Column('text', Text)


class Word(Base):
    '''辞書ワードのデータ'''
    __tablename__ = 'words'

    _id = Column('id', Integer, primary_key = True)
    kaki = Column('kaki', Text)
    yomi = Column('yomi', Text)


def find_or_add_tweet(session, tweet):
    tweets = session.query(Tweet).\
        filter(Tweet.twitterId==tweet.twitterId).\
        all()

    if not tweets:
        session.add(tweet)
        session.commit()

def find_or_add_word(session, word):
    words = session.query(Word).\
        filter(Word.kaki==word.kaki and Word.yomi == word.yomi).\
        all()

    if not words:
        session.add(word)
        session.commit()


Base.metadata.create_all(ENGINE)


if __name__=='__main__':
    tweet = Tweet()
    tweet.twitterId = 1
    tweet.text = 'hello'

    word = Word()
    word.yomi = 'ばにしぇだよ'
    word.kaki = 'ばにしぇだよ〜〜〜www'

    session.add(tweet)
    session.add(word)

    session.commit()
