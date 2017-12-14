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



### <h3 id='3'>Lists</h3>

* [[python.org](https://docs.python.org/3/tutorial/introduction.html#lists)]
* [[linuxconfig](https://linuxconfig.org/python-list-methods)]
* [[dev.google](https://developers.google.com/edu/python/lists)]
* [[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Lists.ipynb)]
* [[digitalocean](https://www.digitalocean.com/community/tutorials/understanding-lists-in-python-3)]
* [[thomas-cokelaer](http://thomas-cokelaer.info/tutorials/python/lists.html)]

```python
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
>>> squares[0]  # indexing returns the item
1
>>> squares[-1]
25
>>> squares[-3:]  # slicing returns a new list
[9, 16, 25]
>>> squares[:]
[1, 4, 9, 16, 25]
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

```python
>>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
>>> 4 ** 3  # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64  # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]
>>> cubes.append(216)  # add the cube of 6
>>> cubes.append(7 ** 3)  # and the cube of 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
```

```python
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters
[]
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4
```

```python
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
```

List methods

Append

In order append() an element onto an array, call the method with the element in the parenthesis.

```python
linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
linux_distros.append("Mint")
print(linux_distros)

>>>
['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo', 'Mint']
>>>
```

Pop

The pop() method can work in two different ways. If you leave the parenthesis empty, it works as the opposite of append().

```python
linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
linux_distros.pop()
print(linux_distros)

>>>
['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch']
>>>

linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch']
linux_distros.pop()
print(linux_distros)

>>>
['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE']
>>>

linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch']
linux_distros.pop(1)
print(linux_distros)

>>>
['Debian', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch']
>>>
```

Insert

In order to use insert() to place a new element into a list, you have to specify the index where you want to insert your new element and the element that you want to insert.

```python
linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
linux_distros.insert(2, "Mint")
print(linux_distros)

>>>
['Debian', 'Ubuntu', 'Mint', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
>>>

print(linux_distros[4])

>>>
CentOS
>>>
```

Remove

remove() works sort of like giving pop an index to remove, but instead of giving remove() an index you give it the actual value of the element. It will find and remove the first occurrence of that value in the list. So, be sure that the first occurrence is the one that you want to remove. Otherwise, it's probably best to figure out the index of the element that you do want to remove and use pop().

```python
linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
linux_distros.remove("Arch")
print(linux_distros)

>>>
['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Gentoo']
>>>
```

Extend

extend() adds two lists together. It adds the list in parenthesis to the list that it is being called on.

```python
linux_distros = ['Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
debian_distros = ['Debian', 'Ubuntu', 'Mint']
linux_distros.extend(debian_distros)
print(linux_distros)

>>>
['Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo', 'Debian', 'Ubuntu', 'Mint']
>>>
```

Index

There is a way to find out the index of an element, and that's the index() method. Like with the others, index() finds the first occurrence of an element, not every occurrence.

```python
linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
print(linux_distros.index("Arch"))

>>>
5
>>>
```

Sort

If you need to sort a list, either alphabetically or numerically, Python has you covered there as well. Just call the sort() method on the list, and it will be saved in the new order. This will overwrite the previous list, so create a copy to sort, if you need to preserve the original.

```python
linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
linux_distros.sort()
print(linux_distros)

>>>
['Arch', 'CentOS', 'Debian', 'Fedora', 'Gentoo', 'OpenSUSE', 'Ubuntu']
>>>
```

```python
numbers_to_sort = [1, 5, 8, 16, 3, 75, 4, 23, 9, 15, 8, 32]
numbers_to_sort.sort()
print(numbers_to_sort)

>>>
[1, 3, 4, 5, 8, 8, 9, 15, 16, 23, 32, 75]
>>>
```

Reverse

reverse() is a bit of an odd method. It reverses the order of elements in a list in place and saves it. It doesn't put them in any kind of special order, it just flips the list around.

```python
linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
linux_distros.reverse()
print(linux_distros)

>>>
['Gentoo', 'Arch', 'OpenSUSE', 'CentOS', 'Fedora', 'Ubuntu', 'Debian']
>>>
```

```python
linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
linux_distros.sort()
linux_distros.reverse()
print(linux_distros)

>>>
['Ubuntu', 'OpenSUSE', 'Gentoo', 'Fedora', 'Debian', 'CentOS', 'Arch']
>>>
```

```
list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
list.sort() -- sorts the list in place (does not return it). (The sorted() function shown below is preferred.)
list.reverse() -- reverses the list in place (does not return it)
list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).
```

### <h3 id='4'>Dictionaries</h3>

* [[python.org](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)]
* [[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Dictionaries.ipynb)]
* [[digitalocean](https://www.digitalocean.com/community/tutorials/understanding-dictionaries-in-python-3)]
* [[thomas-cokelaer](http://thomas-cokelaer.info/tutorials/python/dicts.html)]

Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys. 

```python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'sape': 4139, 'guido': 4127, 'jack': 4098}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'guido': 4127, 'irv': 4127, 'jack': 4098}
>>> list(tel.keys())
['irv', 'guido', 'jack']
>>> sorted(tel.keys())
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```

```python
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'jack': 4098, 'guido': 4127}
```

```python
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```

```python
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'jack': 4098, 'guido': 4127}
```

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
