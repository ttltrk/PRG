
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python</h3>

---

* <a href='#dattyp'>data types</a>
* <a href='#operators'>operators</a>
* <a href='#comments'>comments</a>
* <a href='#numbers'>numbers</a>
* <a href='#strings'>strings</a>
* <a href='#stringmeth'>string methods</a>
* <a href='#variables'>variables</a>
* <a href='#printform'>print formatting</a>
* <a href='#files'>files</a>

---

* <a href='#lists'>lists</a>
* <a href='#list_methods'>list methods</a>
* <a href='#tuples'>tuples</a>
* <a href='#tupmeth'>tuple methods</a>
* <a href='#sets'>sets</a>
* <a href='#dictionary'>dictionary</a>

---

* <a href='#if..else'>if..else</a>
* <a href='#for'>for</a>
* <a href='#while'>while</a>
* <a href='#functions'>functions</a>
* <a href='#lambda'>lambda</a>
* <a href='#list_comprehensions'>list comprehensions</a>

---

* <a href='#oop'>oop</a>

---

<h3 id='dattyp'>Python Data types</h3> 

---

```python
#python data types
int	= 3, 300, 201
float	= 2.3, 4.5, 100.0
str	= 'hello', "Sammy", '2000'
list	= [10, 'hello', 200.3]
dict	= {'key':'value', 'name':'Frankie'}
tup	= (10, 'hello', 200.3)
set	= {'a','b'}
bool	= True, False
```

<a href='#^'>^^^</a>

---

<h3 id='operators'>Python Operators</h3> 

---

```python
#python operators
a == b  (Equals)
a != b  (Not Equals)
a < b   (Less than)
a <= b  (Less than or equal to)
a > b   (Greater than)
a >= b  (Greater than or equal to)
```

<a href='#^'>^^^</a>

---

```python

#python operators
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

---

```python
#python operators
>>> '2' == 2 
False

>>> 'bye' == 'BYE'
False

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
```

<a href='#^'>^^^</a>

---

Logical operators

---

```python
#python operators

and
or
not

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

>>> not 1 == 1 
False

>>> not 1 == 2
True
```

<a href='#^'>^^^</a>

---

<h3 id='comments'>Python comments</h3>

---

```python
#python comments
#This is a comment
#print out Hello
print('Hello')

>>>
Hello
>>>
```

<a href='#^'>^^^</a>

---

```python
#python comments
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

---

```python
#python numbers
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

<a href='#^'>^^^</a>

---

```python
#python numbers
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

<a href='#^'>^^^</a>

---

```python
#python numbers
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

<a href='#^'>^^^</a>

---

```python
#python numbers
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

<a href='#^'>^^^</a>

---

```python
#python numbers
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

```python
#python numbers
a = 5

print(type(a))
print(type(5.0))

c = 5 + 3j

print(c + 3)
print(isinstance(c, complex))

>>>
<class 'int'>
<class 'float'>
(8+3j)
True
>>>
```

<a href='#^'>^^^</a>

---

```python
#python numbers
a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))

>>>
5 is of type <class 'int'>
2.0 is of type <class 'float'>
(1+2j) is complex number? True
>>>
```

<a href='#^'>^^^</a>

---

```python
#python numbers
n1 = 1 + 2.0

print(n1)
print(int(2.3))
print(int(-2.8))
print(float(5))
print(complex('3+5j'))

>>>
3.0
2
-2
5.0
(3+5j)
>>>
```

<a href='#^'>^^^</a>

---

```python
#python numbers
n1 = 1.1 + 2.2
print(n1 == 3.3)
print(n1)

>>>
False
3.3000000000000003
>>>
```

<a href='#^'>^^^</a>

---

```python
#python numbers
import decimal

print(0.1)
print(decimal.Decimal(0.1))

>>>
0.1
0.1000000000000000055511151231257827021181583404541015625
>>>
```

<a href='#^'>^^^</a>

---

```python
#python numbers
import math

print(math.pi)
print(math.cos(math.pi))
print(math.exp(10))
print(math.log10(1000))
print(math.sinh(1))
print(math.factorial(6))

>>>
3.141592653589793
-1.0
22026.465794806718
3.0
1.1752011936438014
720
>>>
```

<a href='#^'>^^^</a>

---

```python
#python numbers
import random

print(random.randrange(10,20))

x = ['a', 'b', 'c', 'd', 'e']

print(random.choice(x))

random.shuffle(x)

print(x)
print(random.random())

