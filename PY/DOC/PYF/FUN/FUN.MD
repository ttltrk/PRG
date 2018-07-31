
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD)

---

### Python Functions

---

```python
#variables
a = "hello world"
b = "xyz"
c = 5
d = 7

#functions
def pr(par1):
  print(par1)
  
def ps(par1, par2):
  return (par1+par2)

def ms(par1,par2):
  return (par1-par2)

#STDOUT
pr(a)
pr(b)
print(ps(c,d))
print(ms(c,d))

>>>
hello world
xyz
12
-2
>>>
```

---

```python
bigger = 0

def func(num1, num2):
  if num1 > num2:
    bigger = num1
  else:
    bigger = num2
  return bigger

print(func(4, 6))

>>>
6
>>>
```

```python
#variables
a = 5
b = 10
bigger = 0

#function
def func(num1, num2):
  if num1 > num2:
    bigger = num1
  else:
    bigger = num2
  return bigger

#print
print(func(a, b))

>>>
10
>>>
```

```python
#variables
a = 5
b = 10
bigger = 0

#function
def func(num1, num2):
  if num1 > num2:
    bigger = num1
  else:
    bigger = num2
  return bigger

#print
print(func(a, 4))
print(func(a, b))

>>>
5
10
>>>
```

---

[JV](https://github.com/ttltrk/PRG/blob/master/JAVA/DOC/OJM/JVF/FUN/FUN.MD)

---
