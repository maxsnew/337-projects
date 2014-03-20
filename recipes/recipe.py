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

        def change_recipe(self, ingredient_update):
                new_recipe = copy.deepcopy(self)
                new_ingredients = [
                        ingredient_update(old_ingredient)
                        for old_ingredient in self.ingredients
                ]
                new_directions = [
                        direction.update_ingredients(self.ingredients, new_ingredients)
                        for direction in new_recipe.directions
                ]
                new_recipe.name        = update_name(self.name, self.ingredients, new_ingredients)
                new_recipe.ingredients = new_ingredients
                new_recipe.directions  = new_directions
                return new_recipe
                
                
        def veggitize(self):
                return self.change_recipe(lambda i: i.veggitize())

        def make_not_veggie(self):
                """Just add bacon"""
                new_recipe = copy.deepcopy(self)
                new_recipe.ingredients = self.ingredients + [bacon]
                new_recipe.directions  = self.directions + [fry_bacon, put_bacon]
                return new_recipe
        def change_cuisine(self, new_cuisine):
                return self.change_recipe(lambda i: i.change_cuisine(new_cuisine))
        
	def make_healthy(self):
                return self.change_recipe(lambda i: i.make_healthy())

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

fry_bacon = Direction([('Fry', 'NNP'), ('bacon', 'NN')])
put_bacon = Direction([('Put', 'VB'), ('bacon', 'NN'), ('on', 'IN'), ('food', 'NN')])
        
bacon = Ingredient({ 'amount': '2 strips', 'name'  : 'bacon' }, 
                   1000,
                   'bacon',
                   '2',
                   'pieces')        
