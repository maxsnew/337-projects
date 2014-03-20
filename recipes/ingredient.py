import copy
import nltk
import re

import download

stemmer = nltk.stem.lancaster.LancasterStemmer()

fg_map = {
        100: u'Dairy and Egg Products',
        200: u'Spices and Herbs',
        300: u'Baby Foods',
        400: u'Fats and Oils',
        500: u'Poultry Products',
        600: u'Soups, Sauces, and Gravies',
        700: u'Sausages and Luncheon Meats',
        800: u'Breakfast Cereals',
        900: u'Fruits and Fruit Juices',
        1000: u'Pork Products',
        1100: u'Vegetables and Vegetable Products',
        1200: u'Nut and Seed Products',
        1300: u'Beef Products',
        1400: u'Beverages',
        1500: u'Finfish and Shellfish Products',
        1600: u'Legumes and Legume Products',
        1700: u'Lamb, Veal, and Game Products',
        1800: u'Baked Products',
        1900: u'Sweets',
        2000: u'Cereal Grains and Pasta',
        2100: u'Fast Foods',
        2200: u'Meals, Entrees, and Side Dishes',
        2500: u'Snacks',
        3500: u'American Indian/Alaska Native Foods',
        3600: u'Restaurant Foods',
}

meat_groups = [500, 700, 1000, 1300, 1700]

class Ingredient(object):
	def __init__(self, food_group, name, quantity, measurement):
		self.name = name
                self.stem = stemmer.stem(name)
		self.quantity = quantity
		self.measurement = measurement
                self.food_group = food_group

        def is_ingredient(self, txt):
                """Returns True if the input is probably the same as this ingredient"""
                other = stemmer.stem(txt)
                return other == self.stem

	def serialize(self):
		return {
			'name': self.name,
			'quantity': self.quantity,
			'measurement': self.measurement
		}
                
        def is_meat(self):
                return self.food_group in meat_groups
                
	def makeVeggie(self):
                """Return a vegetarian substitue for this ingredient"""
                if self.is_meat:
                        # TOFUify!
                        newIngredient = deepcopy(self)
                        newIngredient.name = 'TOFU'
                        newIngredient.food_group = 1600
                        return newIngredient
                else:
                        # Must already be veggie.
                        return self

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
	def parse(db, raw_ingred):
		"""would this take raw_ingred or our new list created in recipe.py?
		Parse ingredient attribute values from the extracted recipe"""
		amount = raw_ingred['amount']
		name = raw_ingred['name']
                food_group = find_food_group(db, name)

		if amount is None:
			newIngredient = Ingredient(food_group, name, None, None)
			return newIngredient
		else:
			match = re.search("[a-zA-Z]+", amount)
			if match == None:
				newIngredient = Ingredient(food_group, name, amount, None)
			else:
				measurement = match.group()
				amount = amount.replace(measurement, '')
				newIngredient = Ingredient(food_group, name, amount, match.group())

		return newIngredient

def find_food_group(db, name):
        # Find the food group
        c = db.cursor()
        results = c.execute('SELECT FoodGroupId FROM Foods WHERE FoodName LIKE ?', ('%'+name+'%',)).fetchall()
        if results:
                return max(set(results), key=results.count)
        else:
                return None # unknown!
