import nltk
import re
import requests
from ingredient import Ingredient
from bs4 import BeautifulSoup
#from tool import Tool
#from method import Method
#from direction import Direction

class Recipe(object):
	def __init__(self, url):
		self.raw = download_recipe(url)
		self.name = extract_name(self.raw)
		self.ingredients = extract_ingredients(self.raw)

	def parseIngredients(self):
		for item in self.ingredients:
			newIngredient = Ingredient(item['name'], item['amount'])
			newIngredient.showIngredient()


def download_recipe(url):
	r = requests.get(url)
	html = r.text
	return BeautifulSoup(html)

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

def extract_name(soup):
	return soup.find(id='itemTitle').text
	
	# def getRecipe(url):
	# 	"""Obtain downloaded recipe"""
	# 	raw_recipe = download.download_recipe(url)
	# 	return Recipe.parse(raw_recipe)
		
	# def parse(raw_recipe):
	# 	"""parsing recipe download into recipe structure"""
	# 	(raw_name, raw_ingredients, raw_directions) = raw_recipe
	# 	name = parseRecipeName(raw_name)
	# 	ingredients = parseIngredients(raw_ingredients)
	# 	tools = parseTools(raw_directions)
	# 	methods = parseMethods(raw_directions)
	# 	directions = parseDirections(raw_directions)		
	# 	return Recipe(name, ingredients, tools, methods, directions)

	# def veggitize(self):
	# 	for oldIngredient in self.ingredients:
	# 		newIngredient = oldIngredient.makeVeggie()
	# 		newDirections = [
	# 			for direction in self.directions:
	# 				direction.updateIngredients(oldIngredient, newIngredient)
	# 		]
	# 		self.directions = newDirections

	# def makeHealthy(self):
	# 	for oldIngredient in self.ingredients:
	# 		newIngredient = oldIngredient.healthy()
	# 		newDirections = [
	# 			for direction in self.directions:
	# 				direction.updateIngredients(oldIngredient, newIngredient)
	# 		]
	# 		self.directions = newDirections
	# 		newMethods = [
	# 			for method in self.methods
	# 				newMethod = method.healthy()
	# 		]
	# 		self.methods = newMethods

# def parseRecipeName(raw_name):
# 	"""Parse recipe name from the extracted recipe"""
# 	name = raw_name
# 	return name
		
# def parseIngredients(raw_ingredients):
# 	"""Parse ingredients from the extracted ingredients"""	
# 	return [Ingredient.parse(i) for i in raw_ingredients]
	
# def parseMethods(raw_directions):
# 	"""Parse methods from the extracted directions by searching for verbs"""
# 	"""return [Method.parse(i) for i in raw_directions]"""
# 	directions = raw_directions
# 	return directions
	
# def parseTools(raw_directions):
# 	"""Parse tools from the extracted directions by hard coding tool list"""
# 	return [Tools.parse(i) for i in raw_ingredients]

# def parseDirections(raw_directions):
# 	"""Parse directions from the extracted directions""
# 	return [Direction.parse(i) for i in raw_directions]