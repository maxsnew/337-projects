import cPickle as pickle
import json
import nltk

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
    
def premade_corpus(fn='goldenglobes.pkl'):
    """Load a premade corpus (faster than remaking it)"""
    with open(fn, 'r') as f:
        return pickle.load(f)

def main():
    """Make the premade corpus and serialize"""
    corp = make_corpus()
    write_corpus(corp)
    return

if __name__ == '__main__':
    main()
