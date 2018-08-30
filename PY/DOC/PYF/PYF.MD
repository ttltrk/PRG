
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD)

---

<h3 id='^'>Python Flash</h3>

---

* <a href='#operators'>operators</a>
* <a href='#comments'>comments</a>
* <a href='#numbers'>numbers</a>
* <a href='#strings'>strings</a>
* <a href='#variables'>variables</a>
* <a href='#lists'>lists</a>
* <a href='#tuples'>tuples</a>
* <a href='#set'>set</a>
* <a href='#dictionary'>dictionary</a>
* <a href='#if..else'>if..else</a>
* <a href='#for'>for</a>
* <a href='#while'>while</a>
* <a href='#functions'>functions</a>
* <a href='#lambda'>lambda</a>
* <a href='#list_comprehensions'>list comprehensions</a>
* <a href='#oop'>oop</a>

---

<h3 id='operators'>Python Operators</h3>

```python
a == b  (Equals)
a != b  (Not Equals)
a < b   (Less than)
a <= b  (Less than or equal to)
a > b   (Greater than)
a >= b  (Greater than or equal to)
```

<a href='#^'>^^^</a>

Arithmetic operator

```python
x = 15
y = 4

print('x + y =',x+y)

print('x - y =',x-y)

print('x * y =',x*y)

print('x / y =',x/y)

print('x // y =',x//y)

print('x ** y =',x**y)

>>>
x + y = 19
x - y = 11
x * y = 60
x / y = 3.75
x // y = 3
x ** y = 50625
>>>
```

<a href='#^'>^^^</a>

Comparison operators

```python
>>> 2 == 2
True

>>> 1 == 1
True

>>> 1 == 0
False
>>> 

>>> 2 != 1
True

>>> 2 != 2
False
>>> 

>>> 2 > 1
True

>>> 2 > 4
False
>>> 

>>> 2 < 4
True

>>> 2 < 1
False
>>> 

>>> 2 >= 2
True

>>> 2 >= 1
True
>>> 

>>> 2 <= 10
True
>>> 

>>> 1 < 2
True

>>> 2 < 3
True

>>> 1 < 2 < 3
True
>>> 

>>> 1 < 2 and 2 < 3
True

>>> 1 < 2 and 2 < 1
False
>>>

>>> 1 < 2 or 2 < 3
True

>>> 1 < 2 or 2 < 1
True
>>> 
```

<a href='#^'>^^^</a>

---

<h3 id='comments'>comments</h3>

One line comment

```python
#This is a comment
#print out Hello
print('Hello')

>>>
Hello
>>>
```

<a href='#^'>^^^</a>

Multi line comment

```python
"""This is also a
perfect example of
multi-line comments"""
print('hello')

>>>
hello
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='numbers'>Python numbers</h3>

```python
x = 1
y = 2.8  
z = 1j   

print(type(x))
print(type(y))
print(type(z))

>>>
<class 'int'>
<class 'float'>
<class 'complex'>
>>>
```

```python
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

>>>
<class 'int'>
<class 'int'>
<class 'int'>
>>>
```

```python
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

>>>
<class 'float'>
<class 'float'>
<class 'float'>
>>>
```

```python
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

>>>
<class 'float'>
<class 'float'>
<class 'float'>
>>>
```

```python
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

>>>
<class 'complex'>
<class 'complex'>
<class 'complex'>
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='strings'>Python strings</h3>

```python
a = "Hello, World!"

print(a[1])
print(a[2:5])

>>>
e
llo
>>>
```

```python
a = " Hello, World! "

print(a.strip())
print(a)

>>>
Hello, World!
 Hello, World! 
>>>
```

```python
a = "Hello, World!"

print(len(a))
print(a.lower())
print(a.upper())
print(a.replace("H", "J"))
print(a.split(","))

>>>
13
hello, world!
HELLO, WORLD!
Jello, World!
['Hello', ' World!']
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='variables'>Python variables</h3>

```python
a = 5
b = 4.0
c = "John"
d = True

print(a, b, c, d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))

>>>
5 4.0 John True
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
>>>
```

```python
a = 5
b = 4.0
c = "John"
d = True

print("a 'a' erteke = " + str(a))
print("a 'b' erteke = " + str(b))
print("a 'c' erteke = " + c)
print("a 'd' erteke = " + str(d))

>>>
a 'a' erteke = 5
a 'b' erteke = 4.0
a 'c' erteke = John
a 'd' erteke = True
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='lists'>Python lists</h3>

```python
lst = ["apple", "banana", "cherry"]

print(lst)

lst[1] = "blackcurrant"

print(lst)

>>>
['apple', 'banana', 'cherry']
['apple', 'blackcurrant', 'cherry']
>>>
```

```python
lst = ["apple", "banana", "cherry"]
lst.append("damson")

print(lst)
print(lst * 2)

>>>
['apple', 'banana', 'cherry', 'damson']
['apple', 'banana', 'cherry', 'damson', 'apple', 'banana', 'cherry', 'damson']
>>>
```

