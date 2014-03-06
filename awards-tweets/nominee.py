import nltk

class Nominee(object):
    def __init__(self, name):
        if name == '':
            raise Exception('Nominee must have nonempty name')
        self.name = name
        self.nametoks = nltk.word_tokenize(name)
        
    def short_name(self, fdist):
        """The most useful portion of this name"""
        # TODO: pick tok using the fdist
        return self.nametoks[0]
        
    def __repr__(self):
        return 'Nominee: Name=%s' % self.name
