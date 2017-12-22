
Nested Statements

[jupyter](http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Nested%20Statements%20and%20Scope.ipynb)

```python
x = 25

def printer():
    x = 50
    return x

print (x)
print (printer())

>>>
25
50
>>>
```

```python
"""
LOCAL
"""

f = lambda x: x**2

print (f(2))

>>>
4
>>>
```

```python
"""
ENCLOSING FUNCTION LOCAL
"""

name = "glob name"

def greet():
    #ENCLOSING FUNCTION
    name = "Sammy"

    def hello():
        print ("Hello " + name)

    hello()

greet()

>>>
Hello Sammy
>>>
```

```python
"""
ENCLOSING FUNCTION LOCAL
"""

name = "glob name"

def greet():
    #ENCLOSING FUNCTION
    name = "Sammy"

    def hello():
        nick = "Steve"
        print ("Hello %s and Hello %s " % (nick, name))

    hello()

greet()

>>>
Hello Steve and Hello Sammy 
>>>
```

```python
"""
GLOBAL
"""

name = "Annie"

print (name)

>>>
Annie
>>>
```

```python
"""
BUILT-IN
"""

len
```

```python
"""
LOCAL VARIABLES
"""

x = 50

def func(x):
    print ("x is" , x)
    x = 2
    print ("Changed local x to" , x)

func(x)
print ("but x is still" , x)

>>>
x is 50
Changed local x to 2
but x is still 50
>>>
```

```python
"""
LOCAL VARIABLES
"""

x = 50

def func(x):
    print ("x is" , x)
    print ("Changed local x to" , x)
    x = 2
    
func(x)
print ("but x is still" , x)

>>>
x is 50
Changed local x to 50
but x is still 50
>>> 
```

```python
"""
GLOBAL STATEMENT
"""

x = 50

def func():
    global x
    print ("This function is now using the global x!")
    print ("Because of global x is: ", x)
    x = 2
    print ("Ran func(), changed global x to" , x)

print ("Before calling func(), x is: " , x)
func()
print ("Value of x (outside of func()) is: " , x)

>>>
Before calling func(), x is:  50
This function is now using the global x!
Because of global x is:  50
Ran func(), changed global x to 2
Value of x (outside of func()) is:  2
>>>
```