>>>
14
e
['b', 'd', 'a', 'e', 'c']
0.14933393166286335
>>>
```

<a href='#^'>^^^</a>

---

```python
#python numbers
import fractions

print(fractions.Fraction(1.5))
print(fractions.Fraction(5))
print(fractions.Fraction(1,3))

>>>
3/2
5
1/3
>>>
```

<a href='#^'>^^^</a>

---

```python
#python numbers
import fractions

print(fractions.Fraction(1.1))
print(fractions.Fraction('1.1'))

>>>
2476979795053773/2251799813685248
11/10
>>>
```

<a href='#^'>^^^</a>

---

```python
#python numbers
from fractions import Fraction as F

print(F(1,3) + F(1,3))
print(1 / F(5,6))
print(F(-3,10) > 0)
print(F(-3,10) < 0)

>>>
2/3
6/5
False
True
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

<a href='#^'>^^^</a>

```python
ms1 = 'Hello'
print(ms1)

ms2 = "Hello"
print(ms2)

ms3 = '''Hello'''
print(ms3)

ms4 = """Hello, welcome to
           the world of Python"""
print(ms4)

>>>
Hello
Hello
Hello
Hello, welcome to
           the world of Python
>>>
```

<a href='#^'>^^^</a>

```python
| P | y | t | h | o | n |
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

<a href='#^'>^^^</a>

```python
str = 'programiz'
print('str = ', str)

print('str[0] = ', str[0])

print('str[-1] = ', str[-1])

print('str[1:5] = ', str[1:5])

print('str[5:-2] = ', str[5:-2])

>>>
str =  programiz
str[0] =  p
str[-1] =  z
str[1:5] =  rogr
str[5:-2] =  am
>>>
```

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

```python
str1 = 'Hello'
str2 ='World!'

print('str1 + str2 = ', str1 + str2)

print('str1 * 3 =', str1 * 3)

>>>
str1 + str2 =  HelloWorld!
str1 * 3 = HelloHelloHello
>>>
```

<a href='#^'>^^^</a>

```python
count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')

>>>
3 letters found
>>>
```

<a href='#^'>^^^</a>

```python
str = 'cold'

list_enumerate = list(enumerate(str))

print('list(enumerate(str) = ', list_enumerate)
print('len(str) = ', len(str))

