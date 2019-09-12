
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [DS](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/DataStruct/DS.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Data Structures - Sets</h3>

---

Set to list

```python
l = list(s)
```

---

Sets are unordered collections of unique elements

```python
s = set()

print(type(s))

>>>
<class 'set'>
>>>
```

<a href='#^'>^^^</a>

```python
s = set()

s.add(1)
print(s)

s.add(2)
print(s)

s.add(2)
print(s)

>>>
{1}
{1, 2}
{1, 2}
>>>
```

<a href='#^'>^^^</a>

```python
l = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
s = set(l)

print(s)

>>>
{1, 2, 3}
>>>
```

<a href='#^'>^^^</a>

```python
s = set('Mississippi')

print(s)

>>>
{'p', 'i', 's', 'M'}
>>>
```

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B)

>>>
{1, 2, 3, 4, 5, 6, 7, 8}
>>>
```

<a href='#^'>^^^</a>

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A & B)

>>>
{4, 5}
>>>
```

<a href='#^'>^^^</a>

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

<a href='#^'>^^^</a>

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A ^ B)

>>>
{1, 2, 3, 6, 7, 8}
>>>
```

<a href='#^'>^^^</a>

```python
sts = {"apple", "banana", "cherry"}

print(sts)

sts.add("damson")

print(sts)

sts.remove("banana")

print(sts)

print(len(sts))

>>>
{'apple', 'banana', 'cherry'}
{'damson', 'apple', 'banana', 'cherry'}
{'damson', 'apple', 'cherry'}
3
>>>
```

<a href='#^'>^^^</a>

---

```python
s = set()
s.add(1)
s.add(2)

print(s)

>>>
{1, 2}
>>>
```

```python
s = set()
s.add(1)
s.add(2)

print(s)
s.clear()
print(s)

>>>
{1, 2}
set()
>>>
```

```python
s = {1,2,3}

sc = s.copy()
s.add(4)

print(s)
print(sc)

>>>
{1, 2, 3, 4}
{1, 2, 3}
>>>
```

```python
s = {1,2,3}

sc = s.copy()
s.add(4)
ss = s.difference(sc)
print(ss)

>>>
{4}
>>>
```

```python
s1 = {1,2,3}
s2 = {1,4,5}

s1.difference_update(s2)

print(s1)

>>>
{2, 3}
>>>
```

```python
s = {1,2,3,4}

s.discard(2)

print(s)

>>>
{1,2,3}
>>>
```

```python
s1 = {1,2,3}
s2 = {1,2,4}

s = s1.intersection(s2)

print(s)

>>>
{1,2}
>>>
```

```python
s1 = {1,2}
s2 = {1,2,4}
s3 = {5}

s = s1.isdisjoint(s2)
ss = s1.isdisjoint(s3)

print(s)
print(ss)

>>>
False
True
>>>
```

```python
s1 = {1,2}
s2 = {1,2,4}
s3 = {5}

s = s1.issubset(s2)
ss = s1.issubset(s3)

print(s)
print(ss)

>>>
True
False
>>>
```

```python
s1 = {1,2,5}
s2 = {1,2,4}
s3 = {4,5,6}

s = s1.symmetric_difference(s2)
ss = s1.symmetric_difference(s3)
sss = s2.symmetric_difference(s3)

print(s)
print(ss)
print(sss)

>>>
{4, 5}
{1, 2, 4, 6}
{1, 2, 5, 6}
>>>
```

```python
s1 = {1,2,5}
s2 = {1,2,4}
s3 = {4,5,6}

s = s1.union(s2)
ss = s1.union(s3)
sss = s2.union(s3)

print(s)
print(ss)
print(sss)

>>>
{1, 2, 4, 5}
{1, 2, 4, 5, 6}
{1, 2, 4, 5, 6}
>>>
```

<a href='#^'>^^^</a>

---
