import requests
from bs4 import BeautifulSoup

def download_recipe(url):
    """Downloads a recipe from an allrecipes.com url and extracts the
       relevant part of the page""" 

    r          = requests.get(url)
    html       = r.text
    return extract_recipe(html)

def extract_recipe(html):
    """Extract the recipe from the kitchen view of an allrecipes recipe,
       returns a pair of lists, ingredients and directions"""
    soup = BeautifulSoup(html)
    directions = []
    # directions = [
    #     div.get_text()
    #     for div in soup.find(id='directions-wrapper')
    #                    .findAll('div', {'class': 'direction'})
    # ]
    ingreds = extract_ingredients(soup)
    return (ingreds, directions)

def extract_ingredients(soup):
    ingreds = [
        make_ingredient(li)
        for ul in soup.findAll('ul', {'class', 'ingredient-wrap'})
        for li in ul.findAll('li')
    ]
    return ingreds
    
def make_ingredient(li):
    amount_span = li.find('span', { 'class': 'ingredient-amount'})
    amount = None
    if amount_span is not None:
        amount = amount_span.get_text() 
    name = li.find('span', { 'class': 'ingredient-name'}).get_text()
    return {
        'amount': amount,
        'name'  : name
    }
