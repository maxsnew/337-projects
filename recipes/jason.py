import sqlite3
import download
from recipe import Recipe

def jason():
    with sqlite3.connect('db/food.db') as c:
        url = raw_input('enter recipe:\n')
        raw = download.download_recipe(url)
        recipe = Recipe.parse(c, raw)

        print('{\n\t"ingredients: ')
        for i in recipe.ingredients:
            if i.measurement == None:
                print ('\t{\n\t\t"name": ' + i.name
              + '\n\t\t"quantity": ' + i.quantity + '\n\t\t"measurement":  None' + '\n\t},')
            else:
                print ('\t{\n\t\t"name": ' + i.name
                  + '\n\t\t"quantity": ' + i.quantity + '\n\t\t"measurement": '
                  + i.measurement + '\n\t},')
        print('\tcooking method: ' + recipe.methods[0].name + ',\t')
        print('\tcooking tools:'),
        for i in recipe.tools:
            print (i.name + ','),
        # for i in recipe.tools:
        #     if recipe.tools[0]:
        #         print("[ " + i.name + ","),
        #     elif recipe.tools[len(recipe.tools)-1]:
        #         print(i.name + " ]"),
        #     else:
        #         print(i.name + ","),
        print('\n}')



if __name__ == '__main__':
    jason()