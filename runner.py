import cPickle as pickle
import json
import nltk

"""
Once runner.pkl is made (use main), just do 
>>> from runner import Runner
>>> r = Runner.read()
And r has everything you need! r.corpus is the corpus, r.fdist the frequency distribution and r.awards is the awards
"""

class Runner(object):
    def __init__(self, awards, fn='goldenglobes.json'):
        self.corpus = Runner.make_corpus(fn)
        self.fdist = nltk.FreqDist(self.corpus)
        self.awards = awards

    def write(self, fn='runner.pkl'):
        with open(fn, 'w') as f:
            pickle.dump(self, f)
            
    def winners(self):
        """Return a map of award -> winner"""
        return { 
            award: award.find_winner(self.fdist)
            for award in self.awards
        }
    
    @staticmethod
    def read(fn = 'runner.pkl'):
        with open(fn, 'r') as f:
            return pickle.load(f)

    @staticmethod
    def make_corpus(fn='goldenglobes.json'):
        """Make an nltk Text object from a file of tweets"""
        with open(fn, 'r') as f:
            words = [
                word 
                for l in f
                for word in nltk.word_tokenize(json.loads(l)['text'])
            ]
        return nltk.Text(words, 'Golden Globes Tweets')
