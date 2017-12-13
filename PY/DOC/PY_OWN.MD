
Own Python Manual
======

### Section 1 - Objects and Data Structure Basics
  * <a href="#1">1 - Numbers</a>
  * <a href="#2">2 - Strings</a>
  * <a href="#3">3 - Lists</a>
  * <a href="#4">4 - Dictionaries</a>
  * <a href="#5">5 - Tuples</a>
  * <a href="#6">6 - Sets</a>
  
### Section 2 - Comparison Operators
  * <a href="#7">7 - Comparison Operators</a>
  
### Section 3 - Python Statements
  * <a href="#8">if, elif and else</a>
  * <a href="#9"></a>
  * <a href="#10"></a>
  * <a href="#11"></a>
  * <a href="#12"></a>
  
Section 1 - Objects and Data Structure Basics
------

### <h3 id='1'>1 - Numbers</h3>

* [[python.org](https://docs.python.org/3/tutorial/introduction.html#numbers)]
* [[jupyter](http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Numbers.ipynb)]
* [[digitalocean](https://www.digitalocean.com/community/tutorials/how-to-do-math-in-python-3-with-operators)]

The interpreter acts as a simple calculator: you can type an expression at it and it will write the value. Expression syntax is straightforward: the operators ```+```, ```-```, ```*``` and ```/``` work just like in most other languages.

int = (e.g. 2, 4, 20) 

float = (e.g. 5.0, 1.6)

|Operation|	What it returns|
|---------|----------------|
|x + y	|Sum of x and y | 1 + 1 = 2 |
|x - y	|Difference of x and y| 2 - 1 = 1 |
|-x	|Changed sign of x| -5|
|+x	|Identity of x| +5|
|x * y	|Product of x and y| 3 * 3 = 9|
|x / y	|Quotient of x and y| 9 / 3 = 3|
|x // y	|Quotient from floor division of x and y| 9 // 3 = |
|x % y	|Remainder of x / y| 16 % 5 = 1|
|x ** y	|x to the y power| 2 ** 2 = 8 |

### <h3 id='2'>2 - Strings</h3>

* [[python.org](https://docs.python.org/3/tutorial/introduction.html#strings)]
* [[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Strings.ipynb)]
* [[digitalocean pt1](https://www.digitalocean.com/community/tutorials/an-introduction-to-working-with-strings-in-python-3)]
* [[digitalocean pt2](https://www.digitalocean.com/community/tutorials/how-to-format-text-in-python-3)]
* [[digitalocean pt3](https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3)]
* [[digitalocean pt4](https://www.digitalocean.com/community/tutorials/how-to-use-variables-in-python-3)]
* [[thomas-cokelaer](http://thomas-cokelaer.info/tutorials/python/strings.html)]

```python
ss = "Sammy Shark!"

print(ss[0])
print(ss[1])
print(ss[2])
print(ss[3])
print(ss[4])
print(ss[5])
print(ss[6])
print(ss[7])
print(ss[8])
print(ss[9])
print(ss[10])
print(ss[11])
print(ss[12])

>>>
S
a
m
m
y
 
S
h
a
r
k
!
>>>
```

```python
ss = "Sammy Shark!"

print(ss[-1])
print(ss[-2])
print(ss[-3])
print(ss[-4])
print(ss[-5])
print(ss[-6])
print(ss[-7])
print(ss[-8])
print(ss[-9])
print(ss[-10])
print(ss[-11])
print(ss[-12])

>>>
!
k
r
a
h
S
 
y
m
m
a
S
>>>
```

```python
ss = "Sammy Shark!"

print(ss[:5])
print(ss[6:11])
print(ss[7:])

>>>
Sammy
Shark
hark!
>>>
```

```python
ss = "Sammy Shark!"

print(ss[0:12:1])
print(ss[0:12:2])
print(ss[0:12:3])
print(ss[::1])
print(ss[::2])
print(ss[::3])

>>>
Sammy Shark!
SmySak
SmSr
Sammy Shark!
SmySak
SmSr
>>>
```

```python
ss = "Sammy Shark!"

print(ss[::-1])
print(ss[::-2])
print(ss[::-3])

>>>
!krahS ymmaS
!rh ma
!a m
>>>
```

### <h3 id='3'>3 - Lists</h3>

* [[python.org](https://docs.python.org/3/tutorial/introduction.html#lists)]
* [[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Lists.ipynb)]
* [[digitalocean](https://www.digitalocean.com/community/tutorials/understanding-lists-in-python-3)]
* [[thomas-cokelaer](http://thomas-cokelaer.info/tutorials/python/lists.html)]

```python
l = [1,2,3]
```

### <h3 id='4'>4 - Dictionaries</h3>

* [[python.org](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)]
* [[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Dictionaries.ipynb)]
* [[digitalocean](https://www.digitalocean.com/community/tutorials/understanding-dictionaries-in-python-3)]
* [[thomas-cokelaer](http://thomas-cokelaer.info/tutorials/python/dicts.html)]

Basic form

```python
d = {'k1':'v1','k2':'v2'}
```

### <h3 id='5'>5 - Tuples</h3>

* [[python.org](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)]
* [[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Tuples.ipynb)]
* [[digitalocean](https://www.digitalocean.com/community/tutorials/understanding-tuples-in-python-3)]
* [[thomas-cokelaer](http://thomas-cokelaer.info/tutorials/python/tuples.html)]

In Python, tuples are part of the standard language. This is a data structure very similar to the list data structure. The main difference being that tuple manipulation are faster than list because tuples are immutable.

In Python tuples are very similar to lists, however, unlike lists they are immutable meaning they can not be changed. You would use tuples to present things that shouldn't be changed, such as days of the week, or dates on a calendar.

A tuple is a data structure that is an immutable, or unchangeable, ordered sequence of elements. Because tuples are immutable, their values cannot be modified.
Tuples are used for grouping data. Each element or value that is inside of a tuple is called an item.

Basic form

```python
t = (1,2,3)
```

### <h3 id='6'>6 - Sets</h3>

* [[python.org](https://docs.python.org/3/tutorial/datastructures.html#sets)]
* [[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Sets%20and%20Booleans.ipynb)]
* [[thomas-cokelaer](http://thomas-cokelaer.info/tutorials/python/sets.html?highlight=sets)]

Section 2 - Comparison Operators
------

### <h3 id="7">7 - Comparison Operators</h3>

* [[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Comparison%20Operators.ipynb)]
* [[jupyter_2](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Chained%20Comparison%20Operators.ipynb)]

Section 3 - Python Statements
------

### <h3 id="8">if, elif and else</h3>

### <h3 id="9">for loops</h3>

### <h3 id="10">while loops</h3>

### <h3 id="11">range()</h3>

### <h3 id="12">List Comprehensions</h3>
