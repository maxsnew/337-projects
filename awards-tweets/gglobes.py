import award

from runner import Runner
from award import (awards, Award)

def main():
    """Make the premade corpus, fdist and serialize"""
    runner = Runner(awards)
    runner.write()
    return

if __name__ == '__main__':
    main()
