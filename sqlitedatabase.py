import sqlite3
dbc = sqlite3.connect("fruits.db")
cur = dbc.cursor()

cur.execute("create table if not exists fruit(name text, quantity integer, color text)")

def addItem(name, quantity, color):
    print(name)
    sql = f"INSERT INTO fruit VALUES('{name}', '{quantity}', '{color}')"
    print(sql)
    cur.execute(sql)
    dbc.commit()

def displayTable():
    sql = "SELECT * FROM fruit"
    cur.execute(sql)
    res = cur.fetchall()
    print(res)

#sql = "insert into fruit values('apple', 10, 'green')"
#cur.execute(sql)
#dbc.commit()

sql = "select * from fruit"
cur.execute(sql)
res = cur.fetchall()
print(res)
choose = input("Enter another fruit y/n ")
if choose == "y":
    name = input("Name : ")
    quantity = input("Quantity : ")
    color = input("Color : ")
    addItem(name,quantity, color)



dbc.close()