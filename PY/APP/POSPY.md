import psycopg2 as p2
import pandas as pd

conn = p2.connect(host="127.0.0.1", database="test", user="postgres", password="***")

def test1():
    cur1 = conn.cursor()
    cur1.execute("select * from blabla where dep = 'blabla'")
    row1 = cur1.fetchall()
    return row1

def test2():
    cur2 = conn.cursor()
    cur2.execute("select lastname, firstname from blabla")
    row2 = cur2.fetchall()
    return row2

lab1 = ['systemid','dep','city']
lab2 = ['lastname','firstname']

pan1 = (pd.DataFrame.from_records(test1(), columns=lab1))
pan2 = (pd.DataFrame.from_records(test2(), columns=lab2))

print(pan1)
print(' ')
print(pan2)
