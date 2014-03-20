import nltk
import download

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
                        for (pos, word) in direction.tagged
                        if pos.startswith('V') and is_cooking_method(word)
                ]
                ordered = nltk.FreqDist(verbs).keys()
                return [
                        Method(v) for v in ordered
                ]


def is_cooking_method(word):
        """TODO: look in a big fat table of cooking methods"""
        return True
