import copy
import nltk
import random
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
	def __init__(self, raw, food_group, name, quantity, measurement):
                self.raw = raw
		self.name = name
                self.stems = [stemmer.stem(tok) for tok in nltk.word_tokenize(name)]
		self.quantity = quantity
		self.measurement = measurement
                self.food_group = food_group

        def pretty(self):
                amount = self.raw['amount']
                name = self.name
                if amount:
                        return ' '.join([amount, name])
                else: 
                        return name
                
        def is_ingredient(self, txt):
                """Returns True if the input is probably the same as this ingredient"""
                other = stemmer.stem(txt)
                return other in self.stems

	def serialize(self):
		return {
			'name': self.name.lower(),
			'quantity': self.quantity if self.quantity is not None else 'unkown',
			'measurement': self.measurement.lower() if self.measurement is not None else 'unkown'
		}
                
        def is_meat(self):
                return self.food_group in meat_groups
                
	def veggitize(self):
                """Return a vegetarian substitue for this ingredient"""
                if self.is_meat():
                        # TOFUify!
                        newIngredient = copy.deepcopy(self)
                        newIngredient.name = 'tofu'
                        newIngredient.food_group = 1600
                        return newIngredient
                else:
                        # Must already be veggie.
                        return self

        def change_cuisine(self, cuisine):
                """Return an item of the desired cuisine in the same food group"""
                fg = self.food_group
                if fg in cuisine.keys():
                        new_ing = copy.deepcopy(self)
                        new_food = random.choice(cuisine[fg])
                        new_ing.name = new_food
                        return new_ing
                else:
                        return self
        def make_healthy(self):
                """Return an healthy replacement ingred in the same food group"""
                fg = self.food_group
                if fg in HealthyIng.keys():
                        new_ing = copy.deepcopy(self)
                        new_food = random.choice(HealthyIng[fg])
                        new_ing.name = new_food
                        return new_ing
                else:
                        return self
                
	@staticmethod
	def parse(db, raw_ingred):
		"""would this take raw_ingred or our new list created in recipe.py?
		Parse ingredient attribute values from the extracted recipe"""
		amount = raw_ingred['amount']
		name = raw_ingred['name']
                food_group = find_food_group(db, name)

		if amount is None:
			newIngredient = Ingredient(raw_ingred, food_group, name, None, None)
			return newIngredient
		else:
			match = re.search("[a-zA-Z]+", amount)
			if match == None:
				newIngredient = Ingredient(raw_ingred, food_group, name, amount, None)
			else:
				measurement = match.group()
				amount = amount.replace(measurement, '')
				newIngredient = Ingredient(raw_ingred, food_group, name, amount, match.group())

		return newIngredient

def find_food_group(db, name):
        # Find the food group
        c = db.cursor()
        results = [
                res[0]
                for tok in nltk.word_tokenize(name)
                for res in c.execute('SELECT FoodGroupId FROM Foods WHERE FoodName LIKE ?', ('%'+tok+'%',)).fetchall()
        ]

        if results:
                return max(set(results), key=results.count)
        else:
                return None # unknown!

# Lists of ingredients for most popular cuisines
Mexican = {
	100: ['evaporated milk', 
	'sweetened condensed milk', 
        'jack cheese',
        'queso fresco',
        'queso blanco',
        'queso enchilado',
        'cotija',
        'panela',
        'crema', 
        'eggs'],
        
        200: ['garlic powder',
        'onion powder',
        'standard chile powder',
        'cumin',
        'oregano',
        'parsley',
        'saffron',
        'cilantro',
        'cinnamon sticks',
        'cloves',
        'bay leaves',
        'achiote',
        'epazote',
        'anise',
        'vanilla',
        'vanilla beans',
        'hoja santa'],
        
        400: ['vegetable oil', 'lard'],
        
        500: ['chicken breasts',
        'chicken pieces',
        'whole chicken'],
        
        600: ['tomato sauce',
        'tomato paste','red chile sauce',
        'green chile sauce',
        'enchilada sauce','chicken stock',
        'beef stock' ],
        
        900: ['limes',
        'lemons', 'plantains', ],
        
        1000: ['pork loin',
        'pork roast',
        'chorizo',
        'ribs'],
        
        1100: ['tomatoes',
        'tomatillos','new mexico chiles',
        'anaheim chiles',
        'hatch chiles',
        'poblano chiles',
        'ancho chiles',
        'chile negro',
        'serrano chiles',
        'guajillo chiles',
        'pasilla chiles',
        'cascabel chiles','diced green chiles',
        'whole green chiles',
        'chipotle chiles','jalapenos','refried beans',
        'black beans','onion',
        'potatoes', 'green onion',
        'bell pepper',
        'avocado',
        'garlic','cucumber',
        'jicama', 'pinto beans'],
        
        1300: ['ground beef',
        'skirt steak', ],
        
        1700: ['veal',
        'lamb'],
        
        1800: ['sugar',
        'honey', 'unsweetened chocolate',
        'mexican chocolate',],
        
        2000: ['flour tortillas',
        'corn tortillas',
        'white flour',
        'corn meal',
        'masa harina',
        'cornmeal',
        'hominy','white rice']
 }  
 
        
      

Chinese = {
	200:['ginger'],
	400: ['rice vinegar',
        'toasted sesame oil'],
        600: ['chili sauce',
        'soy sauce',
        'hoisin sauce',
        'oyster sauce'],
        1100: ['Chinese mushrooms'],
        1400: ['rice wine'],
        1600: ['fermented black beans'],
        2000: ['rice']
}

Italian = {
	100: ['mozzarella',
        'parmesan'],
	200: ['capers',
        'garlic',
        'basil',
        'sage',
        'thyme',
        'oregano'],
        400: ['extra-virgin olive oil',
        'balsamic vinegar'],
        900: ['olives'],
        1000: ['proscuitto'],
        1100: ['canned tomatoes',
        'artichokes'],
        1400: ['wine'],
        1600: ['cannellini beans',
        'pine nuts'],
        2000: ['dried pasta',
        'arborio rice',
        'flour',
        'bread crumbs']
        
}

Indian = {
	200: ['coriander', 'cumin', 'mustard seeds','tumeric', 'cinnamon', 'cardamom','garam masala'],
	1100: ['chickepeas', 'chili peppers', 'lentils', 'mung beans', 'ginger', 'onions', 'garlic']
}

French = {
        100: ['butter', 'cheese'],
        140: ['wine'],
        200: ['vinegar', 'mustard'],
        400: ['olive oil'],
        1100: ['leeks', 'shallots'],
        1800: ['bread'],
}

#List of healthy ingredients

HealthyIng = {
	100: ['egg whites', 'soy milk', 'almond milk'],
	400: ['olive oil', 'almond butter', 'fish oil', 'apple sauce', 'avocado puree', 'mashed bananas'],
	500: ['turkey'],
	600: ['chicken broth', 'vegetable stock', 'low sodium soy sauce'],
	700: ['deli turkey', 'turkey sausage'],
	1300: ['turkey', 'ground turkey', 'quinoa'],
	1900: ['apple sauce', 'vanilla'],
	2000: ['whole wheat pasta', 'brown rice', 'whole wheat flour', 'almond flour', 'coconut flour', 'couscous', 'quinoa', 'zucchini ribbons', 'cauliflower', 'rolled oats'],
	

}
