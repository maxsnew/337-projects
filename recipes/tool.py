import nltk
import download

class Tool(object):
	def __init__(self, setting):
		self.setting = setting
	
	def getRecipe(url):
		"""Obtain downloaded recipe"""
		recipe = download.download_recipe(url)
		return recipe
	
	def parseTool(recipe):
		"""Parse tool attribute values from the extracted recipe"""
		self.setting = """NLTK parsing here"""
		return self