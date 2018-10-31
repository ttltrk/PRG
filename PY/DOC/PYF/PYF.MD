
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

* <a href='#lists'>list</a>
* <a href='#list_methods'>list methods</a>
* <a href='#list_comprehensions'>list comprehensions</a>
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

---

* <a href='#mopali'>modules, packages, libs</a>
* <a href='#numpy'>NumPy</a>
* <a href='#pandas'>Pandas</a>

---

* <a href='#oop'>oop</a>

---

* <a href='#errexc'>errors and exceptions</a>

---

* <a href='#bonobo'>Bonobo</a>

---

* <a href='#db2'>db2</a>
* <a href='#postgresql'>PostgreSQL</a>

---

* <a href='#raspberrypi'>raspberry Pi</a>

---

* <a href='#kivy'>Kivy</a>
* <a href='#processing'>processing</a>

---

* <a href='#py_links'>links</a>

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
<h3 id='^^ops'></h3>

---

* <a href='#aritops'>arithmetic operators</a><br>
* <a href='#assops'>assignment operators</a><br>
* <a href='#compops'>comparison operators</a><br>
* <a href='#logops'>logical operators</a><br>
* <a href='#ideops'>identity operators</a><br>
* <a href='#memops'>membership operators</a><br>
* <a href='#bitops'>bitwise operators</a>

<a href='#^'>^^^</a>

---

<h4 id='aritops'>arithmetic operators</h4>

```python
Operator	Name		Example	Try it
+		Addition	x + y	
-		Subtraction	x - y	
*		Multiplication	x * y	
/		Division	x / y	
%		Modulus	x % y	
**		Exponentiation	x ** y	 
//		Floor division	x // y
```

<a href='#^^ops'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='assops'>assignment operators</h4>

```python
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3
```

<a href='#^^ops'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='compops'>comparison operators</h4>

```python
Operator	Name				Example	
==		Equal				x == y	
!=		Not equal			x != y	
>		Greater than			x > y	
<		Less than			x < y	
>=		Greater than or equal to	x >= y	
<=		Less than or equal to		x <= y
```

<a href='#^^ops'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='logops'>logical operators</h4>

```python
Operator	Description							Example	
and 		Returns True if both statements are true			x < 5 and  x < 10	
or		Returns True if one of the statements is true			x < 5 or x < 4	
not		Reverse the result, returns False if the result is true		not(x < 5 and x < 10)
```

<a href='#^^ops'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='ideops'>identity operators</h4>

```python
Operator	Description						Example	
is 		Returns true if both variables are the same object	x is y	
is not		Returns true if both variables are not the same object	x is not y
```

<a href='#^^ops'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='memops'>membership operators</h4>

```python
Operator	Description										Example
in 		Returns True if a sequence with the specified value is present in the object		x in y	
not in		Returns True if a sequence with the specified value is not present in the object	x not in y
```

<a href='#^^ops'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='bitops'>bitwise operators</h4>

```python
Operator	Name			Description
& 		AND			Sets each bit to 1 if both bits are 1
|		OR			Sets each bit to 1 if one of two bits is 1
 ^		XOR			Sets each bit to 1 if only one of two bits is 1
~ 		NOT			Inverts all the bits
<<		Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>		Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits 
fall off
```

<a href='#^^ops'>^^</a><br>
<a href='#^'>^^^</a>

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

<h4 id='logope'>logical operators</h4>

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

---

```python
| P | y | t | h | o | n |
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

<a href='#^'>^^^</a>

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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

---

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
<h3 id='^^strm'></h3>

---

<a href='#str_capitalize'>capitalize</a><br>
<a href='#str_casefold'>casefold</a><br>
<a href='#str_center'>center</a><br>
<a href='#str_count'>count</a><br>
<a href='#str_encode'>encode</a><br>
<a href='#str_endswith'>endswith</a><br>
<a href='#str_expandtabs'>expandtabs</a><br>
<a href='#str_find'>find</a><br>
<a href='#str_format'>format</a><br>
<a href='#str_format_map'>format_map</a><br>
<a href='#str_index'>index</a><br>
<a href='#str_isalnum'>isalnum</a><br>
<a href='#str_isalpha'>isalpha</a><br>
<a href='#str_isdecimal'>isdecimal</a><br>
<a href='#str_isdigit'>isdigit</a><br>
<a href='#str_isidentifier'>isidentifier</a><br>
<a href='#str_islower'>islower</a><br>
<a href='#str_isnumeric'>isnumeric</a><br>
<a href='#str_isprintable'>isprintable</a><br>
<a href='#str_isspace'>isspace</a><br>
<a href='#str_istitle'>istitle</a><br>
<a href='#str_isupper'>isupper</a><br>
<a href='#str_join'>join</a><br>
<a href='#str_ljust'>ljust</a><br>
<a href='#str_lower'>lower</a><br>
<a href='#str_lstrip'>lstrip</a><br>
<a href='#str_maketrans'>maketrans</a><br>
<a href='#str_partition'>partition</a><br>
<a href='#str_replace'>replace</a><br>
<a href='#str_rfind'>rfind</a><br>
<a href='#str_rindex'>rindex</a><br>
<a href='#str_rpartition'>rpartition</a><br>
<a href='#str_rsplit'>rsplit</a><br>
<a href='#str_rstrip'>rstrip</a><br>
<a href='#str_split'>split</a><br>
<a href='#str_splitlines'>splitlines</a><br>
<a href='#str_startswith'>startswith</a><br>
<a href='#str_swapcase'>swapcase</a><br>
<a href='#str_title'>title</a><br>
<a href='#str_translate'>translate</a><br>
<a href='#str_upper'>upper</a><br>
<a href='#str_zfill'>zfill</a><br>

<a href='#^'>^^^</a>

---

<h4 id='str_capitalize'>capitalize</h4>

```python
txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)

>>>
Hello, and welcome to my world.
>>>
```

<a href='#^^strm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='str_casefold'>casefold</h4>

```python
txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)

>>>
ss
>>>
```

<a href='#^^strm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='str_center'>center</h4>

```python
txt = "banana"

x1 = txt.center(10)
x2 = txt.center(20)
x3 = txt.center(30)
x4 = txt.center(10, 'x')
x5 = txt.center(20, 'x')
x6 = txt.center(30, 'x')

print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
print(x6)

>>>
  banana  
       banana       
            banana            
xxbananaxx
xxxxxxxbananaxxxxxxx
xxxxxxxxxxxxbananaxxxxxxxxxxxx
>>>
```

<a href='#^^strm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='str_count'>count</h4>

```python
s = 'blablaabcdefgblabla'
s1 = 'b'
s2 = 'f'

print(s.count(s1, 5, 10))
print(s.count(s1, 6, 100))
print(s.count(s2, 0, 100))

>>>
1
3
1
>>>
```

```python
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)

>>>
2
>>>
```

<a href='#^^strm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='str_encode'>encode</h4>

```python
string01 = 'pythön!'
print('The string is:', string01)

string02 = string01.encode()
print('The encoded version is:', string02)

string03 = "My name is Ståle"
str03 = string03.encode()
print(str03)

>>>
The string is: pythön!
The encoded version is: b'pyth\xc3\xb6n!'
b'My name is St\xc3\xa5le'
>>>
```

<a href='#^^strm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='str_endswith'>endswith</h4>

```python
txt = "Hello, welcome to my world."

x = txt.endswith(".")
y = txt.endswith("a")

print(x)
print(y)

>>>

>>>
```

<a href='#^^strm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='str_expandtabs'>expandtabs</h4>

```python
txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

>>>
H	e	l	l	o
H       e       l       l       o
H e l l o
H   e   l   l   o
H         e         l         l         o
>>>
```

<a href='#^^strm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='str_find'>find</h4>

```python
txt = "Hello, welcome to my world."

s1 = txt.find("Hello")
s2 = txt.find("welcome")
s3 = txt.find("to")
s4 = txt.find("my")
s5 = txt.find("world")

x1 = txt.find("e", 1, 10)
x2 = txt.find("e", 2, 10)

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(x1)
print(x2)
>>>
0
7
15
18
21
1
8
>>>
```

<a href='#^^strm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id=''></h4>

```python

>>>

>>>
```

<a href='#^^strm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id=''></h4>

```python

>>>

>>>
```

<a href='#^^strm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id=''></h4>

```python

>>>

>>>
```

<a href='#^^strm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id=''></h4>

```python

>>>

>>>
```

<a href='#^^strm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id=''></h4>

```python

>>>

>>>
```

<a href='#^^strm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id=''></h4>

```python

>>>

>>>
```

<a href='#^^strm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id=''></h4>

```python

>>>

>>>
```

<a href='#^^strm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id=''></h4>

```python

>>>

>>>
```

<a href='#^^strm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id=''></h4>

```python

>>>

>>>
```

<a href='#^^strm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id=''></h4>

```python

>>>

>>>
```

<a href='#^^strm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id=''></h4>

```python

>>>

>>>
```

<a href='#^^strm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id=''></h4>

```python

>>>

>>>
```

<a href='#^^strm'>^^</a><br>
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

<a href='#^'>^^^</a>

---

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

---

```python
'String here {} then here {}'.format('something1', 'something2')
```

<a href='#^'>^^^</a>

---

```python
print('this is a string {}'.format('INSERTED'))

>>>
this is a string INSERTED
>>>
```

<a href='#^'>^^^</a>

---

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

---

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

---

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

---

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

---

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

---

```python
mf = open('C:\\path\\path\\path\\test.txt')

print(mf.readlines())

>>>
['hello world\n', 'new line\n', 'third line and hello ']
>>>
```

<a href='#^'>^^^</a>

---

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

---

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

---

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

---

<h3 id='lists'>Python lists</h3>
<h3 id='^^lst'></h3>

---

* <a href='#listtostr'>list to string</a><br>
* <a href='#listtotup'>list to tuple</a><br>
* <a href='#listtodict'>list to dictionary</a>
* <a href='#listtoset'>list to set</a>

<a href='#^'>^^^</a>

---

<h4 id='listtostr'>list to string</h4>

```python
list1 = ['1', '2', '3']
str1 = ''.join(list1)
str2 = ' '.join(list1)
str3 = '-'.join(list1)
str4 = 'x'.join(list1)

