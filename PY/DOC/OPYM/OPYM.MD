OPyM 1.0
======

Own APPS: 

[APPS](https://github.com/ttltrk/PRG/tree/master/PY/APP)

Used sources:

* [[python.org](https://docs.python.org/3/tutorial/index.html)]
* [[jupyter/Jose Portilla](http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/tree/master/)]
* [[digitalocean/Lisa Tagliaferri](https://www.digitalocean.com/community/users/ltagliaferri)]
* [[thomas-cokelaer](http://thomas-cokelaer.info/tutorials/python/index.html)]
* [[Google's Python Class](https://developers.google.com/edu/python/)]

### Section 1.1 - Objects and Data Structure Basics
  * <a href="#1">Numbers</a>
  * <a href="#2">Strings</a>
  * <a href="#3">Lists</a>
  * <a href="#4">Dictionaries</a>
  * <a href="#5">Tuples</a>
  * <a href="#6">Sets</a>
  
### Section 1.2 - Comparison Operators
  * <a href="#7">Comparison Operators</a>
  
### Section 1.3 - Python Statements
  * <a href="#8">if, elif and else</a>
  * <a href="#9">for loops</a>
  * <a href="#10">while loops</a>
  * <a href="#11">range()</a>
  * <a href="#12">List Comprehensions</a>
  
### Section 1.4 - Methods and Functions
  * <a href="#13">Methods</a>
  * <a href="#14">Functions</a>
  * <a href="#15">lambda expressions</a>
  * <a href="#16">Nested Statements and Scope</a>

Section 1.1 - Objects and Data Structure Basics
------

### <h3 id='5'>Tuples</h3>

* [[python.org](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)]
* [[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Tuples.ipynb)]
* [[digitalocean](https://www.digitalocean.com/community/tutorials/understanding-tuples-in-python-3)]
* [[thomas-cokelaer](http://thomas-cokelaer.info/tutorials/python/tuples.html)]

In Python, tuples are part of the standard language. This is a data structure very similar to the list data structure. The main difference being that tuple manipulation are faster than list because tuples are immutable.

In Python tuples are very similar to lists, however, unlike lists they are immutable meaning they can not be changed. You would use tuples to present things that shouldn't be changed, such as days of the week, or dates on a calendar.

A tuple is a data structure that is an immutable, or unchangeable, ordered sequence of elements. Because tuples are immutable, their values cannot be modified.
Tuples are used for grouping data. Each element or value that is inside of a tuple is called an item.

A tuple consists of a number of values separated by commas, for instance:

```python
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
... t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
... v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
```

### <h3 id='6'>Sets</h3>

* [[python.org](https://docs.python.org/3/tutorial/datastructures.html#sets)]
* [[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Sets%20and%20Booleans.ipynb)]
* [[thomas-cokelaer](http://thomas-cokelaer.info/tutorials/python/sets.html?highlight=sets)]

A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. 

```python
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```

Section 1.2 - Comparison Operators
------

### <h3 id="7">Comparison Operators</h3>

* [[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Comparison%20Operators.ipynb)]
* [[jupyter_2](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Chained%20Comparison%20Operators.ipynb)]

```python
>>> 2 == 2
True
>>> 1 == 1
True
>>> 1 == 0
False
>>> 
```

```python
>>> 2 != 1
True
>>> 2 != 2
False
>>> 
```

```python
>>> 2 > 1
True
>>> 2 > 4
False
>>> 
```

```python
>>> 2 < 4
True
>>> 2 < 1
False
>>> 
```

```python
>>> 2 >= 2
True
>>> 2 >= 1
True
>>> 
```

```python
>>> 2 <= 10
True
>>> 
```

```python
>>> 1 < 2
True
>>> 2 < 3
True
>>> 1 < 2 < 3
True
>>> 
```

```python
>>> 1 < 2 and 2 < 3
True
>>> 1 < 2 and 2 < 1
False
>>>
```

```python
>>> 1 < 2 or 2 < 3
True
>>> 1 < 2 or 2 < 1
True
>>> 
```

Section 1.3 - Python Statements
------

### <h3 id="8">if, elif and else</h3>

* [[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/If%2C%20elif%2C%20and%20else%20Statements.ipynb)]

Perhaps the most well-known statement type is the if statement.

```python
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')
...
More
```

```python	
>>> if True:
	print ("It was True")	
It was True
>>> 
```

```python
>>> x = False
>>> if x:
	print ("x was True")
else:
	print ("I will print when x is anything not True")	
I will print when x is anything not True
>>> 
```

```python
>>> x = True
>>> if x:
	print ("x was True")
else:
	print ("I will print when x is anything not True")	
x was True
>>> 
```

```python
loc = "Bank"
if loc == "Auto Shop":
    print ("Welcome to the Auto Shop!")
elif loc == "Bank":
    print ("Welcome to the Bank!")
else:
    print ("Where are you?!")

>>>
Welcome to the Bank!
>>>
```

```python
loc = "Mall"

if loc == "Auto Shop":
    print ("Welcome to the Auto Shop!")
elif loc == "Bank":
    print ("Welcome to the Bank!")
else:
    print ("Where are you?!")
	
>>>
Where are you?!
>>> 
```

```python
loc = "Mall"

if loc == "Auto Shop":
    print ("Welcome to the Auto Shop!")
elif loc == "Bank":
    print ("Welcome to the Bank!")
elif loc == "Mall":
    print ("Welcome to the Mall!")
else:
    print ("Where are you?!")
	
>>>
Welcome to the Mall!
>>> 
```

### <h3 id="9">for loops</h3>

```python
l = [1, 2, 3, 4, 5]

for element in l:
    print (element)
	
>>>
1
2
3
4
5
>>>
```

```python
l = [1, 2, 3, 4, 5]

for element in l:
    print ("something")
	
>>>
something
something
something
something
something
>>> 
```

```python
l = [1, 2, 3, 4, 5]

for num in l:
    if num % 2 == 0:
        print (num)

>>>
2
4
>>> 
```

```python
l = [1, 2, 3, 4, 5]

for num in l:
    if num % 2 == 1:
        print (num)

>>>
1
3
5
>>> 
```

```python
l = [1, 2, 3, 4, 5]

for num in l:
    if num % 2 == 0:
        print ("here is an even")
    else:
        print ("Odd number!")
		
>>>
Odd number!
here is an even
Odd number!
here is an even
Odd number!
>>> 
```

```python
l = [1, 2, 3, 4, 5]
list_sum = 0

for num in l:
    list_sum = list_sum + num

print (list_sum)

>>>
15
>>>
```

```python
l = ("a", "b", "c")
lst = ""

for abc in l:
    lst = lst + abc

print (lst)

>>>
abc
>>>
```

```python
l = [1, 2, 3, 4, 5]
list_sum = 0

for num in l:
    list_sum += num

print (list_sum)

>>>
15
>>>
```

```python
s = "this is a string!"

for item in s:
    print (item)
	
>>>
t
h
i
s
 
i
s
 
a
 
s
t
r
i
n
g
!
>>> 
```

```python
tup = (1, 2, 3, 4, 5)

for t in tup:
    print (t)
	
>>>
1
2
3
4
5
>>> 
```

```python
l = [(2,4),(6,8),(10,12)]

for tup in l:
    print (tup)
	
>>>
(2, 4)
(6, 8)
(10, 12)
>>> 
```

```python
l = [(2,4),(6,8),(10,12)]

for (t1, t2) in l:
    print (t1)
	
>>>
2
6
10
>>> 
```

```python
l = [(2,4),(6,8),(10,12)]

for (t1, t2) in l:
    print (t2)
	
>>>
4
8
12
>>> 
```

```python
l = [(2,4),(6,8),(10,12)]

for (t1, t2) in l:
    print (t1 - t2)
	
>>>
-2
-2
-2
>>> 
```

```python
d = {"k1" : 1, "k2" : 2, "k3" : 3}

for item in d:
    print (item)
	
>>>
k3
k1
k2
>>>
```

```python
d = {"k1" : 1, "k2" : 2, "k3" : 3}

for k, v in d.items():
    print (k)
    print (v)
	
>>>
k2
2
k1
1
k3
3
>>> 
```

### <h3 id="10">while loops</h3>

### <h3 id="11">range()</h3>

### <h3 id="12">List Comprehensions</h3>

Section 1.4 - Methods and Functions
------

### <h3 id="13">Methods</h3>

### <h3 id="14">Functions</h3>

### <h3 id="15">lambda expressions</h3>

### <h3 id="16">Nested Statements and Scope</h3>
