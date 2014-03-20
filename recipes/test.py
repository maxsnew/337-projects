import cPickle as pkl
import sqlite3

import download
from recipe import Recipe

def main():
    with open('chili.pkl') as f:
        with sqlite3.connect('db/food.db') as db:
            raw_recipe = pkl.load(f)
            recipe     = Recipe.parse(db, raw_recipe)
            for d in recipe.directions:
                    print d.tagged
	
if __name__ == '__main__':
    main()
