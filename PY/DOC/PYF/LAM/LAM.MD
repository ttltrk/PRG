
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD)

---

### Python lambda

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

```python
def myfunc(n):
  return lambda a, b : (a + b) * n

mydoubler = myfunc(3)

print(mydoubler(10, 2))

>>>
36
>>>
```

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

---
