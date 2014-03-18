import sqlite3
from food_des import strip

def main():
    """  Blerha sdfadsf """
    conn = sqlite3.connect('food.db')
    c = conn.cursor()
    
    with open('sr26abbr/ABBREV.txt', 'r') as f:
        for l in f:
            fid     = strip(pieces[0])
            cals    = pieces[3]
            protein = pieces[4]
            fat     = pieces[5]
            carbs   = pieces[7]
            sugars  = pieces[9]
            
            rows = c.execute('SELECT FoodName FROM FoodName WHERE FoodNameId=?', fid)
            

    conn.commit()

if __name__ == '__main__':
    main()