print(str1)
print(str2)
print(str3)
print(str4)

>>>
123
1 2 3
1-2-3
1x2x3
>>>
```

<a href='#^^lst'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='listtotup'>list to tuple</h4>

```python
l = [4,5,6]
t = tuple(l)

print(l)
print(t)

>>>
[4, 5, 6]
(4, 5, 6)
>>>
```

<a href='#^^lst'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='listtodict'>list to dictionary</h4>

```python
l = ['bi','double','duo','two']

d = dict((k,2) for k in l)

print(d)

>>>
{'bi': 2, 'double': 2, 'duo': 2, 'two': 2}
>>>
```

<a href='#^^lst'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='listtoset'>list to set</h4>

```python
l1 = ['bi','double','duo','two']
l2 = [1, 2, 3, 4, 5]

s1 = set(l1)
s2 = set(l2)

print(s1)
print(s2)

>>>
{'two', 'bi', 'double', 'duo'}
{1, 2, 3, 4, 5}
>>>
```

<a href='#^^lst'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id=''></h4>

```python

>>>

>>>
```

<a href='#^^lst'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id=''></h4>

```python

>>>

>>>
```

<a href='#^^lst'>^^</a><br>
<a href='#^'>^^^</a>

---

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

---

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

---

```python
# nested list
my_list = ["mouse", [8, 4, 6], ['a']]

print(my_list)

>>>
['mouse', [8, 4, 6], ['a']]
>>>
```

<a href='#^'>^^^</a>

---

```python
#min max
l1 = [1, 2, 3, 50, 60, 100]

print(min(l1))
print(max(l1))

>>>
1
100
>>>
```

---

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

---

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

---

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

---

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

---

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

---

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

---

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

<a href='#^'>^^^</a>

---

```python
>>> x = range(1,5)
>>> type (x)
<class 'range'>
>>> 
```

<a href='#^'>^^^</a>

---

```python
>>> list(range(0, 10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
```

<a href='#^'>^^^</a>

---

```python
>>> list(range(20))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> 
```

<a href='#^'>^^^</a>

---

```python
>>> x = list(range(0,10))
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> type(x)
<class 'list'>
>>> 
```

<a href='#^'>^^^</a>

---

```python
>>> start = 5
>>> stop = 20
>>> list(range(start,stop))
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> 
```

<a href='#^'>^^^</a>

---

```python
>>> start = 5
>>> stop = 20
>>> list(range(start,stop,2))
[5, 7, 9, 11, 13, 15, 17, 19]
>>>
```

---

<h3 id='list_methods'>Python List Methods</h3>
<h3 id='^^lstm'></h3>

---

* <a href='#lstmappend'>append</a><br>
* <a href='#lstmclear'>clear</a><br>
* <a href='#lstmcopy'>copy</a><br>
* <a href='#lstmcount'>count</a><br>
* <a href='#lstmextend'>extend</a><br>
* <a href='#lstmindex'>index</a><br>
* <a href='#lstminsert'>insert</a><br>
* <a href='#lstmpop'>pop</a><br>
* <a href='#lstmremove'>remove</a><br>
* <a href='#lstmreverse'>reverse</a><br>
* <a href='#lstmsort'>sort</a>

---

<h4 id='lstmappend'>append</h4>

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

<a href='#^^lstm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='lstmclear'>clear</h4>

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

<a href='#^^lstm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='lstmcopy'>copy</h4>

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

<a href='#^^lstm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='lstmcount'>count</h4>

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

<a href='#^^lstm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='lstmextend'>extend</h4>

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

<a href='#^^lstm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='lstmindex'>index</h4>

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

<a href='#^^lstm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='lstminsert'>insert</h4>

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

<a href='#^^lstm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='lstmpop'>pop</h4>

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

<a href='#^^lstm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='lstmremove'>remove</h4>

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

<a href='#^^lstm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='lstmreverse'>reverse</h4>

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

<a href='#^^lstm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='lstmsort'>sort</h4>

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

<a href='#^^lstm'>^^</a><br>
<a href='#^'>^^^</a>

---

<h3 id='list_comprehensions'>Python list comprehensions</h3>

---

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

<h3 id='tuples'>Python tuples</h3>

---

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
<h4 id='^^for'></h4>
<a href ='#basscr'>Basic script</a><br>
<a href ='#odevnu'>Odd and Even numbers</a><br>
<a href ='#sumlis'>Sum of the list</a><br>
<a href ='#mullis'>Multiply two lists
<a href ='#itestr'>Iterate a string</a><br>
<a href ='#itetup'>Iterate tuples</a><br>
<a href ='#itedic'>Iterate dictionary</a><br>
<a href ='#forran'>for with range()</a><br><br>
<a href ='#passfor'>pass for</a>
<a href ='#confor'>continue for</a>
<a href ='#brkfor'>break for</a>
<a href ='#enufor'>enumerate for</a>
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

<a href='#^^for'>^^</a><br>
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

<a href='#^^for'>^^</a><br>
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

<a href='#^^for'>^^</a><br>
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

<a href='#^^for'>^^</a><br>
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

<a href='#^^for'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='mullis'>Multiply two lists</h4>

```python
# elements by elements
l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']

for item in zip(l1, l2):
    print(item)
    
>>>
(1, 'a')
(2, 'b')
(3, 'c')
>>>
```

```python
l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
l3 = [100, 200, 300]

for item in zip(l1, l2, l3):
    print(item)
    
>>>
(1, 'a', 100)
(2, 'b', 200)
(3, 'c', 300)
>>>
```

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

<a href='#^^'>^^for</a><br>
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

<a href='#^^'>^^for</a><br>
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

<a href='#^^'>^^for</a><br>
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

<a href='#^^'>^^for</a><br>
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

<a href='#^^'>^^for</a><br>
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

<a href='#^^'>^^for</a><br>
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

<a href='#^^'>^^for</a><br>
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

<a href='#^^'>^^for</a><br>
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

<a href='#^^'>^^for</a><br>
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

<a href='#^^'>^^for</a><br>
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

<a href='#^^'>^^for</a><br>
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

<a href='#^^'>^^for</a><br>
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

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>

---

<h4 id='passfor'>pass for</h4>

```python
x = [1, 2, 3]

for nums in x:
    pass

print('how to use pass')

>>>
how to use pass
>>>
```

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>

---

<h4 id='confor'>continue for</h4>

```print
x = 'sammy'

for letter in x:
    if letter == 'a':
        continue
    print(letter)
    
>>>
s
m
m
y
>>>
```

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>

---

<h4 id='brkfor'>break for</h4>

```python
x = 'sammy'

for letter in x:
    if letter == 'a':
        break
    print(letter)

>>>
s
>>>
```

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>

---

<h4 id='enufor'>enumerate for</h4>

```python
index_count = 0

for letter in 'abc':
    print('at index {} the letter is {}'.format(index_count, letter))
    index_count += 1
    
>>>
at index 0 the letter is a
at index 1 the letter is b
at index 2 the letter is c
>>>
```

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>

---

```python
word = 'abc'

for item in enumerate(word):
    print(item)
    
>>>
(0, 'a')
(1, 'b')
(2, 'c')
>>>
```

---

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>

```python
word = 'abc'

for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')
    
>>>
0
a


1
b


2
c
>>>
```

<a href='#^^'>^^for</a><br>
<a href='#^'>^^^</a>

---

<h3 id='while'>Python while</h3>

---

<h4 id=''>while Template</h4>

```python
while some_boolean_condition:
    #do something
```

<a href='#^'>^^^</a>

```python
while some_boolean_condition:
    #do something
else:
    #do something different
```

<a href='#^'>^^^</a>

---

<h4 id=''>Infinity loop</h4>

```python
x = 0

while x < 10:
    print(f'the current status of x is {x}')
    
>>>
...
>>>
```

<a href='#^'>^^^</a>

---

<h4 id=''>Basic while loop</h4>

```python
x = 0
while x < 5:
    print(f'the current status of x is {x}')
    #x = x + 1
    x += 1
    
>>>
the current status of x is 0
the current status of x is 1
the current status of x is 2
the current status of x is 3
the current status of x is 4
>>>
```

<a href='#^'>^^^</a>

```python
x = 1
while x < 5:
    print(f'the current status of x is {x}')
    #x = x + 1
    x += 1
    
>>>
the current status of x is 1
the current status of x is 2
the current status of x is 3
the current status of x is 4
>>>
```

<a href='#^'>^^^</a>

```python
x = 3
while x < 5:
    print(f'the current status of x is {x}')
    #x = x + 1
    x += 1   
    
>>>
the current status of x is 3
the current status of x is 4
>>>
```

<a href='#^'>^^^</a>

---

<h4 id=''>while with else</h4>

```python
x = 1
while x < 5:
    print(f'the current status of x is {x}')
    #x = x + 1
    x += 1
else:
    print('x is less than 5')
    
>>>
the current status of x is 1
the current status of x is 2
the current status of x is 3
the current status of x is 4
x is less than 5
>>>
```

<a href='#^'>^^^</a>

---

<h4 id=''>break while</h4>

```python
x = 0

while x < 5:
    if x == 2:
        break
    print(f'x is now {x}')
    x += 1
    
>>>
x is now 0
x is now 1
>>>
```

<a href='#^'>^^^</a>

---

```python

>>>

>>>
```

<a href='#^'>^^^</a>

---

```python

>>>

>>>
```

<a href='#^'>^^^</a>

---

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

<a href='#^'>^^^</a>

---

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

<h3 id='functions'>Python functions</h3>
<h3 id='^^def'></h3>

---

* <a href='#temp_01'>temp_01</a>
* <a href='#temp_02'>temp_02</a>
* <a href='#temp_03'>temp_03</a>
* <a href='#temp_04'>temp_04</a>
* <a href='#temp_05'>temp_05</a>
* <a href='#say_hello'>say_hello</a>
* <a href='#sum_strings'>sum_strings</a>
* <a href='#bigger'>bigger</a>
* <a href='#trueorfalse'>true or false</a>
* <a href='#dog_check'>dog_check</a>
* <a href='#cat_check'>cat_check</a>
* <a href='#pig_latin'>pig_latin</a>
* <a href='#lesser_of_two_evens'>lesser_of_two_evens</a>
* <a href='#args'>args</a>
* <a href='#kwargs'>kwargs</a>
* <a href='#animal_crackers'>animal_crackers</a>
* <a href='#makes_twenty'>makes_twenty</a>
* <a href='#defevenodd'>even and odd numbers</a>
* <a href='#old_macdonald'>old_macdonald</a>
* <a href='#uppersec'>upper() every 2nd char</a>
* <a href='#master_yoda'>master_yoda</a>
* <a href='#almost_there'>almost_there</a>
* <a href='#has_33'>has_33</a>
* <a href='#paper_doll'>paper_doll</a>
* <a href='#blackjack'>blackjack</a>
* <a href='#summer_69'>summer_69</a>
* <a href='#count_primes'>count_primes</a>
* <a href='#fibon'>fibon</a>
* <a href='#map'>map</a><br>
* <a href='#filter'>filter</a><br>
* <a href='#funnesstat'>nested statement</a><br>

<a href='#^'>^^^</a>

---

<h4 id='temp_01'>temp_01</h4>

```python
######################
#variables
######################

vn11 = 10
vn12 = 9
vn13 = 5
vn14 = 8

vn31 = 27
vn32 = 71

######################
#Level 1
######################

def l11(a,b):
    x11 = a+b
    return x11

def l12(a,b):
    x12 = a*b
    return x12

######################
#Level 2
######################

def l21():
    y21 = l11(vn11, vn12)+l12(vn13, vn14)
    return y21

def l22():
    y22 = l11(vn11, vn12) - l12(vn13, vn14)
    return y22

######################
#Level 3
######################

def l31():
    z31 = l21() + vn31
    return z31

def l32():
    z32 = l21() + vn32
    return z32

def l33():
    z33 = l22() - 10
    return z33

######################
#prime, again, exit
######################

def prime():
    while True:
        p1 = int(input('n1-n2-n3-n4 or n5 exit \n'))
        if p1 == 1:
            print(l31())
        elif p1 == 2:
            print(l32())
        elif p1 == 3:
            print(l33())
        elif p1 == 4:
            print(l31(), l32(), l33())
        elif p1 == 5:
            return exit()

def again():
    return prime()

def exit():
    print('bye')

######################
#run
######################

prime()
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='temp_02'>temp_02</h4>

```python
#your variables
x = 2
y = 3
m = 'yellow'
n = ' '
p = 'uuuuuugh'

#first todo function
def first(aa, bb):
    a = aa+bb
    return a

#second todo function
def sec(nn, mm):
    k = 'hello'
    return k+n+mm

#third todo function
def third(fff, ooo):
    l = 'fffUUU'
    return l+fff+ooo

#main function
def prime():
    a = int(input('num?'))
    if a == 1:
        print(first(x,y))
    elif a == 2:
        print(sec(n,m))
    elif a == 3:
        print(third(n, p))
    else:
        print('give me a num')

prime()

>>>
num?1
5

num?2
hello yellow

num?3
fffUUU uuuuuugh
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='temp_03'>temp_03</h4>

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

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='temp_04'>temp_04</h4>

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

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='temp_05'>temp_05</h4>

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

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='say_hello'>say_hello</h4>

```python
def say_hello(name='NAME'):
    print('hello', name)

say_hello()
say_hello('trk')

>>>
hello NAME
hello trk
>>>
```

```python
def say_hello(name='trk'):
  print("the say_hello() function has been executed")
  
  def greet():
    return "\t This is inside the greet() function"
  
  def welcome():
    return "\t This is inside the welcome() function"
    
  print(greet())
  print(welcome())
  print("now we are back inside the hello() function")
    
print(say_hello())

>>>
the say_hello() function has been executed
	 This is inside the greet() function
	 This is inside the welcome() function
now we are back inside the hello() function
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='sum_strings'>sum_strings</h4>

```python
def sum_strings(num1, num2):
    return (num1 + num2)

x = add_num("one", "two")

print(x)

>>>
onetwo
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='bigger'>bigger</h4>

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

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='trueorfalse'>true or false</h4>

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

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='dog_check'>dog_check</h4>

```python
def dog_check(s):
    if 'dog' in s:
        return True
    else:
        return False

print(dog_check('my dog ran away'))
print(dog_check('my Dog ran away'))
print(dog_check('my cat ran away'))

>>>
True
False
False
>>>
```

```python
def dog_check(s):
    if 'dog' in s.lower():
        return True
    else:
        return False

print(dog_check('my dog ran away'))
print(dog_check('my Dog ran away'))
print(dog_check('my cat ran away'))

>>>
True
True
False
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='cat_check'>cat_check</h4>

```python
def cat_check(s):
    return 'cat' in s.lower()

print(cat_check('my dog ran away'))
print(cat_check('my Cat ran away'))
print(cat_check('my cat ran away'))

>>>
False
True
True
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='pig_latin'>pig_latin</h4>

```python
def pig_latin(word):
    first_letter = word[0]
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word

print(pig_latin('word'))
print(pig_latin('trk'))
print(pig_latin('Hello'))
print(pig_latin('apple'))

>>>
ordway
rktay
elloHay
appleay
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='args'>args</h4>

```python
def mf(*args):
    return sum(args)*2

print(mf(10, 20, 30))

>>>
120
>>>
```

```python
def mf(*args):
    print (args)

mf(10, 20, 30)

>>>
(10, 20, 30)
>>>
```

```python
def mf(*whatever):
    print (whatever)

mf(1, 2, 3, 4, 5)

>>>
(1, 2, 3, 4, 5)
>>>
```

```python
def mf(*args):
    for item in args:
        print(item)

mf(1, 2, 3, 4, 5)

>>>
1
2
3
4
5
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='defevenodd'>even and odd numbers</h4>

```python
def mf(*args):
    l_e = []
    l_o = []
    for nums in args:
        if nums%2 == 0:
            l_e.append(nums)
        elif nums%2 == 1:
            l_o.append(nums)
    print('odd numbers are:', l_o)
    print('even numbers are:', l_e)

mf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

>>>
odd numbers are: [1, 3, 5, 7, 9]
even numbers are: [2, 4, 6, 8, 10]
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='kwargs'>kwargs</h4>

```python
def mf(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('my fruit of choice is {}' .format(kwargs['fruit']))
    else:
        print('i didnt find any fruit here')

mf(fruit='apple', veggie ='lettuce')

>>>
{'fruit': 'apple', 'veggie': 'lettuce'}
my fruit of choice is apple
>>>
```

```python
def mf(*args, **kwargs):
    print('I would like {} {}' .format(args[0], kwargs['food']))
    print(' ')
    print(args)
    print(kwargs)

mf(10, 20, 30, 40, 50, fruit='apple', food ='eggs')

>>>
I would like 10 eggs
 
(10, 20, 30, 40, 50)
{'fruit': 'apple', 'food': 'eggs'}>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='lesser_of_two_evens'>lesser_of_two_evens</h4>

```python
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        if a < b:
            result = a
        else:
            result = b
    else:
        if a > b:
            result = a
        else:
            result = b
    return result

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(8,4))
print(lesser_of_two_evens(2,5))
print(lesser_of_two_evens(7,5))

>>>
2
4
5
7
>>>
```

```python
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        result = min(a,b)
    else:
        result = max(a,b)
    return result

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(8,4))
print(lesser_of_two_evens(2,5))
print(lesser_of_two_evens(7,5))

