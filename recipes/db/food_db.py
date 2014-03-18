import sqlite3
from food_des import strip

def main():
    """  Blerha sdfadsf """
    conn = sqlite3.connect('food.db')
    c = conn.cursor()
    
    with open('sr26abbr/ABBREV.txt', 'r') as f:
        for l in f:
            pieces = l.split('^')
            fid     = int(strip(pieces[0]))
            cals    = pieces[3]
            protein = pieces[4]
            fat     = pieces[5]
            carbs   = pieces[7]
            sugars  = pieces[9]
            
            rows = c.execute('SELECT FoodName, FoodGroupId FROM FoodName WHERE FoodNameId=?', (fid,))
            
            (name, groupid) = c.fetchone()

            c.execute('INSERT INTO Foods VALUES (?, ?, ?, ?, ?, ?, ?, ?)', 
                      (
                      name,
                      fid,
                      groupid,
                      cals,
                      protein,
                      fat,
                      carbs,
                      sugars
                      )
            )

    conn.commit()

if __name__ == '__main__':
    main()

