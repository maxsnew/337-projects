import cPickle as pickle
import json
import nltk
import re

import wikipedia as wiki

from nltk import FreqDist

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

bestDrama = ['Argo','Django','Pi','Lincoln','Zero']
bestMC = ['Les', 'Exotic','Moonrise','Salmon','Silver']
drama_M = ['Daniel','Richard','John','Joaquin','Denzel']
drama_F = ['Jessica','Marion', 'Helen', 'Naomi', 'Rachel']
MC_male = ['Hugh','Jack','Bradley','Ewan','Bill']
MC_female = ['Jennifer','Emily','Judy','Maggie','Meryl']
support_M = ['Christoph', 'Alan', 'Leonardo','Philip','Tommy']
support_F = ['Anne','Amy','Sally','Helen','Nicole']
director = ['Ben','Kathryn','Ang','Steven','Quentin']
screenplay = ['Quentin','Chris','Tony','David','Mark']
score = ['Mychael','Dario','Alexandre','John','Tom']
song = ['Adele','Keith','Taylor','Claude']
animated = ['Brave', 'Frankenweenie','Transylvania','Rise','Ralph']
foreign = ['Amour','Royal','Intouchables','Tiki','Rust']


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

def winner(corpus):
    from nltk import FreqDist
    fdist = FreqDist(corpus)
    maxm = 0
    winner = ""

    for i in range(len(bestMC)):
      if fdist[bestMC[i]] > maxm:
        maxm = fdist[bestMC[i]]
        winner = bestMC[i]
    print winner 

def main():
    """Make the premade corpus and serialize"""
    corp = make_corpus()
    write_corpus(corp)
    return

if __name__ == '__main__':
    main()
