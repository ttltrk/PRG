
while Loops
======

[while loops.ipynb](http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/While%20loops.ipynb)

[while loops.udemy](https://www.udemy.com/complete-python-bootcamp/learn/v4/t/lecture/3512318?start=0)

```python
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

```python
while test:
	code statement
	if test:
		break
	if test:
		continue
else:
	final code statements
```

```python
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
