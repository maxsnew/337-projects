import nltk
from ingredient import Ingredient
from tool import Tool
from method import Method
from direction import Direction

class Recipe(object):
	def __init__(self, name, ingredients, tools, methods, directions):
		self.name = name
		self.ingredients = ingredients
		self.tools = tools
		self.methods = methods
		self.directions = directions

        def pretty_recipe(self):
                """Returns a string that is a human-readable recipe"""
                raise Exception('Unimplemented: Donald or David')

	def veggitize(self):
		for oldIngredient in self.ingredients:
			newIngredient = oldIngredient.makeVeggie()
			newDirections = [
                                direction.updateIngredients(oldIngredient, newIngredient)
				for direction in self.directions
                                
			]
			self.directions = newDirections

	def makeHealthy(self):
		for oldIngredient in self.ingredients:
			newIngredient = oldIngredient.healthy()
			newDirections = [
                                direction.updateIngredients(oldIngredient, newIngredient)
                                for direction in self.directions
                                
			]
			self.directions = newDirections
			newMethods = [
                                method.healthy()
                                for method in self.methods

			]
			self.methods = newMethods

        @staticmethod
	def parse(raw_recipe):
		"""parsing recipe download into recipe structure"""
		(raw_name, raw_ingredients, raw_directions) = raw_recipe
                tagged_directions = [ 
                        nltk.pos_tag(nltk.word_tokenize(d))
                        for d in raw_directions
                ]
		name = raw_name
		ingredients = [Ingredient.parse(i) for i in raw_ingredients]

		directions = [
                        Direction.parse(d, ingredients)
                        for d in tagged_directions
                ]
		tools   = Tool.find_tools(directions)
		methods = Method.find_methods(directions)
		return Recipe(name, ingredients, tools, methods, directions)
	
