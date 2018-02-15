
Built-in Functions with List
======

[programiz.com](https://www.programiz.com/python-programming/list#method)

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/LISTS/LISTS.MD)

---

* <a href="#1">all()
* <a href="#2">any()
* <a href="#3">enumerate()
* <a href="#4">len()
* <a href="#5">list()
* <a href="#6">max()
* <a href="#7">min()
* <a href="#8">sorted()
* <a href="#9">sum()

---

<h4 id="1">all()</h4>

The all() method returns True when all elements in the given iterable are true. If not, it returns False.

```python
# all values true
l = [1, 3, 4, 5]
print(all(l))

# all values false
l = [0, False]
print(all(l))

# one false value
l = [1, 3, 4, 0]
print(all(l))

# one true value
l = [0, False, 5]
print(all(l))

# empty iterable
l = []
print(all(l))

>>>
True
False
False
False
True
>>>
```

---

<h4 id="2">any()</h4>

The any() method returns True if any element of an iterable is true. If not, this method returns False.

```python
l = [1, 3, 4, 0]
print(any(l))

l = [0, False]
print(any(l))

l = [0, False, 5]
print(any(l))

l = []
print(any(l))

>>>
True
False
True
False
>>>
```

---

<h4 id="3">enumerate()</h4>

The enumerate() method adds counter to an iterable and returns it (the enumerate object).

```python
grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))

# converting to list
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))

>>>
<class 'enumerate'>
[(0, 'bread'), (1, 'milk'), (2, 'butter')]
[(10, 'bread'), (11, 'milk'), (12, 'butter')]
>>>
```

---

<h4 id="4">len()</h4>

The len() function returns the number of items (length) of an object.

```python
e = []
print('e =', len(e))

l = [1, 2, 3]
print('l =', len(l))

t = (1, 2, 3)
print('t =', len(t))

r = range(1, 10)
print('r =', len(r))

>>>
e = 0
l = 3
t = 3
r = 9
>>>
```

---

<h4 id="5">list()</h4>

The list() constructor creates a list in Python.

```python
# empty list
print(list())

# vowel string
vowelString = 'aeiou'
print(list(vowelString))

# vowel tuple
vowelTuple = ('a', 'e', 'i', 'o', 'u')
print(list(vowelTuple))

# vowel list
vowelList = ['a', 'e', 'i', 'o', 'u']
print(list(vowelList))

>>>
[]
['a', 'e', 'i', 'o', 'u']
['a', 'e', 'i', 'o', 'u']
['a', 'e', 'i', 'o', 'u']
>>>
```

---

<h4 id="6">max()</h4>

The max() method returns the largest element in an iterable or largest of two or more parameters.

```python
# using max(arg1, arg2, *args)
print('Maximum is:', max(1, 3, 2, 5, 4))

# using max(iterable)
num = [1, 3, 2, 8, 5, 10, 6]
print('Maximum is:', max(num))

>>>
Maximum is: 5
Maximum is: 10
>>>
```

---

<h4 id="7">min()</h4>

The min() method returns the smallest element in an iterable or smallest of two or more parameters.

```python
# using min(arg1, arg2, *args)
print('Minimum is:', min(1, 3, 2, 5, 4))

# using min(iterable)
num = [3, 2, 8, 5, 10, 6]
print('Minimum is:', min(num))

>>>
Minimum is: 1
Minimum is: 2
>>>
```

---

<h4 id="8">sorted()</h4>

The sorted() method returns a sorted list from the given iterable.

```python
pyList = ['e', 'a', 'u', 'o', 'i']
print(sorted(pyList))

pyString = 'Python'
print(sorted(pyString))

pyTuple = ('e', 'a', 'u', 'o', 'i')
print(sorted(pyTuple))

pyNum = (9, 4, 2, 8, 1)
print(sorted(pyNum))

>>>
['a', 'e', 'i', 'o', 'u']
['P', 'h', 'n', 'o', 't', 'y']
['a', 'e', 'i', 'o', 'u']
[1, 2, 4, 8, 9]
>>>
```

---

<h4 id="9">sum()</h4>

The sum() function adds the items of an iterable and returns the sum.

```python
numbers = [2.5, 3, 4, -5]

# start parameter is not provided
numbersSum = sum(numbers)
print(numbersSum)

# start = 10
numbersSum = sum(numbers, 10)
print(numbersSum)

>>>
4.5
14.5
>>>
```

---
