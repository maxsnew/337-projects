import json
import nltk
import re

# Lancaster puts 'winning', 'winner', 'wins' all under 'win'
stemmer = nltk.LancasterStemmer()

class Tweet(object):
    def __init__(self, s):
        """Create a tweet from a json string"""
        dat = json.loads(s)
        self.rawtext = dat['text']
        text = nltk.word_tokenize(dat['text'])
        self.stemmed = [stemmer.stem(tok) for tok in text]

    def is_win(self):
        return any([
            word in self.stemmed
            for word in ['won', 'win']
        ])

    def has_tok(self, tok):
        return (tok in self.stemmed)
        
    def __repr__(self):
        return 'Tweet: Text: %s...' % (self.rawtext.encode('utf-8'))

    @staticmethod
    def common_names(tweets):
        txt = ' '.join([t.rawtext for t in tweets])
        fd = nltk.FreqDist(re.findall('[A-Z][a-z]+ [A-Z][a-z]+', txt))
        names = [
            name for name in fd.keys()
            if name != 'Golden Globes' and not ('Best' in name)
        ]
        return names
