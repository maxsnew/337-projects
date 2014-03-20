import sqlite3

import download
import ingredient
from recipe import Recipe

def recipe_interface():
    with sqlite3.connect('db/food.db') as c:
        while True:
            #start by getting the url for the recipe
            url = raw_input('What recipe would you like to work on today?\n')
            if(url.find("allrecipes.com/") == -1):
                print("Please put in a url from allrecipes.com")
                continue
            else:
                #print out the original recipe
                raw_recipe = download.download_recipe(url)
                recipe     = Recipe.parse(c, raw_recipe)
                print('\nHere is the original recipe:\n')
                print(recipe.pretty())
                
                # Then ask what transformation to do
                while True:
                    print('What would you like to do with your recipe?')
                    print('1 = Make Vegetarian')
                    print('2 = Make NOT Vegetarian')
                    print('3 = Change cuisine style')
                    print('4 = Make healthy')
                    x = raw_input()
                    if x in trans_choices.keys():
                        new_recipe = trans_choices[x](recipe)
                        break
                    else:
                        print('Please pick a number corresponding to one of the available options')

                print("Here's your new recipe!")
                print(new_recipe.pretty())

        
                
def make_veggie(old_recipe):
    return old_recipe.veggitize()                

cuisine_choices = {
    '1': ingredient.Mexican,
    '2': ingredient.French,
    '3': ingredient.Indian
}
def change_cuisine(recipe):
    while True:
        print('What kind of cuisine would you like to make it?')
        print('1 = Mexican')
        print('2 = French')
        print('3 = Indian')
        i = raw_input()
        if i in cuisine_choices.keys():
            return recipe.change_cuisine(cuisine_choices[i])
        else:
            print 'Invalid option'

def make_not_veggie(recipe):
    return recipe.make_not_veggie()            

def make_healthy(recipe):
    return recipe.make_healthy()
    
trans_choices = {
    '1': make_veggie,
    '2': make_not_veggie,
    '3': change_cuisine,
    '4': make_healthy,
}

            
if __name__ == '__main__':
    recipe_interface()
