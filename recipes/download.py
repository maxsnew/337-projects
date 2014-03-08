import requests

def download_recipe(url):
    """Downloads a recipe from an allrecipes.com url and extracts the
       relevant part of the page""" 

    name = extract_recipe_name(url)
    better_url = 'http://allrecipes.com/recipe/{0}/kitchenview.aspx'.format(name)
    r = requests.get(better_url)
    return r.text

def extract_recipe_name(url):
    """From an allrecipes.com recipe url, extract the name of the recipe"""
    pieces   = url.split('/')
    recipe_i = pieces.index('recipe')
    return pieces[recipe_i+1]