```python
lst = ["apple", "banana", "cherry"]

print(lst)

lst.remove("banana")

print(lst)
print(len(lst))

>>>
['apple', 'banana', 'cherry']
['apple', 'cherry']
2
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='tuples'>Python tuples</h3>

```python
tup = ("apple", "banana", "cherry")

print(tup)

>>>
('apple', 'banana', 'cherry')
>>>
```

```python
tup = ("apple", "banana", "cherry")

print(tup[1])

>>>
banana
>>>
```

```python
tup = ("apple", "banana", "cherry")

tup[1] = "blackcurrant"

>>>
Traceback (most recent call last):
  File "/Users/attilatorok/Desktop/tst.py", line 3, in <module>
    tup[1] = "blackcurrant"
TypeError: 'tuple' object does not support item assignment
>>>
```

```python
tup = ("apple", "banana", "cherry")

print(len(tup))

>>>
3
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='sets'>Python sets</h3>

```python
sts = {"apple", "banana", "cherry"}

print(sts)

sts.add("damson")

print(sts)

sts.remove("banana")

print(sts)

print(len(sts))

>>>
{'apple', 'banana', 'cherry'}
{'damson', 'apple', 'banana', 'cherry'}
{'damson', 'apple', 'cherry'}
3
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='if..else'>Python if..else</h3>

```python
num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")

>>>
3 is a positive number.
This is always printed.
This is also always printed.
>>>
```

<a href='#^'>^^^</a>

```python
num = 3

if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")

>>>
Positive or Zero
>>>
```

<a href='#^'>^^^</a>

```python
num = 3.4

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
    
>>>
Positive number
>>>
```

<a href='#^'>^^^</a>

```python
num = float(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
    
>>>
Enter a number:  10
Positive number
>>>

>>>
Enter a number:  0
Zero
>>>

>>>
Enter a number:  -2
Negative number
>>>
```

<a href='#^'>^^^</a>

```python
a = 33
b = 200

if b > a:
    print("b is greater than a")

>>>
b is greater than a
>>>
```

```python
a = 33
b = 33

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
>>>
a and b are equal
>>>
```

```python
a = 200
b = 33

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
>>>
a is greater than b
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='for'>Python for</h3>

```python
for element in range(5):
    print ("hello world")

>>>
hello world
hello world
hello world
hello world
hello world
>>>
```

```python
l = [1, 2, 3, 4, 5]

for element in l:
    print ("hello world")

>>>
hello world
hello world
hello world
hello world
hello world
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='while'>Python while</h3>

```python
a = "hi world"

i = 1
while i < 6:
  print(a)
  i += 1
  
>>>
hi world
hi world
hi world
hi world
hi world
>>>
```

```python
i = 1
while i < 6:
  print(i)
  i += 1
  
>>>
1
2
3
4
5
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='functions'>Python functions</h3>

```python
#variables
a = "hello world"
b = "xyz"
c = 5
d = 7

#functions
def pr(par1):
  print(par1)
  
def ps(par1, par2):
  return (par1+par2)

def ms(par1,par2):
  return (par1-par2)

#STDOUT
pr(a)
pr(b)
print(ps(c,d))
print(ms(c,d))

>>>
hello world
xyz
12
-2
>>>
```

```python
bigger = 0

def func(num1, num2):
  if num1 > num2:
    bigger = num1
  else:
    bigger = num2
  return bigger

print(func(4, 6))

>>>
6
>>>
```

```python
#variables
a = 5
b = 10
bigger = 0

#function
def func(num1, num2):
  if num1 > num2:
    bigger = num1
  else:
    bigger = num2
  return bigger

#print
print(func(a, b))

>>>
10
>>>
```

```python
#variables
a = 5
b = 10
bigger = 0

#function
def func(num1, num2):
  if num1 > num2:
    bigger = num1
  else:
    bigger = num2
  return bigger

#print
print(func(a, 4))
print(func(a, b))

>>>
5
10
>>>
```

```python
a = 20
b = 4
c = True
d = False

def no(p1,p2,p3):
  if (p3 == True):
    print(p3, p1+p2)
  else:
    print(p3, p1-p2)
  
no(a,b,c)
no(a,b,d)

>>>
(True, 24)
(False, 16)
>>>
```

```python
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
>>>
1
2
3
>>>
```

```python
i = 1
while i < 6:
  print(i)
  if i == 3:
    print("itt volt a harmadik step")
  if i == 5:
    print("itt meg az otodik")
  i += 1
  
>>>
1
2
3
itt volt a harmadik step
4
5
itt meg az otodik
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='lambda'>Python lambda</h3>

```python
#function
def lam(a):
    a = a+10
    return a
    
#lambda
x = lambda b : b + 10

print("a funkcio eredmenye = " + str(lam(9)))
print("a lambda eredmenye = " + str(x(9)))

>>>
a funkcio eredmenye = 19
a lambda eredmenye = 19
>>>
```

```python
x = lambda a, b : a * b
y = lambda a, b, c : a + b + c

print(x(5, 6))
print(y(5, 6, 2))

>>>
30
13
>>>
```

```python
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(3)

print(mydoubler(10))

>>>
30
>>>
```

```python
def myfunc(n):
  return lambda a, b : (a + b) * n

mydoubler = myfunc(3)

print(mydoubler(10, 2))

>>>
36
>>>
```

```python
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))

