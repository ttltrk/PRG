
Tuples
======

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD)

[programiz.com](https://www.programiz.com/python-programming/tuple)

---

* <a href="#1">CREATING A TUPLE</a>
* <a href="#2">CREATING TUPLE WITH ONE ELEMENT</a>
* <a href="#3">INDEXING</a>
* <a href="#4">NEGATIVE INDEXING</a>
* <a href="#5">SLICING</a>
* <a href="#6">CHANGING A TUPLE</a>
* <a href="#7">DELETING A TUPLE</a>
* <a href="#8">TUPLE METHODS</a>

---

<h4 id="1">CREATING A TUPLE</h4>

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

<h4 id="2">CREATING TUPLE WITH ONE ELEMENT</h4>

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

<h4 id="3">INDEXING</h4>

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

<h4 id="4">NEGATIVE INDEXING</h4>

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

<h4 id="5">SLICING</h4>

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

<h4 id="6">CHANGING A TUPLE</h4>

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

<h4 id="7">DELETING A TUPLE</h4>

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

<h4 id="8">TUPLE METHODS</h4>

* count(x)
* index(x)

```python
t = ('a','p','p','l','e',)

print(t.count('p'))
print(t.index('l'))

>>>
2
3
>>>
```

---
