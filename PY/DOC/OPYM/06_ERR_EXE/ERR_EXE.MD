
Errors and Exceptions
======

[jupyter](http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Errors%20and%20Exceptions%20Handling.ipynb)

```python
try:
    2 + 's'
except:
    print("There was a type of error")
finally:
    print("Finally this was printed")
	
>>>
There was a type of error
Finally this was printed
>>>
```

```python
try:
    f = open("test", "w")
    f.write("test write this")
except:
    print("error in writing to the file")
else:
    print("file write was a success")
	
>>>
file write was a success
>>>
```

```python
try:
    f = open("test", "r")
    f.write("test write this")
except:
    print("error in writing to the file")
else:
    print("file write was a success")
	
>>>
error in writing to the file
>>>
```

```python
try:
    f = open("test", "r")
    f.write("test write this")
finally:
    print("Always execute")
	
>>>
Always execute

Traceback (most recent call last):
  File "C:/Program Files (x86)/Python/test.py", line 3, in <module>
    f.write("test write this")
io.UnsupportedOperation: not writable
>>>
```

```python
try:
    f = open("test", "r")
    f.write("test write this")
except:
    print("there was an error")
finally:
    print("Always execute")

>>>
there was an error
Always execute
>>>
```

```python
def askint():
    try:
        val = int(input("Please enter an int: "))
    except:
        print("Looks like you didn't enter an int!")
    finally:
        print("Finally block executed!")
    print(val)

print(askint())

>>>
Please enter an int: 3
Finally block executed!
3
>>>
```

```python
def askint():
    try:
        val = int(input("Please enter an int: "))
    except:
        print("Looks like you didn't enter an int!")
    finally:
        print("Finally block executed!")
    print(val)

print(askint())

>>>
Please enter an int: five
Looks like you didn't enter an int!
Finally block executed!

Traceback (most recent call last):
  File "C:/Program Files (x86)/Python/test.py", line 10, in <module>
    print(askint())
  File "C:/Program Files (x86)/Python/test.py", line 8, in askint
    print(val)
UnboundLocalError: local variable 'val' referenced before assignment
>>>
```

```python
def askint():
    
    try:
        val = int(input("Please enter an int: "))
        
    except:
        print("Looks like you didn't enter an int!")
        val = int(input("Try again: "))
        
    finally:
        print("Finally block executed!")
        
    print(val)

print(askint())

>>>
Please enter an int: five
Looks like you didn't enter an int!
Try again: 5
Finally block executed!
5
>>>
```

```python
def askint():

    while True:
    
        try:
            val = int(input("Please enter an int: "))
        
        except:
            print("Looks like you didn't enter an int!")
            continue
        
        else:
            print("Correct, that is an integer!")
            break

        finally:
            print("Finally block executed!")

        print(val)

print(askint())

>>>
Please enter an int: abc
Looks like you didn't enter an int!
Finally block executed!
Please enter an int: ab
Looks like you didn't enter an int!
Finally block executed!
Please enter an int: b
Looks like you didn't enter an int!
Finally block executed!
Please enter an int: r
Looks like you didn't enter an int!
Finally block executed!
Please enter an int: 5
Correct, that is an integer!
Finally block executed!
>>>
```