>>>
22
33
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='list_comprehensions'>Python list comprehensions</h3>

```python
l = []

for letter in "word":
    l.append(letter)

print (l)

>>>
['w', 'o', 'r', 'd']
>>> 
```

```python
l = [letter for letter in "word"]
print(l)

>>>
['w', 'o', 'r', 'd']
>>> 
```

HUMAN

```python
h_letters = []

for letter in 'human':
    h_letters.append(letter)

print(h_letters)

>>>
['h', 'u', 'm', 'a', 'n']
>>>
```

```python
h_letters = [ letter for letter in 'human' ]
print( h_letters)

>>>
['h', 'u', 'm', 'a', 'n']
>>>
```

```python
lst = []

for x in range(0,11):
  lst.append(x**2)
  
print(lst)

>>>
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>>
```

```python
lst = [x**2 for x in range(0,11)]
print(lst)

>>>
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>>
```

```python
>>> lst = [number for number in range(11) if number % 2 ==0]
>>> lst
[0, 2, 4, 6, 8, 10]
>>> 
```

```python
lst = []

for number in range(11):
    if number %2 == 0:
        lst.append(number)

print (lst)

>>>
[0, 2, 4, 6, 8, 10]
>>> 
```

```python
celsius = [0, 10, 20.1, 34.5]

fahrenheit = [temp for temp in celsius]
    
print (fahrenheit)

>>>
[0, 10, 20.1, 34.5]
>>> 
```

```python
celsius = [0, 10, 20.1, 34.5]

fahrenheit = [(temp * (9/5.0) + 32) for temp in celsius]
    
print (fahrenheit)

>>>
[32.0, 50.0, 68.18, 94.1]
>>> 
```

```python
lst = [x**2 for x in [x**2 for x in range(11)]]

print (lst)

>>>
[0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000]
>>> 
```

<a href='#^'>^^^</a>

---

<h3 id='oop'>Python OOP</h3>

```python
class Complex:
    def __init__(self, alma, korte, szilva):
        self.a = alma
        self.k = korte
        self.sz = szilva

x = Complex(5, 10, 15)

def masik():
    res = x.a + x.k + x.sz
    print('res =', res)
    print('a1 =', x.a)
    print('b1 =', x.k)
    print('c1 =', x.sz)

masik()

>>>
res = 30
a1 = 5
b1 = 10
c1 = 15
>>>
```

```python
class Door:
    def __init__(self, number, status):
        self.number = number
        self.status = status

    def open(self):
        self.status = 'open'

    def close(self):
        self.status = 'closed'

door1 = Door(1, 'closed')
door2 = Door(2, 'open')

print("door1 = Door(1, 'closed') =", door1.number)
print("door2 = Door(2, 'open') =", door2.number)
print("door1 = Door(1, 'closed') =", door1.status)
print("door2 = Door(2, 'open') =", door2.status)

>>>
door1 = Door(1, 'closed') = 1
door2 = Door(2, 'open') = 2
door1 = Door(1, 'closed') = closed
door2 = Door(2, 'open') = open
>>>
```

```python
class Door:

    colour ='brown'

    def __init__(self, number, status):
        self.number = number
        self.status = status

    def open(self):
        self.status = 'open'

    def close(self):
        self.status = 'closed'

door1 = Door(1, 'closed')
door2 = Door(2, 'closed')

print(Door.colour)
print(door1.colour)
print(door2.colour)

Door.colour = 'white'

print(Door.colour)
print(door1.colour)
print(door2.colour)

>>>
brown
brown
brown
white
white
white
>>>
```

```python
class Door:
    colour = 'brown'

    def __init__(self, number, status):
        self.number = number
        self.status = status

    @classmethod
    def knock(cls):
        print("Knock!")

    @classmethod
    def paint(cls, colour):
        cls.colour = colour

    def open(self):
        self.status = 'open'

    def close(self):
        self.status = 'closed'

d = Door
d1 = Door(1, 'open')
d2 = Door(2, 'close')

print(d.colour)
print(d1.colour)
print(d2.colour)

d.paint('white')

print(d.colour)
print(d1.colour)
print(d2.colour)

d1.paint('yellow')

print(d.colour)
print(d1.colour)
print(d2.colour)

>>>
brown
brown
brown
white
white
white
yellow
yellow
yellow
>>>
```

<a href='#^'>^^^</a>

---


