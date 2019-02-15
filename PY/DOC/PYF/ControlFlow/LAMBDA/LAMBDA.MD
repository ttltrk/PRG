
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [CF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/ControlFlow/CF.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Control Flow - lambda</h3>

---

<h4 id='^^lam'></h4>
<a href='#latese'>lambda temp sequence</a><br>
<a href='#lamap'>lambda with map</a><br>
<a href='#lamane'>lambda map names</a><br>
<a href='#lamanerev'>lambda map names reverse</a><br>
<a href='#lamfil'>lambda with filter</a><br>

<a href='#^'>^^^</a>

---

<h4 id='latese'>lambda temp sequence</h4>

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

<a href='#^^lam'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='lamap'>lambda with map</h4>

```python
l = [1, 2, 3, 4, 5]

square = list(map(lambda num: num**2,l))

print(square)

>>>
[1, 4, 9, 16, 25]
>>>
```

<a href='#^^lam'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='lamane'>lambda map names</h4>

```python
l = ['Andy', 'Sam', 'John']

names = list(map(lambda chars:chars[0],l))

print(names)

>>>
['A', 'S', 'J']
>>>
```

<a href='#^^lam'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='lamanerev'>lambda map names reverse</h4>

```python
l = ['Andy', 'Sam', 'John']

names = list(map(lambda chars:chars[::-1],l))

print(names)

>>>
['ydnA', 'maS', 'nhoJ']
>>>
```

<a href='#^^lam'>^^</a><br>
<a href='#^'>^^^</a>

---

```python
even = lambda num: num %2 == 0

print (even(4))

>>>
True
>>>
```

<a href='#^^lam'>^^</a><br>
<a href='#^'>^^^</a>

---


<h4 id='lamfil'>lambda with filter</h4>

```python
l = [1, 2, 3, 4, 5]

square = list(filter(lambda num: num%2==0,l))

print(square)

>>>
[2, 4]
>>>
```

<a href='#^^lam'>^^</a><br>
<a href='#^'>^^^</a>

---

```python
def even(num):
    return num %2 == 0

print (even(10))

>>>
True
>>>
```

<a href='#^'>^^^</a>

---

```python
first = lambda s: s[0]

print (first("hello"))

>>>
h
>>>
```

<a href='#^'>^^^</a>

---

```python
rev = lambda s: s[::-1]

print (rev("hello"))

>>>
olleh
>>> 
```

<a href='#^'>^^^</a>

---

```python
def adder(x, y):
    return x + y

print (adder(10, 12))

>>>
22
>>>
```

<a href='#^'>^^^</a>

---

```python
adder = lambda x, y: x + y

print (adder(15, 2))

>>>
17
>>>
```

<a href='#^'>^^^</a>

---

```python
len_check = lambda item: len(item)

print (len_check("blabla"))

>>>
6
>>>
```

<a href='#^'>^^^</a>

---

```python
#function
def lam(a):
    a = a+10
    return a
    
#lambda
x = lambda b : b + 10

print("a funkcio eredmenye = " + str(lam(9)))
print("a lambda eredmenye = " + str(x(9)))

>>>
a funkcio eredmenye = 19
a lambda eredmenye = 19
>>>
```

<a href='#^'>^^^</a>

---

```python
x = lambda a, b : a * b
y = lambda a, b, c : a + b + c

print(x(5, 6))
print(y(5, 6, 2))

>>>
30
13
>>>
```

<a href='#^'>^^^</a>

---

```python
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(3)

print(mydoubler(10))

>>>
30
>>>
```

<a href='#^'>^^^</a>

---

```python
def myfunc(n):
  return lambda a, b : (a + b) * n

mydoubler = myfunc(3)

print(mydoubler(10, 2))

>>>
36
>>>
```

<a href='#^'>^^^</a>

---

```python
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))

>>>
22
33
>>>
```

<a href='#^'>^^^</a>

---

