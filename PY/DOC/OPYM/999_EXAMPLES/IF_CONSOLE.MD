
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD) - [Examples/Apps](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/999_EXAMPLES/EXAM.MD)

---

### IF CONSOLE

---

```python
#1st function
def dec(var1):
  if (var1  == 100):
    return vd1()
  elif (var1 == 0):
    return trailer()
  else: 
    return vd2()

#2nd function
def jan(var2):
  if (var2  == 100):
    return vj1()
  elif (var2 == 0):
    return trailer()
  else: 
    return vj2()
    
#1st called function by function    
def vd1():
  print("VD1")

#2nd called function by function
def vd2():
  print("VD2")

#3rd called function by function
def vj1():
  print("VJ1")

#4th called function by function
def vj2():
  print("VJ2")
  
#function trailer  
def trailer():
  print("ZZZZZERO!")

#Console input
dec(int(input("num?")))
jan(int(input("num?")))

>>>
num? 0
ZZZZZERO!
num? 0
ZZZZZERO!
>>>

>>>
num? 10
VD2
num? 100
VJ1
>>>
```

---
