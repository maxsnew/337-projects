import nltk
import download
from recipe import Recipe
from ingredient import Ingredient
from tool import Tool
from method import Method

class Direction(object):
	def __init__(self, time, ingredients, tools, methods):
		self.time = time
		self.ingredients = ingredients
		self.tools = tools
		self.methods = methods
		
	def getRecipe(url):
		"""Obtain downloaded recipe"""
		recipe = download.download_recipe(url)
		return recipe
	
	def parseDirection(recipe):
		"""Parse direction/step attributes from the extracted recipe and from other classes"""
		self.time = """NLTK parsing here"""
		"""These next three come from pre-established classes"""
		self.ingredients = Ingredient.parseIngredient(recipe)
		self.tools = Tool.parseTool(recipe)
		self.methods = Method.parseMethod(recipe)
		return self