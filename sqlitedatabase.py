import sqlite3
import csv
dbc = sqlite3.connect("fruits.db")
cur = dbc.cursor()
list= []

def importCsv():
    infile = open("fruits.csv")
    for i in csv.reader(infile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
        list.append(i)
        print(i)
        addItem(i[0], i[1], i[2])

    print(list)

def addItem(name, quantity, color):
    print(name)
    #sql = f"INSERT INTO fruit VALUES('{name}', '{quantity}', '{color}')" # This works but is not recommended

    data = [(name, quantity, color)] #Use this instead, pud data into a list and use executemany
    print(data)
    cur.executemany("INSERT INTO fruit VALUES(?,?,?)",data)
    dbc.commit()

def displayTable():
    sql = "SELECT * FROM fruit ORDER BY name"
    cur.execute(sql)
    res = cur.fetchall() # cur.fetchone() can retreive one item at a time.
    #print(res) # this works fine but prints on one line
    for row in res: # This is a nicer way to display the result
        for col in row:
            print(col, end=' ')
        print()

#sql = "insert into fruit values('apple', 10, 'green')"
#cur.execute(sql)
#dbc.commit()

def deleteItem(item):
    sql = f"DELETE FROM fruit WHERE name = '{item}'"
    cur.execute(sql)
    dbc.commit()

cur.execute("create table if not exists fruit(name text, quantity integer, color text)")
sql = "select * from fruit"
cur.execute(sql)
res = cur.fetchall()
#print(res)


while 1:
    choose = input("Enter a to add a fruit, i to import from csv, dl to delete an item, d to display table : ")
    if choose == "a":
        name = input("Name : ")
        quantity = input("Quantity : ")
        color = input("Color : ")
        addItem(name,quantity, color)

    if choose == "i":
        importCsv()

    if choose == "dl":
        item = input("Name of item to delete : ")
        deleteItem(item)

    if choose == "d":
        displayTable()



dbc.close()