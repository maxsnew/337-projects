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
    return nltk.Text(words)

def main():
    """Nothing to see here yet"""
    return

if __name__ == '__main__':
    main()