>>>
list(enumerate(str) =  [(0, 'c'), (1, 'o'), (2, 'l'), (3, 'd')]
len(str) =  4
>>>
```

<a href='#^'>^^^</a>

```python
print('''He said, "What's there?"''')
print('He said, "What\'s there?"')
print("He said, \"What's there?\"")

>>>
He said, "What's there?"
He said, "What's there?"
He said, "What's there?"
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='stringmeth'>Python String methods</h3>

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

<a href='#^'>^^^</a>

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

```python
a = 'hi this is a string'
b = a.split()
c = a.split('i')

print(b)
print(c)

>>>
['hi', 'this', 'is', 'a', 'string']
['h', ' th', 's ', 's a str', 'ng']
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

<h3 id='printform'>Python Print formatting</h3>

```python
'String here {} then here {}'.format('something1', 'something2')
```

<a href='#^'>^^^</a>

```python
print('this is a string {}'.format('INSERTED'))

>>>
this is a string INSERTED
>>>
```

<a href='#^'>^^^</a>

```python
print('the {} {} {}'.format('fox', 'brown', 'quick'))
print('the {2} {0} {1}'.format('fox', 'brown', 'quick'))
print('the {b} {q} {f}'.format(f='fox', b='brown', q='quick'))

>>>
the fox brown quick
the quick fox brown
the brown quick fox
>>>
```

<a href='#^'>^^^</a>

```python
def choose():
    a1, b1, c1 = 0, 0, 0
    inp = input('a, b, or c? \n')
    if inp == 'a':
        a1 = 1
    elif inp == 'b':
        b1 = 1
    elif inp == 'c':
        c1 = 1
    else:
        return err()
    print('the result is {aa} {bb} {cc}'.format(aa = a1, bb = b1, cc = c1))

def err():
    print('no or wrong pwd')
    
choose()

>>>
a, b, or c? 

a
the result is 1 0 0

b
the result is 0 1 0

c
the result is 0 0 1

xxx
no or wrong pwd
>>>
```

<a href='#^'>^^^</a>

```python
n = 'trk'
a = '35'

print('hi my name is {}'.format(n))
print(f'hi my name is {n} and Im {a}')

>>>
hi my name is trk
hi my name is trk and Im 35
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='files'>Python files</h3>

```python
mf = open('C:\\path\\path\\path\\test.txt')

>>>
Process finished with exit code 0
>>>
```

<a href='#^'>^^^</a>

```python
mf = open('C:\\path\\path\\path\\test.txt')
print(mf.read())

>>>
hello world
new line
third line and hello 
>>>
```

<a href='#^'>^^^</a>

```python
mf = open('C:\\path\\path\\path\\test.txt')
print(mf.read())
#you can't use read() twice, use the seek as it is described below 
mf.seek(0)
print(mf.read())

>>>
hello world
new line
third line and hello 
hello world
new line
third line and hello 
>>>
```

<a href='#^'>^^^</a>

```python
mf = open('C:\\path\\path\\path\\test.txt')

print(mf.readlines())

>>>
['hello world\n', 'new line\n', 'third line and hello ']
>>>
```

<a href='#^'>^^^</a>

```python
with open('C:\\Users\\AttilaTorok\\Desktop\\ADM\\PY\\APPS\\TEST\\test.txt') as myfile:
    contents = myfile.read()

print(contents)

>>>
hello world
new line
third line and hello
>>>
```

<a href='#^'>^^^</a>

```python
with open('C:\\Users\\AttilaTorok\\Desktop\\ADM\\PY\\APPS\\TEST\\test.txt', mode='a') as myfile:
    contents = myfile.write('hey hey hey')

with open('C:\\Users\\AttilaTorok\\Desktop\\ADM\\PY\\APPS\\TEST\\test.txt', mode='r') as myfile:
    contents = myfile.read()

print(contents)
>>>
hey hey hey
>>>
```

<a href='#^'>^^^</a>

```python
with open('C:\\Users\\AttilaTorok\\Desktop\\ADM\\PY\\APPS\\TEST\\zzz.txt', mode='w') as zzz:
    zx = zzz.write('eyyo')

with open('C:\\Users\\AttilaTorok\\Desktop\\ADM\\PY\\APPS\\TEST\\zzz.txt', mode='r') as zzz:
    zx = zzz.read()

print(zx)

>>>
eyyo
>>>
```

<a href='#^'>^^^</a>

```python

>>>

>>>
```

<a href='#^'>^^^</a>

---

<h3 id='lists'>Python lists</h3>

```python
a = [1,2,3]
print(a)

a[2]=4
print(a)

>>>
[1, 2, 3]
[1, 2, 4]
>>>
```

<a href='#^'>^^^</a>

```python
# empty list
my_list = []
print(my_list)

# list of integers
my_list = [1, 2, 3]
print(my_list)

# list with mixed datatypes
my_list = [1, "Hello", 3.4]
print(my_list)

>>>
[]
[1, 2, 3]
[1, 'Hello', 3.4]
>>>
```

<a href='#^'>^^^</a>

```python
# nested list
my_list = ["mouse", [8, 4, 6], ['a']]

print(my_list)

>>>
['mouse', [8, 4, 6], ['a']]
>>>
```

<a href='#^'>^^^</a>

```python
my_list = ['p','r','o','b','e']

print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])

>>>
p
r
o
b
e
>>>
```

<a href='#^'>^^^</a>

```python
n_list = ["Happy", [2,0,1,5]]

print(n_list[0][1])    
print(n_list[1][3])

>>>
a
5
>>>
```

<a href='#^'>^^^</a>

```python
my_list = ['p','r','o','b','e']

print(my_list[-1])
print(my_list[-5])

>>>
e
p
>>>
```

<a href='#^'>^^^</a>

```python
my_list = [1, 2, 3, 4, 5, 6, 7]

print(my_list[2:5])
print(my_list[:-5])
print(my_list[5:])
print(my_list[:])

>>>
[3, 4, 5]
[1, 2]
[6, 7]
[1, 2, 3, 4, 5, 6, 7]
>>>
```

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

```python
print(range(10))
print(list(range(10)))
print(list(range(2, 8)))
print(list(range(2, 20, 3)))

>>>
range(0, 10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[2, 3, 4, 5, 6, 7]
[2, 5, 8, 11, 14, 17]
>>>
```

```python
>>> x = range(1,5)
>>> type (x)
<class 'range'>
>>> 
```

```python
>>> list(range(0, 10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
```

```python
>>> list(range(20))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> 
```

```python
>>> x = list(range(0,10))
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> type(x)
<class 'list'>
>>> 
```

```python
>>> start = 5
>>> stop = 20
>>> list(range(start,stop))
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> 
```

```python
>>> start = 5
>>> stop = 20
>>> list(range(start,stop,2))
[5, 7, 9, 11, 13, 15, 17, 19]
>>>
```

---

<h3 id='list_methods'>Python List Methods</h3>

append

```python
l = [1, 2, 3, 4, 5, 6]
print(l)
l.append(7)
print(l)

>>>
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6, 7]
>>>
```

<a href='#^'>^^^</a>

copy

```python
l = [1, 2, 3, 4, 5, 6]
print(l)
l2 = l.copy()
l2.append(7)
print(l2)

>>>
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6, 7]
>>>
```

<a href='#^'>^^^</a>

count

```python
l = [1, 2, 3, 3, 4, 5, 6]
print(l)
print(l.count(1))
print(l.count(2))
print(l.count(3))

>>>
[1, 2, 3, 3, 4, 5, 6]
1
1
2
>>>
```

<a href='#^'>^^^</a>

clear

```python
l = [1, 2, 3, 4, 5, 6]
print(l)
l.clear()
print(l)

>>>
[1, 2, 3, 4, 5, 6]
[]
>>>
```

<a href='#^'>^^^</a>

extend

```python
l1 = [1, 2, 3, 4, 5, 6]
l2 = [11, 22, 33, 44, 55, 66]
print(l1)
print(l2)
l1.extend(l2)
print(l1)

>>>
[1, 2, 3, 4, 5, 6]
[11, 22, 33, 44, 55, 66]
[1, 2, 3, 4, 5, 6, 11, 22, 33, 44, 55, 66]
>>>
```

<a href='#^'>^^^</a>

index

```python
l = [1, 2, 3, 4, 5, 6]
print(l)
print(l.index(1))
print(l.index(2))
print(l.index(3))

>>>
[1, 2, 3, 4, 5, 6]
0
1
2
>>>
```

<a href='#^'>^^^</a>

insert

```python
l = [1, 2, 3, 4, 5, 6]
print(l)
l.insert(3, "X")
print(l)

>>>
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 'X', 4, 5, 6]
>>>
```

<a href='#^'>^^^</a>

pop

```python
l = [1, 2, 3, 4, 5, 6]
print(l)
l.pop(3)
print(l)

>>>
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 5, 6]
>>>
```

<a href='#^'>^^^</a>

remove

```python
l = [1, 2, 3, 3, 3, 3, 4, 5, 6]
print(l)
l.remove(3)
print(l)
l.remove(4)
print(l)

>>>
[1, 2, 3, 3, 3, 3, 4, 5, 6]
[1, 2, 3, 3, 3, 4, 5, 6]
[1, 2, 3, 3, 3, 5, 6]
>>>
```

<a href='#^'>^^^</a>

reverse

```python
l = [1, 2, 3, 4, 5, 6]
print(l)
l.reverse()
print(l)

>>>
[1, 2, 3, 4, 5, 6]
[6, 5, 4, 3, 2, 1]
>>>
```

<a href='#^'>^^^</a>

sort

```python
l1 = [1, 3, 6, 5, 2, 4]
l2 = ["c", "b", "g", "e", "f", "a", "d"]
print(l1)
print(l2)
l1.sort()
l2.sort()
print(l1)
print(l2)

>>>
[1, 3, 6, 5, 2, 4]
['c', 'b', 'g', 'e', 'f', 'a', 'd']
[1, 2, 3, 4, 5, 6]
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='tuples'>Python tuples</h3>

Tuples are immutable, cannot be changed.

```python
t = (1,2,3)
l = [1,2,3]

print(type(t))
print(type(l))

>>>
<class 'tuple'>
<class 'list'>
>>>
```

<a href='#^'>^^^</a>

```python
t = ()
print(t)

t = (1, 2, 3)
print(t)

t = (1, "Hello", 3.4)
print(t)

t = ("mouse", [8, 4, 6], (1, 2, 3))
print(t)

t = 3, 4.6, "dog"
print(t)

a, b, c = t
print(a)
print(b)
print(c)

>>>
()
(1, 2, 3)
(1, 'Hello', 3.4)
('mouse', [8, 4, 6], (1, 2, 3))
(3, 4.6, 'dog')
3
4.6
dog
>>>
```

<a href='#^'>^^^</a>

```python
t1 = ("hello")
print(type(t1))

t2 = ("hello",)  
print(type(t2))

t3 = "hello",
print(type(t3))

>>>
<class 'str'>
<class 'tuple'>
<class 'tuple'>
>>>
```

<a href='#^'>^^^</a>

```python
t = ('p','e','r','m','i','t')

print(t[0])
print(t[5])

n_t = ("mouse", [8, 4, 6], (1, 2, 3))

print(n_t[0][3])
print(n_t[1][1])
print(n_t[2][2])

>>>
p
t
s
4
3
>>>
```

<a href='#^'>^^^</a>

```python
t = ('p','e','r','m','i','t')

print(t[-1])
print(t[-6])

>>>
t
p
>>>
```

<a href='#^'>^^^</a>

```python
t = ('p','r','o','g','r','a','m','i','z')

print(t[1:4])
print(t[:-7])
print(t[7:])
print(t[:])

>>>
('r', 'o', 'g')
('p', 'r')
('i', 'z')
('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
>>>
```

<a href='#^'>^^^</a>

```python
tup = ("apple", "banana", "cherry")

print(tup)

>>>
('apple', 'banana', 'cherry')
>>>
```

<a href='#^'>^^^</a>

```python
t = (4, 2, 3, [6, 5])
t[3][0] = 9

print(t)

t = ('p','r','o','g','r','a','m','i','z')

print(t)

>>>
(4, 2, 3, [9, 5])
('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
>>>
```

<a href='#^'>^^^</a>

```python
print((1, 2, 3) + (4, 5, 6))
print(("Repeat",) * 3)

>>>
(1, 2, 3, 4, 5, 6)
('Repeat', 'Repeat', 'Repeat')
>>>
```

<a href='#^'>^^^</a>

```python
t = ('p','r','o','g','r','a','m','i','z')
print(t)

del t
print(t)

>>>
('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
Traceback (most recent call last):
  File "python", line 5, in <module>
NameError: name 't' is not defined
>>>
```

<a href='#^'>^^^</a>

```python
tup = ("apple", "banana", "cherry")

print(tup[1])

>>>
banana
>>>
```

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

```python
tup = ("apple", "banana", "cherry")

print(len(tup))

>>>
3
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='tupmeth'>Python tuple methods</h3>

```python
t = ('a','p','p','l','e',)

print(t.count('p'))
print(t.index('l'))

>>>
2
3
>>>
```

<a href='#^'>^^^</a>

---

<h3 id='sets'>Python sets</h3>

Sets are unordered collections of unique elements

```python
s = set()

print(type(s))

>>>
<class 'set'>
>>>
```

<a href='#^'>^^^</a>

```python
s = set()

s.add(1)
print(s)

s.add(2)
print(s)

s.add(2)
print(s)

>>>
{1}
{1, 2}
{1, 2}
>>>
```

<a href='#^'>^^^</a>

```python
l = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
s = set(l)

print(s)

>>>
{1, 2, 3}
>>>
```

<a href='#^'>^^^</a>

```python
s = set('Mississippi')

print(s)

>>>
{'p', 'i', 's', 'M'}
>>>
```

<a href='#^'>^^^</a>

```python
st = {1, 2, 3}
print(st)

st = {1.0, "Hello", (1, 2, 3)}
print(st)

>>>
{1, 2, 3}
{1.0, 'Hello', (1, 2, 3)}
>>>
```

<a href='#^'>^^^</a>

```python
st = {1,2,3,4,3,2}
print(st)

st = set([1,2,3,2])
print(st)

>>>
{1, 2, 3, 4}
{1, 2, 3}
>>>
```

<a href='#^'>^^^</a>

```python
a = {}
print(type(a))

a = set()
print(type(a))

>>>
<class 'dict'>
<class 'set'>
>>>
```

<a href='#^'>^^^</a>

```python
st = {1,3}
print(st)

st.add(2)
print(st)

st.update([2,3,4])
print(st)

st.update([4,5], {1,6,8})
print(st)

>>>
{1, 3}
{1, 2, 3}
{1, 2, 3, 4}
{1, 2, 3, 4, 5, 6, 8}
>>>
```

<a href='#^'>^^^</a>

```python
st = {1, 3, 4, 5, 6}
print(st)

st.discard(4)
print(st)

st.remove(6)
print(st)

st.discard(2)
print(st)

>>>
{1, 3, 4, 5, 6}
{1, 3, 5, 6}
{1, 3, 5}
{1, 3, 5}
>>>
```

<a href='#^'>^^^</a>

```python
st = set("HelloWorld")
print(st)

print(st.pop())

st.pop()
print(st)

st.clear()
print(st)

>>>
{'r', 'e', 'H', 'l', 'o', 'W', 'd'}
r
{'H', 'l', 'o', 'W', 'd'}
set()
>>>
```

<a href='#^'>^^^</a>

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B)

>>>
{1, 2, 3, 4, 5, 6, 7, 8}
>>>
```

<a href='#^'>^^^</a>

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A & B)

>>>
{4, 5}
>>>
```

<a href='#^'>^^^</a>

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A - B)
print(B - A)

>>>
{1, 2, 3}
{8, 6, 7}
>>>
```

<a href='#^'>^^^</a>

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A ^ B)

>>>
{1, 2, 3, 6, 7, 8}
>>>
```

<a href='#^'>^^^</a>

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

<h3 id='dictionary'>Python dictionary</h3>

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

<h3 id='if..else'>Python if..else</h3>

---
<h4 id='^^'></h4>
<a href='#temp'>Template</a><br>
<a href='#ifif'>if</a><br>
<a href='#ifelse'>if..else</a><br>
<a href='#ifelifelse'>if..elif..else</a><br>
<a href='#ifinput'>Nested if with input</a><br><br>

<a href='#^'>^^^</a>

---

<h4 id='basie'>Template</h4>

```python
if some_condition:
    # execute some code
elif some_other_condition:
    # do something different
else:
    # do something else
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='ifif'>if</h4>

```python
a = 33
b = 200

if b > a:
    print("b is greater than a")

>>>
b is greater than a
>>>
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

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

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='ifelse'>if..else</h4>

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

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='ifelifelse'>if..elif..else</h4>

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

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

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

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

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

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='ifinput'>Nested if with input</h4>

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

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

---

<h3 id='for'>Python for</h3>

---
<h4 id='^^'></h4>
<a href ='#basscr'>Basic script</a><br>
<a href ='#odevnu'>Odd and Even numbers</a><br>
<a href ='#sumlis'>Sum of the list</a><br>
<a href ='#itestr'>Iterate a string</a><br>
<a href ='#itetup'>Iterate tuples</a><br>
<a href ='#itedic'>Iterate dictionary</a><br>
<a href ='#forran'>for with range()</a><br><br>
<a href='#^'>^^^</a>

---

<h4 id='basscr'>Basic script</h4>

```python
#python for
l = [1,2,3]

for n in l:
    print(l)

>>>
1
2
3
>>>
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='odevnu'>Odd and Even numbers</h4>

```python
#python for
l = [1,2,3, 4, 5, 6, 7, 8, 9, 10]
for num in l:
    if num % 2 == 0:
        print(num)
    else:
        print(f'odd number:{num}')
	
>>>
odd number:1
2
odd number:3
4
odd number:5
6
odd number:7
8
odd number:9
10
>>>
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='sumlis'>Sum of the list</h4>

```python
#python for
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

sum = 0

for val in numbers:
	sum = sum+val

print("The sum is", sum)

>>>
The sum is 48
>>>
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

```python
#python for
#how to count the sum of the list = final number
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ls = 0

for num in l:
    ls = ls + num

print(ls)

>>>
55
>>>
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

```python
#python for
#how to count the sum of the list = the whole chain
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ls = 0

for num in l:
    ls = ls + num

    print(ls)
    
>>>
1
3
6
10
15
21
28
36
45
55
>>>
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='itestr'>Iterate a string</h4>

```python
#python for
s = 'trk'

for letters in s:
    print(letters)
    
>>>
t
r
k
>>>
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

```python
#python for
for letters in 'trk':
    print(letters)
    
>>>
t
r
k
>>>
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

```python
#python for
for _ in 'trk':
    print('hey')
    
>>>
trk
trk
trk
>>>
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='itetup'>Iterate tuples</h4>

```python
#python for
l = [(1,2),(3,4),(5,6),(7,8)]
print(len(l))

for n in l:
    print(n)
    
>>>
4
(1, 2)
(3, 4)
(5, 6)
(7, 8)
>>>
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

```python
#python for
l = [(1,2),(3,4),(5,6),(7,8)]

for (a,b) in l:
    print(a)
    print(b)
    
>>>
1
2
3
4
5
6
7
8
>>>
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

```python
#python for
l = [(1,2),(3,4),(5,6),(7,8)]

for a,b in l:
    print(a)
    
>>>
1
3
5
7
>>>
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

```python
#python for
l = [(1, 2, 3),(4, 5, 6),(7, 8, 9)]

for a, b, c in l:
    print(b)
    
>>>
2
5
8
>>>
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='itedic'>Iterate dictionary</h4>

```python
#python for
d = {'k1':1, 'k2':2, 'k3':3}

for k,v in d.items():
    print(k)
 
>>>
k1
k2
k3
>>>
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>


```python
#python for
d = {'k1':1, 'k2':2, 'k3':3}

for k,v in d.items:
    print(v)
    
>>>
1
2
3
>>>
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

```python
#python for
d = {'k1':1, 'k2':2, 'k3':3}

for item in d.items():
    print(item)
    
>>>
('k1', 1)
('k2', 2)
('k3', 3)
>>>
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='forran'>for with range()</h4>

```python
#python for
genre = ['pop', 'rock', 'jazz']

for i in range(len(genre)):
	print("I like", genre[i])

>>>
I like pop
I like rock
I like jazz
>>>
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

```python
#python for
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
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

```python
#python for
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

<a href='#^^'>^^</a><br>
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

<a href='#^'>^^^</a>

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

```
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
```

<a href='#^'>^^^</a>

```python
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
```

<a href='#^'>^^^</a>

```python
while test:
	code statement
	if test:
		break
	if test:
		continue
else:
	final code statements
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
```

<a href='#^'>^^^</a>

```python
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
```

<a href='#^'>^^^</a>

---

<h3 id='functions'>Python functions</h3>

```python
a = 10
b = 20
d = 3
e = 6

def elso():
    c = a+b
    return c

def masodik():
    f = d+e
    return f

ee = elso()
mm = masodik()

def harmadik():
    x = ee+mm
    return x

def negyedik(x,y):
    final = x+y
    print(final)

print(harmadik())
negyedik(ee, mm)

>>>
39
39
>>>
```

<a href='#^'>^^^</a>

```python
hometown = 'ds'
age = '35'
user_name = 'trk'

x = 10
y = 20
z = 42

def year(ccc, aaa):
    print("Hello, ", ccc, ". You are", aaa, "old")

def place(ccc, bbb):
    print('hey', ccc, 'you are from', bbb, 'right?')

def greet(ccc):
    print("Hello, ", ccc, ". Good morning!")

def kkk():
    yu = 66+18
    return yu

kyu = kkk()

def ct():
    ppp = z+y+z+kyu
    return ppp

def sowhat():
    xxx = ct() + z
    print(xxx)

year(user_name, age)
place(user_name, hometown)
greet(user_name)
print(ct())
sowhat()
```

<a href='#^'>^^^</a>

```python
def my_add_func(arg1, arg2):    
    print (arg1 + arg2)

my_add_func(1, 2)

>>>
3
>>>
```

<a href='#^'>^^^</a>

```python
def add_num(num1, num2):
    return (num1 + num2)

x = add_num(2, 3)

print(x)

>>>
5
>>>
```

<a href='#^'>^^^</a>

```python
def add_num(num1, num2):
    return (num1 + num2)

x = add_num("one", "two")

print(x)

>>>
onetwo
>>>
```

<a href='#^'>^^^</a>

```python
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
```

<a href='#^'>^^^</a>

```python
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
```

<a href='#^'>^^^</a>

```python
def hello(name='trk'):
  print("the hello() function has been executed")
  
  def greet():
    return "\t This is inside the greet() function"
  
  def welcome():
    return "\t This is inside the welcome() function"
    
  print(greet())
  print(welcome())
  print("now we are back inside the hello() function")
    
print(hello())

>>>
the hello() function has been executed
	 This is inside the greet() function
	 This is inside the welcome() function
now we are back inside the hello() function
>>>
```

<a href='#^'>^^^</a>

```python
def hello(name='trk'):
  
  def greet():
    return "\t This is inside the greet() function"
  
  def welcome():
    return "\t This is inside the welcome() function"
    
  if name == 'trk':
    return greet
  else:
    return welcome
  
print(hello())

>>>
<function hello.<locals>.greet at 0x7f3364132620>
>>>
```

<a href='#^'>^^^</a>

```python
def hello():
  return 'hi trk!'
  
def other(func):
  print('other code goes here')
  print(func())
  
print(other(hello))

>>>
other code goes here
hi trk!
>>>
```

<a href='#^'>^^^</a>

```python
def new_decorator(func):
  
  def wrap_func():
    print('code here, before executing the func')
    
    func()
    
    print('code here will execute after the func()')
    
  return wrap_func
  
def func_needs_decorator():
  print('This function needs a decorator')
  
func_needs_decorator = new_decorator(func_needs_decorator)

print(func_needs_decorator())

>>>
code here, before executing the func
This function needs a decorator
code here will execute after the func()
>>>
```

<a href='#^'>^^^</a>

```python
def new_decorator(func):
  
  def wrap_func():
    print('code here, before executing the func')
    
    func()
    
    print('code here will execute after the func()')
    
  return wrap_func
  
@new_decorator
def func_needs_decorator():
  print('This function needs a decorator')
  
print(func_needs_decorator())

>>>
code here, before executing the func
This function needs a decorator
code here will execute after the func()
>>>
```

<a href='#^'>^^^</a>

```python
def gencubes(n):
  for num in range(n):
    yield num**3
    
for x in gencubes(10):
  print(x)
  
>>>
0
1
8
27
64
125
216
343
512
729
>>>
```

<a href='#^'>^^^</a>

```python
def genfibon(n):
  a = 1
  b = 1
  
  for i in range(n):
    yield a
    t = a
    a = b
    b = t+b 

for num in genfibon(10):
  print(num)
  
>>>
1
1
2
3
5
8
13
21
34
55
>>>
```

<a href='#^'>^^^</a>

```python
def fibon(n):
  a = 1
  b = 1
  
  output = []
  
  for i in range(n):
    output.append(a)
    a,b = b, a+b 
    
  return output
  
print(fibon(10))

>>>
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
>>>
```

<a href='#^'>^^^</a>

```python
def simple_gen():
  for x in range(3):
    yield x
    
g = simple_gen()

print(next(g))
print(next(g))
print(next(g))

>>>
0
1
2
>>>
```

<a href='#^'>^^^</a>

```python
s = 'hello'

for let in s:
  print(let)
  
>>>
h
e
l
l
o
>>>
```

<a href='#^'>^^^</a>

```python
s = 'hello'

s_iter = iter(s)

print(next(s_iter))

>>>
h
>>>
```

<a href='#^'>^^^</a>

```python
s = 'hello'
s_iter = iter(s)

print(next(s_iter))
print('+')
print(next(s_iter))
print('+')
print(next(s_iter))
print('+')
print(next(s_iter))
print('+')
print(next(s_iter))

>>>
h
+
e
+
l
+
l
+
o
>>>
```

<a href='#^'>^^^</a>

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
def square(num):
    result = num**2
    return result

print (square(2))

>>>
4
>>>
```

<a href='#^'>^^^</a>

```python
def square(num):
    return num**2

print (square(3))

>>>
9
>>>
```

<a href='#^'>^^^</a>

```python
def square(num): return num**2

print (square(4))

>>>
16
>>>
```

<a href='#^'>^^^</a>

```python
square = lambda num: num**2

print (square(5))

>>>
25
>>>
```

<a href='#^'>^^^</a>

```python
even = lambda num: num %2 == 0

print (even(4))

>>>
True
>>>
```

<a href='#^'>^^^</a>

```python
def even(num):
    return num %2 == 0

print (even(10))

>>>
True
>>>
```

<a href='#^'>^^^</a>

```python
first = lambda s: s[0]

print (first("hello"))

>>>
h
>>>
```

<a href='#^'>^^^</a>

```python
rev = lambda s: s[::-1]

print (rev("hello"))

>>>
olleh
>>> 
```

<a href='#^'>^^^</a>

```python
def adder(x, y):
    return x + y

print (adder(10, 12))

>>>
22
>>>
```

<a href='#^'>^^^</a>

```python
adder = lambda x, y: x + y

print (adder(15, 2))

>>>
17
>>>
```

<a href='#^'>^^^</a>

```python
len_check = lambda item: len(item)

print (len_check("blabla"))

>>>
6
>>>
```

<a href='#^'>^^^</a>

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
class NameOfClass():

  def __init__(self, param1, param2):
    self.param1 = param1
    self.param2 = param2
  
  def some_methods(self):
    print(self.param1)
```

```python
class Sample():
    pass

my_sample = Sample()

print(type(my_sample))

>>>
<class '__main__.Sample'>
>>>
```

```python
class Dog():

    def __init__(self, breed, name):

        self.breed = breed
        self.name = name

my_dog = Dog(breed='Lab', name='cat')

print(my_dog.breed)
print(my_dog.name)

>>>
Lab
cat
>>>
```

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


