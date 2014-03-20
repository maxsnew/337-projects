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
			'name': self.name,
			'quantity': self.quantity,
			'measurement': self.measurement
		}
                
        def is_meat(self):
                return self.food_group in meat_groups
                
	def veggitize(self):
                """Return a vegetarian substitue for this ingredient"""
                if self.is_meat():
                        # TOFUify!
                        newIngredient = copy.deepcopy(self)
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

Mexican = [
        'red chile sauce',
        'green chile sauce',
        'enchilada sauce',
        'diced green chiles',
        'whole green chiles',
        'chipotle chiles',
        'jalapenos',
        'tomato sauce',
        'tomato paste',
        'refried beans',
        'black beans',
        'tamarind',
        'chicken stock',
        'beef stock',
        'evaporated milk',
        'sweetened condensed milk',
        'new mexico chiles',
        'anaheim chiles',
        'hatch chiles',
        'poblano chiles',
        'ancho chiles',
        'chile negro',
        'serrano chiles',
        'guajillo chiles',
        'pasilla chiles',
        'cascabel chiles',
        
        'pinto beans',
        'black beans',
        'white rice',
        'white rice',
        
        'garlic powder',
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
        'hoja santa',
        'flour tortillas',
        'corn tortillas',
        'white flour',
        'corn meal',
        'masa harina',
        'cornmeal',
        'hominy',
        
        'tomatoes',
        'tomatillos',
        'cilantro',
        'epazote',
        'onion',
        'potatoes',
        'cucumber',
        'parsley',
        'jicama',
        'limes',
        'lemons',
        'green onion',
        'bell pepper',
        'avocado',
        'garlic',
        'plantains',
        
        'jack cheese',
        'queso fresco',
        'queso blanco',
        'queso enchilado',
        'cotija',
        'panela',
        'crema',
        
        'eggs',
        'ground beef',
        'skirt steak',
        'chicken breasts',
        'chicken pieces',
        'whole chicken',
        'veal',
        'lamb',
        'pork loin',
        'pork roast',
        'chorizo',
        'ribs',
        
        'tortilla chips',
        'lard',
        'tequila',
        'vegetable oil',
        'coarse salt',
        'chile sauce',
        'sugar',
        'honey',
        'unsweetened chocolate',
        'mexican chocolate',
        'piloncillo'
]

Chinese = [
        'chili sauce',
        'Chinese mushrooms',
        'soy sauce',
        'fermented black beans',
        'ginger',
        'hoisin sauce',
        'oyster sauce',
        'rice',
        'rice vinegar',
        'rice wine',
        'toasted sesame oil'
]

Italian = [
        'canned tomatoes',
        'dried pasta',
        'arborio rice',
        'flour',
        'cannellini beans',
        'bread crumbs',
        'artichokes',
        'olives',
        'pine nuts',
        'capers',
        'garlic',
        'proscuitto',
        'basil',
        'mozzarella',
        'extra-virgin olive oil',
        'balsamic vinegar',
        'wine',
        'parmesan',
        'sage',
        'thyme',
        'oregano'
]

Indian = [
        'mung beans',
        'lentils',
        'chickpeas',
        'cardamom',
        'chili peppers',
        'cinnamon',
        'coriander',
        'cumin',
        'garam masala',
        'ginger',
        'mustard seeds',
        'onions',
        'garlic',
        'turmeric'
]

French = {
        100: ['butter', 'cheese'],
        140: ['wine'],
        200: ['vinegar', 'mustard'],
        400: ['olive oil'],
        1100: ['leeks', 'shallots'],
        1800: ['bread'],
}


