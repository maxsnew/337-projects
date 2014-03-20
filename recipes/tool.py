import nltk
import download
from method import Method

#stemmer = nltk.stem.lancaster.LancasterStemmer()

class Tool(object):
	def __init__(self, name, setting):
		self.name = name
	
        @staticmethod
        def find_tools(methods):
                """Returns a list of tools"""
                tools = []
                for i in methods:	
                        if (i == 'bake' or i == 'broil' or i == 'roast' or i == 'preheat'):
                                tools.extend('oven')
                        elif (i == 'grill'):
                                tools.extend('grill')
                        elif (i == 'beat' or i == 'whisk'):
                                tools.extend('whisk')
                        elif (i == 'boil' or i == 'blanch' or i == 'poach'):
                                tools.extend('pot')
                        elif (i == 'carve' or i == 'chop' or i == 'cut' or i == 'slice' or i == 'dice'):
                                tools.extend('knife')
                        elif (i == 'fry' or i == 'saute' or i == 'simmer'):
                                tools.extend('skillet')
                        elif (i == 'grate'):
                                tools.extend('grater')
                        elif (i == 'mix' or i == 'stir' or i == 'blend'):
                                tools.extend('electric mixer')
                        elif (i == 'measure'):
                                tools.extend('measuring spoon')
                        elif (i == 'peel'):
                                tools.extend('peeler')
                        elif (i == 'steam' or i == 'drain'):
                                tools.extend('colander')
                        elif (i == 'strain'):
                                tools.extend('strainer')
                        elif (i == 'flip'):
                                tools.extend('spatula')
                        elif (i == 'roll'):
                                tools.extend('rolling pin')
                                tools_noDups = set(tools)
                                return [
                                        Tool(t) for t in tools_noDups
                                ]
