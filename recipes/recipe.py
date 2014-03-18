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
		recipe = download.download_recipe(url)
		return recipe
		
	def parseIngredient(recipe):
		"""Parse recipe attribute values from the extracted recipe"""
		self.name = """NLTK parsing here"""
		self.ingredients = """NLTK parsing here"""
		self.tools = """NLTK parsing here"""
		self.methods = """NLTK parsing here"""
		self.directions = """NLTK parsing here"""
		return self