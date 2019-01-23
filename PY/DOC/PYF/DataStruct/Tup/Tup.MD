
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [DS](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/DataStruct/DS.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Data Structures - Tuples</h3>

---

Tuples are immutable, cannot be changed.

```python
t = (1,2,3)
l = [1,2,3]

print(type(t))
print(type(l))

>>>
<class 'tuple'>
<class 'list'>
>>>
```

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

```python
t = ('p','e','r','m','i','t')

print(t[-1])
print(t[-6])

>>>
t
p
>>>
```

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

```python
tup = ("apple", "banana", "cherry")

print(tup)

>>>
('apple', 'banana', 'cherry')
>>>
```

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

```python
print((1, 2, 3) + (4, 5, 6))
print(("Repeat",) * 3)

>>>
(1, 2, 3, 4, 5, 6)
('Repeat', 'Repeat', 'Repeat')
>>>
```

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

```python
tup = ("apple", "banana", "cherry")

print(tup[1])

>>>
banana
>>>
```

<a href='#^'>^^^</a>

```python
tup = ("apple", "banana", "cherry")

tup[1] = "blackcurrant"

>>>
Traceback (most recent call last):
  File "/Users/attilatorok/Desktop/tst.py", line 3, in <module>
    tup[1] = "blackcurrant"
TypeError: 'tuple' object does not support item assignment
>>>
```

<a href='#^'>^^^</a>

```python
tup = ("apple", "banana", "cherry")

print(len(tup))

>>>
3
>>>
```

<a href='#^'>^^^</a>

---
