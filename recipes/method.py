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

def findVerbs(raw_directions):
	"""Output a list of verbs, sorted by frequency"""
	text = nltk.word_tokenize(raw_directions)
	nltk.pos_tag(text)
	wordFreq = nltk.FreqDist(text)
	verbTagList = [word + "/" + tag for (word, tag) in wordFreq if tag.startswith('V')]
	verbList = [int(i[0]) for i in verbTagList]
	return verbList
		
def parsePrimary(verbList):
	"""Primary will be the most often used verb"""
	return verbList[0]

def parseHelper(verbList): 
	"""Helper will be the second most used verb"""
	return verbList[1]