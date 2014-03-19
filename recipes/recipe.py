import nltk
import download
from ingredient import Ingredient
from tool import Tool
from method import Method
from direction import Direction

class Recipe(object):
	def __init__(self, name, ingredients, tools, methods, directions):
		self.name = name
		self.ingredients = ingredients
		self.tools = tools
		self.methods = methods
		self.directions = directions
	
	def getRecipe(url):
		"""Obtain downloaded recipe"""
		raw_recipe = download.download_recipe(url)
		return Recipe.parse(raw_recipe)
		
	def parse(raw_recipe):
		(raw_name, raw_ingredients, raw_directions) = raw_recipe
		ingredients = parseIngredients(raw_ingredients) """parsing recipe download"""
		""" ... """
		return Recipe(name, ingredients, tools, methods, directions)

	def veggitize(self):
		for oldIngredient in self.ingredients:
			newIngredient = oldIngredient.makeVeggie()
			newDirections = [
				for direction in self.directions:
					direction.updateIngredients(oldIngredient, newIngredient)
			]
			self.directions = newDirections

	def makeHealthy(self):
		for oldIngredient in self.ingredients:
			newIngredient = oldIngredient.healthy()
			newDirections = [
				for direction in self.directions:
					direction.updateIngredients(oldIngredient, newIngredient)
			]
			self.directions = newDirections
			newMethods = [
				for method in self.methods
					newMethod = method.healthy()
			]
			self.methods = newMethods

def parseRecipeName(raw_name):
	"""Parse recipe name from the extracted recipe"""
	name = raw_name
	return name
		
def parseIngredients(raw_ingredients):
	"""Parse ingredients from the extracted recipe"""	
	return [Ingredient.parse(i) for i in raw_ingredients]
	
def getMethods(raw_directions):
	"""Parse methods from the extracted recipe by searching for verbs"""
	self.methods = """NLTK parsing here"""
	
def getTools(raw_directions):
	"""Not sure what to do, so I'm hard coding a list of tools in tools.py"""
	self.tools = """NLTK parsing here"""

def getDirections(raw_directions):
	"""Parse directions from the extracted recipe"""
	return [Direction.parse(i) for i in raw_directions]
	