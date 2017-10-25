
[Complete Python Bootcamp: Go from zero to hero in Python](https://www.udemy.com/complete-python-bootcamp/learn/v4/content)
======

### Course Overview
  * <a href='#1'>Course Introduction</a>
  * <a href='#2'>Course Curriculum Overview</a>
  * <a href='#3'>Python 2 vs Python 3</a>
  * <a href='#4'>Have to Approach this Course</a>
  * <a href='#5'>Course Faq</a>

### Python Setup
  * <a href='#6'>Installation Notes</a>
  * <a href='#7'>Jupyter Notebook Installation</a>
  * <a href='#8'>IDE Selection</a>
  * <a href='#9'>Jupyther (iPython) Notebooks</a>
  * <a href='#10'>Faq - Notebooks</a>
  * <a href='#11'>Additional Resources</a>
  * <a href='#12'>Git and Github Overview</a> 

### Python Objects and Data Structure Basics
  * <a href='#13'>Numbers</a> 
  * <a href='#14'>Numbers Faq</a> 
  * <a href='#15'>Strings</a> 
  * <a href='#16'>Strings Faq</a> 
  * <a href='#17'>Print Formatting</a> 
  * <a href='#18'>Print Formatting Faq</a> 
  * <a href='#19'>Lists</a> 
  * <a href='#20'>Lists Faq</a> 
  * <a href='#21'>Dictionaries</a> 
  * <a href='#22'>Dictionaries Faq</a> 
  * <a href='#23'>Tuples</a> 
  * <a href='#24'>Files</a> 
  * <a href='#25'>Sets and Booleans</a> 
  * <a href='#26'>Resources Form More Basic Practice</a> 
  * <a href='#27'>Objects and Data Structures Assessment Test</a> 
  * <a href='#28'>Objects and Data Structures Assessment Solutions</a> 
  
### Python Comparison Operators
  * <a href='#29'>Comparison Operators</a>
  * <a href='#30'>Chained Comparison Operators</a>
 
### Python Statements
  * <a href='#31'>Introduction to Python Statements</a>
  * <a href='#32'>IF, ELIF and ELSE Statements</a>
  * <a href='#33'>FOR Loops</a>
  * <a href='#34'>WHILE Loops</a>
  * <a href='#35'>RANGE()</a>
  * <a href='#36'>List Comprehensions</a>
  * <a href='#37'>Statements Assessments Test</a>
  * <a href='#38'>Statements Assessments Solutions</a>
  
### Methods and Functions
  * <a href='#39'>Methods</a>
  * <a href='#40'>Functions</a>
  * <a href='#41'>Lambda Expressions</a>
  * <a href='#42'>Nested Statements and Scope</a>
  * <a href='#43'>Functions and Methods Homework</a>
  * <a href='#44'>Functions and Methods Homework Hints and Tips</a>
  * <a href='#45'>Functions and Methods Homework Solutions</a>
  
### Milestone Project 1
  * <a href='#46'>Milestone Project 1 Session</a>
  * <a href='#47'>Milestone Project 1 Assignment Overview</a>
  * <a href='#48'>Milestone Project 1 Help</a>
  * <a href='#49'>Milestone Project 1 Solution PT 1</a>
  * <a href='#50'>Milestone Project 1 Solution PT 2</a>
  * <a href='#51'>Milestone Project 1 Solution PT 3</a>

### Object Oriented Programming
  * <a href='#52'>OOP PT1 - Objects</a>
  * <a href='#53'>OOP PT2 - Classes</a>
  * <a href='#54'>OOP PT3 - Methods</a>
  * <a href='#55'>OOP PT4 - Inheritance</a>
  * <a href='#56'>OOP PT5 - Special Methods</a>
  * <a href='#57'>OOP - Homework Assignment</a>
  * <a href='#58'>OOP - Homework Solution</a>
  
### Errors And Exceptions Handling
  * <a href='#59'>Errors and Exceptions</a>
  * <a href='#60'>Exception Handling: Try, Except, Finally</a>
  * <a href='#61'>Errors and Exceptions HO</a>
  * <a href='#62'>Errors and Exceptions HO Solution</a>

Python Objects and Data Structure Basics
------

### <h4 id='13'>Numbers</h4>

```python
>>> 3/2
1.5
>>> 3.0/2
1.5
>>> float(3)/2
1.5
>>> float(3)
3.0
>>> 
>>> a = 5
>>> a
5
>>> a+a
10
>>> a
5
>>> a = a+a
>>> a
10
>>> a = a+a
>>> a
20
>>> 
>>> my_income = 100
>>> tax_rate = 0.1
>>> my_taxes = my_income*tax_rate
>>> my_taxes
10.0
>>> 
```

### <h4 id='15'>Strings</h4> 

```python
>>> 'hello'
'hello'
>>>
```

```python
>>> 'this is also a string'
'this is also a string'
>>>
```

```python
>>> "this is a string too"
'this is a string too'
>>>
```

```python
>>> "I'm a string"
"I'm a string"
>>>
```

```python
>>> ' "this is a quote" '
' "this is a quote" '
>>>
```

```python
>>> print ("hello world 1")
hello world 1
>>>
```

```python
>>> print ("here is a new line \n and here is the second line")
here is a new line 
 and here is the second line
>>>
```

```python
>>> print ("here is a new line \t and here is the second line")
here is a new line 	 and here is the second line
>>> 
```

```python
>>> len("hello world")
11
>>> 
```

```python
>>> s = "hello world"
>>> print (s)
hello world
>>> s
'hello world'
>>>
```

```python
>>> s[0] #indexing
'h'
>>>
```

```python
>>> s[1:]
'ello world'
>>>
```

```python
>>> s[:3]
'hel'
>>> 
```

```python
>>> s[:]
'hello world'
>>> s[-1]
'd'
>>> s[:-1]
'hello worl'
>>> 
```

```python
>>> s[::1]
'hello world'
>>> s[::2]
'hlowrd'
>>> s[::-1]
'dlrow olleh'
>>> 
```

```python
>>> s
'hello world'
>>> s + ' concatenate me!'
'hello world concatenate me!'
>>> 
```

```python
>>> letter = 'z'
>>> letter
'z'
>>> letter*10
'zzzzzzzzzz'
>>> 
```

```python
>>> s = 'hello'
>>> s.upper()
'HELLO'
>>> s.lower()
'hello'
>>> s.split()
['hello']
>>> s.split('e')
['h', 'llo']
>>> 
```

017. PRINT FORMATTING

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Print%20Formatting.ipynb

----------------------------------

#016.1.

>>> print ("this is a string")
this is a string

----------------------------------

#016.2.

>>> s = "string"
>>> print ("Place my variable here: %s" % (s))
Place my variable here: string
>>> 

----------------------------------

#016.3.

>>> x = 13.13
>>> print ("Floating point number: %1.2f" % (x))
Floating point number: 13.13
>>> print ("Floating point number: %1.2f" % (13.145))
Floating point number: 13.14
>>> print ("Floating point number: %1.3f" % (13.145))
Floating point number: 13.145
>>> print ("Floating point number: %25.3f" % (13.145))
Floating point number:                    13.145
>>> 

----------------------------------

#016.4.

>>> print ("First %s, Second %s, Third %s" % ("hi", "two", 3))
First hi, Second two, Third 3
>>> 

----------------------------------

#016.5.

>>> print ("First {x}, Second {x}".format(x="inserted"))
First inserted, Second inserted
>>> 

----------------------------------

#016.6.

>>> print ("First {x}, Second {x}, Third {y}".format(x="inserted", y="szohi"))
First inserted, Second inserted, Third szohi
>>> 

----------------------------------

BONUS SOURCE: https://pyformat.info/

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

019. LISTS

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Lists.ipynb

temp_list = [1, 2.5, "string"]

----------------------------------

#019.1.

>>> my_list = [1, 2, 3]
>>> my_list
[1, 2, 3]
>>> 

----------------------------------

#019.2.

>>> my_list = ["string", 23, 1.2, "o"]
>>> my_list
['string', 23, 1.2, 'o']
>>> len(my_list)
4
>>> 

----------------------------------

#019.3.

>>> my_list = ["one", "two", "three", 4, 5]
>>> my_list[0]
'one'
>>> my_list[1:]
['two', 'three', 4, 5]
>>> my_list[:3]
['one', 'two', 'three']
>>> 

----------------------------------

#019.4.

>>> my_list
['one', 'two', 'three', 4, 5]
>>> my_list + ["new item"]
['one', 'two', 'three', 4, 5, 'new item']
>>> my_list
['one', 'two', 'three', 4, 5]
>>> my_list = my_list + ["permanent add"]
>>> my_list
['one', 'two', 'three', 4, 5, 'permanent add']
>>>

----------------------------------

#019.5.

>>> my_list
['one', 'two', 'three', 4, 5, 'permanent add']
>>> my_list * 2
['one', 'two', 'three', 4, 5, 'permanent add', 'one', 'two', 'three', 4, 5, 'permanent add']
>>> 

----------------------------------

#019.6.

>>> l = [1, 2, 3]
>>> l
[1, 2, 3]
>>> l.append("append me!")
>>> l
[1, 2, 3, 'append me!']
>>> l.pop()
'append me!'
>>> l
[1, 2, 3]
>>> x = l.pop(0)
>>> x
1
>>> l
[2, 3]
>>> l[99]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    l[99]
IndexError: list index out of range
>>> 

----------------------------------

#019.7.

>>> new_list = ["a", "e", "x", "b", "c"]
>>> new_list
['a', 'e', 'x', 'b', 'c']
>>> new_list.reverse()
>>> new_list
['c', 'b', 'x', 'e', 'a']
>>> new_list.sort()
>>> new_list
['a', 'b', 'c', 'e', 'x']
>>> 

----------------------------------

#019.8.

>>> l_1 = [1, 2, 3]
>>> l_2 = [4, 5, 6]
>>> l_3 = [7, 8, 9]
>>> matrix = [l_1, l_2, l_3]
>>> matrix
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> matrix[0]
[1, 2, 3]
>>> matrix[0][2]
3
>>> matrix[1][1]
5
>>> matrix[2][0]
7
>>> 

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

21. DICTIONARIES

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Dictionaries.ipynb

temp_dict = {"key1" : "value1", "key2" : "value2"}

----------------------------------

#21.1.

>>> my_dict = {"key1" : "value1", "key2" : "value2"}
>>> my_dict
{'key2': 'value2', 'key1': 'value1'}
>>> my_dict["key1"]
'value1'
>>> 

----------------------------------

#21.2.

>>> my_dict = {"K1" : 123, "K2" : 3.4, "K3" : "string"}
>>> my_dict["K1"]
123
>>> 

----------------------------------

#21.3.

>>> my_dict["K3"]
'string'
>>> my_dict["K3"][0]
's'
>>> my_dict["K3"][::-1]
'gnirts'
>>> my_dict["K3"].upper()
'STRING'
>>> 

----------------------------------

#21.4.

>>> my_dict["K1"]
123 
>>> my_dict["K1"] - 120
3
>>> my_dict["K1"]
123
>>> 

----------------------------------

#21.5.

>>> my_dict = {"K1" : 123, "K2" : 3.4, "K3" : "string"}
>>> my_dict["K1"] = my_dict["K1"] - 120
>>> my_dict["K1"]
3
>>> my_dict
{'K3': 'string', 'K2': 3.4, 'K1': 3}
>>> 

----------------------------------

#21.6.

>>> my_dict["K1"]
3
>>> my_dict["K1"] = my_dict["K1"] + 100
>>> my_dict["K1"]
103
>>> my_dict["K1"] += 100
>>> my_dict["K1"]
203
>>> 

----------------------------------

#21.7.

>>> d = {}
>>> d
{}
>>> d["animal"] = "DOG"
>>> d
{'animal': 'DOG'}
>>> d["answer"] = 42
>>> d
{'answer': 42, 'animal': 'DOG'}
>>> 

----------------------------------

#21.8.

>>> d = {"K1" : {"nestkey" : {"subnestkey" : "value"}}}
>>> d
{'K1': {'nestkey': {'subnestkey': 'value'}}}
>>> d["K1"]
{'nestkey': {'subnestkey': 'value'}}
>>> d["K1"]["nestkey"]
{'subnestkey': 'value'}
>>> d["K1"]["nestkey"]["subnestkey"]
'value'
>>> d["K1"]["nestkey"]["subnestkey"].upper()
'VALUE'
>>> 

----------------------------------

#21.9.

>>> d = {}
>>> d["k1"] = 1
>>> d["k2"] = 2
>>> d["k3"] = 3
>>> d
{'k1': 1, 'k3': 3, 'k2': 2}
>>> d.keys()
dict_keys(['k1', 'k3', 'k2'])
>>> d.values()
dict_values([1, 3, 2])
>>> d.items()
dict_items([('k1', 1), ('k3', 3), ('k2', 2)])
>>> 

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

023. TUPLES

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Tuples.ipynb

temp_tuples = (1, 2, 3)

----------------------------------

#023.1.

>>> t = (1, 2, 3)
>>> t
(1, 2, 3)
>>> len(t)
3
>>> 

----------------------------------

#023.2.

>>> t = ("one", 2)
>>> t
('one', 2)
>>> t[0]
'one'
>>> t[1]
2
>>>  

----------------------------------

#023.3.

>>> t.index("one")
0
>>> t.index(2)
1
>>> t.count("one")
1
>>> 

----------------------------------

#023.4.

>>> t = (1, 1, 2, 3)
>>> t.count(1)
2
>>> 

----------------------------------

#023.5.

>>> l = [2, 2, 3]
>>> l
[2, 2, 3]
>>> l = [1, 2, 3]
>>> l
[1, 2, 3]
>>> l[0] = "s"
>>> l
['s', 2, 3]
>>> t = (1, 2, 3)
>>> t
(1, 2, 3)
>>> t[0] = "s"
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    t[0] = "s"
TypeError: 'tuple' object does not support item assignment
>>> 

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

24. FILES

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Files.ipynb

----------------------------------

#024.1.

>>> f = open("test.txt")
>>> f.read()
'this is a test line\n'
>>> f.read()
''
>>> f.seek(0)
0
>>> f.read()
'this is a test line\n'
>>> f.seek(0)
0
>>> f.readlines()
['this is a test line\n']
>>> 

----------------------------------

#024.2.

>>> f.seek(0)
0
>>> f.read()
'First line\nSecond line\n'
>>> for line in open("test.txt"):
	print (line)

	
First line

Second line

>>> 

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

025. SETS AND BOOLEANS

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Sets%20and%20Booleans.ipynb

#sets

----------------------------------

#025.1.

>>> x = set()
>>> x
set()
>>> 

----------------------------------

#025.2.

>>> x.add(1)
>>> x
{1}
>>> x.add(2)
>>> x
{1, 2}
>>> x.add(1)
>>> x
{1, 2}
>>> 

----------------------------------

#025.3.

>>> l = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4]
>>> l
[1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4]
>>> set(l)
{1, 2, 3, 4}
>>> 

