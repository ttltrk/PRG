
---

### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD) - Numbers

---

* <a href="#1">Number Data Type in Python</a>
* <a href="#2">System Prefix</a>
* <a href="#3">Type Conversion</a>
* <a href="#4">Python Decimal</a>
* <a href="#5">Python Fractions</a>
* <a href="#6">Python Mathematics</a>

---

[src - programiz](https://www.programiz.com/python-programming/variables-datatypes)

---

<h4 id="1">NUMBER DATA TYPE IN PYTHON</h4>

```python
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

```python
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

---

<h4 id="2">SYSTEM PREFIX</h4>

|Number|System Prefix|
|-----|------|
|Binary|'0b' or '0B'|
|Octal|'0o' or '0O'|
|Hexadecimal|'0x' or '0X'|

```python
print(0b1101011)
print(0xFB + 0b10)
print(0o15)

>>>
107
253
13
>>>
```
---

<h4 id="3">TYPE CONVERSION</h4>

```python
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

---

<h4 id="4">PYTHON DECIMAL</h4>

```python
n1 = 1.1 + 2.2
print(n1 == 3.3)
print(n1)

>>>
False
3.3000000000000003
>>>
```

```python
import decimal

print(0.1)
print(decimal.Decimal(0.1))

>>>
0.1
0.1000000000000000055511151231257827021181583404541015625
>>>
```

---

<h4 id="5">PYTHON FRACTIONS</h4>

```python
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

```python
import fractions

print(fractions.Fraction(1.1))
print(fractions.Fraction('1.1'))

>>>
2476979795053773/2251799813685248
11/10
>>>
```

```python
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

---

<h4 id="6">PYTHON MATHEMATICS</h4>

```python
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

```python
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

---

Src

[programiz](https://www.programiz.com/python-programming/variables-datatypes)

---
