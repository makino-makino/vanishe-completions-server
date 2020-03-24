import json
import argparse

from models import find_or_add_words, session, Word



def load(filename):
    with open(filename) as f:
        data = json.load(f)
    
    for word_dict in data:
        word = Word()
        word.yomi = word_dict['yomi']
        word.kaki = word_dict['kaki']

        find_or_add_words(session, word)

    session.commit()
    

parser = argparse.ArgumentParser()
parser.add_argument("command")
parser.add_argument("--file")
args = parser.parse_args()


if args.command == 'load':
    load(args.file)
    
