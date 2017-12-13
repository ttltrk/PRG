
OPyM 1.0
======

[APPS](https://github.com/ttltrk/PRG/tree/master/PY/APP)

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

### <h3 id='1'>Numbers</h3>

* [[python.org](https://docs.python.org/3/tutorial/introduction.html#numbers)]
* [[jupyter](http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Numbers.ipynb)]
* [[digitalocean](https://www.digitalocean.com/community/tutorials/how-to-do-math-in-python-3-with-operators)]

The interpreter acts as a simple calculator: you can type an expression at it and it will write the value. Expression syntax is straightforward: the operators ```+```, ```-```, ```*``` and ```/``` work just like in most other languages.

int = (e.g. 2, 4, 20) 

float = (e.g. 5.0, 1.6)

|Operation|	What it returns| Examples |
|---------|----------------|----------|
|x + y	|Sum of x and y | 1 + 1 = 2 |
|x - y	|Difference of x and y| 2 - 1 = 1 |
|-x	|Changed sign of x| -5|
|+x	|Identity of x| +5|
|x * y	|Product of x and y| 3 * 3 = 9|
|x / y	|Quotient of x and y| 17 / 3 = 5.666666666666667|
|x // y	|Quotient from floor division of x and y| 17 // 3 = 5|
|x % y	|Remainder of x / y| 17 % 3 = 2|
|x ** y	|x to the y power| 2 ** 3 = 8 |

PEMDAS

|Rank|Operators| Stands For|
|---|-----|----|
|1| ()   []   ->   .   ::	|Function call, scope, array/member access|
|2| !   ~   -   +   *   &   sizeof   type cast   ++   --  	|(most) unary operators, sizeof and type casts (right to left)|
|3| *   /   % MOD	|Multiplication, division, modulo|
|4| +   -	|Addition and subtraction|
|5| <<   >>	|Bitwise shift left and right|
|6|	<   <=   >   >=	|Comparisons: less-than and greater-than|
|7| ==   !=	|Comparisons: equal and not equal|
|8|	&	|Bitwise AND|
|9|	^	|Bitwise exclusive OR (XOR)|
|10|	|	|Bitwise inclusive (normal) OR|
|11|	&&	|Logical AND|
|12|	||	|Logical OR|
|13|	 ? :	|Conditional expression (ternary)|
|14|	=   +=   -=   *=   /=   %=   &=   |=   ^=   <<=   >>=	|Assignment operators (right to left)|
|15| ,	|Comma operator|

|Assignment Operator|Stands For|
|-------------------|----------|
|y += 1          |# add then assign value|
|y -= 1          |# subtract then assign value|
|y *= 2          |# multiply then assign value|
|y /= 3          |# divide then assign value|
|y // = 5        |# floor divide then assign value|
|y **= 2         |# increase to the power of then assign value|
|y %= 3          |# return remainder then assign value|


```python
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # division always returns a floating point number
1.6
```

```python
>>> 17 / 3  # classic division returns a float
5.666666666666667
>>>
>>> 17 // 3  # floor division discards the fractional part
5
>>> 17 % 3  # the % operator returns the remainder of the division
2
>>> 5 * 3 + 2  # result * divisor + remainder
17
```

```python
>>> 5 ** 2  # 5 squared
25
>>> 2 ** 7  # 2 to the power of 7
128
```

```python
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
```

```python
>>> 4 * 3.75 - 1
14.0
```

```python
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
```

### <h3 id='2'>Strings</h3>

* [[python.org](https://docs.python.org/3/tutorial/introduction.html#strings)]
* [[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Strings.ipynb)]
* [[digitalocean pt1](https://www.digitalocean.com/community/tutorials/an-introduction-to-working-with-strings-in-python-3)]
* [[digitalocean pt2](https://www.digitalocean.com/community/tutorials/how-to-format-text-in-python-3)]
* [[digitalocean pt3](https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3)]
* [[digitalocean pt4](https://www.digitalocean.com/community/tutorials/how-to-use-variables-in-python-3)]
* [[thomas-cokelaer](http://thomas-cokelaer.info/tutorials/python/strings.html)]

Besides numbers, Python can also manipulate strings, which can be expressed in several ways. They can be enclosed in single quotes ```('...')``` or double quotes ```("...")``` with the same result.

```python
>>> 'spam eggs'  # single quotes
'spam eggs'
>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"
>>> "doesn't"  # ...or use double quotes instead
"doesn't"
>>> '"Yes," he said.'
'"Yes," he said.'
>>> "\"Yes,\" he said."
'"Yes," he said.'
>>> '"Isn\'t," she said.'
'"Isn\'t," she said.'
```

```python
>>> '"Isn\'t," she said.'
'"Isn\'t," she said.'
>>> print('"Isn\'t," she said.')
"Isn't," she said.
>>> s = 'First line.\nSecond line.'  # \n means newline
>>> s  # without print(), \n is included in the output
'First line.\nSecond line.'
>>> print(s)  # with print(), \n produces a new line
First line.
Second line.
```

```python
>>> print('C:\some\name')  # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name')  # note the r before the quote
C:\some\name
```

```python
>>> # 3 times 'un', followed by 'ium'
>>> 3 * 'un' + 'ium'
'unununium'
```

```python
>>> 'Py' 'thon'
'Python'
```

```python
>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
```

```python
>>> prefix = 'Py'
>>> prefix 'thon'  # can't concatenate a variable and a string literal
  ...
SyntaxError: invalid syntax
>>> ('un' * 3) 'ium'
  ...
SyntaxError: invalid syntax
>>> prefix + 'thon'
'Python'
```

```python
>>> word = 'Python'
>>> word[0]  # character in position 0
'P'
>>> word[5]  # character in position 5
'n'
>>>
>>> word[-1]  # last character
'n'
>>> word[-2]  # second-last character
'o'
>>> word[-6]
'P'
>>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'
>>> word[:2]   # character from the beginning to position 2 (excluded)
'Py'
>>> word[4:]   # characters from position 4 (included) to the end
'on'
>>> word[-2:]  # characters from the second-last (included) to the end
'on'
```

```python

 | P | y | t | h | o | n |
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

```python
>>> word[42]  # the word only has 6 characters
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

```python
>>> word[4:42]
'on'
>>> word[42:]
''
```

```python
>>> word[0] = 'J'
  ...
TypeError: 'str' object does not support item assignment
>>> word[2:] = 'py'
  ...
TypeError: 'str' object does not support item assignment
```

```python
>>> 'J' + word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'
```

```python
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s)
34
```

```python
s = 'Hello World concatenate me!'

print(s.upper())
print(s.lower())
print(s.split())
print(s.split('W'))

>>>
HELLO WORLD CONCATENATE ME!
hello world concatenate me!
['Hello', 'World', 'concatenate', 'me!']
['Hello ', 'orld concatenate me!']
>>>
```

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

### <h3 id='3'>Lists</h3>

* [[python.org](https://docs.python.org/3/tutorial/introduction.html#lists)]
* [[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Lists.ipynb)]
* [[digitalocean](https://www.digitalocean.com/community/tutorials/understanding-lists-in-python-3)]
* [[thomas-cokelaer](http://thomas-cokelaer.info/tutorials/python/lists.html)]

```python
l = [1,2,3]
```

### <h3 id='4'>Dictionaries</h3>

* [[python.org](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)]
* [[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Dictionaries.ipynb)]
* [[digitalocean](https://www.digitalocean.com/community/tutorials/understanding-dictionaries-in-python-3)]
* [[thomas-cokelaer](http://thomas-cokelaer.info/tutorials/python/dicts.html)]

Basic form

```python
d = {'k1':'v1','k2':'v2'}
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

Basic form

```python
t = (1,2,3)
```

### <h3 id='6'>Sets</h3>

* [[python.org](https://docs.python.org/3/tutorial/datastructures.html#sets)]
* [[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Sets%20and%20Booleans.ipynb)]
* [[thomas-cokelaer](http://thomas-cokelaer.info/tutorials/python/sets.html?highlight=sets)]

Section 1.2 - Comparison Operators
------

### <h3 id="7">Comparison Operators</h3>

* [[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Comparison%20Operators.ipynb)]
* [[jupyter_2](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Chained%20Comparison%20Operators.ipynb)]

Section 1.3 - Python Statements
------

### <h3 id="8">if, elif and else</h3>

* [[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/If%2C%20elif%2C%20and%20else%20Statements.ipynb)]

### <h3 id="9">for loops</h3>

### <h3 id="10">while loops</h3>

### <h3 id="11">range()</h3>

### <h3 id="12">List Comprehensions</h3>

Section 1.4 - Methods and Functions
------

### <h3 id="13">Methods</h3>

### <h3 id="14">Functions</h3>

### <h3 id="15">lambda expressions</h3>

### <h3 id="16">Nested Statements and Scope</h3>
