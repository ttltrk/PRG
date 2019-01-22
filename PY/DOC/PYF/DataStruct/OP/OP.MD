
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [DS](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/DataStruct/DS.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Data Structures - Data Types - Python Operators</h3>

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
