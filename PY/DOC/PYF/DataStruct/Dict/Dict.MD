

---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [DS](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/DataStruct/DS.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Data Structures - Dictionary</h3>

---

how to find any string (in our case bingo) in the dictionary 

```python
import string as st

def bingo(array): 
    
    abc=st.ascii_lowercase
    
    labc=list(abc)    
    lnum=list(range(1,len(abc)+1))
    dic = dict(zip(lnum,labc))

    res=[dic[nums] for nums in array]
    print(res)
    
    if 'b' in res and 'i' in res and 'n' in res and 'g' in res and 'o' in res:
        return True
    else:
        return False
    
print(bingo([1, 2, 3, 7, 5, 14, 7, 15, 9, 10]))

>>>
['a', 'b', 'c', 'g', 'e', 'n', 'g', 'o', 'i', 'j']
True
>>>
```

<a href='#^'>^^^</a>

---

join two list into the one dict

```python
    #join odd integers with odd occurencies into the dict
    dictionary = dict(zip(seq, listOutOrigin))
    print(dictionary)
```

<a href='#^'>^^^</a>

---

max value and key from dict

```python
    #max value and max key from dict
    max_value = max(dictionary.values())  # maximum value
    max_keys = [k for k, v in dictionary.items() if v == max_value]  # getting all keys containing the `maximum`
    print(max_value, max_keys)
```

<a href='#^'>^^^</a>

---

```python
{'key1':'value1','key2':'value2'}
```

<a href='#^'>^^^</a>

```python
d = {'key1':'value1','key2':'value2'}
print(d)
print(d['key1'])

>>>
{'key1': 'value1', 'key2': 'value2'}
value1
>>>
```

<a href='#^'>^^^</a>

```python
prices = {'apple':1.20, 'orange':2.15, 'milk':0.99}

print(prices['apple'])

>>>
1.2
>>>
```

<a href='#^'>^^^</a>

```python
d = {'k1':123, 'k2':[0,1,2], 'k3':{'ins':'100'}}

print(d['k2'])
print(d['k2'][2])
print(d['k3']['ins'])

>>>
[0, 1, 2]
2
100
>>>
```

<a href='#^'>^^^</a>

```python
d = {'k1':123, 'k2':[0,1,2], 'k3':{'ins':'100'}, 'k4':['a','b','c']}

print(d['k4'][2])
print(d['k4'][2].upper())

>>>
c
C
>>>
```

<a href='#^'>^^^</a>

```python
d = {'k1':100, 'k2':200}

d['k3'] = 300

print(d)

d['k1'] = 'NEW VALUE'

print(d)

>>>
{'k1': 100, 'k2': 200, 'k3': 300}
{'k1': 'NEW VALUE', 'k2': 200, 'k3': 300}
>>>
```

<a href='#^'>^^^</a>

```python
d = {'k1':100, 'k2':200}

d['k3'] = 300

print(d)
print(d.keys())
print(d.values())
print(d.items())


>>>
{'k1': 100, 'k2': 200, 'k3': 300}
dict_keys(['k1', 'k2', 'k3'])
dict_values([100, 200, 300])
dict_items([('k1', 100), ('k2', 200), ('k3', 300)])
>>>
```

<a href='#^'>^^^</a>

```python
my_dict = {}

my_dict1 = {
  1: 'apple', 
  2: 'ball'}

my_dict2 = {
  'name': 'John', 
  1: [2, 4, 3]}

my_dict3 = dict({
  1:'apple', 
  2:'ball'})

my_dict4 = dict([
  (1,'apple'), 
  (2,'ball')])
  
print(my_dict)
print(my_dict1)
print(my_dict2)
print(my_dict3)
print(my_dict4)

>>>
{}
{1: 'apple', 2: 'ball'}
{'name': 'John', 1: [2, 4, 3]}
{1: 'apple', 2: 'ball'}
{1: 'apple', 2: 'ball'}
>>>
```

<a href='#^'>^^^</a>

---

```python
d = {'k1':1,'k2':2}
a = {x:x**2 for x in range(10)}
print(a)

>>>
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>>
'''
```

```python
'''
d = {'k1':1,'k2':2}
a = {k:v**2 for k,v in zip(['a','b'],range(2))}
print(a)

>>>
{'a': 0, 'b': 1}
>>>
```

<a href='#^'>^^^</a>

---
