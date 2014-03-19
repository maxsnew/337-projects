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
			

	def showIngredient(self):
		current = self.quantity

		if current == None:
			print ('{\n\t"name": ' + self.name
		      	  + '\n\t"quantity": None'
		      	  + '\n\t"measurement": None' + '\n},')
		else:
			match = re.search("[^a-zA-Z]+", current)
			self.quantity = match.group()

			print ('{\n\t"name": ' + self.name
			      + '\n\t"quantity": ' + self.quantity
			      + '\n\t"measurement": ' + self.measurement + '\n},')

	def __init__(self, name, quantity, measurement, descriptor, preparation):
		self.name = name
		self.quantity = 0
		self.measurement = measurement
		self.descriptor = descriptor
		self.preparation = preparation

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
				match = re.search("[a-zA-Z]+", current)
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