>>>
2
4
5
7
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='animal_crackers'>animal_crackers</h4>

```python
def animal_crackers(text):
    wordlist = text.split()
    print(wordlist)

    first = wordlist[0]
    second = wordlist[1]

    return first[0] == second[0]

print(animal_crackers('Levelhead Llama'))
print(animal_crackers('Crazy Kangaroo'))

>>>
['Levelhead', 'Llama']
True
['Crazy', 'Kangaroo']
False
>>>
```

```python
def animal_crackers(text):
    wordlist = text.split()

    return wordlist[0][0] == wordlist[1][0]

print(animal_crackers('Levelhead Llama'))
print(animal_crackers('Crazy Kangaroo'))

>>>
True
False
>>>
```

```python
def animal_crackers(text):
    wordlist1 = text.split()
    wordlist2 = text.lower().split()

    print(wordlist1[0][0] == wordlist1[1][0])
    print(wordlist2[0][0] == wordlist2[1][0])

animal_crackers('Crazy cat')

>>>
False
true
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='makes_twenty'>makes_twenty</h4>

```python
def makes_twenty(n1, n2):
    if n1+n2 == 20:
        return True
    elif n1 == 20:
        return True
    elif n2 == 20:
        return True
    else:
        return False

print(makes_twenty(10, 10))
print(makes_twenty(20, 10))
print(makes_twenty(10, 20))
print(makes_twenty(21, 19))

>>>
True
True
True
False
>>>
```

```python
def makes_twenty(n1, n2):
    return (n1+n2) == 20 or n1 == 20 or n2 == 20

print(makes_twenty(10, 10))
print(makes_twenty(20, 10))
print(makes_twenty(10, 20))
print(makes_twenty(21, 19))

>>>
True
True
True
False
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='old_macdonald'>old_macdonald</h4>

```python
def old_macdonald(name):
    first_letter = name[0]
    inbetween = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]

    return first_letter.upper()+inbetween+fourth_letter.upper()+rest

print(old_macdonald('macdonald'))

>>>
MacDonald
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='uppersec'>upper() every 2nd char</h4>

```python
def test(text):
    s1 = text[0:100:2].upper()
    s2 = text[1:100:2].lower()
    l1 = list(s1)
    l2 = list(s2)
    baz = [x + y for x, y in zip(l1, l2)]
    s3 = ''.join(baz)
    return s3

print(test('abcdefgijklmnop'))

>>>
AbCdEfGiJkLmNo
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='master_yoda'>master_yoda</h4>

```python
def master_yoda(text):
    wordlist = text.split()
    reverse_word_list = wordlist[::-1]
    return ' '.join(reverse_word_list)

print(master_yoda('I am home'))

>>>
home am I
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='almost_there'>almost_there</h4>

```python
def almost_there(n):
    return (abs(100-n) <= 10) or (abs(200-n) <= 10)

