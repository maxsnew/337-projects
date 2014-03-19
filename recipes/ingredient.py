import nltk
import download

class Ingredient(object):
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
		name = parseIngredientName(raw_ingred)
		quantity = parseQuantity(raw_ingred)
		measurement = parseMeasurement(raw_ingred)
		descriptor = parseDescriptor(raw_ingred)
		preparation = parsePreparation(raw_ingred)
		return Ingredient(name, quantity, measurement, descriptor, preparation)

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
