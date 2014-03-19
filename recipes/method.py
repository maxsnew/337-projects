import nltk
import download
from recipe import Recipe

class Method(object):
	def __init__(self, primary, helper):
		self.primary = primary
		self.helper = helper
	
	def getRecipe(url):
		"""Obtain downloaded recipe"""
		recipe = download.download_recipe(url)
		return recipe
	
	def parseMethod(recipe):
		"""Parse cooking method attributes from the extracted recipe"""
		self.primary = """NLTK parsing here"""
		self.helper = """NLTK parsing here"""
		return self

	def healthy(self):
		## i think the only healthy alternative pair thats significant is deep-fry to baking
		newIngredient = self.primary
		return newIngredient