print(almost_there(104))
print(almost_there(89))
print(almost_there(189))
print(almost_there(204))
print(almost_there(211))

>>>
True
False
False
True
False
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='has_33'>has_33</h4>

```python
def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i+1] ==3:
            return True

    return False

print(has_33([1,3,3]))
print(has_33([3,1,3]))
print(has_33([1,3,1,3]))
print(has_33([1,2,3,3]))

>>>
True
False
False
True
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='paper_doll'>paper_doll</h4>

```python
def paper_doll(text):
    result = ''
    for char in text:
        result += char*3
    return result


print(paper_doll('hello'))
print(paper_doll('trk'))

>>>
hhheeellllllooo
tttrrrkkk
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='blackjack'>blackjack</h4>

```python
def blackjack(a, b, c):
    if sum([a, b, c]) <= 21:
        return sum([a, b, c])
    elif 11 in [a, b, c] and sum([a, b, c]) <= 31:
        return sum([a, b, c])-10
    else:
        return 'BUST'

print(blackjack(8, 7, 9))
print(blackjack(5, 6, 7))
print(blackjack(9, 9, 11))

>>>
BUST
18
19
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='summer_69'>summer_69</h4>

```python
def summer_69(arr):
    total = 0
    add = True

    for num in arr:
        while add:
            if num!=6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

print(summer_69([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
print(summer_69([5, 6, 7, 8, 9, 10]))
print(summer_69([6, 7, 8, 9, 10]))

>>>
36
15
10
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='spy_game'>spy_game</h4>

```python
def spy_game(nums):

    code = [0, 0, 7, 'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

print(spy_game([1, 2, 3, 0, 4, 0, 7]))
print(spy_game([1, 2, 3, 0, 0, 7]))
print(spy_game([0, 7, 0]))

>>>
True
True
False
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='count_primes'>count_primes</h4>

```python
def count_primes(num):
    if num < 2:
        return 0
    primes = [2]
    x = 3

    while x <= num:
        for y in range(3,x,2):
            if x%2 == 0:
                x +=2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(count_primes(20))

>>>
[2, 3, 5, 7, 9, 11, 13, 15, 17, 19]
10
>>>
```

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

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='fibon'>fibon</h4>

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

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='map'>map</h4>

```python
def square(num):
    return num**2

nums = [1, 2, 3, 4, 5]

for item in map(square, nums):
    print(item)
    
>>>
1
4
9
16
25
>>>
```

```python
def square(num):
    return num**2

nums = [1, 2, 3, 4, 5]

print(list(map(square,nums)))

>>>
[1, 4, 9, 16, 25]
>>>
```

```python
def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy', 'Eve', 'Sally']

print(list(map(splicer, names)))

>>>
['EVEN', 'E', 'S']
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='filter'>filter</h4>

```python
def check_even(num):
    return num%2 == 0

mynums = [1, 2, 3, 4, 5, 6]

print(list(filter(check_even, mynums)))

>>>
[2, 4, 6]
>>>
```

```python
def check_even(num):
    return num%2 == 0

mynums = [1, 2, 3, 4, 5, 6]

for n in filter(check_even,mynums):
    print(n)
    
>>>
2
4
6
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='funnesstat'>Nested statement</h4>

```python
name = 'THIS IS A GLOBAL STRING'

def greet():

    name = 'Sammy'

    def hello():
        name = 'IM A LOCAL'
        print('Hello '+name)

    hello()

greet()

>>>
Hello IM A LOCAL
>>>
```

```python
name = 'THIS IS A GLOBAL STRING'

def greet():

    name = 'Sammy'

    def hello():
        #name = 'IM A LOCAL'
        print('Hello '+name)

    hello()

greet()

>>>
Hello Sammy
>>>
```

```python
name = 'THIS IS A GLOBAL STRING'

def greet():

    #name = 'Sammy'

    def hello():
        #name = 'IM A LOCAL'
        print('Hello '+name)

    hello()

greet()

>>>
Hello THIS IS A GLOBAL STRING
>>>
```

```python
x = 50

def func(x):
    print(f'X is {x}')

    x = 200
    print(f'I just LOCALLY changed x to {x}')

func(x)
print(f'outside print x is: {x}')

>>>
X is 50
I just LOCALLY changed x to 200
outside print x is: 50
>>>
```

```python
x = 50

def func():
    global x
    print(f'X is {x}')

    x = 'NEW VALUE'
    print(f'I just LOCALLY changed x to {x}')

func()
print(f'outside print x is: {x}')

>>>
X is 50
I just LOCALLY changed x to NEW VALUE
outside print x is: NEW VALUE
>>>
```

<a href='#^^def'>^^</a><br>
<a href='#^'>^^^</a>

---

<h3 id='lambda'>Python lambda</h3>

---

<h4 id='^^lam'></h4>
<a href='#latese'>lambda temp sequence</a><br>
<a href='#lamap'>lambda with map</a><br>
<a href='#lamane'>lambda map names</a><br>
<a href='#lamanerev'>lambda map names reverse</a><br>
<a href='#lamfil'>lambda with filter</a><br>

<a href='#^'>^^^</a>

---

<h4 id='latese'>lambda temp sequence</h4>

```python
def square(num):
    result = num**2
    return result

print (square(2))

>>>
4
>>>
```

```python
def square(num):
    return num**2

print (square(3))

>>>
9
>>>
```

```python
def square(num): return num**2

print (square(4))

>>>
16
>>>
```

```python
square = lambda num: num**2

print (square(5))

>>>
25
>>>
```

<a href='#^^lam'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='lamap'>lambda with map</h4>

```python
l = [1, 2, 3, 4, 5]

square = list(map(lambda num: num**2,l))

print(square)

>>>
[1, 4, 9, 16, 25]
>>>
```

<a href='#^^lam'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='lamane'>lambda map names</h4>

```python
l = ['Andy', 'Sam', 'John']

names = list(map(lambda chars:chars[0],l))

print(names)

>>>
['A', 'S', 'J']
>>>
```

<a href='#^^lam'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='lamanerev'>lambda map names reverse</h4>

```python
l = ['Andy', 'Sam', 'John']

names = list(map(lambda chars:chars[::-1],l))

print(names)

>>>
['ydnA', 'maS', 'nhoJ']
>>>
```

<a href='#^^lam'>^^</a><br>
<a href='#^'>^^^</a>

---

```python
even = lambda num: num %2 == 0

print (even(4))

>>>
True
>>>
```

<a href='#^^lam'>^^</a><br>
<a href='#^'>^^^</a>

---


<h4 id='lamfil'>lambda with filter</h4>

```python
l = [1, 2, 3, 4, 5]

square = list(filter(lambda num: num%2==0,l))

print(square)

>>>
[2, 4]
>>>
```

<a href='#^^lam'>^^</a><br>
<a href='#^'>^^^</a>

---

```python
def even(num):
    return num %2 == 0

print (even(10))

>>>
True
>>>
```

<a href='#^'>^^^</a>

---

```python
first = lambda s: s[0]

print (first("hello"))

>>>
h
>>>
```

<a href='#^'>^^^</a>

---

```python
rev = lambda s: s[::-1]

print (rev("hello"))

>>>
olleh
>>> 
```

<a href='#^'>^^^</a>

---

```python
def adder(x, y):
    return x + y

print (adder(10, 12))

>>>
22
>>>
```

<a href='#^'>^^^</a>

---

```python
adder = lambda x, y: x + y

print (adder(15, 2))

>>>
17
>>>
```

<a href='#^'>^^^</a>

---

```python
len_check = lambda item: len(item)

print (len_check("blabla"))

>>>
6
>>>
```

<a href='#^'>^^^</a>

---

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

<a href='#^'>^^^</a>

---

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

<a href='#^'>^^^</a>

---

```python
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(3)

print(mydoubler(10))

>>>
30
>>>
```

<a href='#^'>^^^</a>

---

```python
def myfunc(n):
  return lambda a, b : (a + b) * n

mydoubler = myfunc(3)

print(mydoubler(10, 2))

>>>
36
>>>
```

<a href='#^'>^^^</a>

---

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

<h3 id='mopali'>Modules, Packages, Libs</h3>

---

<a href='#shuffle'>shuffle</a>
<a href='randint'>randint</a>
<a href='pippip'>pip</a>

---

<h4 id='shuffle'>shuffle</h4>

```python
from random import shuffle

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

shuffle(l)
print(l)

>>>
[5, 2, 4, 3, 1, 8, 9, 6, 7]
>>>
```

---

<h4 id='randint'>randint</h4>

```python
from random import randint

print(randint(0, 100))

>>>
58
>>>
```

---

<h4 id='pippip'>pip</h4>

```
download --> get-pip.py
launch --> get-pip.py
in cmd --> py -m pip instal <pkg_name>
```

---

<h3 id='numpy'>NumPy</h3>

---

<h4 id='^^numpy'></h4>
<a href='#numarrays'>NumPy Arrays</a><br>
<a href='#nuarrin'>NumPy Array Indexing</a><br>
<a href='#nuinse'>NumPy Indexing and Selection</a><br>

<a href='#^'>^^^</a>

---

<h4 id='numarrays'>NumPy Arrays</h4>

```python
import numpy as np

l = [1, 2, 3, 4, 5]

arr = np.array(l)

print('l =', l)
print('arr =', arr)

>>>
l = [1, 2, 3, 4, 5]
arr = [1 2 3 4 5]
>>>
```

```python
import numpy as np

l = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]

arr = np.array(l)

print(l)
print(arr)

>>>
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[1 2 3]
 [4 5 6]
 [7 8 9]]
>>>
```

```python
import numpy as np

ran1 = np.arange(0, 10)
ran2 = np.arange(0, 10, 2)

print(ran1)
print(ran2)

>>>
[0 1 2 3 4 5 6 7 8 9]
[0 2 4 6 8]
>>>
```

```python
import numpy as np

zer1 = np.zeros(3)
zer2 = np.zeros((3, 3))
one1 = np.ones(4)
one2 = np.ones((2, 4))

print(zer1)
print(zer2)
print(one1)
print(one2)

>>>
[0. 0. 0.]
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
[1. 1. 1. 1.]
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]]
>>>
```

```python
import numpy as np

