import requests
from bs4 import BeautifulSoup

def download_recipe(url):
    """Downloads a recipe from an allrecipes.com url and extracts the
       relevant part of the page""" 

    name       = extract_recipe_name(url)
    better_url = 'http://allrecipes.com/recipe/{0}/kitchenview.aspx'.format(name)
    r          = requests.get(better_url)
    html       = r.text
    return extract_recipe(html)

def extract_recipe(html):
    """Extract the recipe from the kitchen view of an allrecipes recipe"""
    soup = BeautifulSoup(html)
    directions = [
        div.get_text()
        for div in soup.find(id='directions-wrapper')
                       .findAll('div', {'class': 'direction'})
    ]
    ingreds = [
        div.get_text()
        for div in soup.find('div', {'class', 'ingred-div'}).findAll('li')
    ]
    return (ingreds, directions)
    
def extract_recipe_name(url):
    """From an allrecipes.com recipe url, extract the name of the recipe"""
    pieces   = [piece.lower() for piece in url.split('/')]
    recipe_i = pieces.index('recipe')
    return pieces[recipe_i+1]
