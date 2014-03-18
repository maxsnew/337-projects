import nltk
import download

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
		"""Parse ingredient attribute values from the recipe"""
		self.name = """NLTK parsing here"""
		self.quantity = """NLTK parsing here"""
		self.measurement = """NLTK parsing here"""
		self.descriptor = """NLTK parsing here"""
		self.preparation = """NLTK parsing here"""