lin1 = np.linspace(1, 5, 10)

print(lin1)

>>>
[1.         1.44444444 1.88888889 2.33333333 2.77777778 3.22222222
 3.66666667 4.11111111 4.55555556 5.        ]
>>>
```

```python
import numpy as np

eye1 = np.eye(2)
eye2 = np.eye(4)
eye3 = np.eye(6)

print(eye1)
print(eye2)
print(eye3)

>>>
[[1. 0.]
 [0. 1.]]
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
[[1. 0. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0. 0.]
 [0. 0. 1. 0. 0. 0.]
 [0. 0. 0. 1. 0. 0.]
 [0. 0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 0. 1.]]
>>>
```

```python
import numpy as np

rand1 = np.random.rand(2)
rand2 = np.random.rand(5, 5)

print(rand1)
print(rand2)

>>>
[0.53429942 0.03083587]
[[0.56266049 0.26195416 0.27630701 0.57626409 0.70289117]
 [0.48973053 0.41366423 0.61769248 0.318832   0.26887037]
 [0.71457293 0.24885933 0.26328144 0.54152156 0.40952062]
 [0.48591904 0.40144865 0.96884957 0.13419017 0.7895068 ]
 [0.08522755 0.95422188 0.78722507 0.08625817 0.12516238]]
>>>
```

```python
import numpy as np

ranin1 = np.random.randint(9)
ranin2 = np.random.randint(10,30)
ranin3 = np.random.randint(50,100, 10)

print(ranin1)
print(ranin2)
print(ranin3)

>>>
2
22
[57 94 89 57 61 78 55 70 69 82]
>>>
```

```python
import numpy as np

arr = np.arange(25)
resh1 = arr.reshape(5,5)

print(resh1)

>>>
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
>>>
```

```python
import numpy as np

ranarr = np.random.randint(0, 50, 10)
maxran = ranarr.max()
print(ranarr)
print(maxran)

>>>
[22 15 25 13 48 25 24 44  6  3]
48
>>>
```

```python
import numpy as np

ranarr = np.random.randint(0, 50, 10)

maxran = ranarr.max()
minran = ranarr.min()
maxarg = ranarr.argmax()
minarg = ranarr.argmin()

print(ranarr)
print(' ')
print('the highest number of the arr:', maxran)
print('the lowest number of the arr:', minran)
print('the position of the highest num in the arr:', maxarg)
print('the position of the lowest num in the arr:', minarg)

>>>
[43 29 39 19 36 37 10 20 46 37]
 
the highest number of the arr: 46
the lowest number of the arr: 10
the position of the highest num in the arr: 8
the position of the lowest num in the arr: 6
>>>
```

<a href='#^^numpy'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='nuarrin'>NumPy Array Indexing</h4>

```python
import numpy as np

arr = np.arange(0, 11)

print(arr)
print(arr[2])
print(arr[5])
print(arr[1:4])
print(arr[2:8])

>>>
[ 0  1  2  3  4  5  6  7  8  9 10]
2
5
[1 2 3]
[2 3 4 5 6 7]
>>>
```

```python
import numpy as np

arr = np.arange(0, 11)
arr[0:5]=100
print(arr)

>>>
[100 100 100 100 100   5   6   7   8   9  10]
>>>
```

```python
import numpy as np

arr = np.arange(0, 11)
sa = arr[0:6]
print(sa)
sa[:] = 99
print(sa)

>>>
[0 1 2 3 4 5]
[99 99 99 99 99 99]
>>>
```

```python
import numpy as np

arr = np.arange(0, 11)
arr_copy = arr.copy()
print(arr)
print(arr_copy)
arr_copy[:] = 100
print(arr)
print(arr_copy)

>>>
[ 0  1  2  3  4  5  6  7  8  9 10]
[ 0  1  2  3  4  5  6  7  8  9 10]
[ 0  1  2  3  4  5  6  7  8  9 10]
[100 100 100 100 100 100 100 100 100 100 100]
>>>
```

<a href='#^^numpy'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='nuinse'>NumPy Indexing and Selection</h4>

```python
import numpy as np

arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

print(arr_2d)
print(arr_2d[0])
print(arr_2d[0][0])
print(arr_2d[1,1])
print(arr_2d[2,2])

>>>
[[ 5 10 15]
 [20 25 30]
 [35 40 45]]
[ 5 10 15]
5
25
45
>>>
```

```python
import numpy as np

arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

print(arr_2d)
print(arr_2d[:2])
print(arr_2d[:2,1:])

>>>
[[ 5 10 15]
 [20 25 30]
 [35 40 45]]
[[ 5 10 15]
 [20 25 30]]
[[10 15]
 [25 30]]
>>>
```

```python
import numpy as np

arr = np.arange(1, 11)

print(arr > 5)

>>>
[False False False False False  True  True  True  True  True]
>>>
```

```python
import numpy as np

arr = np.arange(1, 11)
bool_arr = arr > 5
print(bool_arr)

a = arr[bool_arr]
print(a)

a1 = arr[arr<3]
a2 = arr[arr>7]
print(a1)
print(a2)

>>>
[False False False False False  True  True  True  True  True]
[ 6  7  8  9 10]
[1 2]
[ 8  9 10]
>>>
```

```python
import numpy as np

arr_2d = np.arange(50).reshape(5,10)
print(arr_2d)
print(' ')

a1 = arr_2d[1:3,3:5]
print(a1)

>>>
[[ 0  1  2  3  4  5  6  7  8  9]
 [10 11 12 13 14 15 16 17 18 19]
 [20 21 22 23 24 25 26 27 28 29]
 [30 31 32 33 34 35 36 37 38 39]
 [40 41 42 43 44 45 46 47 48 49]]
 
[[13 14]
 [23 24]]
>>>
```

<a href='#^^numpy'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='Numoper'>NumPy Operations</h4>

```python
import numpy as np

arr = np.arange(0,11)
s = arr+arr
m = arr*arr
h = arr+100
e = arr ** 2

print(s)
print(m)
print(h)
print(e)

>>>
[ 0  2  4  6  8 10 12 14 16 18 20]
[  0   1   4   9  16  25  36  49  64  81 100]
[100 101 102 103 104 105 106 107 108 109 110]
[  0   1   4   9  16  25  36  49  64  81 100]
>>>
```

```python
import numpy as np

arr = np.arange(0,11)
np1 = np.sqrt(arr)
np2 = np.sin(arr)

print(np1)
print('')
print(np2)

>>>
[0.         1.         1.41421356 1.73205081 2.         2.23606798
 2.44948974 2.64575131 2.82842712 3.         3.16227766]

[ 0.          0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427
 -0.2794155   0.6569866   0.98935825  0.41211849 -0.54402111]
>>>
```

<a href='#^^numpy'>^^</a><br>
<a href='#^'>^^^</a>

---

<h3 id='pandas'>Pandas</h3>

---

<h4 id='^^pand'></h4>
<a href='#panser'>Series</a><br>
<a href='#pddataframe'>DataFrame</a><br>
<a href='#missingdata'>Missing data</a><br>

<a href='#^'>^^^</a>

---

<h4 id='panser'>Series</h4>

```python
import numpy as np
import pandas as pd

lab = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a':10, 'b':20, 'c':30}

a1 = pd.Series(data = my_data)
a2 = pd.Series(data = my_data, index=lab)
a3 = pd.Series(arr)
a4 = pd.Series(d)

print('------------ LIST')
print(a1)
print('------------ LIST with INDEX')
print(a2)
print('------------ ARRAY')
print(a3)
print('------------ DICTIONARY')
print(a4)

>>>
------------ LIST
0    10
1    20
2    30
dtype: int64
------------ LIST with INDEX
a    10
b    20
c    30
dtype: int64
------------ ARRAY
0    10
1    20
2    30
dtype: int32
------------ DICTIONARY
a    10
b    20
c    30
dtype: int64
>>>
```

```python
import numpy as np
import pandas as pd

ser1 = pd.Series([1, 2, 3, 4], ['USA', 'GER', 'USSR', 'JPN'])

print(ser1)
print(ser1['USA'])

>>>
USA     1
GER     2
USSR    3
JPN     4
dtype: int64
1
>>>
```

<a href='#^^pand'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='pddataframe'>DataFrame</h4>

```python
import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)
print('')
print(df['W'])
print('')
print(df.W)
print('')
x = df.X
print(x)
print('')
print(df[['W', 'Z']])

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509

A    2.706850
B    0.651118
C   -2.018168
D    0.188695
E    0.190794
Name: W, dtype: float64

A    2.706850
B    0.651118
C   -2.018168
D    0.188695
E    0.190794
Name: W, dtype: float64

A    0.628133
B   -0.319318
C    0.740122
D   -0.758872
E    1.978757
Name: X, dtype: float64

          W         Z
A  2.706850  0.503826
B  0.651118  0.605965
C -2.018168 -0.589001
D  0.188695  0.955057
E  0.190794  0.683509
>>>
```

```python
import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

df['new'] = df['W'] + df['Y']

print(df)

>>>
          W         X         Y         Z       new
A  2.706850  0.628133  0.907969  0.503826  3.614819
B  0.651118 -0.319318 -0.848077  0.605965 -0.196959
C -2.018168  0.740122  0.528813 -0.589001 -1.489355
D  0.188695 -0.758872 -0.933237  0.955057 -0.744542
E  0.190794  1.978757  2.605967  0.683509  2.796762
>>>
```

```python
 import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df.loc['A'])

>>>
W    2.706850
X    0.628133
Y    0.907969
Z    0.503826
Name: A, dtype: float64
>>>
```

```python
import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

l1 = df.loc['C']
print(l1)

l2 = df.iloc[2]
print(l2)

>>>
W   -2.018168
X    0.740122
Y    0.528813
Z   -0.589001
Name: C, dtype: float64
W   -2.018168
X    0.740122
Y    0.528813
Z   -0.589001
Name: C, dtype: float64
>>>
```

```python
 import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

