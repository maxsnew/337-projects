import cPickle as pkl

import download
from recipe import Recipe

def main():
    with open('chili.pkl') as f:
        raw_recipe = pkl.load(f)
        recipe     = Recipe.parse(raw_recipe)
        print recipe
	
if __name__ == '__main__':
    main()
