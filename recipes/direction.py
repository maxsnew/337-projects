import nltk
import download
from ingredient import Ingredient
from tool import Tool
from method import Method

class Direction(object):
	def __init__(self, time, ingredients, tools, methods):
		self.time = time
		self.ingredients = ingredients
		self.tools = tools
		self.methods = methods
	
	def parse(raw_directions):
		"""Parse direction/step attributes from the extracted recipe and from other classes"""
		time = parseTime(raw_directions)
		"""These next three come from pre-established classes, not sure if correct"""
		ingredients = Ingredient.parseIngredient(raw_ingredients)
		tools = Tool.parseTool(raw_directions)
		methods = Method.parseMethod(raw_directions)
		return Direction(time, ingredients, tools, methods)

	def updateIngredient(self, old, new):
		for ingredient in self.ingredients
			if ingredient == old:
				ingredient = new
		return ingredient

def parseTime(raw_directions):
	"""will work on this later, it's optional to break up directions into a direction objects with attribs like time, etc"""