----------------------------------

#booleans

----------------------------------

#025.4.

>>> a = True
>>> a
True
>>> 

----------------------------------

#025.5.

>>> 1 > 2
False
>>> 11 > 2
True
>>> 

----------------------------------

#025.6.

>>> b = None
>>> b
>>> 

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

026. RESOURCES FORM MORE BASIC PRACTICE

----------------------------------

Basic Practice:

http://codingbat.com/python

More Mathematical (and Harder) Practice:

https://projecteuler.net/archives

List of Practice Problems:

http://www.codeabbey.com/index/task_list

A SubReddit Devoted to Daily Practice Problems:

https://www.reddit.com/r/dailyprogrammer

A very tricky website with very few hints and touch problems (Not for beginners but still interesting)

http://www.pythonchallenge.com/

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

029. COMPARISON OPERATORS

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Comparison%20Operators.ipynb

----------------------------------

#029.1.

>>> 2 == 2
True
>>> 1 == 1
True
>>> 1 == 0
False
>>> 

----------------------------------

#029.2.

>>> 2 != 1
True
>>> 2 != 2
False
>>> 

----------------------------------

#029.3.

>>> 2 > 1
True
>>> 2 > 4
False
>>> 

----------------------------------

#029.4.

>>> 2 < 4
True
>>> 2 < 1
False
>>> 

