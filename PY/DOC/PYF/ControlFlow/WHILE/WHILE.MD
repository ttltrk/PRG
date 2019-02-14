
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [CF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/ControlFlow/CF.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Control Flow - while</h3>

---

<h4 id=''>while Template</h4>

```python
while some_boolean_condition:
    #do something
```

<a href='#^'>^^^</a>

```python
while some_boolean_condition:
    #do something
else:
    #do something different
```

<a href='#^'>^^^</a>

---

<h4 id=''>Infinity loop</h4>

```python
x = 0

while x < 10:
    print(f'the current status of x is {x}')
    
>>>
...
>>>
```

<a href='#^'>^^^</a>

---

<h4 id=''>Basic while loop</h4>

```python
x = 0
while x < 5:
    print(f'the current status of x is {x}')
    #x = x + 1
    x += 1
    
>>>
the current status of x is 0
the current status of x is 1
the current status of x is 2
the current status of x is 3
the current status of x is 4
>>>
```

<a href='#^'>^^^</a>

```python
x = 1
while x < 5:
    print(f'the current status of x is {x}')
    #x = x + 1
    x += 1
    
>>>
the current status of x is 1
the current status of x is 2
the current status of x is 3
the current status of x is 4
>>>
```

<a href='#^'>^^^</a>

```python
x = 3
while x < 5:
    print(f'the current status of x is {x}')
    #x = x + 1
    x += 1   
    
>>>
the current status of x is 3
the current status of x is 4
>>>
```

<a href='#^'>^^^</a>

---

<h4 id=''>while with else</h4>

```python
x = 1
while x < 5:
    print(f'the current status of x is {x}')
    #x = x + 1
    x += 1
else:
    print('x is less than 5')
    
>>>
the current status of x is 1
the current status of x is 2
the current status of x is 3
the current status of x is 4
x is less than 5
>>>
```

<a href='#^'>^^^</a>

---

<h4 id=''>break while</h4>

```python
x = 0

while x < 5:
    if x == 2:
        break
    print(f'x is now {x}')
    x += 1
    
>>>
x is now 0
x is now 1
>>>
```

<a href='#^'>^^^</a>

---

```python

>>>

>>>
```

<a href='#^'>^^^</a>

---

```python

>>>

>>>
```

<a href='#^'>^^^</a>

---

```python
a = "hi world"

i = 1
while i < 6:
  print(a)
  i += 1
  
>>>
hi world
hi world
hi world
hi world
hi world
>>>
```

<a href='#^'>^^^</a>

```python
i = 1
while i < 6:
  print(i)
  i += 1
  
>>>
1
2
3
4
5
>>>
```

<a href='#^'>^^^</a>

```
x = 0

while x < 10:
    print ("X is currently: ", x)
    x +=1
	
>>>
X is currently:  0
X is currently:  1
X is currently:  2
X is currently:  3
X is currently:  4
X is currently:  5
X is currently:  6
X is currently:  7
X is currently:  8
X is currently:  9
>>> 
```

<a href='#^'>^^^</a>

```python
x = 0

while x < 10:
    print ("X is currently: ", x)
    x +=1
else:
    print ("All done!")
	
>>>
X is currently:  0
X is currently:  1
X is currently:  2
X is currently:  3
X is currently:  4
X is currently:  5
X is currently:  6
X is currently:  7
X is currently:  8
X is currently:  9
All done!
>>> 
```

<a href='#^'>^^^</a>

```python
while test:
	code statement
	if test:
		break
	if test:
		continue
else:
	final code statements
x = 0

while x < 10:
    print ("X is currently: ", x)
    print ("X is still less than 10, adding 1 to x")
    x +=1

    if x==3:
        print ("Hey x equals 3!")
    else:
        print ("continuing")
        continue
		
>>>
X is currently:  0
X is still less than 10, adding 1 to x
continuing
X is currently:  1
X is still less than 10, adding 1 to x
continuing
X is currently:  2
X is still less than 10, adding 1 to x
Hey x equals 3!
X is currently:  3
X is still less than 10, adding 1 to x
continuing
X is currently:  4
X is still less than 10, adding 1 to x
continuing
X is currently:  5
X is still less than 10, adding 1 to x
continuing
X is currently:  6
X is still less than 10, adding 1 to x
continuing
X is currently:  7
X is still less than 10, adding 1 to x
continuing
X is currently:  8
X is still less than 10, adding 1 to x
continuing
X is currently:  9
X is still less than 10, adding 1 to x
continuing
>>> 
```

<a href='#^'>^^^</a>

```python
x = 0

while x < 10:
    print ("X is currently: ", x)
    print ("X is still less than 10, adding 1 to x")
    x +=1

    if x==3:
        print ("Hey x equals 3!")
        break
    else:
        print ("continuing")
        continue
		
>>>
X is currently:  0
X is still less than 10, adding 1 to x
continuing
X is currently:  1
X is still less than 10, adding 1 to x
continuing
X is currently:  2
X is still less than 10, adding 1 to x
Hey x equals 3!
>>>
```

<a href='#^'>^^^</a>

---

```python
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
>>>
1
2
3
>>>
```

<a href='#^'>^^^</a>

---

```python
i = 1
while i < 6:
  print(i)
  if i == 3:
    print("itt volt a harmadik step")
  if i == 5:
    print("itt meg az otodik")
  i += 1
  
>>>
1
2
3
itt volt a harmadik step
4
5
itt meg az otodik
>>>
```

<a href='#^'>^^^</a>

---

