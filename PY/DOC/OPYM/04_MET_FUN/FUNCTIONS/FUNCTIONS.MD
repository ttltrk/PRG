
Functions
======

[jupyter](http://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Functions.ipynb)

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD)

```python
def name_of_function():
	pass

name_of_function()

>>> 

>>>
```

```python
def name_of_function(arg1, arg2):    
    pass

print (name_of_functions())

>>>
Traceback (most recent call last):
  File "C:/Program Files (x86)/Python/test.py", line 4, in <module>
    print (name_of_functions())
NameError: name 'name_of_functions' is not defined
>>> 
```

```python
def my_add_func(arg1, arg2):    
    print (arg1 + arg2)

my_add_func(1, 2)

>>>
3
>>>
```

```python
def say_hello():
    print ("hello!")

say_hello()

>>>
hello!
>>>
```

```python
def greeting(name):
    print ("hello "+ name)

greeting("trk")

>>>
hello trk
>>>
```


```python
def add_num(num1, num2):
    return (num1 + num2)

x = add_num(2, 3)

print(x)

>>>
5
>>>
```

```python
def add_num(num1, num2):
    return (num1 + num2)

x = add_num("one", "two")

print(x)

>>>
onetwo
>>>
```

```python
def is_prime(num):
    """
    IN: A number
    OUT: A print statement wheter or not the number is prime.
    """

    for n in range(2, num):
        if num % n == 0:
            print ("not prime")
            break
        else:
            print ("the number is prime!")
            
is_prime(12)

>>>
not prime
>>>
```

```python
def is_prime(num):
    """
    IN: A number
    OUT: A print statement wheter or not the number is prime.
    """

    for n in range(2, num):
        if num % n == 0:
            print ("not prime")
            break
        else:
            print ("the number is prime!")
            
is_prime(11)
    
>>>
the number is prime!
the number is prime!
the number is prime!
the number is prime!
the number is prime!
the number is prime!
the number is prime!
the number is prime!
the number is prime!
>>> 
```