----------------------------------

#029.5.

>>> 2 >= 2
True
>>> 2 >= 1
True
>>> 

----------------------------------

#029.6.

>>> 2 <= 10
True
>>> 

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

030. CHAINED COMPARISON OPERATORS

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Chained%20Comparison%20Operators.ipynb

----------------------------------

#030.1.

>>> 1 < 2
True
>>> 2 < 3
True
>>> 1 < 2 < 3
True
>>> 

----------------------------------

#030.2.

>>> 1 < 2 and 2 < 3
True
>>> 1 < 2 and 2 < 1
False
>>>

----------------------------------

#030.3.

>>> 1 < 2 or 2 < 3
True
>>> 1 < 2 or 2 < 1
True
>>> 

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

032. IF, ELIF AND ELSE STATEMENTS

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/If%2C%20elif%2C%20and%20else%20Statements.ipynb

if case1:
	perform action1
elif case2:
	perform action2
else:
	perform action3
	
----------------------------------

#032.1.
	
>>> if True:
	print ("It was True")	
It was True
>>> 

----------------------------------

#032.2.

>>> x = False
>>> if x:
	print ("x was True")
else:
	print ("I will print when x is anything not True")	
I will print when x is anything not True
>>> 

----------------------------------

#032.3.

>>> x = True
>>> if x:
	print ("x was True")
else:
	print ("I will print when x is anything not True")	
x was True
>>> 

----------------------------------

#032.4.

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

----------------------------------

#032.5.

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
	
----------------------------------

#032.6.

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

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

033. FOR LOOPS

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/For%20Loops.ipynb

for item in object:
	statements to do stuff

----------------------------------

#033.1.

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

----------------------------------

#033.2.

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

----------------------------------

#033.3.

l = [1, 2, 3, 4, 5]

for num in l:
    if num % 2 == 0:
        print (num)

>>>
2
4
>>> 

----------------------------------

#033.4.

l = [1, 2, 3, 4, 5]

for num in l:
    if num % 2 == 1:
        print (num)

>>>
1
3
5
>>> 

----------------------------------

#033.5.

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

----------------------------------

#033.6.

l = [1, 2, 3, 4, 5]
list_sum = 0

for num in l:
    list_sum = list_sum + num

print (list_sum)

>>>
15
>>>

----------------------------------

#033.7.

l = ("a", "b", "c")
lst = ""

for abc in l:
    lst = lst + abc

print (lst)

>>>
abc
>>>

----------------------------------

#033.8.

l = [1, 2, 3, 4, 5]
list_sum = 0

for num in l:
    list_sum += num

print (list_sum)

>>>
15
>>>

----------------------------------

#033.9.

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

----------------------------------

#033.10.

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

----------------------------------

#033.11.

l = [(2,4),(6,8),(10,12)]

for tup in l:
    print (tup)
	
>>>
(2, 4)
(6, 8)
(10, 12)
>>> 

----------------------------------

#033.12.

l = [(2,4),(6,8),(10,12)]

for (t1, t2) in l:
    print (t1)
	
>>>
2
6
10
>>> 

----------------------------------

#033.13.

l = [(2,4),(6,8),(10,12)]

for (t1, t2) in l:
    print (t2)
	
>>>
4
8
12
>>> 

----------------------------------

#033.14.

l = [(2,4),(6,8),(10,12)]

for (t1, t2) in l:
    print (t1 - t2)
	
>>>
-2
-2
-2
>>> 

----------------------------------

#033.15.

d = {"k1" : 1, "k2" : 2, "k3" : 3}

for item in d:
    print (item)
	
>>>
k3
k1
k2
>>>

----------------------------------

#033.16.

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

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

034. WHILE LOOPS

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/While%20loops.ipynb

while test:
	code statement
else:
	final code statements
	
----------------------------------

#035.1.

x = 0

while x < 10:
    print ("X is currently: ", x)
    x +=1
	
>>>
X is currently:  0
X is currently:  1
X is currently:  2
X is currently:  3
X is currently:  4
X is currently:  5
X is currently:  6
X is currently:  7
X is currently:  8
X is currently:  9
>>> 

----------------------------------

#035.2.

x = 0

while x < 10:
    print ("X is currently: ", x)
    x +=1
else:
    print ("All done!")
	
>>>
X is currently:  0
X is currently:  1
X is currently:  2
X is currently:  3
X is currently:  4
X is currently:  5
X is currently:  6
X is currently:  7
X is currently:  8
X is currently:  9
All done!
>>> 

----------------------------------

#035.3.

while test:
	code statement
	if test:
		break
	if test:
		continue
else:
	final code statements

----------------------------------

#035.4.

x = 0

while x < 10:
    print ("X is currently: ", x)
    print ("X is still less than 10, adding 1 to x")
    x +=1

    if x==3:
        print ("Hey x equals 3!")
    else:
        print ("continuing")
        continue
		
