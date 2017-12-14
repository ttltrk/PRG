
Numbers
======

[[python.org](https://docs.python.org/3/tutorial/introduction.html#numbers)] - 
[[jupyter](http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Numbers.ipynb)] -
[[digitalocean](https://www.digitalocean.com/community/tutorials/how-to-do-math-in-python-3-with-operators)]

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD)

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

