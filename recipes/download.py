import requests
from bs4 import BeautifulSoup

def download_recipe(url):
    """Downloads a recipe from an allrecipes.com url and extracts the
       relevant part of the page""" 

    r          = requests.get(url)
    html       = r.text
    return extract_recipe(html)

def extract_recipe(html):
    """Extract the recipe from an allrecipes recipe webpage,
       returns a pair of lists, ingredients and directions"""
    soup = BeautifulSoup(html)
    name = extract_name(soup)
    directions = [
        d.get_text()
        for d in soup.find(   'div',  {'class': 'directions'})
                     .findAll('span', {'class':'plaincharacterwrap'})
    ]
    ingreds = extract_ingredients(soup)
    return (name, ingreds, directions)

def extract_ingredients(soup):
    """Extracts the ingredients from a recipe into a map of amount and name. Amount may be None"""
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

def extract_name(soup):
    return soup.find(id='itemTitle').text
