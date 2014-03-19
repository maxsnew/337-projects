import nltk
import download

class Method(object):
	def __init__(self, primary, helper):
		self.primary = primary
		self.helper = helper
	
	def parseMethod(recipe):
		"""Parse cooking method attributes from the extracted recipe"""
		""" Use NLTK to find verbs """
		
		"""Primary will be the most often used verb"""
		self.primary = """NLTK parsing here"""
		"""Helper will be the second most used verb"""
		self.helper = """NLTK parsing here"""
		return self