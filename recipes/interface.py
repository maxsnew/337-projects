import download
from recipe import Recipe

#vegetarian, cuisine, and healthy are filler names for the programs David is going to write
def recipe_interface():
    #start by getting the url for the recipe
    while True:
        url = raw_input('What recipe would you like to work on today?\n')
        if(url.find("allrecipes.com/") == -1):
            print("Please put in a url from allrecipes.com")
            continue
        else:
            #print out the original recipe
            raw_recipe = download.download_recipe(url)
            recipe     = Recipe.parse(raw_recipe)
            print([
                i.serialize()
                for i in recipe.ingredients
            ])
            print('Here is the original recipe:')
            print(recipe.pretty_recipe())

            # Then ask what transformation to do
            while True:
                print('What would you like to do with your recipe?')
                print('1 = Make Vegetarian/Vegan')
                print('2 = Change cuisine style')
                print('3 = Find healthier alternatives')
                x = raw_input()
                if(x == '1'):
                    new_recipe = recipe.veggitize()
                    break
                elif(x == '2'):
                    new_recipe = cuisine(recipe)
                    break
                elif(x == '3'):
                    new_recipe = recipe.makeHealthy()
                    break
                else:
                    print('Please pick a number corresponding to one of the available options')
            # Then print the new recipe
            print("Here's your new recipe!")
            print(recipe.pretty_recipe())

if __name__ == '__main__':
    recipe_interface()
