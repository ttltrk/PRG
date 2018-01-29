
Functions within functions
======

[<<<](https://github.com/ttltrk/PRG/blob/master/PY/DOC/OPYM/OPYM.MD)

[jupyter](https://nbviewer.jupyter.org/github/jmportilla/Complete-Python-Bootcamp/blob/master/Decorators.ipynb)

```python
def hello(name='trk'):
  print("the hello() function has been executed")
  
  def greet():
    return "\t This is inside the greet() function"
  
  def welcome():
    return "\t This is inside the welcome() function"
    
  print(greet())
  print(welcome())
  print("now we are back inside the hello() function")
    
print(hello())

>>>
the hello() function has been executed
	 This is inside the greet() function
	 This is inside the welcome() function
now we are back inside the hello() function
>>>
```

```python
def hello(name='trk'):
  
  def greet():
    return "\t This is inside the greet() function"
  
  def welcome():
    return "\t This is inside the welcome() function"
    
  if name == 'trk':
    return greet
  else:
    return welcome
  
print(hello())

>>>
<function hello.<locals>.greet at 0x7f3364132620>
>>>
```
