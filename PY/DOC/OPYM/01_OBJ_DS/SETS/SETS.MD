
---

### Set

---

Set is an unordered collection of unique items. Set is defined by values separated by comma inside braces { }. Items in a set are not ordered.

---

* CREATE A SET
* CHANGE SET IN PY
* REMOVE ELEMENTS FROM A SET
* SET UNION
* SET INTERSECTION
* SET DIFFERENCE
* SET SIMMETRIC DIFFERENCE

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

[src - programiz.com](https://www.programiz.com/python-programming/set)

---