>>>
X is currently:  0
X is still less than 10, adding 1 to x
continuing
X is currently:  1
X is still less than 10, adding 1 to x
continuing
X is currently:  2
X is still less than 10, adding 1 to x
Hey x equals 3!
X is currently:  3
X is still less than 10, adding 1 to x
continuing
X is currently:  4
X is still less than 10, adding 1 to x
continuing
X is currently:  5
X is still less than 10, adding 1 to x
continuing
X is currently:  6
X is still less than 10, adding 1 to x
continuing
X is currently:  7
X is still less than 10, adding 1 to x
continuing
X is currently:  8
X is still less than 10, adding 1 to x
continuing
X is currently:  9
X is still less than 10, adding 1 to x
continuing
>>> 

----------------------------------

#035.5.

x = 0

while x < 10:
    print ("X is currently: ", x)
    print ("X is still less than 10, adding 1 to x")
    x +=1

    if x==3:
        print ("Hey x equals 3!")
        break
    else:
        print ("continuing")
        continue
		
>>>
X is currently:  0
X is still less than 10, adding 1 to x
continuing
X is currently:  1
X is still less than 10, adding 1 to x
continuing
X is currently:  2
X is still less than 10, adding 1 to x
Hey x equals 3!
>>>

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

035. RANGE() 

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Range%28%29.ipynb

----------------------------------

#035.1.

>>> x = range(1,5)
>>> type (x)
<class 'range'>
>>> 

----------------------------------

#035.2.

