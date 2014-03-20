import nltk
import download
from method import Method

stemmer = nltk.stem.lancaster.LancasterStemmer()
st = stemmer.stem

tool_map =  {st('bake'): 'oven',
             st('broil'): 'oven',
             st('roast'): 'oven',
             st('preheat'): 'oven',
             st( 'grill'): 'grill',
             st( 'beat'):'whisk',
             st('whisk'):'whisk',
             st( 'boil'): 'pot',
             st('blanch'): 'pot',
             st('poach'): 'pot',
             st( 'carve'): 'knife',
             st('chop'): 'knife',
             st('cut'): 'knife',
             st('slice'): 'knife',
             st('dice'): 'knife',
             st( 'fry'): 'skillet',
             st('saute'): 'skillet',
             st('simmer'): 'skillet',
             st( 'grate'): 'grater',
             st( 'mix'): 'spoon',
             st('stir'): 'spoon',
             st('blend'): 'blender',
             st('measure'): 'measuring spoon',
             st('weigh'): 'scale',
             st('peel'): 'peeler',
             st( 'drain'): 'colander',
             st('steam'): 'colander',
             st('flip'): 'spatula',
             st('roll'): 'rolling pin',
}

class Tool(object):
	def __init__(self, name):
		self.name = name

        def pretty(self):
                return self.name

        def serialize(self):
                return self.name.lower()
                
        @staticmethod
        def find_tools(text):
                """Returns a list of tools"""
                tools = []
                for tok in text:
                        stemmed = st(tok)
                        if stemmed in tool_map:
                                tools.append(tool_map[stemmed])
                        
                tools_noDups = set(tools)
                return [
                        Tool(t) for t in tools_noDups
                ]
