import nltk
import download
from recipe import Recipe

class Ingredient(object):
	def __init__(self, name, quantity, measurement, descriptor, preparation):
		self.name = name
		self.quantity = 0
		self.measurement = measurement
		self.descriptor = descriptor
		self.preparation = preparation
	
	def getRecipe(url):
		"""Obtain downloaded recipe"""
		recipe = download.download_recipe(url)
		return recipe
		
	def parseIngredient(recipe):
		"""Parse ingredient attribute values from the extracted recipe"""
		self.name = """NLTK parsing here"""
		self.quantity = """NLTK parsing here"""
		self.measurement = """NLTK parsing here"""
		self.descriptor = """NLTK parsing here"""
		self.preparation = """NLTK parsing here"""
		return self

	def makeVeggie(self):
                """Return a vegetarian substitue for this ingredient"""
		newIngredient = self
		return newIngredient

	def healthy(self):
				#Return a healthier alternative for this ingredient
				# whole milk --> skim milk
				# butter --> olive oil
				# mayo 	--> greek yogurt or avocado
				# pasta --> whole-grain pasta
				# bread --> whole-grain bread
				# ice cream --> cool whip
		newIngredient = self
		return newIngredient
