import json
import sqlite3
import sys

import download as d
from recipe import Recipe

def dump_recipe(url):
    with sqlite3.connect('db/food.db') as c:
        raw    = d.download_recipe(url)
        recipe = Recipe.parse(c, raw)
        return recipe.serialize()
    

def main():
    url    = raw_input('Please input a valid allrecipes.com recipe url')
    print dump_recipe(url)

if __name__ == '__main__':
    main()
