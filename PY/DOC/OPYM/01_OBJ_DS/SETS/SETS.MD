
Sets
======

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD)

* [programiz.com](https://www.programiz.com/python-programming/set)
* [[python.org](https://docs.python.org/3/tutorial/datastructures.html#sets)]
* [[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Sets%20and%20Booleans.ipynb)]
* [[thomas-cokelaer](http://thomas-cokelaer.info/tutorials/python/sets.html?highlight=sets)]

---

CREATE A SET

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

---

CHANGE SET IN PY

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

---

REMOVE ELEMENTS FROM A SET

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

---

SET UNION

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B)

>>>
{1, 2, 3, 4, 5, 6, 7, 8}
>>>
```

---

SET INTERSECTION

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A & B)

>>>
{4, 5}
>>>
```

---

SET DIFFERENCE

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

---

SET SIMMETRIC DIFFERENCE

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A ^ B)

>>>
{1, 2, 3, 6, 7, 8}
>>>
```

---

A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. 

```python
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```