l1 = df.loc['B', 'Y']
print(l1)

>>>
-0.8480769834036315
>>>
```

```python
import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

l1 = df.loc[['A', 'B'], ['X', 'Y']]
print(l1)

>>>
          X         Y
A  0.628133  0.907969
B -0.319318 -0.848077
>>>
```

```python
import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
print('')
print(df > 0)

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509

       W      X      Y      Z
A   True   True   True   True
B   True  False  False   True
C  False   True   True  False
D   True  False  False   True
E   True   True   True   True
>>>
```

```python
import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
print('')

booldf = df > 0
d1 = df[booldf]

print(d1)

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509

          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118       NaN       NaN  0.605965
C       NaN  0.740122  0.528813       NaN
D  0.188695       NaN       NaN  0.955057
E  0.190794  1.978757  2.605967  0.683509
>>>
```

```python
import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
print('')

d1 = df['W']>0

print(d1)

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509

A     True
B     True
C    False
D     True
E     True
Name: W, dtype: bool
>>>
```

```python
import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
print('')

d1 = df['W']>0

print(d1)

d2 = df[df['W']>0]

print(d2)

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509

A     True
B     True
C    False
D     True
E     True
Name: W, dtype: bool
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509
>>>
```

```python
import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
print('')

d1 = df[df['Z']<0]
print(d1)

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509

          W         X         Y         Z
C -2.018168  0.740122  0.528813 -0.589001
>>>
```

```python
import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
print('')

d1 = df[df['W']>0]
#it is same as df[df['W']>0]['X']
print(d1)
print('')
print(d1['X'])

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509

          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509

A    0.628133
B   -0.319318
D   -0.758872
E    1.978757
Name: X, dtype: float64
>>>
```

```python
import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
print('')

d1 = df[df['W']>0][['Y', 'X']]
print(d1)

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509

          Y         X
A  0.907969  0.628133
B -0.848077 -0.319318
D -0.933237 -0.758872
E  2.605967  1.978757
>>>
```

```python
import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
print('')

d1 = df[df['W']>0][['Y', 'X']]
print(d1)
print('')

d2 = df[(df['W']>0) & (df['Y']>1)]
print(d2)

>>>
          W         X         Y         Z
A  2.706850  0.628133  0.907969  0.503826
B  0.651118 -0.319318 -0.848077  0.605965
C -2.018168  0.740122  0.528813 -0.589001
D  0.188695 -0.758872 -0.933237  0.955057
E  0.190794  1.978757  2.605967  0.683509

          Y         X
A  0.907969  0.628133
B -0.848077 -0.319318
D -0.933237 -0.758872
E  2.605967  1.978757

          W         X         Y         Z
E  0.190794  1.978757  2.605967  0.683509
>>>
```

```python
import pandas
import numpy

newind = 'CA NY WY OR CO'.split()
print(newind)

>>>
['CA', 'NY', 'WY', 'OR', 'CO']
>>>
```

```python
 import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

newind = 'CA NY WY OR CO'.split()
df['States'] = newind

print(df)

>>>
          W         X         Y         Z States
A  2.706850  0.628133  0.907969  0.503826     CA
B  0.651118 -0.319318 -0.848077  0.605965     NY
C -2.018168  0.740122  0.528813 -0.589001     WY
D  0.188695 -0.758872 -0.933237  0.955057     OR
E  0.190794  1.978757  2.605967  0.683509     CO
>>>
```

```python
import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

newind = 'CA NY WY OR CO'.split()
df['States'] = newind
a = df.set_index('States')

print(a)

>>>
               W         X         Y         Z
States                                        
CA      2.706850  0.628133  0.907969  0.503826
NY      0.651118 -0.319318 -0.848077  0.605965
WY     -2.018168  0.740122  0.528813 -0.589001
OR      0.188695 -0.758872 -0.933237  0.955057
CO      0.190794  1.978757  2.605967  0.683509
>>>
```

```python
import numpy as np
import pandas as pd

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside,inside))
#hier_index = pd.MultiIndex.from_tuples(hier_index)

print(hier_index)

>>>
[('G1', 1), ('G1', 2), ('G1', 3), ('G2', 1), ('G2', 2), ('G2', 3)]
>>>
```

```python
import numpy as np
import pandas as pd

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

print(hier_index)

>>>
MultiIndex(levels=[['G1', 'G2'], [1, 2, 3]],
           labels=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]])
>>>
```

```python
import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
df = pd.DataFrame(randn(6,2),hier_index,['A','B'])

print(df)

>>>
             A         B
G1 1  2.706850  0.628133
   2  0.907969  0.503826
   3  0.651118 -0.319318
G2 1 -0.848077  0.605965
   2 -2.018168  0.740122
   3  0.528813 -0.589001
>>>
```

```python
import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
a = df.loc['G1']
print(a)

>>>
          A         B
1  2.706850  0.628133
2  0.907969  0.503826
3  0.651118 -0.319318
>>>
```

```python
import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
a = df.loc['G1']
a1 = df.loc['G1'].loc[1]

print(a1)

>>>
A    2.706850
B    0.628133
Name: 1, dtype: float64
>>>
```

```python
import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
a = df.loc['G1']
a1 = df.loc['G1'].loc[1]
df.index.names = ['Groups', 'Num']
print(df)

>>>
                   A         B
Groups Num                    
G1     1    2.706850  0.628133
       2    0.907969  0.503826
       3    0.651118 -0.319318
G2     1   -0.848077  0.605965
       2   -2.018168  0.740122
       3    0.528813 -0.589001
>>>
```

<a href='#^^pand'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='missingdata'>Missing Data</h4>

```python
import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)
print(df)

>>>
     A    B  C
0  1.0  5.0  1
1  2.0  NaN  2
2  NaN  NaN  3
>>>
```

```python
import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)

a1 = df.dropna()
print(a1)

>>>
     A    B  C
0  1.0  5.0  1
>>>
```

```python
import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)

a1 = df.dropna(axis=1)
print(a1)

>>>
   C
0  1
1  2
2  3
>>>
```

```python
import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)

a1 = df.dropna(thresh=2)
print(a1)

>>>
     A    B  C
0  1.0  5.0  1
1  2.0  NaN  2
>>>
```

```python
import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)

a1 = df.dropna(thresh=2)
a2 = df.fillna(value='FILL VALUE')
print(a2)

>>>
            A           B  C
0           1           5  1
1           2  FILL VALUE  2
2  FILL VALUE  FILL VALUE  3
>>>
```

```python
import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)

a1 = df.dropna(thresh=2)
a2 = df.fillna(value='FILL VALUE')
a3 = df['A'].fillna(value=df['A'].mean())
print(a3)

>>>
0    1.0
1    2.0
2    1.5
Name: A, dtype: float64
>>>
```

<a href='#^^pand'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='groupby'>Groupby</h4>

```python
import numpy as np
import pandas as pd

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)

print(df)

>>>
  Company   Person  Sales
0    GOOG      Sam    200
1    GOOG  Charlie    120
2    MSFT      Amy    340
3    MSFT  Vanessa    124
4      FB     Carl    243
5      FB    Sarah    350
>>>
```

```python
import numpy as np
import pandas as pd

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)

byComp = df.groupby('Company')
a1 = byComp.mean()

print(a1)

>>>
         Sales
Company       
FB       296.5
GOOG     160.0
MSFT     232.0
>>>
```

```python
import numpy as np
import pandas as pd

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)

byComp = df.groupby('Company')

a1 = byComp.mean()
a2 = byComp.sum()

print(a2)

>>>
         Sales
Company       
FB         593
GOOG       320
MSFT       464
>>>
```

```python
import numpy as np
import pandas as pd

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)

byComp = df.groupby('Company')

a1 = byComp.mean()
a2 = byComp.sum()
a3 = byComp.std()

print(a3)

>>>
              Sales
Company            
FB        75.660426
GOOG      56.568542
MSFT     152.735065
>>>
```

```python
import numpy as np
import pandas as pd

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)

byComp = df.groupby('Company')

a1 = byComp.mean()
a2 = byComp.sum()
a3 = byComp.std()
a4 = byComp.sum().loc['FB']

print(a4)

>>>
Sales    593
Name: FB, dtype: int64
>>>
```

```python
import numpy as np
import pandas as pd

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)

byComp = df.groupby('Company')

a1 = byComp.mean()
a2 = byComp.sum()
a3 = byComp.std()
a4 = byComp.sum().loc['FB']
a5 = df.groupby('Company').count()

print(a5)

>>>
         Person  Sales
Company               
FB            2      2
GOOG          2      2
MSFT          2      2
>>>
```

```python
import numpy as np
import pandas as pd

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)

byComp = df.groupby('Company')

a1 = byComp.mean()
a2 = byComp.sum()
a3 = byComp.std()
a4 = byComp.sum().loc['FB']
a5 = df.groupby('Company').count()
a6 = df.groupby('Company').max()

print(a6)

>>>
          Person  Sales
Company                
FB         Sarah    350
GOOG         Sam    200
MSFT     Vanessa    340
>>>
```

```python
import numpy as np
import pandas as pd

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)

byComp = df.groupby('Company')

a1 = byComp.mean()
a2 = byComp.sum()
a3 = byComp.std()
a4 = byComp.sum().loc['FB']
a5 = df.groupby('Company').count()
a6 = df.groupby('Company').max()
a7 = df.groupby('Company').describe()

print(a7)

>>>
        Sales                                                        
        count   mean         std    min     25%    50%     75%    max
Company                                                              
FB        2.0  296.5   75.660426  243.0  269.75  296.5  323.25  350.0
GOOG      2.0  160.0   56.568542  120.0  140.00  160.0  180.00  200.0
MSFT      2.0  232.0  152.735065  124.0  178.00  232.0  286.00  340.0
>>>
```

<a href='#^^pand'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='mejoco'>Merging, Joining and Concatenating</h4>

```python
import pandas as pd

df1 = pd.DataFrame({'A':['A0','A1','A2','A3'],
                    'B':['B0','B1','B2','B3'],
                    'C':['C0','C1','C2','C3'],
                    'D':['D0','D1','D2','D3']},
                   index=[0,1,2,3])

