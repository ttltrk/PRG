
Lambda Expressions
======

[jupyter](http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Lambda%20expressions.ipynb)

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

```python
even = lambda num: num %2 == 0

print (even(4))

>>>
True
>>>
```

```python
def even(num):
    return num %2 == 0

print (even(10))

>>>
True
>>>
```

```python
first = lambda s: s[0]

print (first("hello"))

>>>
h
>>>
```

```python
rev = lambda s: s[::-1]

print (rev("hello"))

>>>
olleh
>>> 
```

```python
def adder(x, y):
    return x + y

print (adder(10, 12))

>>>
22
>>>
```

```python
adder = lambda x, y: x + y

print (adder(15, 2))

>>>
17
>>>
```

```
check this out!!!

map()
filter()
reduce()
```

[[pythonconquerstheuniverse](https://pythonconquerstheuniverse.wordpress.com/)]

```python
len_check = lambda item: len(item)

print (len_check("blabla"))

>>>
6
>>>
```
