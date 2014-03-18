import nltk
import download

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