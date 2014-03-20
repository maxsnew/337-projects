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
		print(self.name + "\n")
		for i in self.ingredients:
			if i.measurement == None:
				print(i.quantity + " " + i.name)
				continue
			else:
				print(i.quantity + " " + i.measurement + " " + i.name)
		for i in self.directions:
			print(i.tagged)
		

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
	def parse(db, raw_recipe):
		"""parsing recipe download into recipe structure"""
		(raw_name, raw_ingredients, raw_directions) = raw_recipe
                tagged_directions = [ 
                        nltk.pos_tag(nltk.word_tokenize(d))
                        for d in raw_directions
                ]
		name = raw_name
		ingredients = [Ingredient.parse(db, i) for i in raw_ingredients]

		directions = [
                        Direction.parse(d, ingredients)
                        for d in tagged_directions
                ]
		tools   = Tool.find_tools(directions)
		methods = Method.find_methods(directions)
		return Recipe(name, ingredients, tools, methods, directions)
	
