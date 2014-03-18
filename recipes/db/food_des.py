import sqlite3

def main():
    """Rebuilds Food Name DB from sr26 files """
    conn = sqlite3.connect('food.db')
    c = conn.cursor()

    with open('sr26/FOOD_DES.txt') as f:
        for l in f:
            pieces = l.split('^')
            fid = strip(pieces[0])
            groupid = strip(pieces[1])
            name = strip(pieces[2])
            c.execute('INSERT INTO FoodName VALUES (?, ?, ?)', (fid, groupid, name))

    conn.commit()

def strip(s):
    return s[1:-1]

if __name__ == '__main__':
    main()
