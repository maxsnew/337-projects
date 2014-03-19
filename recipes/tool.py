import nltk
import download

class Tool(object):
	def __init__(self, name, setting):
		self.name = name
		self.setting = setting
	
	def parse(raw_directions):
		"""Parse tool attribute values from the extracted recipe"""
		name = parseName(raw_directions)
		setting = parseSetting(raw_directions)
		return Tool(name, setting)

# def listTools(raw_directions):
# 	"""Not sure how to do this one, maybe look at cooking methods and match commonly used cooking verbs with hard coded tool nouns"""
# 	tools = []
# 	verbs = method.findVerbs(raw_directions)
# 	for i in verbs:	
# 		if (i == 'bake' or i == 'broil' or i == 'roast' or i == 'preheat')
# 			tools.extend('oven')
# 		elif i == 'grill'
# 			tools.extend('grill')
# 		elif (i == 'beat' or i == 'whisk')
# 			tools.extend('whisk')
# 		elif i == 'boil'
# 			tools.extend('pot')
# 		elif (i == 'carve' or i == 'chop' or i == 'cut' or i == 'slice' or i == 'dice')
# 			tools.extend('knife')
# 		elif (i == 'fry' or i == 'saute' or i == 'simmer')
# 			tools.extend('skillet')
# 		elif i == 'grate'
# 			tools.extend('grater')
# 		elif (i == 'mix' or i == 'stir' or i == 'blend')
# 			tools.extend('electric mixer')
# 		elif i == 'measure'
# 			tools.extend('measuring spoon')
# 		elif i == 'peel'
# 			tools.extend('peeler')
# 		elif (i == 'steam' or i == 'drain')
# 			tools.extend('colander')
# 		elif i == 'strain'
# 			tools.extend('strainer')
# 		elif i == 'flip'
# 			tools.extend('spatula')
# 		elif i == 'roll'
# 			tools.extend('rolling pin')	
# 	toolList = set(tools)
# 	return toolList
		
def parseName(raw_directions):
	tools = listTools(raw_directions)
	for i in tools:
		name = 	i
	return name
	
def parseSetting(raw_directions):
	setting = 'None' """not sure how to pull these, and it's not necessary, just thought it would be cool =( """
	return setting