>>> list(range(0, 10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 

----------------------------------

#035.3.

>>> list(range(20))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> 

----------------------------------

#035.4.

>>> x = list(range(0,10))
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> type(x)
<class 'list'>
>>> 

----------------------------------

#035.5.

>>> start = 5
>>> stop = 20
>>> list(range(start,stop))
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> 

----------------------------------

#035.6.

>>> start = 5
>>> stop = 20
>>> list(range(start,stop,2))
[5, 7, 9, 11, 13, 15, 17, 19]
>>> 

----------------------------------

#035.7.

l = [1, 2, 3, 4, 5]

for num in range(1,11):
    print (num)
	
>>>
1
2
3
4
5
6
7
8
9
10
>>> 

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

036. LIST COMPREHENSIONS

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/List%20Comprehensions.ipynb

----------------------------------

#036.1.

l = []

for letter in "word":
    l.append(letter)

print (l)

>>>
['w', 'o', 'r', 'd']
>>> 

----------------------------------

#036.2.

>>> l = [letter for letter in "word"]
>>> l
['w', 'o', 'r', 'd']
>>> 

----------------------------------

#036.3.

>>> lst = [letter for letter in "word"]
>>> lst
['w', 'o', 'r', 'd']
>>> 

----------------------------------

#036.4.

>>> lst = [x**2 for x in range(0,11)]
>>> lst
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> 

----------------------------------

#036.5.

>>> lst = [number for number in range(11) if number % 2 ==0]
>>> lst
[0, 2, 4, 6, 8, 10]
>>> 

----------------------------------

#036.6.

lst = []

for number in range(11):
    if number %2 == 0:
        lst.append(number)

print (lst)

>>>
[0, 2, 4, 6, 8, 10]
>>> 

----------------------------------

#036.7.

celsius = [0, 10, 20.1, 34.5]

fahrenheit = [temp for temp in celsius]
    
print (fahrenheit)

>>>
[0, 10, 20.1, 34.5]
>>> 

----------------------------------

#036.8.

celsius = [0, 10, 20.1, 34.5]

fahrenheit = [(temp * (9/5.0) + 32) for temp in celsius]
    
print (fahrenheit)

>>>
[32.0, 50.0, 68.18, 94.1]
>>> 

----------------------------------

#036.9.

lst = [x**2 for x in [x**2 for x in range(11)]]

print (lst)

>>>
[0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000]
>>> 

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

038. STATEMENT ASSESSMENT SOLUTIONS

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Statements%20Assessment%20Test%20-%20Solutions.ipynb

----------------------------------

#038.1.

st = 'Print only the words that start with s in this sentence'

for word in st.split():
    if word[0] == 's':
        print (word)
		
>>>
start
s
sentence
>>> 

----------------------------------

#038.2.

# print all the even numbers from 0 to 10

>>> range(0,11,2)
range(0, 11, 2)
>>> list(range(0,11,2))
[0, 2, 4, 6, 8, 10]
>>> 

----------------------------------

#038.3.

# create a list of all numbers between 1 and 50 that are divisible by 3

>>> [x for x in range(1,50) if x%3 == 0]
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
>>> 

----------------------------------

#038.4.

# if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'

for word in st.split():
    if len(word)%2 == 0:
        print (word+" <-- has an even length!")
		
>>>
word <-- has an even length!
in <-- has an even length!
this <-- has an even length!
sentence <-- has an even length!
that <-- has an even length!
an <-- has an even length!
even <-- has an even length!
number <-- has an even length!
of <-- has an even length!
>>> 

----------------------------------

#038.5.

"""
Write a program that prints the integers from 1 to 20. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
"""

for num in range(1,21):
    if num % 5 == 0 and num % 3 == 0:
        print ("FizzBuzz")
    elif num % 3 == 0:
        print ("Fizz")
    elif num % 5 == 0:
        print ("Buzz")
    else:
        print (num)
		
>>>
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
>>> 

----------------------------------

#038.6.

>>> st = 'Create a list of the first letters of every word in this string'
>>> [word[0] for word in st.split()]
['C', 'a', 'l', 'o', 't', 'f', 'l', 'o', 'e', 'w', 'i', 't', 's']
>>> 

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

0.39 METHODS

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Methods.ipynb

----------------------------------

#039.1.

>>> l = [1,2,3,4,5]
>>> l.append(6)
>>> l
[1, 2, 3, 4, 5, 6]
>>> 

----------------------------------

#039.2.

>>> l
[1, 2, 3, 4, 5, 6]
>>> l.count(3)
1
>>> l.append(3)
>>> l
[1, 2, 3, 4, 5, 6, 3]
>>> l.count(3)
2
>>> 

----------------------------------

#039.3.

>>> help(l.count)
Help on built-in function count:

count(...) method of builtins.list instance
    L.count(value) -> integer -- return number of occurrences of value

>>> 

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

040. FUNCTIONS

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Functions.ipynb

----------------------------------

#040.1.

def name_of_function():
	pass

name_of_function()

>>> 
>>>

----------------------------------

#040.2.

def name_of_function(arg1, arg2):    
    pass

print (name_of_functions())

>>>
Traceback (most recent call last):
  File "C:/Program Files (x86)/Python/test.py", line 4, in <module>
    print (name_of_functions())
NameError: name 'name_of_functions' is not defined
>>> 

----------------------------------

#040.3.

def my_add_func(arg1, arg2):    
    print (arg1 + arg2)

my_add_func(1, 2)

>>>
3
>>>

----------------------------------

#040.4.

def say_hello():
    print ("hello!")

say_hello()

>>>
hello!
>>>

----------------------------------

#040.5.

def greeting(name):
    print ("hello "+ name)

greeting("trk")

>>>
hello trk
>>>

----------------------------------

#040.6.

def add_num(num1, num2):
    return (num1 + num2)

x = add_num(2, 3)

print(x)

>>>
5
>>>

----------------------------------

#040.7.

def add_num(num1, num2):
    return (num1 + num2)

x = add_num("one", "two")

print(x)

>>>
onetwo
>>>

----------------------------------

#040.8.

def is_prime(num):
    """
    IN: A number
    OUT: A print statement wheter or not the number is prime.
    """

    for n in range(2, num):
        if num % n == 0:
            print ("not prime")
            break
        else:
            print ("the number is prime!")
            
is_prime(12)

>>>
not prime
>>>

----------------------------------

#040.9.

def is_prime(num):
    """
    IN: A number
    OUT: A print statement wheter or not the number is prime.
    """

    for n in range(2, num):
        if num % n == 0:
            print ("not prime")
            break
        else:
            print ("the number is prime!")
            
is_prime(11)
    
>>>
the number is prime!
the number is prime!
the number is prime!
the number is prime!
the number is prime!
the number is prime!
the number is prime!
the number is prime!
the number is prime!
>>> 

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

041. LAMBDA EXPRESSIONS

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Lambda%20expressions.ipynb

----------------------------------

#041.1.

def square(num):
    result = num**2
    return result

print (square(2))

>>>
4
>>>

----------------------------------

#041.2.

def square(num):
    return num**2

print (square(3))

>>>
9
>>>

----------------------------------

#041.3.

def square(num): return num**2

print (square(4))

>>>
16
>>>

----------------------------------

#041.4.

square = lambda num: num**2

print (square(5))

>>>
25
>>>

----------------------------------

#041.5.

even = lambda num: num %2 == 0

print (even(4))

>>>
True
>>>

----------------------------------

#041.6.

def even(num):
    return num %2 == 0

print (even(10))

>>>
True
>>>

----------------------------------

#041.7.

first = lambda s: s[0]

print (first("hello"))

>>>
h
>>>

----------------------------------

#041.8.

rev = lambda s: s[::-1]

print (rev("hello"))

>>>
olleh
>>> 

----------------------------------

#041.9.

def adder(x, y):
    return x + y

print (adder(10, 12))

>>>
22
>>>

----------------------------------

#041.10.

adder = lambda x, y: x + y

print (adder(15, 2))

>>>
17
>>>

----------------------------------

#041.11.

check this out!!!

map()
filter()
reduce()

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

https://pythonconquerstheuniverse.wordpress.com/

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

----------------------------------

#041.12.

len_check = lambda item: len(item)

print (len_check("blabla"))

>>>
6
>>>

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

042. NESTED STATEMENTS AND SCOPE

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Nested%20Statements%20and%20Scope.ipynb

----------------------------------

#042.1.

x = 25

def printer():
    x = 50
    return x

print (x)
print (printer())

>>>
25
50
>>>

----------------------------------

#042.2.

# LOCAL

f = lambda x: x**2

print (f(2))

>>>
4
>>>

----------------------------------

#042.3.

# ENCLOSING FUNCTION LOCAL

name = "glob name"

def greet():
    #ENCLOSING FUNCTION
    name = "Sammy"

    def hello():
        print ("Hello " + name)

    hello()

greet()

>>>
Hello Sammy
>>>

----------------------------------

#042.4.

# ENCLOSING FUNCTION LOCAL

name = "glob name"

def greet():
    #ENCLOSING FUNCTION
    name = "Sammy"

    def hello():
        nick = "Steve"
        print ("Hello %s and Hello %s " % (nick, name))

    hello()

greet()

>>>
Hello Steve and Hello Sammy 
>>>

----------------------------------

#042.5.

# GLOBAL

name = "Annie"

print (name)

>>>
Annie
>>>

----------------------------------

#042.6.

# BUILT-IN

len

----------------------------------

#042.7.

# LOCAL VARIABLES

x = 50

def func(x):
    print ("x is" , x)
    x = 2
    print ("Changed local x to" , x)

func(x)
print ("but x is still" , x)

>>>
x is 50
Changed local x to 2
but x is still 50
>>>

----------------------------------

#042.8.

# LOCAL VARIABLES

x = 50

def func(x):
    print ("x is" , x)
    print ("Changed local x to" , x)
    x = 2
    
func(x)
print ("but x is still" , x)

>>>
x is 50
Changed local x to 50
but x is still 50
>>> 

----------------------------------

#042.9.

# GLOBAL STATEMENT

x = 50

def func():
    global x
    print ("This function is now using the global x!")
    print ("Because of global x is: ", x)
    x = 2
    print ("Ran func(), changed global x to" , x)

print ("Before calling func(), x is: " , x)
func()
print ("Value of x (outside of func()) is: " , x)

>>>
Before calling func(), x is:  50
This function is now using the global x!
Because of global x is:  50
Ran func(), changed global x to 2
Value of x (outside of func()) is:  2
>>>

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

049. MILESTONE PROJECT 1 SOLUTION PT 1

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Milestone%20Project%201-%20Walkthrough%20Steps%20Workbook.ipynb

----------------------------------

#049.1.

#STEP 1 - Write a function that can print out a board.

def display_board(board):

    print("  |  |")
    print("--|--|--")
    print("  |  |")

print(display_board([]))

>>>
  |  |
--|--|--
  |  |
>>>

----------------------------------

#049.2.

#STEP 1 - Write a function that can print out a board.

def display_board(board):

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

board = ["X"] * 10
print(display_board(board))

>>>
   |   |
 X | X | X
   |   |
-----------
   |   |
 X | X | X
   |   |
-----------
   |   |
 X | X | X
   |   |
>>>

----------------------------------

#049.3.

#STEP 1 - Write a function that can print out a board.

def display_board(board):

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

board = ["X", "O"] * 10
print(display_board(board))

>>>
   |   |
 O | X | O
   |   |
-----------
   |   |
 X | O | X
   |   |
-----------
   |   |
 O | X | O
   |   |
>>>

----------------------------------

#49.4.

#STEP 1 - Write a function that can print out a board.

def display_board(board):

    print('      1   2   3   4   5   6   7   8   9   10 ')
    print('    -----------------------------------------')
    print('    |   |   |   |   |   |   |   |   |   |   |')
    print('  0 | ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' | ' + board[10] + ' |')
    print('    |   |   |   |   |   |   |   |   |   |   |')
    print('    -----------------------------------------')
    print('    |   |   |   |   |   |   |   |   |   |   |')
    print(' 10 | ' + board[11] + ' | ' + board[12] + ' | ' + board[13] + ' | ' + board[14] + ' | ' + board[15] + ' | ' + board[16] + ' | ' + board[17] + ' | ' + board[18] + ' | ' + board[19] + ' | ' + board[20] + ' |')
    print('    |   |   |   |   |   |   |   |   |   |   |')
    print('    -----------------------------------------')
    print('    |   |   |   |   |   |   |   |   |   |   |')
    print(' 20 | ' + board[21] + ' | ' + board[22] + ' | ' + board[23] + ' | ' + board[24] + ' | ' + board[25] + ' | ' + board[26] + ' | ' + board[27] + ' | ' + board[28] + ' | ' + board[29] + ' | ' + board[30] + ' |')
    print('    |   |   |   |   |   |   |   |   |   |   |')
    print('    -----------------------------------------')
    print('    |   |   |   |   |   |   |   |   |   |   |')
    print(' 30 | ' + board[31] + ' | ' + board[32] + ' | ' + board[33] + ' | ' + board[34] + ' | ' + board[35] + ' | ' + board[36] + ' | ' + board[37] + ' | ' + board[38] + ' | ' + board[39] + ' | ' + board[40] + ' |')
    print('    |   |   |   |   |   |   |   |   |   |   |')
    print('    -----------------------------------------')
    print('    |   |   |   |   |   |   |   |   |   |   |')
    print(' 40 | ' + board[41] + ' | ' + board[42] + ' | ' + board[43] + ' | ' + board[44] + ' | ' + board[45] + ' | ' + board[46] + ' | ' + board[47] + ' | ' + board[48] + ' | ' + board[49] + ' | ' + board[50] + ' |')
    print('    |   |   |   |   |   |   |   |   |   |   |')
    print('    -----------------------------------------')
    print('    |   |   |   |   |   |   |   |   |   |   |')
    print(' 50 | ' + board[51] + ' | ' + board[52] + ' | ' + board[53] + ' | ' + board[54] + ' | ' + board[55] + ' | ' + board[56] + ' | ' + board[57] + ' | ' + board[58] + ' | ' + board[59] + ' | ' + board[60] + ' |')
    print('    |   |   |   |   |   |   |   |   |   |   |')
    print('    -----------------------------------------')
    print('    |   |   |   |   |   |   |   |   |   |   |')
    print(' 60 | ' + board[61] + ' | ' + board[62] + ' | ' + board[63] + ' | ' + board[64] + ' | ' + board[65] + ' | ' + board[66] + ' | ' + board[67] + ' | ' + board[68] + ' | ' + board[69] + ' | ' + board[70] + ' |')
    print('    |   |   |   |   |   |   |   |   |   |   |')
    print('    -----------------------------------------')
    print('    |   |   |   |   |   |   |   |   |   |   |')
    print(' 70 | ' + board[71] + ' | ' + board[72] + ' | ' + board[73] + ' | ' + board[74] + ' | ' + board[75] + ' | ' + board[76] + ' | ' + board[77] + ' | ' + board[78] + ' | ' + board[79] + ' | ' + board[80] + ' |')
    print('    |   |   |   |   |   |   |   |   |   |   |')
    print('    -----------------------------------------')
    print('    |   |   |   |   |   |   |   |   |   |   |')
    print(' 80 | ' + board[81] + ' | ' + board[82] + ' | ' + board[83] + ' | ' + board[84] + ' | ' + board[85] + ' | ' + board[86] + ' | ' + board[87] + ' | ' + board[88] + ' | ' + board[89] + ' | ' + board[90] + ' |')
    print('    |   |   |   |   |   |   |   |   |   |   |')
    print('    -----------------------------------------')
    print('    |   |   |   |   |   |   |   |   |   |   |')
    print(' 90 | ' + board[91] + ' | ' + board[92] + ' | ' + board[93] + ' | ' + board[94] + ' | ' + board[95] + ' | ' + board[96] + ' | ' + board[97] + ' | ' + board[98] + ' | ' + board[99] + ' | ' + board[100] + ' |')
    print('    |   |   |   |   |   |   |   |   |   |   |')
    print('    -----------------------------------------')

board = ["X", "O"] * 100
print(display_board(board))


>>>
      1   2   3   4   5   6   7   8   9   10 
    -----------------------------------------
    |   |   |   |   |   |   |   |   |   |   |
  0 | O | X | O | X | O | X | O | X | O | X |
    |   |   |   |   |   |   |   |   |   |   |
    -----------------------------------------
    |   |   |   |   |   |   |   |   |   |   |
 10 | O | X | O | X | O | X | O | X | O | X |
    |   |   |   |   |   |   |   |   |   |   |
    -----------------------------------------
    |   |   |   |   |   |   |   |   |   |   |
 20 | O | X | O | X | O | X | O | X | O | X |
    |   |   |   |   |   |   |   |   |   |   |
    -----------------------------------------
    |   |   |   |   |   |   |   |   |   |   |
 30 | O | X | O | X | O | X | O | X | O | X |
    |   |   |   |   |   |   |   |   |   |   |
    -----------------------------------------
    |   |   |   |   |   |   |   |   |   |   |
 40 | O | X | O | X | O | X | O | X | O | X |
    |   |   |   |   |   |   |   |   |   |   |
    -----------------------------------------
    |   |   |   |   |   |   |   |   |   |   |
 50 | O | X | O | X | O | X | O | X | O | X |
    |   |   |   |   |   |   |   |   |   |   |
    -----------------------------------------
    |   |   |   |   |   |   |   |   |   |   |
 60 | O | X | O | X | O | X | O | X | O | X |
    |   |   |   |   |   |   |   |   |   |   |
    -----------------------------------------
    |   |   |   |   |   |   |   |   |   |   |
 70 | O | X | O | X | O | X | O | X | O | X |
    |   |   |   |   |   |   |   |   |   |   |
    -----------------------------------------
    |   |   |   |   |   |   |   |   |   |   |
 80 | O | X | O | X | O | X | O | X | O | X |
    |   |   |   |   |   |   |   |   |   |   |
    -----------------------------------------
    |   |   |   |   |   |   |   |   |   |   |
 90 | O | X | O | X | O | X | O | X | O | X |
    |   |   |   |   |   |   |   |   |   |   |
    -----------------------------------------
>>> 

----------------------------------

#49.5.

#STEP 2 - Write a function that can take in a player input and assign their marker as "X" or "O".

def player_input():

    marker = " "
    while not (marker == "O" or marker == "X"):
        marker = input("Player 1 do you want to be X or O? \n ").upper()

    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")

print(player_input())

>>>
Player 1 do you want to be X or O? 
 O
('O', 'X')
>>>

----------------------------------

#49.6.

#STEP 2 - Write a function that can take in a player input and assign their marker as "X" or "O".

def player_input():

    marker = " "
    while not (marker == "O" or marker == "X"):
        marker = input("Player 1 do you want to be X or O? \n ").upper()

    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")

print(player_input())

>>>
Player 1 do you want to be X or O? 
 X
('X', 'O')
>>>

----------------------------------

#49.7.

#STEP 2 - Write a function that can take in a player input and assign their marker as "X" or "O".

def player_input():

    marker = " "
    while not (marker == "O" or marker == "X"):
        marker = input("Player 1 do you want to be X or O? \n ").upper()

    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")

print(player_input())

>>>
Player 1 do you want to be X or O? 
 1
Player 1 do you want to be X or O? 
 2
Player 1 do you want to be X or O? 
 o
('O', 'X')
>>>

----------------------------------

#49.8.

"""
STEP 3 - Write a function that takes, in the board list object, a marker ("X", "O"), and
a desired position (number 1-9) and assigns it to the board.
"""

def place_marker(board, marker, position):
    board[position] = marker
	
>>>
None
>>>

----------------------------------

#49.9.

"""
STEP 4 - Write a function that takes, in a board and a mark (X or O) and then checks to see if that mark
has won.
"""

def win_check(board, mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the left side
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
	
>>>
None
>>>

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

050. MILESTONE PROJECT 1 SOLUTION PT 2

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Milestone%20Project%201-%20Walkthrough%20Steps%20Workbook.ipynb

----------------------------------

#050.1.

#STEP 5 - Write a function that uses the random module to randomly decide which player goes first.

# ---> COINFLIP!!! <---

import random

def choose_first():
    if random.randint(0,1) == 0:
        return "Player 1"
    else:
        return "Player 2"

print (choose_first())

>>>
Player 1
>>> 

>>>
Player 2
>>> 

>>>
Player 2
>>> 

>>>
Player 2
>>> 

>>>
Player 1
>>> 

>>>
Player 2
>>> 

>>>
Player 1
>>> 

----------------------------------

#050.2.

#STEP 6 - Write a function that returns a boolean indicating whether a space on the board is freely available.

def space_check(board, position):
    return board[position] == " "
	
>>>
None
>>>

----------------------------------

#050.3.

#STEP 7 - Write a function that checks if the board is full and returns a boolean value. True if full.

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True
	
>>>
None
>>>

----------------------------------

#050.4.

"""
STEP 8 - Write a function that asks for a player next position (num 1-9) and then uses the function
from step 6 to check if its a free position.
"""

def player_choice(board):

    position = " "

    while position not in "1 2 3 4 5 6 7 8 9".split() or not space_check(board, int(position)):
        position = input("Choose your next position: (1-9) ")

    return int(position)
	
>>>
None
>>>

----------------------------------

#050.5.

"""
STEP 9 - Write a function that asks the player if they want to play again and returns a boolean True
if they do want to play again.
"""

def replay():

    return input("Do you want to play again? Enter Yes or No ").lower().startswith("y")
	
>>>
None
>>>

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

051. MILESTONE PROJECT 1 SOLUTION PT 3

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Milestone%20Project%201-%20Walkthrough%20Steps%20Workbook.ipynb

----------------------------------

#051.1.

#STEP 10 - Using while loops and the functions you've made to run the game!

print("Welcome to TicTacToe!")

    theBoard = [" "]*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + "Will go first!")

    game_on = True

    while game_on:

        if turn == "Player 1":
            #Player's 1 turn

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print("Congrat Player 1 has won the game!")
                game_on = False

            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("The game is a drew!")
                    break
                else:
                    turn = "Player 2"

        else:
            #Player's 2 turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print("Congrat Player 2 has won the game!")
                game_on = False

            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("The game is a drew!")
                    break
                else:
                    turn = "Player 1"

    if not replay():
        break
		
----------------------------------
				
--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

053. OOP - PT1 - OBJECTS

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Object%20Oriented%20Programming.ipynb

----------------------------------

#053.1.

l = [1, 2, 3]

print(l.count(2))

>>>
1
>>>

----------------------------------

#053.2.

>>> 1
1
>>> type(1)
<class 'int'>
>>>

>>> type([1, 2, 3])
<class 'list'>
>>>

>>> type((1, 2, 3))
<class 'tuple'>
>>>

>>> type({"k1" : 1})
<class 'dict'>
>>> 

----------------------------------

#053.3.

def square(num):
    return num ** 2

print(type(square))

>>>
<class 'function'>
>>> 

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

054. OOP - PT2 - CLASSES

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Object%20Oriented%20Programming.ipynb

----------------------------------

#054.1.

class Sample(object):
    pass

x = Sample()

print(x)
	
>>>
<__main__.Sample object at 0x02D77E50>
>>>

----------------------------------

#054.2.

class Dog(object):

    def __init__(self, breed):
        self.breed = breed

sam = Dog(breed="Lab")

print(sam)

>>>
<__main__.Dog object at 0x02D27E50>
>>>

----------------------------------

#054.3.

class Dog(object):

    def __init__(self, breed):
        self.breed = breed

sam = Dog(breed="Lab")

print(sam.breed)

>>>
Lab
>>>

----------------------------------

#054.4.

class Dog(object):

    #Class Object Attribute
    species = "mammal"

    def __init__(self, breed):
        self.breed = breed

sam = Dog(breed="Lab")

print(sam.species)

>>>
mammal
>>>

----------------------------------

#054.5.

class Dog(object):

    #Class Object Attribute
    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

sam = Dog(breed="Lab", name = "Sammy")

print(sam.name)

>>>
Sammy
>>>

----------------------------------

#054.6.

class Dog(object):

    #Class Object Attribute
    species = "mammal"

    def __init__(self, breed, name, fur=True):
        self.breed = breed
        self.name = name
        self.fur = fur

sam = Dog(breed="Lab", name = "Sammy")

print(sam.fur)

>>>
True
>>>

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

055. OOP - PT3 - METHODS

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Object%20Oriented%20Programming.ipynb

----------------------------------

#055.1.

class Circle(object):
    pass
	
>>>
None
>>>

----------------------------------

#055.2.

class Circle(object):

    #Class object attributes
    pi = 3.14

    def __init__(self):
        pass

c = Circle()

print(c)

>>>
<__main__.Circle object at 0x02D47E50>
>>>

----------------------------------

#055.3.

class Circle(object):

    #Class object attributes
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

c = Circle()

print(c.pi)
print(c.radius)

>>>
3.14
1
>>>

----------------------------------

#055.4.

class Circle(object):

    #Class object attributes
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

c = Circle(radius = 100)

print(c.pi)
print(c.radius)

>>>
3.14
100
>>>

----------------------------------

#055.5.

class Circle(object):

    #Class object attributes
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        #radius**2 * pi
        return (self.radius**2) * Circle.pi

c = Circle(radius = 100)

print(c.area)

>>>
<bound method Circle.area of <__main__.Circle object at 0x02D87E50>>
>>>

----------------------------------

#055.6.

class Circle(object):

    #Class object attributes
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        #radius**2 * pi
        return (self.radius**2) * Circle.pi

c = Circle(radius = 100)

print(c.area())

>>>
31400.0
>>>

----------------------------------

#055.7.

class Circle(object):

    #Class object attributes
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        #radius**2 * pi
        return (self.radius**2) * Circle.pi

    def set_radius(self, new_radius):
        #This methods takes in a radius and resets the current radius of the circle
        self.radius = new_radius
        

c = Circle(radius = 10)
c.set_radius(20)

print(c.radius)

>>>
20
>>>

----------------------------------

#055.8.

class Circle(object):

    #Class object attributes
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        #radius**2 * pi
        return (self.radius**2) * Circle.pi

    def set_radius(self, new_radius):
        #This methods takes in a radius and resets the current radius of the circle
        self.radius = new_radius

    def get_radius(self):
        return self.radius
        

c = Circle(radius = 10)

print(c.get_radius())

>>>
10
>>>

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

056. OOP - PT4 - INHERITANCE

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Object%20Oriented%20Programming.ipynb

----------------------------------

#056.1.

class Animal(object):

    def __init__(self):
        print("Animal created")

a = Animal()

print(a)

>>>
Animal created
>>>

----------------------------------

#056.2.

class Animal(object):

    def __init__(self):
        print("Animal created")

    def whoAmI (self):
        print("Animal")

    def eat(self):
        print("Eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("woof!")

d = Dog()

print(d)
print(d.whoAmI())
print(d.eat())
print(d.bark())

>>>
Animal created
Dog created
Dog
Eating
woof!
>>>

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

057. OOP - PT5 - SPECIAL METHODS

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Object%20Oriented%20Programming.ipynb

----------------------------------

#057.1.

class Book(object):

    def __init__(self, title, author, pages):

        print("A book has been created!")
        self.title = title
        self.author = author
        self.pages = pages

b = Book("Python","Jose",100)

print(b)

>>>
A book has been created!
>>>

----------------------------------

#057.2.

class Book(object):

    def __init__(self, title, author, pages):

        print("A book has been created!")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):

        return("Title: %s, Author: %s, pages: %s " % (self.title, self.author, self.pages))

b = Book("Python","Jose",100)

print(b)

>>>
A book has been created!
Title: Python, Author: Jose, pages: 100
>>>

----------------------------------

#057.3.

class Book(object):

    def __init__(self, title, author, pages):

        print("A book has been created!")
        self.title = title
        self.author = author
        self.pages = pages

    def __len__(self):

        return self.pages

b = Book("Python","Jose",100)

print(len(b))

>>>
A book has been created!
100
>>>

----------------------------------

#057.4.

class Book(object):

    def __init__(self, title, author, pages):

        print("A book has been created!")
        self.title = title
        self.author = author
        self.pages = pages

    def __del__(self):

        print("A book is gone!")

b = Book("Python","Jose",100)

del b

>>>
A book has been created!
A book is gone!
>>>

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

059. OOP - HOMEWORK SOLUTION

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Object%20Oriented%20Programming%20Homework%20-Solution.ipynb

----------------------------------

#059.1.

#Problem 1

"""
Fill in the Line class methods to accept coordinate as a pair of tuples
and return the slope and distance of the line.
"""

class Line(object):

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ( (x2-x1)**2 + (y2-y1)**2 )**0.5

    def slope(self):
        x1,x2 = self.coor1
        x2,y2 = self.coor2
        return float ((y2-y1))/(x2-x1)

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print(li.distance())
print(li.slope())

>>>
9.433981132056603
1.6
>>> 

----------------------------------

#059.2.

#Problem 2

#Fill in the class

class Cylinder(object):

    def __init__ (self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * (3.14)* (self.radius)**2

    def surface_area(self):
        top = (3.14)* (self.radius)**2
        return 2*top + 2*3.14*self.radius*self.height

c = Cylinder(2,3)

print(c.volume())
print(c.surface_area())

>>>
56.52
94.2
>>> 

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

061 EXCEPTIONS HANDLING: TRY, EXCEPT, FINALLY

http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Errors%20and%20Exceptions%20Handling.ipynb

----------------------------------

#061.1.

try:
    2 + 's'
except:
    print("There was a type of error")
finally:
    print("Finally this was printed")
	
>>>
There was a type of error
Finally this was printed
>>>

----------------------------------

#061.2.

try:
    f = open("test", "w")
    f.write("test write this")
except:
    print("error in writing to the file")
else:
    print("file write was a success")
	
>>>
file write was a success
>>>

----------------------------------

#061.3.

try:
    f = open("test", "r")
    f.write("test write this")
except:
    print("error in writing to the file")
else:
    print("file write was a success")
	
>>>
error in writing to the file
>>>

----------------------------------

#061.4.

try:
    f = open("test", "r")
    f.write("test write this")
finally:
    print("Always execute")
	
>>>
Always execute

Traceback (most recent call last):
  File "C:/Program Files (x86)/Python/test.py", line 3, in <module>
    f.write("test write this")
io.UnsupportedOperation: not writable
>>>

----------------------------------

#061.5.

try:
    f = open("test", "r")
    f.write("test write this")
except:
    print("there was an error")
finally:
    print("Always execute")

>>>
there was an error
Always execute
>>>

----------------------------------

#061.6.

def askint():
    try:
        val = int(input("Please enter an int: "))
    except:
        print("Looks like you didn't enter an int!")
    finally:
        print("Finally block executed!")
    print(val)

print(askint())

>>>
Please enter an int: 3
Finally block executed!
3
>>>

----------------------------------

#061.7.

def askint():
    try:
        val = int(input("Please enter an int: "))
    except:
        print("Looks like you didn't enter an int!")
    finally:
        print("Finally block executed!")
    print(val)

print(askint())

>>>
Please enter an int: five
Looks like you didn't enter an int!
Finally block executed!

Traceback (most recent call last):
  File "C:/Program Files (x86)/Python/test.py", line 10, in <module>
    print(askint())
  File "C:/Program Files (x86)/Python/test.py", line 8, in askint
    print(val)
UnboundLocalError: local variable 'val' referenced before assignment
>>>

----------------------------------

#061.8.

def askint():
    
    try:
        val = int(input("Please enter an int: "))
        
    except:
        print("Looks like you didn't enter an int!")
        val = int(input("Try again: "))
        
    finally:
        print("Finally block executed!")
        
    print(val)

print(askint())

>>>
Please enter an int: five
Looks like you didn't enter an int!
Try again: 5
Finally block executed!
5
>>>

----------------------------------

#061.9.

def askint():

    while True:
    
        try:
            val = int(input("Please enter an int: "))
        
        except:
            print("Looks like you didn't enter an int!")
            continue
        
        else:
            print("Correct, that is an integer!")
            break

        finally:
            print("Finally block executed!")

        print(val)

print(askint())

>>>
Please enter an int: abc
Looks like you didn't enter an int!
Finally block executed!
Please enter an int: ab
Looks like you didn't enter an int!
Finally block executed!
Please enter an int: b
Looks like you didn't enter an int!
Finally block executed!
Please enter an int: r
Looks like you didn't enter an int!
Finally block executed!
Please enter an int: 5
Correct, that is an integer!
Finally block executed!
>>>

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

----------------------------------

----------------------------------

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

----------------------------------

----------------------------------

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

----------------------------------

----------------------------------

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

----------------------------------

----------------------------------

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

----------------------------------

----------------------------------

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

----------------------------------

----------------------------------

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

----------------------------------

----------------------------------

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

----------------------------------

----------------------------------

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

----------------------------------

----------------------------------

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

----------------------------------

----------------------------------

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

----------------------------------

----------------------------------

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

----------------------------------

----------------------------------

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

----------------------------------

----------------------------------

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

----------------------------------

----------------------------------

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------

----------------------------------

----------------------------------

----------------------------------

--------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

--------------------------------------------------------------------------
