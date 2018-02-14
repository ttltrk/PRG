
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

---

<h4 id="4">len()</h4>

---

<h4 id="5">list()</h4>

---

<h4 id="6">max()</h4>

---

<h4 id="7">min()</h4>

---

<h4 id="8">sorted()</h4>

---

<h4 id="9">sum()</h4>

---
