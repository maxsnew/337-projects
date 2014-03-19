import download
import recipe

#vegetarian, cuisine, and healthy are filler names for the programs David is going to write
def recipe_interface():
    #start by getting the url for the recipe
    while True:
    y = input('What recipe would you like to work on today?')
    if(y.find("allrecipes.com/") == -1):
        print("Please put in a url from allrecipes.com")
        recipe_interface()
    else:
<<<<<<< HEAD
        recipe = Recipe()
        #print out the original recipe
        print('Here is the original recipe' recipe.getRecipe())
        #Then ask what transformation to do
        while True:
            print('What would you like to do with your recipe?')
            print('1 = Make Vegetarian/Vegan')
            print('2 = Change cuisine style')
            print('3 = Find healthier alternatives')
            x = input()
            if(x == '1'):
                recipe.veggitize()
                break
            elif(x == '2'):
                changed = cuisine(recipe)
                break
            elif(x == '3'):
                recipe.makeHealthy()
                break
            else:
                print('Please pick a number corresponding to one of the available options')
        #Then print the new recipe
        print("Here's your new recipe!/n" recipe)
=======
        break
    #print out the original recipe
    print('Here is the original recipe' recipe)
    #Then ask what transformation to do
    while True:
        print('What would you like to do with your recipe?')
        print('1 = Make Vegetarian/Vegan')
        print('2 = Change cuisine style')
        print('3 = Find healthier alternatives')
        x = input()
        if(x == '1'):
            changed = vegetarian(recipe)
            break
        elif(x == '2'):
            changed = cuisine(recipe)
            break
        elif(x == '3'):
            changed = healthy(recipe)
            break
        else:
            print('Please pick a number corresponding to one of the available options')
    #Then print the new recipe
    print('Here's your new recipe!' changed)
>>>>>>> 93c7dde25b83c1108f548c3649e7831f8f6b3d0e
