import json
import sqlite3
import sys

import download as d
from recipe import Recipe

def main():
    with sqlite3.connect('db/food.db') as c:
        url    = raw_input('Please input a valid allrecipes.com recipe url')
        raw    = d.download_recipe(url)
        recipe = Recipe.parse(c, raw)
        print json.dumps(recipe.serialize(), indent=4)

if __name__ == '__main__':
    main()
