import nltk
import download

class Tool(object):
	def __init__(self, setting):
		self.setting = setting
	
	def parse(raw_directions):
		"""Parse tool attribute values from the extracted recipe"""
		setting = parseSetting(raw_directions)
		return Tool(setting)

def parseSetting(raw_directions):
	"""Not sure how to do this one, maybe look for hard-coded verbs like "set, preheat, heat, etc."""