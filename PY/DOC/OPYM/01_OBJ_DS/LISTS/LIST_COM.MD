
List Comprehensions
======

[jupyter](http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/List%20Comprehensions.ipynb) |
[programiz.com](https://www.programiz.com/python-programming/list-comprehension)

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/01_OBJ_DS/LISTS/LISTS.MD)

* List comprehension is an elegant way to define and create lists based on existing lists.
* List comprehension is generally more compact and faster than normal functions and loops for creating list.
* However, we should avoid writing very long list comprehensions in one line to ensure that code is user-friendly.
* Remember, every list comprehension can be rewritten in for loop, but every for loop can’t be rewritten in the form of list comprehension.

---

WORD

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
>>> l = [letter for letter in "word"]
>>> l
['w', 'o', 'r', 'd']
>>> 
```


```python
>>> lst = [letter for letter in "word"]
>>> lst
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

---

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

---

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
