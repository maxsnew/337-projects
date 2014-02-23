import award

import cPickle as pickle
import json
import nltk
import re
import wikipedia as wiki
from nltk import FreqDist

def make_corpus(fn='goldenglobes.json'):
    """Make an nltk Text object from a file of tweets"""
    with open(fn, 'r') as f:
        words = [
            word 
            for l in f
            for word in nltk.word_tokenize(json.loads(l)['text'])
        ]
    return nltk.Text(words, 'Golden Globes Tweets')

def write_corpus(corpus, fn='goldenglobes.pkl'):
    """Serialize a premade corpus to disk"""
    with open(fn, 'w') as f:
        pickle.dump(corpus, f)

def load_pkl(fn):
    with open(fn, 'r') as f:
        return pickle.load(f)
    
def premade_corpus(fn='goldenglobes.pkl'):
    """Load a premade corpus (faster than remaking it)"""
    return load_pkl(fn)

def premade_fdist(fn='fdist.pkl'):
    return load_pkl(fn)

def main():
    """Make the premade corpus, fdist and serialize"""
    corp = make_corpus()
    fdist = nltk.FreqDist(corp)
    write_corpus(corp)
    write_fdist(fdist)
    return

if __name__ == '__main__':
    main()
