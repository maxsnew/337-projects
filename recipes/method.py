import nltk
import download

class Method(object):
	def __init__(self, primary, helper):
		self.primary = primary
		self.helper = helper
	
	def parse(raw_directions):
		"""Parse cooking method attributes from the extracted recipe"""
		""" Use NLTK to find verbs """
		primary = parsePrimary(raw_directions)
		helper = parseHelper(raw_directions)
		return Method(primary, helper)

def parsePrimary(raw_directions):
	"""Primary will be the most often used verb"""

def parseHelper(raw_directions): 
	"""Helper will be the second most used verb"""