import cPickle as pickle
import json
import nltk
import re

import wikipedia as wiki

# Scraped and then manually filtered out
awards = [u'Best Drama Series',
          u'Best Comedy Series',
          u'Best Actor in a Television Drama Series',
          u'Best Actor in a Television Comedy Series',
          u'Best Actress in a Television Drama Series',
          u'Best Actress in a Television Comedy Series',
          u'Best Mini-Series or Motion Picture made for Television',
          u'Best Actor in a Mini-Series or Motion Picture made for Television',
          u'Best Actress in a Mini-Series or Motion Picture made for Television',
          u'Best Supporting Actor in a Series, Mini-Series or Motion Picture made for Television',
          u'Best Supporting Actress in a Series, Mini-Series or Motion Picture made for Television',
          u'Best Motion Picture Drama',
          u'Best Motion Picture Musical or Comedy',
          u'Best Director', 
          u'Best Actor Motion Picture Drama',
          u'Best Actor  Motion Picture Musical or Comedy',
          u'Best Actress Motion Picture Drama',
          u'Best Actress Motion Picture Musical or Comedy',
          u'Best Supporting Actor Motion Picture', 
          u'Best Supporting Actress Motion Picture',
          u'Best Screenplay',
          u'Best Original Score', 
          u'Best Original Song',
          u'Best Foreign Language Film',
          u'Best Animated Feature Film ']

awards = [ 'Best Motion Picture Drama',
           'Best Motion Picture Musical or Comedy',
           'Best Director',
           'Best Actor Motion Picture Drama'
]

def scrape_awards_section(sec):
    """Get the awards out of a section"""
    return [a for (a,b) in re.findall('(Best[^\(\n]*)(\(since\))?.*', sec)]

def find_awards(page_name='Golden Globes'):
    """Find out what all the awards are!"""
    p = wiki.page(page_name)
    mpawards = [award for award in scrape_awards('Motion picture awards')].split('\n')
    tvawards = [award for award in scrape_awards('Television awards')].split('\n')
    awards = [award 
              for sec in sections 
              for award in scrape_awards_section(p.section(sec)) 
              if not ('awarded' in award.lower()) and not (re.match('[0-9]{4}', award))
    ]
    return awards

def get_tweets(fn='goldenglobes.json'):
    """Make an array of tweets directly loaded from json"""
    with open(fn, 'r') as f:
        tweets = [
            json.loads(l)
            for l in f
        ]

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
