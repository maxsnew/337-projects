import nltk
import download

stemmer = nltk.stem.lancaster.LancasterStemmer()

class Method(object):
	def __init__(self, name):
		self.name = name
		self.helper = helper

        @staticmethod
        def find_methods(directions):
                """Returns the cooking methods sorted by frequency"""
                verbs = [
                        word
                        for direction in directions
                        for (word, pos) in direction.tagged
                        if pos.startswith('V') and is_cooking_method(word)
                ]
                ordered = nltk.FreqDist(verbs).keys()
                return [
                        Method(v) for v in ordered
                ]


methods = ['bake', 'roast', 'broil', 'preheat', 'grill', 'fry', 'saute', 'sweat', 'torch', 'flambe', 'blanch', 'boil', 'braise', 'poach', 'scald', 'simmer', 'steam', 'smoke', 'reduce', 'brine', 'blacken', 'brown', 'caramelize', 'curdle', 'dry', 'glaze', 'infuse', 'juice', 'marinate', 'parboil', 'sear', 'steep', 'stew' 'beat', 'whisk', 'carve','chop', 'cut', 'slice', 'dice', 'mix', 'stir', 'measure', 'peel', 'flip', 'roll',]
stemmed_methods = [stemmer.stem(m) for m in methods]

def is_cooking_method(word):
        """look in a list of cooking methods"""
        return stemmer.stem(word) in stemmed_methods 
