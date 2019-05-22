
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [C](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [scripts](https://github.com/ttltrk/PRG/blob/master/APPS.MD)

---

### column records to the list - lists to the dictionary

```python
import psycopg2 as p2
import pandas as pd

#--------------------------------------------
# connection to the db 

conn = p2.connect(host="127.0.0.1", database="test", user="postgres", password="***")

#--------------------------------------------
# your queries

def test1():
    cur1 = conn.cursor()
    cur1.execute("select bla from blabla where dep = 'bla' ORDER BY bla ASC")
    row1 = cur1.fetchall()
    return row1

def test2():
    cur2 = conn.cursor()
    cur2.execute("select bla from blabla ORDER BY bla ASC")
    row2 = cur2.fetchall()
    return row2

#--------------------------------------------
# column headers

lab1 = ['bla']
lab2 = ['bla']

#--------------------------------------------
# pandas dataframe connection

pan1 = (pd.DataFrame.from_records(test1(), columns=lab1))
pan2 = (pd.DataFrame.from_records(test2(), columns=lab2))

print(pan1)
print(' ')
print(pan2)
print(' ')

#--------------------------------------------
# add column records to the list

pan1['new'] = pan1['bla']
dfToList1 = pan1['new'].tolist()

pan2['new'] = pan2['bla']
dfToList2 = pan2['new'].tolist()

print(dfToList1)
print(dfToList2)
print(' ')

#--------------------------------------------
# concatenate two list into to the dictionary

d1 = dict(zip(dfToList1, dfToList2))
d2 = {k: v for (k, v) in d1.items() if v == 'doe'}  
#d1d2 = list(d2.keys())

print(d1)
print(d2)
```