df2 = pd.DataFrame({'A':['A4','A5','A6','A7'],
                    'B':['B4','B5','B6','B7'],
                    'C':['C4','C5','C6','C7'],
                    'D':['D4','D5','D6','D7']},
                   index=[4,5,6,7])

df3 = pd.DataFrame({'A':['A8','A9','A10','A11'],
                    'B':['B8','B9','B10','B11'],
                    'C':['C8','C9','C10','C11'],
                    'D':['D8','D9','D10','D11']},
                   index=[8,9,10,11])

print(df1)
print('')
print(df2)
print('')
print(df3)

>>>
    A   B   C   D
0  A0  B0  C0  D0
1  A1  B1  C1  D1
2  A2  B2  C2  D2
3  A3  B3  C3  D3

    A   B   C   D
4  A4  B4  C4  D4
5  A5  B5  C5  D5
6  A6  B6  C6  D6
7  A7  B7  C7  D7

      A    B    C    D
8    A8   B8   C8   D8
9    A9   B9   C9   D9
10  A10  B10  C10  D10
11  A11  B11  C11  D11
>>>
```

```python
import pandas as pd

df1 = pd.DataFrame({'A':['A0','A1','A2','A3'],
                    'B':['B0','B1','B2','B3'],
                    'C':['C0','C1','C2','C3'],
                    'D':['D0','D1','D2','D3']},
                   index=[0,1,2,3])

df2 = pd.DataFrame({'A':['A4','A5','A6','A7'],
                    'B':['B4','B5','B6','B7'],
                    'C':['C4','C5','C6','C7'],
                    'D':['D4','D5','D6','D7']},
                   index=[4,5,6,7])

df3 = pd.DataFrame({'A':['A8','A9','A10','A11'],
                    'B':['B8','B9','B10','B11'],
                    'C':['C8','C9','C10','C11'],
                    'D':['D8','D9','D10','D11']},
                   index=[8,9,10,11])

a1 = pd.concat([df1,df2,df3])

print(a1)

>>>
      A    B    C    D
0    A0   B0   C0   D0
1    A1   B1   C1   D1
2    A2   B2   C2   D2
3    A3   B3   C3   D3
4    A4   B4   C4   D4
5    A5   B5   C5   D5
6    A6   B6   C6   D6
7    A7   B7   C7   D7
8    A8   B8   C8   D8
9    A9   B9   C9   D9
10  A10  B10  C10  D10
11  A11  B11  C11  D11
>>>
```

```python
import pandas as pd

df1 = pd.DataFrame({'A':['A0','A1','A2','A3'],
                    'B':['B0','B1','B2','B3'],
                    'C':['C0','C1','C2','C3'],
                    'D':['D0','D1','D2','D3']},
                   index=[0,1,2,3])

df2 = pd.DataFrame({'A':['A4','A5','A6','A7'],
                    'B':['B4','B5','B6','B7'],
                    'C':['C4','C5','C6','C7'],
                    'D':['D4','D5','D6','D7']},
                   index=[4,5,6,7])

df3 = pd.DataFrame({'A':['A8','A9','A10','A11'],
                    'B':['B8','B9','B10','B11'],
                    'C':['C8','C9','C10','C11'],
                    'D':['D8','D9','D10','D11']},
                   index=[8,9,10,11])

a1 = pd.concat([df1,df2,df3])
a2 = pd.concat([df1,df2,df3],axis=1)

print(a2)

>>>
      A    B    C    D    A    B    C    D    A    B    C    D
0    A0   B0   C0   D0  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
1    A1   B1   C1   D1  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
2    A2   B2   C2   D2  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
3    A3   B3   C3   D3  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
4   NaN  NaN  NaN  NaN   A4   B4   C4   D4  NaN  NaN  NaN  NaN
5   NaN  NaN  NaN  NaN   A5   B5   C5   D5  NaN  NaN  NaN  NaN
6   NaN  NaN  NaN  NaN   A6   B6   C6   D6  NaN  NaN  NaN  NaN
7   NaN  NaN  NaN  NaN   A7   B7   C7   D7  NaN  NaN  NaN  NaN
8   NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN   A8   B8   C8   D8
9   NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN   A9   B9   C9   D9
10  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  A10  B10  C10  D10
11  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  A11  B11  C11  D11
>>>
```

```python
import pandas as pd

df1 = pd.DataFrame({'A':['A0','A1','A2','A3'],
                    'B':['B0','B1','B2','B3'],
                    'C':['C0','C1','C2','C3'],
                    'D':['D0','D1','D2','D3']},
                   index=[0,1,2,3])

df2 = pd.DataFrame({'A':['A4','A5','A6','A7'],
                    'B':['B4','B5','B6','B7'],
                    'C':['C4','C5','C6','C7'],
                    'D':['D4','D5','D6','D7']},
                   index=[4,5,6,7])

df3 = pd.DataFrame({'A':['A8','A9','A10','A11'],
                    'B':['B8','B9','B10','B11'],
                    'C':['C8','C9','C10','C11'],
                    'D':['D8','D9','D10','D11']},
                   index=[8,9,10,11])

a1 = pd.concat([df1,df2,df3])
a2 = pd.concat([df1,df2,df3],axis=1)

