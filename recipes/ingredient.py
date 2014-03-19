import nltk
import re
import download

class Ingredient(object):
	def __init__(self, name, quantity, measurement):
		self.name = name
		self.quantity = quantity
		self.measurement = measurement

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
	
# 	def parse(raw_ingred): """would this take raw_ingred or our new list created in recipe.py?"""
# 		"""Parse ingredient attribute values from the extracted recipe"""
# 		name = parseIngredientName(raw_ingred)
# 		quantity = parseQuantity(raw_ingred)
# 		measurement = parseMeasurement(raw_ingred)
# 		descriptor = parseDescriptor(raw_ingred)
# 		preparation = parsePreparation(raw_ingred)
# 		return Ingredient(name, quantity, measurement, descriptor, preparation)

# 	def makeVeggie(self):
#                 """Return a vegetarian substitue for this ingredient"""
# 		newIngredient = self
# 		return newIngredient

# 	def healthy(self):
# 				#Return a healthier alternative for this ingredient
# 				# whole milk --> skim milk
# 				# butter --> olive oil
# 				# mayo 	--> greek yogurt or avocado
# 				# pasta --> whole-grain pasta
# 				# bread --> whole-grain bread
# 				# ice cream --> cool whip
# 		newIngredient = self
# 		return newIngredient

# def parseIngredientName(raw_ingred):

# def parseQuantity(raw_ingred):

# def parseMeasurement(raw_ingred):

# def parseDescriptor(raw_ingred):

# def parsePreparation(raw_ingred):

