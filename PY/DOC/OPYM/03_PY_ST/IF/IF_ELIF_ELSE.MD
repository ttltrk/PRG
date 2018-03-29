
---

### if, elif and else

---

Perhaps the most well-known statement type is the if statement.

The if statement is used for conditional execution:

It selects exactly one of the suites by evaluating the expressions one by one until one is found to be true (see section Boolean operations for the definition of true and false); then that suite is executed (and no other part of the if statement is executed or evaluated). If all expressions are false, the suite of the else clause, if present, is executed.

---

```python
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')
...
More
```

```python	
>>> if True:
	print ("It was True")	
It was True
>>> 
```

```python
>>> x = False
>>> if x:
	print ("x was True")
else:
	print ("I will print when x is anything not True")	
I will print when x is anything not True
>>> 
```

```python
>>> x = True
>>> if x:
	print ("x was True")
else:
	print ("I will print when x is anything not True")	
x was True
>>> 
```

```python
loc = "Bank"
if loc == "Auto Shop":
    print ("Welcome to the Auto Shop!")
elif loc == "Bank":
    print ("Welcome to the Bank!")
else:
    print ("Where are you?!")

>>>
Welcome to the Bank!
>>>
```

```python
loc = "Mall"

if loc == "Auto Shop":
    print ("Welcome to the Auto Shop!")
elif loc == "Bank":
    print ("Welcome to the Bank!")
else:
    print ("Where are you?!")
	
>>>
Where are you?!
>>> 
```

```python
loc = "Mall"

if loc == "Auto Shop":
    print ("Welcome to the Auto Shop!")
elif loc == "Bank":
    print ("Welcome to the Bank!")
elif loc == "Mall":
    print ("Welcome to the Mall!")
else:
    print ("Where are you?!")
	
>>>
Welcome to the Mall!
>>> 
```

---

* [src - jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/If%2C%20elif%2C%20and%20else%20Statements.ipynb)
* [src - python.org](https://docs.python.org/3/tutorial/controlflow.html)

---