left = pd.DataFrame({'key':['K0','K1','K2','K3'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})

right = pd.DataFrame({'key':['K0','K1','K2','K3'],
                     'C':['C0','C1','C2','C3'],
                     'D':['D0','D1','D2','D3']})

print(left)
print('')
print(right)

>>>
  key   A   B
0  K0  A0  B0
1  K1  A1  B1
2  K2  A2  B2
3  K3  A3  B3

  key   C   D
0  K0  C0  D0
1  K1  C1  D1
2  K2  C2  D2
3  K3  C3  D3
>>>
```

```python
import pandas as pd

df1 = pd.DataFrame({'A':['A0','A1','A2','A3'],
                    'B':['B0','B1','B2','B3'],
                    'C':['C0','C1','C2','C3'],
                    'D':['D0','D1','D2','D3']},
                   index=[0,1,2,3])

df2 = pd.DataFrame({'A':['A4','A5','A6','A7'],
                    'B':['B4','B5','B6','B7'],
                    'C':['C4','C5','C6','C7'],
                    'D':['D4','D5','D6','D7']},
                   index=[4,5,6,7])

df3 = pd.DataFrame({'A':['A8','A9','A10','A11'],
                    'B':['B8','B9','B10','B11'],
                    'C':['C8','C9','C10','C11'],
                    'D':['D8','D9','D10','D11']},
                   index=[8,9,10,11])

a1 = pd.concat([df1,df2,df3])
a2 = pd.concat([df1,df2,df3],axis=1)

left = pd.DataFrame({'key':['K0','K1','K2','K3'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})

right = pd.DataFrame({'key':['K0','K1','K2','K3'],
                     'C':['C0','C1','C2','C3'],
                     'D':['D0','D1','D2','D3']})

a3 = pd.merge(left,right,how='inner',on='key')

print(a3)

>>>
  key   A   B   C   D
0  K0  A0  B0  C0  D0
1  K1  A1  B1  C1  D1
2  K2  A2  B2  C2  D2
3  K3  A3  B3  C3  D3
>>>
```

```python
import pandas as pd

df1 = pd.DataFrame({'A':['A0','A1','A2','A3'],
                    'B':['B0','B1','B2','B3'],
                    'C':['C0','C1','C2','C3'],
                    'D':['D0','D1','D2','D3']},
                   index=[0,1,2,3])

df2 = pd.DataFrame({'A':['A4','A5','A6','A7'],
                    'B':['B4','B5','B6','B7'],
                    'C':['C4','C5','C6','C7'],
                    'D':['D4','D5','D6','D7']},
                   index=[4,5,6,7])

df3 = pd.DataFrame({'A':['A8','A9','A10','A11'],
                    'B':['B8','B9','B10','B11'],
                    'C':['C8','C9','C10','C11'],
                    'D':['D8','D9','D10','D11']},
                   index=[8,9,10,11])

a1 = pd.concat([df1,df2,df3])
a2 = pd.concat([df1,df2,df3],axis=1)

left = pd.DataFrame({'key1':['K0','K1','K2','K3'],
                     'key2':['K0','K1','K0','K1'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})

right = pd.DataFrame({'key1':['K0','K1','K2','K3'],
                      'key2':['K0','K0','K0','K0'],
                     'C':['C0','C1','C2','C3'],
                     'D':['D0','D1','D2','D3']})

#a3 = pd.merge(left,right,how='inner',on='key')
a4 = pd.merge(left,right,on=['key1','key2'])

print(a4)

>>>
  key1 key2   A   B   C   D
0   K0   K0  A0  B0  C0  D0
1   K2   K0  A2  B2  C2  D2
>>>
```

```python

>>>

>>>
```

```python
 
>>>

>>>
```

```python
 
>>>

>>>
```

```python

>>>

>>>
```

```python
 
>>>

>>>
```

```python
 
>>>

>>>
```

```python

>>>

>>>
```

```python
 
>>>

>>>
```

---

<h3 id='oop'>Python OOP</h3>

---

```python
class NameOfClass():

    def __init__(self,param1,param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        print(self.param1)
```

```python
class Dog():

    def __init__(self,breed):
        self.breed = breed

my_dog = Dog(breed='Lab')

print(my_dog.breed)

>>>
Lab
>>>
```

```python
class Dog():

    def __init__(self,mybreed):
        self.breed = mybreed

my_dog = Dog(mybreed='Huskie')

print(my_dog.breed)

>>>
Huskie
>>>
```

```python
class Dog():

    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots

my_dog = Dog(breed='Huskie', name='Sam', spots='False')

print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)

>>>
Huskie
Sam
False
>>>
```

```python
class Dog():

    species ='mammal'

    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots

my_dog = Dog(breed='Huskie', name='Sam', spots='False')

print(my_dog.species)

>>>
mammal
>>>
```

```python
class Dog():

    species ='mammal'

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

    def bark(self):
        print('WOOF')

my_dog = Dog('lab','Frankie')

print(my_dog.name)
print(my_dog.species)
my_dog.bark()

>>>
Frankie
mammal
WOOF
>>>
```

```python
class Dog():

    species ='mammal'

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

    def bark(self):
        print('WOOF, My name is {}'.format(self.name))

my_dog = Dog('lab','Frankie')

my_dog.bark()

>>>
WOOF, My name is Frankie
>>>
```

```python
class Dog():

    species ='mammal'

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

    def bark(self,number):
        print('WOOF, My name is {} and the number is {}'.format(self.name,number))

my_dog = Dog('lab','Frankie')

my_dog.bark(2)

>>>
WOOF, My name is Frankie and the number is 2
>>>
```

```python
class Circle():

    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius

    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle()

print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumference())

>>>
3.14
1
6.28
>>>
```

```python
class Circle():

    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius

    def get_circumference(self):
        print(self.radius * self.pi * 2)

my_circle = Circle(5)

print(my_circle.pi)
print(my_circle.radius)
my_circle.get_circumference()

>>>
3.14
5
31.4
>>>
```

```python
class Circle():

    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius*radius*self.pi

    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle(5)

print(my_circle.area)

>>>
78.5
>>>
```

```python
class Circle():

    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius*radius*Circle.pi

    def get_circumference(self):
        return self.radius * Circle.pi * 2

my_circle = Circle(5)

print(my_circle.area)
print(my_circle.get_circumference())

>>>
78.5
31.4000000
>>>
```

```python
class Animal():
    
    def __init__(self):
        print('ANIMAL CREATED')

myanimal = Animal()

myanimal

>>>
ANIMAL CREATED
>>>
```

```python
class Animal():
    
    def __init__(self):
        print('ANIMAL CREATED')

    def whoami(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')

myanimal = Animal()

myanimal.eat()
myanimal.whoami()

>>>
ANIMAL CREATED
I am eating
I am an animal
>>>
```

```python
class Animal():
    
    def __init__(self):
        print('ANIMAL CREATED')

    def whoami(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

mydog = Dog()

>>>
ANIMAL CREATED
Dog created
>>>
```

```python
class Animal():
    
    def __init__(self):
        print('ANIMAL CREATED')

    def whoami(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

mydog = Dog()
mydog.eat()
mydog.whoami()

>>>
ANIMAL CREATED
Dog created
I am eating
I am an animal
>>>
```

```python
class Animal():
    
    def __init__(self):
        print('ANIMAL CREATED')

    def whoami(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    def whoami(self):
        print('I am a dog')

myanimal = Animal()
mydog = Dog()

mydog.whoami()
myanimal.whoami()

>>>
ANIMAL CREATED
ANIMAL CREATED
Dog created
I am a dog
I am an animal
>>>
```

```python
class Animal():
    
    def __init__(self):
        print('ANIMAL CREATED')

    def whoami(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    def eat(self):
        print('I am a dog and eating')

    def bark(self):
        print('WOOF')

mydog = Dog()

mydog.eat()
mydog.bark()

>>>
ANIMAL CREATED
Dog created
I am a dog and eating
WOOF
>>>
```

```python
class Dog():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + ' says woof'

class Cat():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + ' says meow'

niko = Dog('niko')
felix = Cat('felix')

print(niko.speak())
print(felix.speak())

>>>
niko says woof
felix says meow
>>>
```

```python
class Dog():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + ' says woof'

class Cat():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + ' says meow'

def pet_speak(pet):
    print(pet.speak())

niko = Dog('niko')
felix = Cat('felix')

pet_speak(niko)
pet_speak(felix)

>>>
niko says woof
felix says meow
>>>
```

```python
class Book():

    def __init__(self,title,author,pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

b = Book('Python manual','trk',99)

print(b)
print(str(b))
print(len(b))

>>>
Python manual by trk
Python manual by trk
99
>>>
```

```python
class Book():

    def __init__(self,title,author,pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book object has been deleted')

b = Book('Python manual','trk',99)

del b
print(b)

>>>
A book object has been deleted

Traceback (most recent call last):
    print(b)
NameError: name 'b' is not defined
>>>
```

```python
class Line:

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):

        x1,y1 = self.coor1
        x2,y2 = self.coor2
        
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def slope(self):

        x1,y1 = self.coor1
        x2,y2 = self.coor2

        return (y2-y1) / (x2-x1)

c1 = (3,2)
c2 = (8,10)

myline = Line(c1,c2)

print(myline.distance())
print(myline.slope())

>>>
9.433981132056603
1.6
>>>
```

```python
class Cylinder:

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * 3.14 * (self.radius)**2

    def surface_area(self):
        top = 3.14 * (self.radius**2)
        return (2*top) + (2*3.14*self.radius*self.height)

mycyl = Cylinder(2,3)

print(mycyl.volume())
print(mycyl.surface_area())

>>>
56.52
94.2
>>>
```

```python
class Account():

    def __init__(self,owner,balance=0):

        self.owner = owner
        self.balance = balance

    def deposit(self,dep_amt):

        self.balance = self.balance + dep_amt
        print(f'Added {dep_amt} to the balance')

    def withdrawal(self,wd_amt):

        if self.balance >= wd_amt:
            self.balance = self.balance
            print('Withdrawal accepted')
        else:
            print('Sorry not enough funds')

    def __str__(self):

        return f'Owner: {self.owner} \nBalance: {self.balance}'

a = Account('Sam',500)

print(a)
a.deposit(100)
print(a)

>>>
Owner: Sam 
Balance: 500
Added 100 to the balance
Owner: Sam 
Balance: 600
>>>
```

```python
class Account():

    def __init__(self,owner,balance=0):

        self.owner = owner
        self.balance = balance

    def deposit(self,dep_amt):

        self.balance = self.balance + dep_amt
        print(f'Added {dep_amt} to the balance')

    def withdrawal(self,wd_amt):

        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt
            print('Withdrawal accepted')
        else:
            print('Sorry not enough funds')

    def __str__(self):

        return f'Owner: {self.owner} \nBalance: {self.balance}'

a = Account('Sam',500)

print(a)
a.withdrawal(350)
print(a)

>>>
Owner: Sam 
Balance: 500
Withdrawal accepted
Owner: Sam 
Balance: 150
>>>
```

---

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

* <h3 id='errexc'>errors and exceptions</h3>

---

```python
def add(n1,n2):
    print(n1+n2)

num1 = 10
num2 = input('add a number ')

add(num1,num2)

>>>
add a number 20
Traceback (most recent call last):
  File "C:tt3.py", line 12, in <module>
    add(num1,num2)
  File "C:t3.py", line 7, in add
    print(n1+n2)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>
```

```python
try:
    result = 10+10

except:
    print('hey it looks like you are not adding correctly!')

print(result)

>>>
20
>>>
```

```python
try:
    result = 10+'10'

except:
    print('hey it looks like you are not adding correctly!')

else:
    print('add went well')
    print(result)

>>>
hey it looks like you are not adding correctly!
>>>
```

```python
try:
    result = 10+10

except:
    print('hey it looks like you are not adding correctly!')

else:
    print('add went well')
    print(result)

>>>
add went well
20
>>>
```

```python
try:
    f = open('C:\\Users\\AttilaTorok\\Desktop\\ADM\\PY\\APPS\\TEST\\TEST\\testfile.txt', 'w') 
    f.write('Write a test line')
    
except TypeError:
    print('There was a type error!')

except OSError:
    print('Hey you have an OS error!')

finally:
    print('I always run!')

>>>
I always run!
>>>
```

```python
def ask_for_int():
    try:
        result = int(input('Please provide number: '))
    except:
        print('Whoops, that is not a number')
    finally:
        print('End of try/except/finally')

ask_for_int()

>>>
Please provide number: 17
End of try/except/finally
>>>

>>>
Please provide number: dd
Whoops, that is not a number
End of try/except/finally
>>>
```

```python
def ask_for_int():

    while True:
        try:
            result = int(input('Please provide number: '))
        except:
            print('Whoops, that is not a number')
            continue
        else:
            print('Yes thank you')
            break
        finally:
            print('End of try/except/finally')
            print('I will always run at the end')

ask_for_int()

>>>
Please provide number: 2
Yes thank you
End of try/except/finally
I will always run at the end
>>>

>>>
Please provide number: dd
Whoops, that is not a number
End of try/except/finally
I will always run at the end
Please provide number: cc
Whoops, that is not a number
End of try/except/finally
I will always run at the end
Please provide number: 3
Yes thank you
End of try/except/finally
I will always run at the end
>>>
```

---

<h3 id='bonobo'>Bonobo</h3>

---

<a href='#boninstall'>Install</a><br>
<a href='#bonver'>Version</a><br>
<a href='#bonfirstjob'>First Job</a><br><br>

<a href='#^'>^^^</a>

---

<h4 id='boninstall'>Install</h4>

```python
#install bonobo
py -m pip install bonobo
```

<a href='#^'>^^^</a>

---

<h4 id='bonver'>Version</h4>

```python
#check version
py -m bonobo version

>>>
bonobo v.0.6.3
>>>
```

<a href='#^'>^^^</a>

---

<h4 id='bonfirstjob'>First Job</h4>

```python
C:\path\path>py -m bonobo init first.py
INFO|0000|init: Generated first.py using template 'default'.

C:\path\path>first.py
Hello
World
 - extract in=1 out=2 [done]
 - transform in=2 out=2 [done]
 - load in=2 [done]
```

<a href='#^'>^^^</a>

---

<h3 id='db2'>DB2</h3>

<a href='#^'>^^^</a>

---

<h3 id='postgresql'>PostgreSQL</h3>

<a href='#^'>^^^</a>

---

<h3 id='raspberrypi'>Raspberry Pi</h3>

<a href='#^'>^^^</a>

---

<h3 id='kivy'>Kivy</h3>

---

<a href='#kivyinstall'>Install</a><br>

<a href='#^'>^^^</a>

---

<h3 id='processing'>Processing</h3>

<a href='#^'>^^^</a>

---

<h3 id='py_links'>Python links</h3>

* [python.org](https://docs.python.org/3/tutorial/index.html)
* [programiz](https://www.programiz.com/python-programming)
* [udemy - from 0 to hero](https://www.udemy.com/complete-python-bootcamp/learn/v4/content)

<a href='#^'>^^^</a>

---


