
Numbers
======

[programiz.com](https://www.programiz.com/python-programming/variables-datatypes)

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD)

---

* NUMBER DATA TYPE IN PYTHON
* SYSTEM PREFIX
* TYPE CONVERSION
* PYTHON DECIMAL
* PYTHON FRACTIONS

---

NUMBER DATA TYPE IN PYTHON

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

SYSTEM PREFIX

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

TYPE CONVERSION

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

PYTHON DECIMAL

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

PYTHON FRACTIONS

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

---

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

