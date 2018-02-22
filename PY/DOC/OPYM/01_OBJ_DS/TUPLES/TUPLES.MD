
Tuples
======

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD)

* [programiz.com](https://www.programiz.com/python-programming/tuple)
* [python.org](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
* [jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Tuples.ipynb)
* [digitalocean](https://www.digitalocean.com/community/tutorials/understanding-tuples-in-python-3)
* [thomas-cokelaer](http://thomas-cokelaer.info/tutorials/python/tuples.html)

---

In Python, tuples are part of the standard language. This is a data structure very similar to the list data structure. The main difference being that tuple manipulation are faster than list because tuples are immutable.

In Python tuples are very similar to lists, however, unlike lists they are immutable meaning they can not be changed. You would use tuples to present things that shouldn't be changed, such as days of the week, or dates on a calendar.

A tuple is a data structure that is an immutable, or unchangeable, ordered sequence of elements. Because tuples are immutable, their values cannot be modified.
Tuples are used for grouping data. Each element or value that is inside of a tuple is called an item.

---

CREATING A TUPLE

```python
t = ()
print(t)

t = (1, 2, 3)
print(t)

t = (1, "Hello", 3.4)
print(t)

t = ("mouse", [8, 4, 6], (1, 2, 3))
print(t)

t = 3, 4.6, "dog"
print(t)

a, b, c = t
print(a)
print(b)
print(c)

>>>
()
(1, 2, 3)
(1, 'Hello', 3.4)
('mouse', [8, 4, 6], (1, 2, 3))
(3, 4.6, 'dog')
3
4.6
dog
>>>
```

CREATING TUPLE WITH ONE ELEMENT

```python
t1 = ("hello")
print(type(t1))

t2 = ("hello",)  
print(type(t2))

t3 = "hello",
print(type(t3))

>>>
<class 'str'>
<class 'tuple'>
<class 'tuple'>
>>>
```

---

INDEXING

```python
t = ('p','e','r','m','i','t')

print(t[0])
print(t[5])

n_t = ("mouse", [8, 4, 6], (1, 2, 3))

print(n_t[0][3])
print(n_t[1][1])
print(n_t[2][2])

>>>
p
t
s
4
3
>>>
```

NEGATIVE INDEXING

```python
t = ('p','e','r','m','i','t')

print(t[-1])
print(t[-6])

>>>
t
p
>>>
```

---

SLICING

```python
t = ('p','r','o','g','r','a','m','i','z')

print(t[1:4])
print(t[:-7])
print(t[7:])
print(t[:])

>>>
('r', 'o', 'g')
('p', 'r')
('i', 'z')
('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
>>>
```

---

CHANGING A TUPLE

```python
t = (4, 2, 3, [6, 5])
t[3][0] = 9

print(t)

t = ('p','r','o','g','r','a','m','i','z')

print(t)

>>>
(4, 2, 3, [9, 5])
('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
>>>
```

```python
print((1, 2, 3) + (4, 5, 6))
print(("Repeat",) * 3)

>>>
(1, 2, 3, 4, 5, 6)
('Repeat', 'Repeat', 'Repeat')
>>>
```

---

DELETING A TUPLE

```python
t = ('p','r','o','g','r','a','m','i','z')
print(t)

del t
print(t)

>>>
('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
Traceback (most recent call last):
  File "python", line 5, in <module>
NameError: name 't' is not defined
>>>
```

---
