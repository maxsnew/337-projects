import nltk
import download
from ingredient import Ingredient
from tool import Tool
from method import Method

class Direction(object):
	def __init__(self, tagged):
                self.tagged  = tagged

        def pretty(self):
                untagged = [ untag(t) for t in self.tagged ]
                return ' '.join(untagged)

	@staticmethod
	def parse(tagged_direction, ingredients):
		"""Parse direction/step attributes from the extracted recipe and from other classes"""
                tagged_with_ingreds = [ 
                        tag_if_ingredient(tagged, ingredients)
                        for tagged in tagged_direction
                ]
		return Direction(tagged_with_ingreds)

        def update_ingredients(self, olds, news):
                new_dir = self
                for i in range(len(olds)):
                        old = olds[i]
                        new = news[i]
                        new_dir = new_dir.update_ingredient(old, new)
                return new_dir
                
	def update_ingredient(self, old, new):
                if old is new:
                        return Direction(self.tagged)
                new_tagged = [
                        replace_tagged(tagged, old, new)
                        for tagged in self.tagged
                ]
		return Direction(new_tagged)

def replace_tagged(tagged, old, new):
        lhs, pos  = tagged
        if isinstance(lhs, tuple):
                word, ing = lhs
                if ing is old:
                        return ((new.name, new), pos)
        return (lhs, pos)

def tag_if_ingredient(tagged, ingredients):
        word, pos = tagged
        if pos == 'NN' or pos == 'NNS':
                for ing in ingredients:
                        if ing.is_ingredient(word):
                                return ((word, ing), pos)
                        
        return tagged

def untag(t):
        lhs, _ = t
        if isinstance(lhs, tuple):
                word, _ = lhs
                return word
        else:
                return lhs
                
