import award

from runner import Runner
from award import (awards, Award)

import cPickle as pickle
import json
import nltk

def main():
    """Make the premade corpus, fdist and serialize"""
    runner = Runner(awards)
    runner.write()
    # winners = runner.winners()
    # for w in winners:
    #     print w
    return

if __name__ == '__main__':
    main()
