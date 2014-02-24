import json
import nltk

# Lancaster puts 'winning', 'winner', 'wins' all under 'win'

stemmer = nltk.LancasterStemmer()

class Tweet(object):
    def __init__(self, s):
        """Create a tweet from a json string"""
        dat = json.loads(s)
        self.raw  = dat
        self.rawtext = dat['text']
        self.text = nltk.word_tokenize(dat['text'])
        self.stemmed = [stemmer.stem(tok) for tok in self.text]

    def is_win(self):
        return any([
            word in self.stemmed
            for word in ['won', 'win']
        ])

    def __repr__(self):
        return 'Tweet: Text: %s...' % (self.text[:8])