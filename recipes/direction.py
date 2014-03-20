import nltk
import download
from ingredient import Ingredient
from tool import Tool
from method import Method

class Direction(object):
	def __init__(self, tagged):
                self.tagged  = tagged

	@staticmethod
	def parse(tagged_direction, ingredients):
		"""Parse direction/step attributes from the extracted recipe and from other classes"""
                tagged_with_ingreds = [ 
                        tag_if_ingredient(tagged, ingredients)
                        for tagged in tagged_direction
                ]
		return Direction(tagged_with_ingreds)

	def updateIngredient(self, old, new):
                new_tagged = [
                        replace_tagged(tagged, old, new)
                        for tagged in self.tagged
                ]
		return Direction(new_tagged)

def replace_tagged(tagged, old, new):
        lhs, pos  = tagged
        if isinstance(rhs, tuple):
                word, ing = lhs
                if ing is old:
                        return ((word, new), pos)
        return (lhs, pos)

def tag_if_ingredient(tagged, ingredients):
        word, pos = tagged
        if pos == 'NN' or pos == 'NNS':
                for ing in ingredients:
                        if ing.is_ingredient(word):
                                return ((word, ing), pos)
                        
        return tagged

def parseTime(raw_directions):
	"""will work on this later, it's optional to break up directions into a direction objects with attribs like time, etc"""
        return None
