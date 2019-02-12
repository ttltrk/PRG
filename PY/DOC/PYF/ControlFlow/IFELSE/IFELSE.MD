
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [CF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/ControlFlow/CF.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Control Flow - if...else</h3>

---

---
<h4 id='^^'></h4>
<a href='#temp'>Template</a><br>
<a href='#ifif'>if</a><br>
<a href='#ifelse'>if..else</a><br>
<a href='#ifelifelse'>if..elif..else</a><br>
<a href='#ifinput'>Nested if with input</a><br><br>

<a href='#^'>^^^</a>

---

<h4 id='basie'>Template</h4>

```python
if some_condition:
    # execute some code
elif some_other_condition:
    # do something different
else:
    # do something else
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='ifif'>if</h4>

```python
a = 33
b = 200

if b > a:
    print("b is greater than a")

>>>
b is greater than a
>>>
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

```python
num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")

>>>
3 is a positive number.
This is always printed.
This is also always printed.
>>>
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='ifelse'>if..else</h4>

```python
num = 3

if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")

>>>
Positive or Zero
>>>
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='ifelifelse'>if..elif..else</h4>

```python
num = 3.4

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
    
>>>
Positive number
>>>
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

```python
a = 200
b = 33

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
>>>
a is greater than b
>>>
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

```python
a = 33
b = 33

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
>>>
a and b are equal
>>>
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

---

<h4 id='ifinput'>Nested if with input</h4>

```python
num = float(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
    
>>>
Enter a number:  10
Positive number
>>>

>>>
Enter a number:  0
Zero
>>>

>>>
Enter a number:  -2
Negative number
>>>
```

<a href='#^^'>^^</a><br>
<a href='#^'>^^^</a>

---
