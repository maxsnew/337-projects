import nltk
import re
import download

class Ingredient(object):

	def __init__(self, name, quantity, measurement):
		self.name = name
		self.quantity = quantity
		self.measurement = measurement

        def parseIngredients(self):
		for item in extract_ingredients(self.raw):
			current = item['amount']
			if current == None:
				newIngredient = Ingredient(item['name'], None, None)
				newIngredient.showIngredient()
			else:
				match = re.search("[a-zA-Z]+", current)
				if match == None:
					newIngredient = Ingredient(item['name'], item['amount'], "None")
					self.ingredients.append(newIngredient)
					newIngredient.showIngredient()
					continue
				else:
					newIngredient = Ingredient(item['name'], item['amount'], match.group())
					self.ingredients.append(newIngredient)
					newIngredient.showIngredient()

	def displayIngred(self):
		for ingred in self.ingredients:
			ingred.showIngredient()
			

	def serialize(self):
		return {
			'name': self.name,
			'quantity': self.quantity,
			'measurement': self.measurement
		}

	def makeVeggie(self):
                """Return a vegetarian substitue for this ingredient"""
		newIngredient = self
		return newIngredient

	def healthy(self):
				#Return a healthier alternative for this ingredient
				# whole milk --> skim milk
				# butter --> olive oil
				# mayo 	--> greek yogurt or avocado
				# pasta --> whole-grain pasta
				# bread --> whole-grain bread
				# ice cream --> cool whip
		newIngredient = self
		return newIngredient

	@staticmethod
	def parse(raw_ingred):
		"""would this take raw_ingred or our new list created in recipe.py?
		Parse ingredient attribute values from the extracted recipe"""
		amount = raw_ingred['amount']
		name = raw_ingred['name']
		if amount is None:
			newIngredient = Ingredient(name, None, None)
			return newIngredient
		else:
			match = re.search("[a-zA-Z]+", amount)
			if match == None:
				newIngredient = Ingredient(name, amount, None)
			else:
				measurement = match.group()
				amount = amount.replace(measurement, '')
				newIngredient = Ingredient(name, amount, match.group())
			
		return newIngredient
def parseIngredientName(raw_ingred):
        raise Exception('Leesha or David')
                        
def parseQuantity(raw_ingred):
        raise Exception('Leesha or David')

def parseMeasurement(raw_ingred):
        raise Exception('Leesha or David')

def parseDescriptor(raw_ingred):
        raise Exception('Leesha or David')

def parsePreparation(raw_ingred):
        raise Exception('Leesha or David')
