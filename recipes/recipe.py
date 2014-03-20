import copy
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

	def pretty(self):
                header = 'Recipe: ' + self.name
                ingred_header = 'You will need the following ingredients: '
                ingreds = pretty_list(self.ingredients)
                tools_header = 'And the following tools:'
                tools   = pretty_list(self.tools)
                dirs_header = 'Here are the directions:'
                directions  = pretty_list(self.directions)
                return '\n'.join([header, '\n',ingred_header,ingreds, '\n',tools_header,tools,'\n',dirs_header, directions])

	def veggitize(self):
                new_recipe = copy.deepcopy(self)
                new_ingredients = [
                        old_ingredient.veggitize()
                        for old_ingredient in self.ingredients
                ]
                new_directions = [
                        direction.update_ingredients(self.ingredients, new_ingredients)
                        for direction in new_recipe.directions
                ]
                new_recipe.name        = update_name(self.name, self.ingredients, new_ingredients)
                new_recipe.ingredients = new_ingredients
                new_recipe.directions  = new_directions
                if new_recipe.ingredients is self.ingredients:
                        print 'wtf'
                        raise Exception('wtf')
                return new_recipe
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
		methods = Method.find_methods(directions)
		tools   = Tool.find_tools(methods)
		return Recipe(name, ingredients, tools, methods, directions)
	
def pretty_list(l):
        return '\n'.join([
                str(i+1) + '. ' + l[i].pretty()
                for i in range(len(l))
        ])

def update_name(name, olds, news):
        return ' '.join([
                update_ing(tok, olds, news)
                for tok in nltk.word_tokenize(name)
        ])

def update_ing(tok, olds, news):
        for i in range(len(olds)):
                if olds[i].is_ingredient(tok.lower()):
                        return news[i].name
        return tok
