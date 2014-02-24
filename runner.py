import cPickle as pickle
import json
import nltk
import re

from tweet import Tweet

"""
Once runner.pkl is made (use main), just do 
>>> from runner import Runner
>>> r = Runner.read()
And r has everything you need! r.corpus is the corpus, r.fdist the frequency distribution and r.awards is the awards
"""

class Runner(object):
    def __init__(self, awards, fn='goldenglobes.json'):
        self.tweets = Runner.read_tweets(fn)
        # corpus = nltk.Text(
        #     [ word for t in self.tweets for word in t.text ]
        #     , 'Golden Globe Tweets')
        # self.fdist = nltk.FreqDist(corpus)
        self.awards = awards

    def write(self, fn='runner.pkl'):
        with open(fn, 'w') as f:
            pickle.dump(self, f)
            
    def winners(self):
        """Return a map of award -> winner"""
        return { 
            award: award.find_winner(self.tweets)
            for award in self.awards
        }
        
    def hosts(self):
        """Returns top 5 candidates for host"""
        relevant = [
            t for t in self.tweets
            if 'hosting' in t.rawtext
        ]
        return Tweet.common_names(relevant)[:5]
        
    def presenters(self):
        """Return a map of award -> presenter candidates"""
        return {
            award: award.find_presenter(self.tweets)
            for award in self.awards
        }

    def nominees(self):
        """Hard coded :/"""
        return {
            award: award.nominees
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
        
    @staticmethod
    def read_tweets(fn='goldenglobes.json'):
        with open(fn, 'r') as f:
            tweets = [ Tweet(l) for l in f ]
        return tweets

if __name__ == '__main__':
    r = Runner.read()
    hosts = r.hosts()
    print 'Top candidates for host:'
    for host in hosts:
        print host

    print 'AWARDS'
    winners = r.winners()
    presenters = r.presenters()
    for award in r.awards:
        winner = winners[award]
        presenter_cands = presenters[award]
        print '********'
        print award
        print 'Nominees'        
        for nom in award.nominees:
            print nom

        print
        if len(presenter_cands) == 0:
            print 'No presenter candidates found'
        else:
            print 'Presenter candidates:'
            for pres in presenter_cands:
                print pres
        print
        print 'Winner:'
        print winner
        print '********'
