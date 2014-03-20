import nltk
import download

class Tool(object):
	def __init__(self, name, setting):
		self.name = name
	
        @staticmethod
        def find_tools(directions): #where would it use directions?
                """Returns a list of tools"""
				tools = [
						'oven',
						'grill',
						'whisk',
						'pot',
						'knife',
						'skillet',
						'grater',
						'mixer',
						'measuring spoon',
						'measuring cup',
						'peeler',
						'colander',
						'strainer',
						'spatula',
						'rolling pin',
						'bowl',
						'blender',
						'cutting board',
						'ladle',
						'oven mits',
						'baking pan',
						'baking sheet',
						'tongs',
						'shears',
						'thermometer',
						'timer',
						'baster',
						'blow torch',
						'funnel'					
                ]
				return [
						Tool(t) for t in tools
				]

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
