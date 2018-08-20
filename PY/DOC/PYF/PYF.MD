
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD)

---

### Python Flash

---

* [operators](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/OP/OP.MD)
* [numbers](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/NUM/NUM.MD)
* [strings](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/STR/STR.MD)
* [variables](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/VAR/VAR.MD)

---

* [lists](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/LST/LST.MD)
* [tuples](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/TUP/TUP.MD)
* [set](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/SET/SET.MD)
* [dictionary]()

---

* [if..else](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/IF/IF.MD)
* [for](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/FOR/FOR.MD)
* [while](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/WHILE/WHILE.MD)

---

* [functions](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/FUN/FUN.MD)
* [lambda](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/LAM/LAM.MD)
* [list comprehensions](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/LCO/LCO.MD)
* [oop](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/OOP/OOP.MD)

---

[JVF](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/JVF/JVF.MD)

---

### Python operators

```python
a == b  (Equals)
a != b  (Not Equals)
a < b   (Less than)
a <= b  (Less than or equal to)
a > b   (Greater than)
a >= b  (Greater than or equal to)
```

---

### Python numbers

```python
x = 1
y = 2.8  
z = 1j   

print(type(x))
print(type(y))
print(type(z))

>>>
<class 'int'>
<class 'float'>
<class 'complex'>
>>>
```

```python
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

>>>
<class 'int'>
<class 'int'>
<class 'int'>
>>>
```

```python
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

>>>
<class 'float'>
<class 'float'>
<class 'float'>
>>>
```

```python
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

>>>
<class 'float'>
<class 'float'>
<class 'float'>
>>>
```

```python
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

>>>
<class 'complex'>
<class 'complex'>
<class 'complex'>
>>>
```

---

### Python strings

```python
a = "Hello, World!"

print(a[1])
print(a[2:5])

>>>
e
llo
>>>
```

```python
a = " Hello, World! "

print(a.strip())
print(a)

>>>
Hello, World!
 Hello, World! 
>>>
```

```python
a = "Hello, World!"

print(len(a))
print(a.lower())
print(a.upper())
print(a.replace("H", "J"))
print(a.split(","))

>>>
13
hello, world!
HELLO, WORLD!
Jello, World!
['Hello', ' World!']
>>>
```

---

### Python variables

```python
a = 5
b = 4.0
c = "John"
d = True

print(a, b, c, d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))

>>>
5 4.0 John True
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
>>>
```

```python
a = 5
b = 4.0
c = "John"
d = True

print("a 'a' erteke = " + str(a))
print("a 'b' erteke = " + str(b))
print("a 'c' erteke = " + c)
print("a 'd' erteke = " + str(d))

>>>
a 'a' erteke = 5
a 'b' erteke = 4.0
a 'c' erteke = John
a 'd' erteke = True
>>>
```

---

### Python lists

```python
lst = ["apple", "banana", "cherry"]

print(lst)

lst[1] = "blackcurrant"

print(lst)

>>>
['apple', 'banana', 'cherry']
['apple', 'blackcurrant', 'cherry']
>>>
```

```python
lst = ["apple", "banana", "cherry"]
lst.append("damson")

print(lst)
print(lst * 2)

>>>
['apple', 'banana', 'cherry', 'damson']
['apple', 'banana', 'cherry', 'damson', 'apple', 'banana', 'cherry', 'damson']
>>>
```

```python
lst = ["apple", "banana", "cherry"]

print(lst)

lst.remove("banana")

print(lst)
print(len(lst))

>>>
['apple', 'banana', 'cherry']
['apple', 'cherry']
2
>>>
```

---

### Python tuples

```python
tup = ("apple", "banana", "cherry")

print(tup)

>>>
('apple', 'banana', 'cherry')
>>>
```

```python
tup = ("apple", "banana", "cherry")

print(tup[1])

>>>
banana
>>>
```

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

```python
tup = ("apple", "banana", "cherry")

print(len(tup))

>>>
3
>>>
```

---
